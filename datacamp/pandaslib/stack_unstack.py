import pandas as pd

users = pd.DataFrame()

#                 visitors  signups
# city   weekday
# Austin Mon           326        3
#        Sun           139        7
# Dallas Mon           456        5
#        Sun           237       12

# Unstack users by 'weekday': byweekday
byweekday = users.unstack('weekday')

# Print the byweekday DataFrame
print(byweekday)

#         visitors      signups
# weekday      Mon  Sun     Mon Sun
# city
# Austin       326  139       3   7
# Dallas       456  237       5  12

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level='weekday'))