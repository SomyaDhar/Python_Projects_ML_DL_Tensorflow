import tkinter
from PIL import  Image, ImageTk   # conda install pillow
import math

class Snake(tkinter.Canvas):
	def __init__(self):
		super().__init__(height=630, width=620, background="black", highlightthickness=0)
		self.score = 0
		self.snake_position = [(160,300),(140,300),(120,300),(100,300), (80,300), (60,300), (40,300)]
		self.food_position = (500,100)

		self.direction = 'Right'
		self.bind_all("<Key>", self.on_key_press)

		try:
			self.snake_img = Image.open('./images/snake.png')
			self.snake_body = ImageTk.PhotoImage(self.snake_img)
			self.food_img = Image.open('./images/food.png')
			self.food = ImageTk.PhotoImage(self.food_img)
		except IOError as err:
			print(err)

		self.create_text(80, 50, text=f"Score: {self.score}", fill='#FFF', font=('TkDefaultFont', 24))
		for x,y in self.snake_position:
			self.create_image(x, y, image=self.snake_body, tag='snake')

		self.create_image(*self.food_position, image=self.food, tag='food')

		self.after(200, self.actions) # game speed


	def move(self):
		headX, headY = self.snake_position[0]

		if self.direction == 'Left':
			new_head_pos = (headX - 20, headY)
		elif self.direction == 'Right':
			new_head_pos = (headX + 20, headY)
		elif self.direction == 'Down':
			new_head_pos = (headX, headY + 20)
		elif self.direction == 'Up':
			new_head_pos = (headX, headY - 20)

		self.snake_position = [new_head_pos] + self.snake_position[:-1]
		self.food_collision()

		for s, p in zip(self.find_withtag('snake'), self.snake_position):
			self.coords(s,p)


	def actions(self):
		self.food_collision()

		if self.collision_check():
			print('Game Over')
			return
		self.move()
		
		self.after(200, self.actions)



	def collision_check(self):
		headX, headY = self.snake_position[0]
		return (headX, headY) in self.snake_position[1:] or (headX < 1 or headX > 619) or (headY<1 or headY>629)


	def on_key_press(self, e):
		new_direction = e.keysym
		self.direction = new_direction
		print(self.direction)

    def food_collision(self):
        for pos in self.food_position: 			         
            if pos == self.snake_position[0]: 
				#self.food_position.remove(pos) 
				self.set_new_food_position() 

	def set_new_food_position(self):
		x = random.randint(1, 619) 
        y = random.randint(1, 629) 
        for pos in self.snake_position: 
            if pos == [x, y]: 
                self.set_new_food_position() 
        self.food_position.append([x, y])

       