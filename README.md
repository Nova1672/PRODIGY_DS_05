# PRODIGY_DS_05
# Traffic Accident Data Visualization

## Overview
This Python script analyzes and visualizes traffic accident data using Pandas, Matplotlib, and Seaborn. The script creates several informative visualizations that help understand patterns and distributions in accident occurrences based on various factors.

## Features
- **Data Loading**: Reads traffic accident data from a CSV file (`traffic_accidents.csv`)
- **DateTime Conversion**: Properly converts the crash date to datetime format
- **Multiple Visualizations**: Generates six different plots showing accident distributions

## Visualizations Included
1. **Weather Condition Distribution**: Shows accidents by different weather conditions
2. **Lighting Condition Distribution**: Displays accidents by time of day lighting conditions
3. **Hourly Accident Distribution**: Histogram of accidents throughout the day (24 hours)
4. **Crash Type Distribution**: Breakdown of accidents by primary collision type
5. **Road Surface Condition**: Accidents categorized by roadway surface conditions
6. **Road Alignment**: Accident distribution based on road alignment (straight, curved, etc.)

## Requirements
- Python 3.x
- pandas
- matplotlib
- seaborn

## Usage
1. Ensure you have the required libraries installed (`pip install pandas matplotlib seaborn`)
2. Place your `traffic_accidents.csv` file in the same directory
3. Run the script: `python main.py`

## Output
The script will display six separate matplotlib figures showing the different accident distributions. Each plot is sized for clarity (12x6 inches) and uses Seaborn's whitegrid style for clean visualization.

## Customization
You can easily modify:
- Figure sizes by changing the `figsize` parameter
- Color schemes by adding Seaborn palette parameters
- Sort orders by modifying the `order` parameter in countplots

This script provides a comprehensive starting point for analyzing traffic accident patterns and can be extended with additional visualizations or statistical analyses as needed.
