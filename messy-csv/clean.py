import pandas as pd
df = pd.read_csv('food_delivery_orders.csv')
print(df.shape)
# print(df.head())

print(df.isnull().sum())
print(df.duplicated().sum())


category_mapping = {
    "FAST FOOD": "Fast Food",
    "Fast Food": "Fast Food",
    "fast food": "Fast Food",
    "Fastfood": "Fast Food",
    "Fast-Food": "Fast Food",
    "Italian": "Italian",
    "ITALIAN": "Italian",
    "italian": "Italian",
    "Itallian": "Italian",
    "Asain": "Asian",
    "asian": "Asian",
    "Asian": "Asian",
    "ASIAN": "Asian",
    "mexican": "Mexican",
    "Mexican": "Mexican",
    "Mexcian": "Mexican",
    "MEXICAN": "Mexican",
    "indian": "Indian",
    "INDIAN": "Indian",
    "Indian": "Indian",
}

df['category']= df["category"].map(category_mapping)
# print(df['category'].unique())

df['city'] = df['city'].str.strip()
df['city'] = df['city'].str.title()
# print(df['city'].unique())

df ['order_date'] = pd.to_datetime(df['order_date'],format='mixed',dayfirst=False)
# print(df["order_date"].head(10))

df['amount'] = df["amount"].str.replace('$',"",regex=False)
df["amount"] = pd.to_numeric(df["amount"])
# print(df["amount"].head(10))
# print(df["amount"].isnull().sum())

df = df.drop_duplicates()
print(df.shape)

df["amount"] = df["amount"].fillna(df["amount"].median())
df['delivery_time_min'] = df["delivery_time_min"].fillna(df["delivery_time_min"].median())
df["customer_rating"] = df["customer_rating"].fillna(df["customer_rating"].median())

# print(df.isnull().sum())

df.loc[df["delivery_time_min"]<0,'delivery_time_min'] = df["delivery_time_min"].median()
df.loc[df['delivery_time_min']>120,"delivery_time_min"] = df["delivery_time_min"].median()

# print(df['delivery_time_min'].describe())
df.to_csv('cleaned_orders.csv',index=False)

df = pd.read_csv('cleaned_orders.csv')

# 1: What's the average order amount per category?

print(df.groupby("category")["amount"].mean())

# 2:Which city has the most orders?

print(df['city'].value_counts())

# 3: Average delivery time per restaurant
print(df.groupby("restaurant")["delivery_time_min"].mean())

#4: which restaurant has the highest average customer rating?
avg_ratings=df.groupby("restaurant")["customer_rating"].mean()
print(avg_ratings.idxmax())

#5: Total revenue (sum of amount) per city
print(df.groupby("city")["amount"].sum())

#6: How many orders came from each category?
print(df["category"].value_counts())

#7: Average customer rating per category
print(df.groupby("category")["customer_rating"].mean())

#8:Which category has the fastest average delivery time?

avg_delivery = df.groupby("category")["delivery_time_min"].mean()
print(avg_delivery)
print(avg_delivery.idxmin())

#9:Average order amount per city AND category combined
pivot = df.pivot_table(values='amount',index='city',columns='category',aggfunc='mean')
print(pivot)

#10: Is there a relationship between delivery time and customer rating?
correlation =df['delivery_time_min'].corr(df['customer_rating'])
print(correlation)