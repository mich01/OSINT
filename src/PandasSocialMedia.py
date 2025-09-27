import pandas as pd
# Load data into a pandas DataFrame
data = pd.read_csv('../Data/social_media_data.csv')

sample_data = pd.concat([data] * 100, ignore_index=True)
sample_data.to_csv('../Data/social_media_data.csv.csv', index=False)
print("Generated sample CSV with 100 rows saved as 'sample_osint_data.csv'")
# Filter and analyze data
top_users = sample_data.groupby('Platform')['Followers'].sum()
print(top_users)
