import tkinter

_root_window = tkinter.Tk()
_root_window.title('Shape test')

_canvas = tkinter.Canvas(_root_window, width=500, height=300)
_canvas.pack()

_canvas.create_rectangle(20, 20, 100, 150)
_canvas.create_line(0,0,500,300)
_canvas.create_polygon(20,20, 70,40, 240,200, 50,70)


_root_window.mainloop()


