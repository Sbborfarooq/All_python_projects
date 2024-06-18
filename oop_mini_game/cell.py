
#importing the button class from tkinter
from tkinter import Button,Label
import setting
import random
import ctypes #library use to through generic messages and warnings
import sys


class cell:
    all=[]
    cell_count=setting.CELL_COUNT  #this is initial cell_count
    cell_count_label_object=None
    def __init__(self,x,y, is_mine=False):
       #below false means that value is false each of our cells at first

        self.is_mine=is_mine
        self.is_opned=False
        self.is_mine_canidate=False
        self.cell_btn_obj=None
        self.x=x
        self.y=y
        #append all the object to  cell.all list
        cell.all.append(self)



    #creating the instance mehtod that will create button 
    def create_btn_obj(self,location ):
        btn=Button(
            location,
            width=10,#increasing the button size 
            height=3,
           

        )
        btn.bind('<Button-1>',self.left_click_action)
        btn.bind('<Button-3>',self.right_click_action)
        self.cell_btn_obj=btn
    
    #this label is not belong to each of our cells that is the general
    #info about the game this is not mehtod to call with every object
    #thats why this is static method(this method is just the use case for calss not for the use case for the isntance) 
    @staticmethod
    def create_cell_count_label(location):
        lbl=Label(
                location,
                bg="black",
                fg='white',
                text=f'cell left.{cell.cell_count}',
                width=10,
                height=3,
                font=('',30)
                )
        cell.cell_count_label_object=lbl
    
    def left_click_action(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            #condition if cell is equal to zero then open the surrounding cells
            if self.surrounded_cell_mines_length==0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
    def get_cell_by_axis(self,x,y):
        #return the cell object based on the value of x,y
        for cell_obj  in cell.all:
            if cell_obj.x==x and cell_obj.y==y:
                return cell_obj #stop the iteration and return that cell_object
    @property #read only attribute
    def surrounded_cells(self):
        cells=[
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1)
                                                    ]
        #to remove none values we use list compherision 
        cells=[cell for cell in cells if cell is not None]
        return cells 
    @property
    def surrounded_cell_mines_length(self):
        counter=0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter+=1
        return counter


    def show_cell(self):
       
       if not self.is_opned:
            
            #every time thes show method is called it will decrease by one
            cell.cell_count-=1
            self.cell_btn_obj.configure(text=self.surrounded_cell_mines_length)

            #replace the text of cell count label with the newer count
            if cell.cell_count_label_object:
                cell.cell_count_label_object.configure(
                    text=f'cell left.{cell.cell_count}'
                        )
            #if this was a mine canidate, then for safety we should
            #conffigure the background color to SystemButtonFace
            self.cell_btn_obj.configure( bg="SystemButtonFace")
                
        #mark the cell as opned (use is as the last line of this method)
       self.is_opned=True
    def show_mine(self):
    #A logic to intrupt the game and display a message that a player is lost
        self.cell_btn_obj.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0,'you clicked on a mine','Game over',0)
        sys.exit()
    def right_click_action(self,event):
        if not self.is_mine_canidate:
            self.cell_btn_obj.configure(
                bg="orange"
            )
            self.is_mine_canidate=True
        else:
            self.cell_btn_obj.configure(
                bg="SystemButtonFace"
            )
            self.is_mine_canidate=False
    #now making the mines in game by using static method 
    @staticmethod
    def randomize_mines(): #take random cells and make them min
        picked_cells=random.sample(cell.all,setting.MINES_COUNTS)
        for picked_cell in picked_cells:
            picked_cell.is_mine=True


    def __repr__(self):#representation of our object
        return f"cell({self.x},{self.y})"
        