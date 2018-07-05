# Import insert and select from sqlalchemy
from sqlalchemy import delete, create_engine, MetaData, Table, Column, String, Integer, insert, select, func, and_

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

def populate_census():

    # Create a insert statement for census: stmt
    stmt = insert(census)

    csv_reader = open('./data/census.csv', mode='rt')

    # Create an empty list and zeroed row count: values_list, total_rowcount
    values_list = []
    total_rowcount = 0

    # Enumerate the rows of csv_reader
    for idx, row in enumerate(csv_reader):
        row = row.rstrip('\n').replace('\"','').split(",")
        #  create data and append to values_list
        data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3], 'pop2008': row[4]}
        values_list.append(data)

        # Check to see if divisible by 51
        if idx % 50 == 0:
            results = engine.execute(stmt, values_list)
            total_rowcount += results.rowcount
            values_list = []

    csv_reader.close()

    if len(values_list) > 0:
        results = engine.execute(stmt, values_list)
        total_rowcount += results.rowcount


populate_census()

# Build a statement to empty the census table: stmt
stmt = delete(census)

# Execute the statement: results
results = engine.execute(stmt)

# Print affected rowcount
print(results.rowcount)

# Print the results of executing the statement to verify there are no rows
print(engine.execute(select([func.count(census)])).scalar())

populate_census()

# Build a statement to count records using the sex column for Men ('M') age 36: stmt
stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the select statement and use the scalar() fetch method to save the record count
to_delete = engine.execute(stmt).scalar()

# Build a statement to delete records from the census table: stmt_del
stmt_del = delete(census)

# Append a where clause to target Men ('M') age 36
stmt_del = stmt_del.where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the statement: results
results = engine.execute(stmt_del)

# Print affected rowcount and to_delete record count, make sure they match
print(results.rowcount, to_delete)