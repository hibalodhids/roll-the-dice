import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = data = {
    "Name": ["Ali", "Sara", "Omar", "Aisha", "Hassan", "Fatima"],
    "Math": [88, 76, 90, 65, 70, 95],
    "Science": [92, 70, 85, 60, 78, 89],
    "StudyHours": [10, 8, 12, 5, 7, 15]
}

df = pd.DataFrame(data)

# 2. Average score
df["Average"] = df[["Math", "Science"]].mean(axis=1)
print("Average Marks:\n", df[["Name", "Average"]])

# 3. Highest score
print("\nHighest Math score:", df["Math"].max())
print("Highest Science score:", df["Science"].max())

# 4. Visualization: Bar plot
sns.barplot(x="Name", y="Average", data=df)
plt.title("Average Marks of Students")
plt.show()