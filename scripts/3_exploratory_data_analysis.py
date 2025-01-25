import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# Load the dataset
file_path = "data/combined_data.csv"  # Adjust to your file path
combined_data = pd.read_csv(file_path)

# Convert necessary columns to datetime
combined_data['Date_of_Journey'] = pd.to_datetime(combined_data['Date_of_Journey'], format='%d/%m/%Y', errors='coerce')
combined_data['Dep_Time'] = pd.to_datetime(combined_data['Dep_Time'], format='%H:%M', errors='coerce')
combined_data['Arrival_Time'] = pd.to_datetime(combined_data['Arrival_Time'], format='%H:%M', errors='coerce')

# Parse Duration column to minutes
def parse_duration(duration_str):
    hours, minutes = 0, 0
    if 'h' in duration_str:
        hours = int(duration_str.split('h')[0])
    if 'm' in duration_str:
        minutes = int(duration_str.split('h')[-1].split('m')[0]) if 'h' in duration_str else int(duration_str.split('m')[0])
    return hours * 60 + minutes

combined_data['Duration'] = combined_data['Duration'].apply(parse_duration)

# Extract additional date-related information
combined_data['Month'] = combined_data['Date_of_Journey'].dt.month
combined_data['DayOfWeek'] = combined_data['Date_of_Journey'].dt.dayofweek
combined_data['Dep_Hour'] = combined_data['Dep_Time'].dt.hour

# General Distribution of Flights

# Distribution of Total Stops with customized color palette
plt.figure(figsize=(8, 6))
sns.countplot(x='Total_Stops', data=combined_data, palette='Blues')
plt.title('Distribution of Flights by Number of Stops', fontsize=16)
plt.xlabel('Number of Stops', fontsize=14)
plt.ylabel('Count of Flights', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Price Distribution
plt.figure(figsize=(8, 6))
sns.histplot(combined_data['Price'], kde=True, bins=30, color='green')
plt.title('Price Distribution', fontsize=16)
plt.xlabel('Price', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Flight Delays (Arrival and Departure)

# Calculate delays in minutes
combined_data['ArrivalDelay'] = (combined_data['Arrival_Time'] - combined_data['Dep_Time']).dt.total_seconds() / 60

# Distribution of Arrival Delays
plt.figure(figsize=(8, 6))
sns.histplot(combined_data['ArrivalDelay'], kde=True, bins=30, color='red')
plt.title('Arrival Delay Distribution', fontsize=16)
plt.xlabel('Arrival Delay (Minutes)', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Percentage of Delayed Flights
combined_data['Is_Delayed'] = combined_data['ArrivalDelay'].apply(lambda x: 1 if x > 0 else 0)
delay_percentage = combined_data['Is_Delayed'].mean() * 100
print(f"Percentage of Delayed Flights: {delay_percentage:.2f}%")

# Delay Trends by Month, Day of the Week, and Hour

# Delay Trend by Month
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='ArrivalDelay', data=combined_data, color='purple')
plt.title('Arrival Delay Trend by Month', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Arrival Delay (Minutes)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Delay Trend by Day of the Week
plt.figure(figsize=(10, 6))
sns.lineplot(x='DayOfWeek', y='ArrivalDelay', data=combined_data, color='brown')
plt.title('Arrival Delay Trend by Day of the Week', fontsize=16)
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Average Arrival Delay (Minutes)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Delay Trend by Hour of Departure
plt.figure(figsize=(10, 6))
sns.lineplot(x='Dep_Hour', y='ArrivalDelay', data=combined_data, color='teal')
plt.title('Arrival Delay Trend by Hour of Departure', fontsize=16)
plt.xlabel('Hour of Departure', fontsize=14)
plt.ylabel('Average Arrival Delay (Minutes)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Average Flight Duration by Airline
avg_duration_by_airline = combined_data.groupby('Airline')['Duration'].mean().sort_values()

plt.figure(figsize=(12, 6))
sns.barplot(x=avg_duration_by_airline.index, y=avg_duration_by_airline.values, palette='viridis')
plt.title('Average Flight Duration by Airline', fontsize=16)
plt.xlabel('Airline', fontsize=14)
plt.ylabel('Average Duration (Minutes)', fontsize=14)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Average Price by Airline
avg_price_by_airline = combined_data.groupby('Airline')['Price'].mean().sort_values()

plt.figure(figsize=(12, 6))
sns.barplot(x=avg_price_by_airline.index, y=avg_price_by_airline.values, palette='magma')
plt.title('Average Price by Airline', fontsize=16)
plt.xlabel('Airline', fontsize=14)
plt.ylabel('Average Price', fontsize=14)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Average Price vs. Duration
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Duration', y='Price', data=combined_data, color='blue')
plt.title('Average Price vs. Duration', fontsize=16)
plt.xlabel('Duration (Minutes)', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# --- 10. Correlation Heatmap ---
correlation_matrix = combined_data[['Duration', 'Price', 'ArrivalDelay', 'Dep_Hour', 'Month', 'DayOfWeek']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# KDE Plot of Price
plt.figure(figsize=(8, 6))
sns.kdeplot(combined_data['Price'], shade=True, color='purple')
plt.title('KDE Plot of Price', fontsize=16)
plt.xlabel('Price', fontsize=14)
plt.ylabel('Density', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Pie Chart for Delayed vs On-time Flights
delay_counts = combined_data['Is_Delayed'].value_counts()
labels = ['On-time', 'Delayed']
colors = ['lightgreen', 'lightcoral']

plt.figure(figsize=(8, 6))
plt.pie(delay_counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'edgecolor': 'black'})
plt.title('Percentage of Delayed vs On-time Flights', fontsize=16)
plt.show()