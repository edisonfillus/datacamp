# import pandas
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, MetaData, Table, select, func

engine = create_engine(
    'postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([census.columns.state, func.count(census.columns.age)]).group_by(census.columns.state)
results = engine.execute(stmt).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()

# Plot the DataFrame
df.plot.bar()
plt.show()