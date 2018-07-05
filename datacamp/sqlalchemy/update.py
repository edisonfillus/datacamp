# Import create_engine function
from sqlalchemy import create_engine, MetaData, Table, select, update

# Create an engine to the census database
engine = create_engine('sqlite:///./data/census.sqlite')

metadata = MetaData()

state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)

# Build a select statement: select_stmt
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')

results = engine.execute(select_stmt).fetchall()

# Print the results of executing the select_stmt
print(results[0].keys())
print(results)

# Build a statement to update the fips_state to 36: stmt
stmt = update(state_fact).values(fips_state=36)
print(stmt)

# Append a where clause to limit it to records for New York state
stmt = stmt.where(state_fact.columns.name == 'New York')

# Execute the statement: results
results = engine.execute(stmt)

# Print rowcount
print(results.rowcount)

# Execute the select_stmt again to view the changes
print(engine.execute(select_stmt).fetchall())

# Build a statement to update the notes to 'The Wild West': stmt
stmt = update(state_fact).values(notes='The Wild West')

# Append a where clause to match the West census region records
stmt = stmt.where(state_fact.columns.census_region_name == 'West')

print(stmt)

# Execute the statement: results
results = engine.execute(stmt)

# Print rowcount
print(results.rowcount)