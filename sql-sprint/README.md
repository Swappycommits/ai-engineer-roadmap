# SQL Analyst Sprint

The same 10 analytical questions from the Messy CSV project, answered in SQL against a real PostgreSQL database instead of Pandas - to directly compare the two approaches on identical data.

## Setup

PostgreSQL runs in a Docker container:
docker run --name phase2-postgres -e POSTGRES_PASSWORD=phase2pass -p 5555:5432 -d postgres

The cleaned dataset from the previous project is loaded into a table called "orders" using SQLAlchemy and psycopg2.

## Usage

Start the Postgres container if it isn't running:
docker start phase2-postgres

Load the data (only needs to be run once, or whenever the data changes):
python load_data.py

Run the analysis:
python queries.py

## The 10 questions, in SQL

1. Average order amount per category
2. Which city has the most orders
3. Average delivery time per restaurant
4. Restaurant with the highest average customer rating
5. Total revenue per city
6. Order count per category
7. Average customer rating per category
8. Category with the fastest average delivery time
9. Average order amount per city and category combined
10. Correlation between delivery time and customer rating

Every result matched the Pandas answers from the previous project exactly, confirming both tools converge on the same truth about the data when used correctly.

## Pandas to SQL mapping

.groupby(col) -> GROUP BY col
.mean() -> AVG(...)
.sum() -> SUM(...)
.value_counts() -> COUNT(*) with GROUP BY
.idxmax() -> ORDER BY ... DESC LIMIT 1
pivot_table -> GROUP BY on multiple columns (long format instead of wide grid)
.corr() -> CORR(col1, col2)

## What I learned
- Running PostgreSQL locally via Docker, including real troubleshooting of port conflicts
- Connecting Python to Postgres using SQLAlchemy and psycopg2
- Loading a Pandas DataFrame directly into a SQL table with .to_sql()
- Writing GROUP BY, aggregate functions (AVG, SUM, COUNT, CORR), and ORDER BY/LIMIT in raw SQL
- The direct conceptual mapping between Pandas operations and their SQL equivalents
- SQL requires explicit sorting (ORDER BY) where Pandas sometimes sorts automatically
- The value of cross-checking two tools that should produce the same answer, and catching a real discrepancy in the process