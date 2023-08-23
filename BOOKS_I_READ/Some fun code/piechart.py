import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu']
eating = [1,2,2,1]
sleeping = [7,6,8,8]
working = [7,8,8,8]
playing = [3,5,1,3]
plt.stackplot(days, eating,sleeping,working,playing, colors=['k','r','b','m'],
              labels=[eating,sleeping,working,playing])
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()