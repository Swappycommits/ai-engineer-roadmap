import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:phase2pass@localhost:5555/postgres")

df = pd.read_csv('cleaned_orders.csv')
df.to_sql("orders",engine,if_exists="replace",index=False)

print("Data Loaded Successfully")
print(df.shape)