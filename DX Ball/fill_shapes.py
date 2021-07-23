import tkinter
import random

_root_window = tkinter.Tk()
_root_window.title('Fill Shape test')

_canvas = tkinter.Canvas(_root_window, width=500, height=300)
_canvas.pack()

def randRect(n):

	for i in range(n):
		x1 = random.randint(0, 400)
		y1 = random.randint(0, 200)
		x2 = x1 + random.randint(20, 100)
		y2 = y1 + random.randint(20, 100)

		_canvas.create_rectangle(x1, y1, x2, y2, fill='green')



randRect(50)
_root_window.mainloop()
