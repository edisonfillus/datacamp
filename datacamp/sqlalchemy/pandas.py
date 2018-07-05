import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select, func

engine = create_engine(
    'postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([census.columns.state, func.count(census.columns.age)])
stmt = stmt.group_by(census.columns.state)
results = engine.execute(stmt).fetchall()

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)
