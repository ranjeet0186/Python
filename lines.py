import matplotlib.pyplot as plt

x1= [1,2,3]
y1 = [5,7,8]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x1,y1, label = 'First Plot', color = 'blue')
plt.plot(x2,y2, label = 'Second Plot' , color = 'red')

plt.title('My Line Plot')
plt.xlabel('Employee')
plt.ylabel('Time')
plt.legend()
plt.show()