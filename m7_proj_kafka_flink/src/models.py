import json
from dataclasses import dataclass, asdict

@dataclass
class GreenTrip:
    lpep_pickup_datetime: str # datatime as string for homework request
    lpep_dropoff_datetime: str # datatime as string for homework request
    PULocationID: int
    DOLocationID: int
    passenger_count: float
    trip_distance: float
    tip_amount: float
    total_amount: float

def greentrip_from_row(row):
    return GreenTrip(
        lpep_pickup_datetime = str(row["lpep_pickup_datetime"]),    # datatime as string for homework request
        lpep_dropoff_datetime = str(row["lpep_dropoff_datetime"]),   # datatime as string for homework request
        PULocationID=int(row['PULocationID']),
        DOLocationID=int(row['DOLocationID']),
        passenger_count=float(row['passenger_count']),
        trip_distance=float(row['trip_distance']),
        tip_amount=float(row['tip_amount']),
        total_amount=float(row['total_amount'])
    )

def greentrip_serializer(greentrip_obj):
    greentrip_dict = asdict(greentrip_obj)    
    greentrip_json = json.dumps(greentrip_dict).encode('utf-8')
    return greentrip_json


def greentrip_deserializer(greentrip_bytes):
    json_str = greentrip_bytes.decode('utf-8')
    greentrip_dict = json.loads(json_str)
    return GreenTrip(**greentrip_dict)


""" Workshop elements
@dataclass
class Ride:
    PULocationID: int
    DOLocationID: int
    trip_distance: float
    total_amount: float
    tpep_pickup_datetime: int  # epoch milliseconds


def ride_from_row(row):
    return Ride(
        PULocationID=int(row['PULocationID']),
        DOLocationID=int(row['DOLocationID']),
        trip_distance=float(row['trip_distance']),
        total_amount=float(row['total_amount']),
        tpep_pickup_datetime=int(row['tpep_pickup_datetime'].timestamp() * 1000),
    )


def ride_deserializer(ride_bytes):
    json_str = ride_bytes.decode('utf-8')
    ride_dict = json.loads(json_str)
    return Ride(**ride_dict)


def ride_serializer(ride_obj):
    ride_dict = asdict(ride_obj)    
    ride_json = json.dumps(ride_dict).encode('utf-8')
    return ride_json

"""