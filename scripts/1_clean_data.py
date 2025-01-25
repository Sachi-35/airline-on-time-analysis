import pandas as pd

# Load the datasets
flight_data = pd.read_csv('data/flight_data.csv')
delay_data = pd.read_csv('data/delay_data.csv')
cancellation_data = pd.read_csv('data/cancellation_data.csv')
passenger_data = pd.read_csv('data/passenger_data.csv')

# Handle missing values in flight_data
flight_data['Route'] = flight_data['Route'].fillna('Unknown')  
flight_data['Total_Stops'] = flight_data['Total_Stops'].fillna('Unknown') 
flight_data['Price'] = flight_data['Price'].fillna(0)  

# Handle missing values in delay_data
delay_data['May-19'] = delay_data['May-19'].fillna(delay_data['May-19'].median())  
delay_data['Jun-19'] = delay_data['Jun-19'].fillna(delay_data['Jun-19'].median()) 

# Handle missing values in cancellation_data
cancellation_data['January'] = cancellation_data['January'].fillna(cancellation_data['January'].median())  
cancellation_data['February'] = cancellation_data['February'].fillna(cancellation_data['February'].median())  
cancellation_data['March'] = cancellation_data['March'].fillna(cancellation_data['March'].median()) 
cancellation_data['April'] = cancellation_data['April'].fillna(cancellation_data['April'].median())  
cancellation_data['May'] = cancellation_data['May'].fillna(cancellation_data['May'].median()) 
cancellation_data['June'] = cancellation_data['June'].fillna(cancellation_data['June'].median())  

# Handle missing values in passenger_data
passenger_data['2019-20'] = passenger_data['2019-20'].fillna(0)  

# Save the cleaned data to new CSV files (or overwrite the existing ones)
flight_data.to_csv('data/flight_data_cleaned.csv', index=False)  
delay_data.to_csv('data/delay_data_cleaned.csv', index=False)  
cancellation_data.to_csv('data/cancellation_data_cleaned.csv', index=False)  
passenger_data.to_csv('data/passenger_data_cleaned.csv', index=False)  

print("Missing values filled, and cleaned data saved successfully!")