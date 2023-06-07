import os
import pandas as pd

# Specify the directory path (use '.' for the current directory)
directory_path = 'data/btcusdt_210601_210924'

# Get the list of files and directories in the specified directory
dir_entries = os.listdir(directory_path)

# Filter out directories, leaving only files
files = [entry for entry in dir_entries if os.path.isfile(os.path.join(directory_path, entry))]

# Sort the files alphabetically
sorted_files = sorted(files)

# Initialize an empty DataFrame to store the aggregated results

#for num in [1,5,10,15,30,60]:
aggregated_data_list = []

# Loop through the sorted file names
for file_name in sorted_files:
    # Check if the file is a CSV file
    if file_name.endswith('.csv'):
        # Read the CSV file into a DataFrame
        data = pd.read_csv(os.path.join(directory_path, file_name))

        # Perform the aggregation function (e.g., calculate the mean)
        data['midpoint'] = (data['ask1'] + data['bid1'] )/ 2
        data1 = data[['threshold_time_ms', 'midpoint']]
        data1.index = pd.to_datetime(data1["threshold_time_ms"], unit='ms')
        data2 = data[['midpoint']]
        resampled_df = data1.resample(str(1)+ 'D').agg({'midpoint': ['first', 'last', 'max', 'min', 'mean']}) #T is number of minutes


        # Flatten the multi-level column names
        resampled_df.columns = ['open', 'close', 'high', 'low', 'mean']

        # Append the aggregated result to the aggregated_data list
        aggregated_data_list.append(resampled_df)

# Concatenate all DataFrames in the aggregated_data_list
aggregated_data = pd.concat(aggregated_data_list)

# Save the aggregated_data DataFrame to a new CSV file
aggregated_data.to_csv('aggregated_data_' + str(1) + '_day_intervals.csv')