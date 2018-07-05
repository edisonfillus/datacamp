
# Import create_engine function
from sqlalchemy import create_engine, MetaData, Table, select, update

# Create an engine to the census database
engine = create_engine('sqlite:///./data/census.sqlite')

metadata = MetaData()

state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)
flat_census = Table('flat_census', metadata, autoload=True, autoload_with=engine)


# Build a statement to select name from state_fact: stmt
fips_stmt = select([state_fact.columns.name])

# Append a where clause to Match the fips_state to flat_census fips_code
fips_stmt = fips_stmt.where(state_fact.columns.fips_state == flat_census.columns.fips_code)

print(fips_stmt)


# Build an update statement to set the name to fips_stmt: update_stmt
update_stmt = update(flat_census).values(state_name=fips_stmt)

# Execute update_stmt: results
results = engine.execute(update_stmt)

# Print rowcount
print(results.rowcount)