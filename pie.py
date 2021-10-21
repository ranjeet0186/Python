import matplotlib.pyplot as plt

slices = [23,45,10,22]
runs = ['Off Side', 'Leg Side', ' Front Foot', 'Covers']
col = ['green','blue','orange','yellow']
plt.pie(slices, labels=runs, colors=col)
plt.title('Virat Runs Chart')
plt.show()