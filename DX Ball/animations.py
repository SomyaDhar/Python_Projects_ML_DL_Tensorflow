import tkinter
import time


_root_window = tkinter.Tk()
_root_window.title('Animation test')

_canvas = tkinter.Canvas(_root_window, width=500, height=300)
_canvas.pack()

tid = _canvas.create_polygon(10,10, 10,70, 50,40, fill='red')

for i in range(100):
	_canvas.move(tid, 5, 0)
	_root_window.update()
	time.sleep(0.005)



_root_window.mainloop()


