from sqlalchemy import create_engine, MetaData, Table, String, Integer, Column

engine = create_engine('sqlite://')  # in memory

metadata = MetaData()
# Define a new table with a name, count, amount, and valid column: data
census = Table('census', metadata,
               Column('state', String(255)),
               Column('sex', String(1)),
               Column('age', Integer()),
               Column('pop2000', Integer()),
               Column('pop2008', Integer())
               )

# Use the metadata to create the table
metadata.create_all(engine)

# Drop the census table
census.drop(engine)

# Check to see if state_fact exists
print(census.exists(engine))

# Drop all tables
metadata.drop_all(engine)

# Check to see if census exists
print(census.exists(engine))