import pandas as pd
import ydata_profiling
# Load OSINT data into a DataFrame
data = pd.read_csv('../Data/social_media_data.csv')
# Generate the data profile report
profile = data.profile_report(title='OSINT Data Profile')
# Save the report to HTML
profile.to_file(output_file="osint_data_profile.html")
