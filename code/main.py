import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Load and preprocess data
df = pd.read_csv('movies.csv')
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Set overall aesthetics
sns.set_style("darkgrid")
sns.set_context("poster")
sns.set_palette("viridis")

# Initialize and create the plot
plt.figure(figsize=(16, 12))
scatter = sns.scatterplot(
    x=df['RATING'],
    y=df['RunTime'],
    hue=df['RunTime'],
    size=df['RunTime'],
    sizes=(20, 200),   # Adjust point sizes
    alpha=0.7,         # Transparency
    edgecolor=None     # Remove edge color
)

# Customize the plot
plt.title('Movie Runtime vs. Rating', fontsize=20)
plt.xlabel('Rating', fontsize=16)
plt.ylabel('Runtime (minutes)', fontsize=16)
plt.legend(title='Runtime', bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend position

# Remove the top and right spines for a cleaner look
sns.despine()

# Display the plot
plt.tight_layout()  # Ensure layout is optimized
plt.show()
