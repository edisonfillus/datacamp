# Import insert and select from sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float, Boolean, insert, select, func

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

# Create a insert statement for census: stmt
stmt = insert(census)

csv_reader = open('./data/census.csv', mode='rt')

# Create an empty list and zeroed row count: values_list, total_rowcount
values_list = []
total_rowcount = 0

# Enumerate the rows of csv_reader
for idx, row in enumerate(csv_reader):
    # create data and append to values_list
    data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3], 'pop2008': row[4]}
    values_list.append(data)

    # Check to see if divisible by 51
    if idx % 50 == 0:
        results = engine.execute(stmt, values_list)
        total_rowcount += results.rowcount
        values_list = []

if len(values_list) > 0:
    results = engine.execute(stmt, values_list)
    total_rowcount += results.rowcount

# Print total rowcount
print(total_rowcount)

# Build a select statement to validate the insert
stmt = select([func.count(census)])

# Print the result of executing the query.
print(stmt, ' = ', engine.execute(stmt).scalar())
