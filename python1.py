import pandas as pd
import matplotlib.pyplot as plt
data = {
    'ID': ['001', '002', '003', '004'],
    'Team': ['Australia', 'India', 'West Indies', 'England'],
    'Win': [78, 63, 43, 52],
    'Lost': [25, 30, 35, 39],
    'No Result': [1, 1, 0, 1],
    'Tie': [1, 1, 2, 1],
    'Total': [105, 95, 80, 93]}
CWC = pd.DataFrame(data)
print("Teams having more than 50 wins:")
print(CWC[CWC['Win'] > 50])
#new_row = {'ID': '005', 'Team': 'New Zealand', 'Win': 59, 'Lost': 38, 'No Result': 1, 'Tie': 1, 'Total': 99}CWC = CWC._append(new_row, ignore_index=True)
#CWC['Title Won'] = [6, 2, 2, 1, 0]
#print("\nTotal number of rows in the DataFrame:", len(CWC))
#print("\nUpdated DataFrame:")print(CWC)

