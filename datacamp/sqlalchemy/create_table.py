# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float, Boolean

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

# Print table details
print(repr(data))


# Define a new table with a name, count, amount, and valid column: data
data2 = Table('data2', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print the table details
print(repr(metadata.tables['data2']))