import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [7,8,9,10,11,12]

plt.scatter(x,y, label = 'Scatter Chart', color = 'red')
plt.xlabel('Days')
plt.ylabel('Distance')
plt.title('Workout')
plt.legend()
plt.show()