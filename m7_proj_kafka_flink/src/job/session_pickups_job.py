from pyflink.datastream import StreamExecutionEnvironment, CheckpointingMode
from pyflink.table import EnvironmentSettings, StreamTableEnvironment

def create_source_table(t_env):
    ddl = """
        CREATE TABLE green_trips (
            PULocationID INT,
            DOLocationID INT,
            tip_amount DOUBLE,
            lpep_pickup_datetime VARCHAR,
            event_timestamp AS TO_TIMESTAMP(lpep_pickup_datetime, 'yyyy-MM-dd HH:mm:ss'),
            WATERMARK FOR event_timestamp AS event_timestamp - INTERVAL '5' SECOND
        ) WITH (
            'connector' = 'kafka',
            'topic' = 'green-trips',
            'properties.bootstrap.servers' = 'redpanda:29092',
            'scan.startup.mode' = 'earliest-offset',
            'format' = 'json',
            'json.ignore-parse-errors' = 'true'
        )
    """
    t_env.execute_sql(ddl)


def create_sink_table(t_env):
    ddl = """
        CREATE TABLE session_pickups (
            session_start TIMESTAMP(3),
            session_end TIMESTAMP(3),
            pickup_location_id INT,
            trip_count BIGINT,
            PRIMARY KEY (session_start, pickup_location_id) NOT ENFORCED
        ) WITH (
            'connector' = 'jdbc',
            'url' = 'jdbc:postgresql://postgres:5432/postgres',
            'table-name' = 'session_pickups',
            'username' = 'postgres',
            'password' = 'postgres',
            'driver' = 'org.postgresql.Driver'
        )
    """
    t_env.execute_sql(ddl)


def session_job():
    env = StreamExecutionEnvironment.get_execution_environment()
    
#    env.enable_checkpointing(10000, CheckpointingMode.EXACTLY_ONCE)
    
    env.set_parallelism(1)

    settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
    t_env = StreamTableEnvironment.create(env, environment_settings=settings)

    create_source_table(t_env)
    create_sink_table(t_env)

    t_env.execute_sql(
        """
        INSERT INTO session_pickups
        SELECT
            window_start AS session_start,
            window_end AS session_end,
            PULocationID AS pickup_location_id,
            COUNT(*) AS trip_count
        FROM TABLE(
            SESSION(
                TABLE green_trips,
                DESCRIPTOR(event_timestamp),
                INTERVAL '5' MINUTES
            )
        )
        GROUP BY window_start, window_end, PULocationID
        """
    ).wait()


if __name__ == "__main__":
    session_job()