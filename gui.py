try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *

master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()


w.create_rectangle(0, 0, 500, 500, fill="blue")
w.create_rectangle(100, 100, 400, 400, fill="yellow")
w.create_line(100, 0,  100, 100, fill="yellow", width=3)
w.create_line(200, 0,  200, 100, fill="yellow", width=3)
w.create_line(300, 0,  300, 100, fill="yellow", width=3)
w.create_line(400, 0,  400, 100, fill="yellow", width=3)

w.create_line(100, 400, 100, 500, fill="yellow", width=3)
w.create_line(200, 400, 200, 500, fill="yellow", width=3)
w.create_line(300, 400, 300, 500, fill="yellow", width=3)
w.create_line(400, 400, 400, 500, fill="yellow", width=3)

w.create_line(0, 100, 100, 100, fill="yellow", width=3)
w.create_line(0, 200, 100, 200, fill="yellow", width=3)
w.create_line(0, 300, 100, 300, fill="yellow", width=3)
w.create_line(0, 400, 100, 400, fill="yellow", width=3)

w.create_line(500, 100, 400, 100, fill="yellow", width=3)
w.create_line(500, 200, 400, 200, fill="yellow", width=3)
w.create_line(500, 300, 400, 300, fill="yellow", width=3)
w.create_line(500, 400, 400, 400, fill="yellow", width=3)

mainloop()
