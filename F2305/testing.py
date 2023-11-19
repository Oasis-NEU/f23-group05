import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

weekdays = ["Monday, Tuesday, Wednesday, Thursday, Friday"]

data = [[45,68,35,74,95], [51,76,16,59,2], [52,59,77,71,78], [1, 2, 4, 1, 10], [78,99,92,48,95]]

rng = np.random.default_rng(2022)
df = pd.DataFrame({'Engagement': rng.integers(1000, 100000, 1000),
                   'Weekday': rng.integers(0, 7, 1000),
                   'Hour': rng.integers(7, 22, 1000)})


fig = px.imshow(data,
                labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
                x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                y=['Morning', 'Afternoon', 'Evening']
               )
fig.update_xaxes(side="top")
fig.show()


out = df.groupby(['Hour', 'Weekday'])['Engagement'].mean().unstack()
# print(df)
sns.heatmap(out)
plt.show()