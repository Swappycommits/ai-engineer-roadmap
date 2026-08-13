import pandas as pd
from sqlalchemy import create_engine,text

engine = create_engine("postgresql://postgres:phase2pass@localhost:5555/postgres")

def run_query(sql):
    with engine.connect() as conn:
        result =pd.read_sql(text(sql),conn)
        return result
# Test query

# print(run_query("SELECT * FROM orders LIMIT 5"))

#1:Average order amount per category

#print(run_query("SELECT category,AVG(amount) AS avg_amount FROM orders GROUP BY category "))

# 2: Which city has the most orders?

#print(run_query("SELECT city,COUNT(*) AS order_count FROM orders GROUP BY city ORDER BY order_count DESC"))

#3: Average delivery time per restaurant

#print(run_query("SELECT restaurant,AVG(delivery_time_min) AS avg_del_time From orders GROUP BY restaurant"))

#4: Restaurant with the highest average customer rating

#print(run_query("SELECT restaurant, AVG(customer_rating) AS avg_rating FROM orders GROUP BY restaurant ORDER BY avg_rating DESC"))

#5:Total revenue per city

#print(run_query("SELECT city,SUM(amount) AS revenue FROM orders GROUP BY city ORDER BY revenue DESC"))

#6:Order count per category

#print(run_query("SELECT category, COUNT(*) AS order_count FROM orders GROUP BY category"))

#7:Average customer rating per category

#print(run_query("SELECT category, AVG(customer_rating) AS avg_rating FROM orders GROUP BY category"))

#8:Category with the fastest average delivery time

#print(run_query("SELECT category, AVG(delivery_time_min) AS avg_del_time FROM orders GROUP BY category ORDER BY avg_del_time DESC" ))

#9:Average order amount per city AND category

#print(run_query("SELECT city,category,AVG(amount) AS avg_amount FROM orders GROUP BY city,category ORDER BY city,category"))

#10:Correlation between delivery time and customer rating

#print(run_query("SELECT CORR(delivery_time_min,customer_rating) AS correlation FROM orders"))
