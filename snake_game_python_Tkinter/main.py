import tkinter
from Snake import Snake

root = tkinter.Tk()
root.title('Snake')
root.resizable(False, False)

board = Snake()
board.pack()

root.mainloop()
