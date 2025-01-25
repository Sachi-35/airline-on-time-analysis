import pandas as pd

# Load cleaned data
flight_data = pd.read_csv('data/flight_data_cleaned.csv')
delay_data = pd.read_csv('data/delay_data_cleaned.csv')
cancellation_data = pd.read_csv('data/cancellation_data_cleaned.csv')
passenger_data = pd.read_csv('data/passenger_data_cleaned.csv')

# Merge the datasets
# Merge flight_data with delay_data on 'Airline'
combined_data = pd.merge(flight_data, delay_data, how='left', left_on='Airline', right_on='Airlines')

# Merge with cancellation_data on 'Airline'
combined_data = pd.merge(combined_data, cancellation_data, how='left', left_on='Airline', right_on='Airlines')

# Merge with passenger_data on 'Source' (assuming 'Source' in flight_data corresponds to 'Airport' in passenger_data)
combined_data = pd.merge(combined_data, passenger_data, how='left', left_on='Source', right_on='Airport')

# Save the combined dataset for future use
combined_data.to_csv('data/combined_data.csv', index=False)

print("Datasets combined successfully and saved as 'combined_data.csv'.")