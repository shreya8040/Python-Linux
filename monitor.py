from textout import t
import plotext as plt


v=list(range(len(t)))
s=[100]*len(t)

plt.canvas_color('black')

plt.ylim(0,100)

plt.bar(v,t)

plt.show()
