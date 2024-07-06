import pandas as pd

# Load the master file into a DataFrame
master_df = pd.read_csv('master_file.txt', sep='\s+', header=None)

# Identify event types
cv_indices = master_df[76] == 'dccv'
binary_indices = (master_df[78] == 'ombin') | (master_df[78] == 'omcassan')
single_indices = master_df[92] == 'dcnormffp'

# Extract relevant columns for each event type
cv_events = master_df[cv_indices][[0, 76, 77, 78, 79]]
binary_events = master_df[binary_indices][[0, 78, 79, 80, 81]]
single_events = master_df[single_indices][[0, 92, 93, 94, 95]]

# Rename columns for clarity
cv_events.columns = ['ID', 'EventType', 'RepeatedID', 'FilenameRoot', 'LightCurveNumber']
binary_events.columns = ['ID', 'EventType', 'Column', 'FilenameRoot', 'LightCurveNumber']
single_events.columns = ['ID', 'EventType', 'Column', 'FilenameRoot', 'LightCurveNumber']

# Combine all events into one DataFrame
all_events = pd.concat([cv_events, binary_events, single_events])

# Display the matched IDs with their respective light curves
print(all_events)
