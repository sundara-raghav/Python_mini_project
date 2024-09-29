

import csv
import matplotlib.pyplot as plt

# Initialize data containers
years = []
population_data = {
    'Tamil Nadu': [],
    'Karnataka': [],
    'Kerala': [],
    'Andhra Pradesh': [],
    'Telangana': []
}

# Read the CSV file
with open(r'C:\Users\Sundara Raghav .G\OneDrive\Desktop\south_india_population_trend.csv.txt', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        years.append(int(row['Year']))
        for state in population_data.keys():
            population_data[state].append(float(row[state]))

# Bar chart: Population of South Indian States in 2020
states = list(population_data.keys())
population_2020 = [population_data[state][years.index(2020)] for state in states]  # Data for 2020

plt.bar(states, population_2020, color=['blue', 'green', 'red', 'orange', 'purple'])
plt.title('Population of South Indian States (2020)')
plt.xlabel('State')
plt.ylabel('Population (Millions)')
plt.show()

# Histogram: Distribution of populations in 2020
plt.hist(population_2020, bins=5, edgecolor='black', color='skyblue')
plt.title('Population Distribution in South Indian States (2020)')
plt.xlabel('Population (Millions)')
plt.ylabel('Frequency')
plt.show()

# Line graph: Population trends of South Indian States
for state, populations in population_data.items():
    plt.plot(years, populations, label=state, marker='o')

plt.title('Population Trends of South Indian States (2010-2025)')
plt.xlabel('Year')
plt.ylabel('Population (Millions)')
plt.legend()
plt.grid(True)
plt.show()

# Pie chart: Population distribution among South Indian States (2020)
plt.pie(population_2020, labels=states, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'orange', 'purple'])
plt.title('Population Distribution in South Indian States (2020)')
plt.show()
