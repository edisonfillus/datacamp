# Import insert and select from sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float, Boolean, insert, select

engine = create_engine('sqlite://')  # in memory

metadata = MetaData()
# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255)),
             Column('count', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
             )

# Use the metadata to create the table
metadata.create_all(engine)

# Build an insert statement to insert a record into the data table: stmt
stmt = insert(data).values(name='Anna', count=1, amount=1000.00, valid=True)

# Execute the statement via the connection: results
results = engine.execute(stmt)

# Print result rowcount
print(results.rowcount)

# Build a select statement to validate the insert
stmt = select([data]).where(data.columns.name == 'Anna')

# Print the result of executing the query.
print(engine.execute(stmt).first())
