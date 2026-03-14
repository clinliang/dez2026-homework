from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import EnvironmentSettings, StreamTableEnvironment

print("DEBUG: Script started")
# 你的其他代码..

def create_source_table(t_env):
    ddl = """
        CREATE TABLE IF NOT EXISTS green_trips (
            PULocationID INT,
            DOLocationID INT,
            tip_amount DOUBLE,
            lpep_pickup_datetime VARCHAR,
            event_timestamp AS TO_TIMESTAMP(
                lpep_pickup_datetime,
                'yyyy-MM-dd HH:mm:ss'
            ),
            WATERMARK FOR event_timestamp AS
            event_timestamp - INTERVAL '5' SECOND
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
        CREATE TABLE IF NOT EXISTS hourly_revenue_sink (
            window_start TIMESTAMP(3),
            window_end TIMESTAMP(3),
            total_tip_amount DOUBLE,
            PRIMARY KEY (window_start) NOT ENFORCED
        ) WITH (
            'connector' = 'jdbc',
            'url' = 'jdbc:postgresql://postgres:5432/postgres',
            'table-name' = 'hourly_revenue',
            'username' = 'postgres',
            'password' = 'postgres',
            'driver' = 'org.postgresql.Driver'
        )
    """
    t_env.execute_sql(ddl)

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
    t_env = StreamTableEnvironment.create(env, environment_settings=settings)

    create_source_table(t_env)
    create_sink_table(t_env)

    t_env.execute_sql(
        """
        INSERT INTO hourly_revenue_sink
        SELECT
            window_start,
            window_end,
            SUM(tip_amount) AS total_tip_amount
        FROM TABLE(
            TUMBLE(
                TABLE green_trips,
                DESCRIPTOR(event_timestamp),
                INTERVAL '1' HOUR
            )
        )
        GROUP BY window_start, window_end
        """
    ).wait()

if __name__ == "__main__":
    main()