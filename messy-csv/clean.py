import pandas as pd
df = pd.read_csv('food_delivery_orders.csv')
print(df.shape)
print(df.head())

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
print(df['category'].unique())

df['city'] = df['city'].str.strip()
df['city'] = df['city'].str.title()
print(df['city'].unique())