import tkinter

# init tk
root = tkinter.Tk()

# create canvas
myCanvas = tkinter.Canvas(root, bg="yellow", height=400, width=400)

# draw arcs
coord = 10, 10, 300, 300
arc = myCanvas.create_arc(coord, start=0, extent=100, fill="blue")
arc1 = myCanvas.create_arc(coord, start=100, extent=140, fill="green")
arv2 = myCanvas.create_arc(coord, start=140, extent=220, fill="red")

# add to window and show
myCanvas.pack()
root.mainloop()
