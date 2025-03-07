import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "/mnt/data/nutrition.csv"
df = pd.read_csv(file_path)

# Display basic information about the dataset
print(df.info())
print(df.head())

# Summary statistics
summary_stats = df.describe()
print(summary_stats)

# Histogram of calories
plt.figure(figsize=(8, 5))
plt.hist(df["calories"], bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Calories")
plt.ylabel("Frequency")
plt.title("Distribution of Calories")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Scatter plot of calories vs fats
plt.figure(figsize=(8, 5))
plt.scatter(df["fats"], df["calories"], color='red', alpha=0.5)
plt.xlabel("Fats (g)")
plt.ylabel("Calories")
plt.title("Calories vs Fats")
plt.grid(True)
plt.show()

# Scatter plot of protein vs carbohydrates
plt.figure(figsize=(8, 5))
plt.scatter(df["protein"], df["carbohydrates"], color='green', alpha=0.5)
plt.xlabel("Protein (g)")
plt.ylabel("Carbohydrates (g)")
plt.title("Protein vs Carbohydrates")
plt.grid(True)
plt.show()

# Pie chart of macronutrient distribution (average values)
avg_values = df[['protein', 'carbohydrates', 'fats']].mean()
labels = ['Protein', 'Carbohydrates', 'Fats']
colors = ['blue', 'orange', 'red']
plt.figure(figsize=(6, 6))
plt.pie(avg_values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title("Average Macronutrient Distribution")
plt.show()

# Bar chart of top 10 highest calorie foods
top_calories = df[['label', 'calories']].sort_values(by='calories', ascending=False).head(10)
plt.figure(figsize=(10, 5))
plt.barh(top_calories['label'], top_calories['calories'], color='purple')
plt.xlabel("Calories")
plt.ylabel("Food Items")
plt.title("Top 10 Highest Calorie Foods")
plt.gca().invert_yaxis()
plt.show()

# Line chart of calorie trends across food items
plt.figure(figsize=(12, 5))
plt.plot(df['label'][:20], df['calories'][:20], marker='o', linestyle='-', color='blue')
plt.xticks(rotation=90)
plt.xlabel("Food Items")
plt.ylabel("Calories")
plt.title("Calorie Trends Across First 20 Food Items")
plt.grid(True)
plt.show()
