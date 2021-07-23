import tkinter
import tkinter.ttk
import random
from insertion_sort import insertion_sort

APP_WIDTH = 900

root_window = tkinter.Tk()
root_window.title('Insertion sort visualizer')
root_window.config(bg='black')

my_var1 = tkinter.IntVar()
my_var2 = tkinter.StringVar()

my_min = tkinter.IntVar()
my_max = tkinter.IntVar()
my_size = tkinter.IntVar()

arr = []

def selected():
    if my_var1.get() == 0:
        print('Random')
    elif my_var1.get() == 1:
        print('Manual')

def displayBar(arr, colorMap):
    c.delete('all')
    cw = APP_WIDTH
    ch = 500
    xw = cw / (len(arr)+1)
    off = 50
    s = 20
    
    norm_data = [i/max(arr) for i in arr]
    
    for i,h in enumerate(norm_data):
        x0 = i*xw + off + s
        y0 = ch - h*400
        
        x1 = (i+1) * xw + off
        y1 = ch
        
        c.create_rectangle(x0, y0, x1, y1, fill=colorMap[i])
        c.create_text((x0+x1)/2, y0-5, text=str(arr[i]))
    root_window.update_idletasks()
    



def initialize_values():
    
    global arr
    arr = []
    minVal = int(my_min.get())
    maxVal = int(my_max.get())
    size = int(my_size.get())
    print(minVal, maxVal, size)

    for _ in range(size):
        arr.append(random.randrange(minVal, maxVal+1))
    
    print(arr)
    displayBar(arr, ['red' for i in range(len(arr))])
    
def startAlgo():
    global arr
    speed = int(slider_animation.get())
    insertion_sort(arr, displayBar, speed)
        

# root window
f = tkinter.ttk.Frame(root_window, width=APP_WIDTH, height=100)
f.grid(row=0, column=0, padx = 10, pady = 10)

c = tkinter.Canvas(root_window, width=APP_WIDTH, height=500, bg='gray')
c.grid(row=1, column=0, padx=10, pady=10)


# add items inside frame
rb_rand_val = tkinter.ttk.Radiobutton(f, text='Random Number', variable=my_var1, value=0, command=selected)
rb_rand_val.grid(row=0,column=0, padx=10, pady=5)

minVal = tkinter.Scale(f, from_=0, to=5, variable=my_min, label='Min Value')
minVal.grid(row=0,column=1, padx=10, pady=5)

maxVal = tkinter.Scale(f, from_=5, to=100, variable=my_max, label='Max Value')
maxVal.grid(row=0,column=2, padx=10, pady=5)

size = tkinter.Scale(f, from_=0, to=100, variable=my_size, label='Size')
size.grid(row=0,column=3, padx=10, pady=5)

rb_man_val = tkinter.ttk.Radiobutton(f, text='Manual Number', variable=my_var1, value=1, command=selected)
rb_man_val.grid(row=0,column=4, padx=10, pady=5)

inp_man_num = tkinter.ttk.Entry(f, width=20, textvariable=my_var2)
inp_man_num.grid(row=0,column=5, padx=10, pady=5)

btn_man = tkinter.ttk.Button(f, text='Generate', command=initialize_values)
btn_man.grid(row=0, column=6, padx=10, pady=5)

# lbl_animation = tkinter.ttk.Label(f, text='Animation Speed: ')
# lbl_animation.grid(row=1, column=0, padx=10, pady=5)

slider_animation = tkinter.Scale(f, from_=0.1, to=2.0, length=200, resolution=0.2, digits=2, orient=tkinter.HORIZONTAL, label='Speed')
slider_animation.grid(row=1, column=0,padx=10, pady=5)

btn_sort = tkinter.ttk.Button(f, text='Start Sorting', command=startAlgo)
btn_sort.grid(row=1, column=1, padx=10, pady=5)

root_window.mainloop()