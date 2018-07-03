# Create an engine to the census database
from sqlalchemy import create_engine, MetaData, Table, select, and_

engine = create_engine(
    'postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

# Use the .table_names() method on the engine to print the table names
print(engine.table_names())

metadata = MetaData()

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Create a select query: stmt
stmt = select([census]).where(census.columns.sex == 'F')

# Execute the query to retrieve all the data returned: results
results = engine.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2008
for result in results:
    print(result.age, result.sex, result.pop2008)

stmt = select([census]).where(census.columns.state.in_(['New York', 'Texas']))

# Loop over the ResultProxy and print the state and its population in 2000
for result in engine.execute(stmt):
    print(result.state, result.pop2000)

# Select only non-male records from California using and_
stmt = select([census]).where(
    and_(
        census.columns.state == 'California',
        census.columns.sex != 'M'
    )
)

# Loop over the ResultProxy printing the age and sex
for result in engine.execute(stmt):
    print(result.age, result.sex)

