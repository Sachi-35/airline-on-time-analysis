**Airline Performance Analysis**

**Project Overview**

This project analyzes airline performance based on flight data from 2019. The analysis focuses on understanding trends in flight delays, cancellations, passenger traffic, and airline-specific performance metrics.


Objectives: 
  Identify patterns in flight delays and cancellations.
  Analyze passenger traffic trends.
  Visualize and interpret the performance of major airlines.


Datasets:
Flight Data (2019):
  Contains airline names, journey dates, source and destination airports, and other flight details.
Delay Data (2019):
  Monthly flight delay counts by major airlines.
Cancellation Data (2019):
  Flights canceled by each airline monthly.
Passenger Traffic Data (2019):
  Monthly passenger counts for all airlines.


Features: 
Data Cleaning: Handling missing values, removing duplicates, and merging datasets.
Analysis:
  Monthly trends in flight delays and cancellations.
  Passenger traffic distribution.
  Performance metrics for major airlines.
Visualizations: Line plots, bar charts, and heatmaps to represent insights.


How to Run the Project:
Clone this repository:
  git clone https://github.com/Sachi-35/airline-on-time-analysis.git


Install dependencies:
  Clone this repository:
    pip install -r requirements.txt
  Run the preprocessing script to clean and merge the data:
    python scripts/data_preprocessing.py
  Run the analysis script to generate visualizations:
    python scripts/analysis.py

Results:
Visualizations showcasing:
  Airlines with the highest delays and cancellations.
  Seasonal trends in passenger traffic.
  Performance comparison of airlines.

Dependencies:
Python 3.8 or above

Libraries:
pandas,
numpy,
matplotlib,
seaborn, and,
scikit-learn

License:
This project is licensed under the MIT License.
