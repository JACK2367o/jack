import pandas as pd
import matplotlib.pyplot as plt

# Creating the initial DataFrame with given data
data = {
    'ID': ['001', '002', '003', '004'],
    'Team': ['Australia', 'India', 'West Indies', 'England'],
    'Win': [78, 63, 43, 52],
    'Lost': [25, 30, 35, 39],
    'No Result': [1, 1, 0, 1],
    'Tie': [1, 1, 2, 1],
    'Total': [105, 95, 80, 93]
}

CWC = pd.DataFrame(data)
print(CWC)

# Display the team having more than 50 wins
print("Teams having more than 50 wins:")
print(CWC[CWC['Win'] > 50])

# Add a new row for New Zealand
new_row = {'ID': '005', 'Team': 'New Zealand', 'Win': 59, 'Lost': 38, 'No Result': 1, 'Tie': 1, 'Total': 99}
CWC = CWC._append(new_row, ignore_index=True)

# Add a new column 'Title Won'
CWC['Title Won'] = [6, 2, 2, 1, 0]

# Display total number of rows in DataFrame
print("\nTotal number of rows in the DataFrame:", len(CWC))

# Display the updated DataFrame
print("\nUpdated DataFrame:")
print(CWC)

# Draw a bar chart to visualize the performances (Wins of teams)
plt.figure(figsize=(10, 6))
plt.bar(CWC['Team'], CWC['Win'], color='skyblue')

# Add labels and title
plt.xlabel('Teams')
plt.ylabel('Number of Wins')
plt.title('Team Performances - Number of Wins')

# Add legend
plt.legend(['Wins'])

# Display the bar chart
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
