#importing the library 

from tkinter import *  #here * this symbol means import everything 
import setting 
import utils 
from cell import cell 

#now creating the basic window 
#overriding the setting of the window by all the below methods
root=Tk() #it will create the basic window 
root.configure(bg="black")
root.geometry(f'{setting.WIDTH}x{setting.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False,False)

 
"""calling our frame class in tkinter to make frames"""

top_frame=Frame(
    root,
    bg='black', #change it later
    width=setting.WIDTH,
    height=utils.height_percent(25) #25% of height
)
top_frame.place(x=0,y=0)   #this place method will tell whats our frames staring position 

#now making another frame
left_frame=Frame(root,
    bg='black',#change later
    width=utils.width_percent(25),
    height=utils.height_percent(75) #75% of the height           
                 )
left_frame.place(x=0,y=utils.height_percent(25))

#now creating the center frame
center_frame=Frame(
    root,
    bg='black',
    width=utils.width_percent(75),
    height=utils.height_percent(75)
)
center_frame.place(x=utils.width_percent(25),
                y=utils.height_percent(25))

#initating our cell class with for loop
for x in range(setting.GRID_SIZE):
    for y in range(setting.GRID_SIZE):
        c=cell(x,y)
        c.create_btn_obj(center_frame)
        c.cell_btn_obj.grid(
            column=x , row=y
            )

# print(cell.all)
#show the true false of obj_cells
# for c in cell.all:
#     print(c.is_mine)


#call the label from cell class
cell.create_cell_count_label(left_frame)
cell.cell_count_label_object.place(x=0,y=0)

cell.randomize_mines()








root.mainloop()      