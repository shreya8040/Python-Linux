from textout import t
import plotext as plt
<<<<<<< HEAD
l=len(t)
v=[l]
v=t
s = [100,100,100,100,100,100,100,100]
z= plt.bar(v,s)
=======
v=list(range(len(t)))
s=[100]*len(t)

plt.canvas_color('black')
plt.plot_size(100,20)
plt.ylim(0,100)

plt.bar(v,t)
>>>>>>> b198608 (update)
plt.show()
