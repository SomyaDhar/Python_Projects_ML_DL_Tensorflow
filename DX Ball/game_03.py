import tkinter
import time
import random

_root_window = tkinter.Tk()
_root_window.title('game')
_root_window.resizable(0,0)
_root_window.wm_attributes('-topmost',1)


_canvas = tkinter.Canvas(_root_window, width=500, height=500)
_canvas.pack()
_root_window.update()

class Ball:

	def __init__(self, canvas, color):
		self.canvas = canvas
		self.x = random.randint(-5,5)
		self.y = 1
		self.canvas_width = self.canvas.winfo_width()
		self.canvas_height = self.canvas.winfo_height()
		self.ball_id = self.canvas.create_oval(10,10,40,40, fill=color)
		self.canvas.move(self.ball_id, self.canvas_width/2, self.canvas_height/2 - 100)
		self.score = 0

		
		
	def draw(self):
		pos = self.canvas.coords(self.ball_id)
		if pos[3] >= self.canvas_height:
			self.y = -1
		if pos[1] <= 0:
			self.y = 1
		if pos[0] <= 0:
			self.x = (-1) * self.x
		if pos[2] >= self.canvas_width:
			self.x = (-1) * self.x

		self.canvas.move(self.ball_id, self.x, self.y)

	def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
	



class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.Paddle_id = canvas.create_rectangle(0,0, 100, 10, fill=color)
        self.canvas.move(self.Paddle_id, 200, 300)
        self.speed = 0
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.speed, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.speed = 0
        if pos[2] >= 500:
            self.speed = 0

    def move_left(self, evt):
        self.speed = -2
    def move_right(self, evt):
        self.speed = 2




b = Ball(_canvas, 'blue')

#_root_window.mainloop()

while True:
	b.draw()
	_root_window.update_idletasks()
	_root_window.update()
	time.sleep(0.01)

go_label = canvas.create_text(250,200,text="GAME OVER",font=("Helvetica",30))
