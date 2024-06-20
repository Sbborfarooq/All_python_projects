from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES     # type: ignore


def change(text="type",src='english',dest='urdu'):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb_sor.get()
    d=comb_dest.get()
    #now getting the data from source txt
    msg=sor_tex.get(1.0,END)
    textget=change(text=msg,src=s,dest=d)
    dest_tex.delete(1.0,END) 
    dest_tex.insert(END,textget)






root=Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg='red')

lbl_txt=Label(root,text='Translator',font=("Time New Roman ",40,"bold"))
lbl_txt.place(x=100,y=40,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)

lbl_txt=Label(root,text='Source Text',font=("Time New Roman ",20,"bold"),fg='black',bg='red')
lbl_txt.place(x=100,y=100,height=20,width=300)

sor_tex=Text(frame,font=("Time New Roman ",40,"bold"),wrap=WORD)
sor_tex.place(x=10,y=130,height=100,width=480)

#now making the combobox 
list_text=list(LANGUAGES.values())
comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=250,height=40,width=150)
comb_sor.set('english')

#button
button_change=Button(frame,text='Translate',relief=RAISED,command=data)
button_change.place(x=170,y=250,height=40,width=150)

comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=250,height=40,width=150) #here is how the x is placed button x is 120 + width 100=220 so 
comb_dest.set('english') # the comb_dest placment will be started from 230 in x same we can count for all the other 


lbl_txt=Label(root,text='Destination Text',font=("Time New Roman ",20,"bold"),fg='black',bg='red')
lbl_txt.place(x=10,y=300,height=20,width=490)


dest_tex=Text(frame,font=("Time New Roman ",20,"bold"),wrap=WORD)
dest_tex.place(x=10,y=340,height=150,width=480)




























root.mainloop()