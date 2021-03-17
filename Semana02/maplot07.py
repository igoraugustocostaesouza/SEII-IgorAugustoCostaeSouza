#Autor: Igor Augusto
#Data: 16/03/2021

x=[0,1,2,3,4]
y=[0,2,4,6,8]

plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='- -', makersize=10)
#plt.plot(x,y, 'r^--', label='2x')
plt.title('first graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize':20})
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8,10])

plt.legend()

plt.plot(show)
