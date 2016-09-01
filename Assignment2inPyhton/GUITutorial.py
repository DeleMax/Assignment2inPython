'''
Created on Jul 30, 2016

@author: DELEMAX
'''

from tkinter import*

root = Tk()

label_l = Label(root, text = "File Name")
entry_1 = Entry(root)


label_l.grid(row=0)


entry_1.grid(row=0, column=1)


c_1 = Checkbutton(root, text= "Use Kruskal's Algorithm")
c_2 = Checkbutton(root, text= "Use Prim's Algorithm")

c_1.grid(columnspan=2)
c_2.grid(columnspan=2)

button_1 = Button(root, text = "Compute")
button_2 = Button(root, text = "Step")

button_1.grid(columnspan = 3)
button_2.grid(columnspan = 4)

root.mainloop()


label_2.grid(columnspan = 10)


c_1 = Checkbutton(root, text= "Use Kruskal's Algorithm")
c_2 = Checkbutton(root, text= "Use Prim's Algorithm")

c_1.grid(columnspan=2)
c_2.grid(columnspan=2)

button_1 = Button(root, text = "Compute", command= do)
button_2 = Button(root, text = "Step", command = loadme)

button_1.grid(columnspan = 3)
button_2.grid(columnspan = 4

