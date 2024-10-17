from tkinter import *
from tkinter import ttk

root = Tk()
root.title("แปลงค่าคำอุปสรรค")

# Input_1
choice_101 = IntVar()  # เก็บค่าจาก number_1
choice_102 = StringVar()  # เก็บค่าจาก combo_1

Label(text="โปรดเลือกคำอุปสรรค", font=30, padx=100).grid(row=0, column=1)

number_1 = Entry(font=30, width=30, textvariable=choice_101)
number_1.grid(row=1, column=1)

combo_1 = ttk.Combobox(width=10, font=30, textvariable=choice_102)
combo_1["values"] = ("E", "P", "T", "G", "M", "k", "h", "da","No")
combo_1.grid(row=1, column=2)

######################################################################################################

# Input_2
choice_201 = StringVar()  # เก็บค่าจาก combo_2

Label(text="โปรดเลือกคำอุปสรรค", font=30, padx=100).grid(row=0, column=4)

number_2 = Entry(font=30, width=30)
number_2.grid(row=1, column=4)

combo_2 = ttk.Combobox(width=10, font=30, textvariable=choice_201)
combo_2["values"] = ("E", "P", "T", "G", "M", "k", "h", "da","No")
combo_2.grid(row=1, column=5)


##############################################################################################################

def calculater():
    No = choice_101.get()
    Prefixes = choice_102.get()
    Prefixes_2 = choice_201.get()

    if Prefixes == "E":
        Prefixes = 10 ** 18
    if Prefixes == "P":
        Prefixes = 10 ** 15
    if Prefixes == "T":
        Prefixes = 10 ** 12
    if Prefixes == "G":
        Prefixes = 10 ** 9
    if Prefixes == "M":
        Prefixes = 10 ** 6
    if Prefixes == "k":
        Prefixes = 10 ** 3
    if Prefixes == "h":
        Prefixes = 10 ** 2
    if Prefixes == "da":
        Prefixes = 10 ** 1
    if Prefixes == "No":
        Prefixes = 1

    result = (No * Prefixes)


    if Prefixes_2 == "E":
        Prefixes_2 = 10 ** 18
    if Prefixes_2 == "P":
        Prefixes_2 = 10 ** 15
    if Prefixes_2 == "T":
        Prefixes_2 = 10 ** 12
    if Prefixes_2 == "G":
        Prefixes_2 = 10 ** 9
    if Prefixes_2 == "M":
        Prefixes_2 = 10 ** 6
    if Prefixes_2 == "k":
        Prefixes_2 = 10 ** 3
    if Prefixes_2 == "h":
        Prefixes_2 = 10 ** 2
    if Prefixes_2 == "da":
        Prefixes_2 = 10 ** 1
    if Prefixes_2 == "No":
        Prefixes_2 = 1

    result_2 = result/Prefixes_2

    number_2.delete(0, END)
    number_2.insert(0,result_2)

Button(text="แปลงค่า", font=25, width=15,command=calculater).grid(row=3, column=3)
Button(text="ล้างค่า", font=25, width=15).grid(row=4, column=3)

root.mainloop()

