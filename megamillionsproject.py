import pandas as pd
import plotly as px
import numpy as np
from matplotlib import pyplot as plt
df = pd.read_csv("/Users/petermarus/Downloads/megamillions_winning_numbers.csv")
ball_1 = df['ball1'].value_counts().nlargest(5)
ball_2 = df['ball2'].value_counts().nlargest(5)
ball_3 = df['ball3'].value_counts().nlargest(5)
ball_4 = df['ball4'].value_counts().nlargest(5)
ball_5 = df['ball5'].value_counts().nlargest(5)
megaball = df['megaball'].value_counts().nlargest(5)
jackpot_estimated = df['jackpot_estimated'].value_counts()


#Bar charts showing the five most common numbers drawn at each position

#ball 1
ball_1.plot(kind='bar')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Frequency of Numbers, First Ball')
plt.xticks(rotation=45)
plt.show()

#ball 2
ball_2.plot(kind='bar')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Frequency of Numbers, Second Ball')
plt.show()

#ball 3
ball_3.plot(kind='bar')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Frequency of Numbers, Third Ball')
plt.show()

#ball 4
ball_4.plot(kind='bar')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Frequency of Numbers, Fourth Ball')
plt.show()

#ball 5
ball_5.plot(kind='bar')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Frequency of Numbers, Fifth Ball')
plt.show()

#Megaball
megaball.plot(kind='bar')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Frequency of Numbers, Megaball')
plt.show()
