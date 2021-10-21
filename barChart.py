import matplotlib.pyplot as plt

x1 = [1,3,5,7,9]
y1 = [2,4,6,8,10]

x2 = [2,4,6,8,10]
y2 = [1,3,5,7,9]
plt.bar(x1,y1, label = 'Managers', color = 'blue')
plt.bar(x2,y2, label = 'Employees', color = 'green')
plt.title("Employee Matrix")
plt.xlabel('Employee')
plt.ylabel('Time')
plt.legend()
plt.show()
