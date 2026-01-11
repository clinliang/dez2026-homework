import sys
import pandas as pd

print('arguments', sys.argv)
# sys.argv: ['pipline.py', '12']
month = int(sys.argv[1])

df = pd.DataFrame({"week":[1,2,3,4], "num_passengers":[40,50,60,70]})
df['month'] = month
print(df)

df.to_parquet(f"output_{month}.parquet")

print(f'Hello from mdp_nytaxi, {month}th month!')