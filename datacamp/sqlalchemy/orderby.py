# Create an engine to the census database
from sqlalchemy import create_engine, MetaData, Table, select, desc

engine = create_engine(
    'postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

metadata = MetaData()

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)


# Build a query to select the state column, order by state
stmt = select([census.columns.state]).order_by(census.columns.state)

# Execute the query and store the results: results
results = engine.execute(stmt).fetchall()

# Print the first 10 results
print(results[:10])

# Build a query to select the state column, Order by state in descending order
stmt = select([census.columns.state]).order_by(desc(census.columns.state))

# Execute the query and store the results: rev_results
rev_results = engine.execute(stmt).fetchall()

# Print the first 10 rev_results
print(rev_results[:10])

# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])

# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records: results
results = engine.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])