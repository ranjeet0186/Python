import matplotlib.pyplot as plt

slices = [33,24,50,15,7]

courses = ['Python','PHP','Java','R Language','Ruby']
cols = ['pink','yellow','green','blue','red']
plt.pie(slices, 
    labels=courses,
    colors=cols)
plt.title('Language Analysis')
plt.show()
