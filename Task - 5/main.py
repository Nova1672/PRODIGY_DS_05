import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

data = pd.read_csv('traffic_accidents.csv')
data['crash_date'] = pd.to_datetime(data['crash_date'])

plt.figure(figsize=(12, 6))
sns.countplot(data=data, y='weather_condition', order=data['weather_condition'].value_counts().index)
plt.title('Distribution of Accidents by Weather Condition')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=data, y='lighting_condition', order=data['lighting_condition'].value_counts().index)
plt.title('Distribution of Accidents by Lighting Condition')
plt.xlabel('Number of Accidents')
plt.ylabel('Lighting Condition')
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(data['crash_hour'], bins=24, kde=True)
plt.title('Distribution of Accidents by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=data, y='first_crash_type', order=data['first_crash_type'].value_counts().index)
plt.title('Distribution of Accidents by First Crash Type')
plt.xlabel('Number of Accidents')
plt.ylabel('First Crash Type')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=data, y='roadway_surface_cond', order=data['roadway_surface_cond'].value_counts().index)
plt.title('Distribution of Accidents by Roadway Surface Condition')
plt.xlabel('Number of Accidents')
plt.ylabel('Roadway Surface Condition')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=data, y='alignment', order=data['alignment'].value_counts().index)
plt.title('Distribution of Accidents by Road Alignment')
plt.xlabel('Number of Accidents')
plt.ylabel('Road Alignment')
plt.show()
