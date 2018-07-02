# Import create_engine
from sqlalchemy import create_engine, Table, MetaData

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///./data/census.sqlite')

# Print table names
print(engine.table_names())

metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))

# Reflect the census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print the column names
print(census.columns.keys())

# Print full table metadata
print(repr(metadata.tables['census']))
