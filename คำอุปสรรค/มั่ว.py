from tkinter import *
from tkinter import ttk
root = Tk()
root.title("แปลงค่าคำอุปสรรค")

# Input_1
choice_101 = IntVar() # เก็บค่าจาก number_1
choice_102 = StringVar()  # เก็บค่าจาก combo_1

Label(text="โปรดเลือกคำอุปสรรค",font=30,padx=100).grid(row=0,column=1)

number_1 = Entry(font=30,width=30,textvariable=choice_101)
number_1.grid(row=1,column=1)

combo_1 = ttk.Combobox(width=10,font=30,textvariable=choice_102)
combo_1["values"] = ("E","P","T","G","M","k","h","da")
combo_1.grid(row=1,column=2)

######################################################################################################

# Input_2
choice_201 = StringVar() # เก็บค่าจาก combo_2

Label(text="โปรดเลือกคำอุปสรรค",font=30,padx=100).grid(row=0,column=4)

number_2 = Entry(font=30,width=30)
number_2.grid(row=1,column=4)

combo_2 = ttk.Combobox(width=10,font=30,textvariable=choice_201)
combo_2["values"] = ("E","P","T","G","M","k","h","da")
combo_2.grid(row=1,column=5)

##############################################################################################################

def calculater():


Button(text="แปลงค่า",font=25,width=15).grid(row=3,column=3)
Button(text="ล้างค่า",font=25,width=15).grid(row=4,column=3)




root.mainloop()
