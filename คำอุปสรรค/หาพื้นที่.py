from tkinter import*
import tkinter.messagebox
RR = Tk()
RR.title("โปรแกรมการหาพื้นที่ต่างๆ");
RR.geometry('700x1200');
RR.option_add("*Font","K2D 25")
text2=Label(text="โปรแกรมคำนวณหาพื้นที่",fg="#1D6A96",bg="#D1EDE1").grid(row=1,column=1,padx=5,pady=20)
RR.configure(background="white")
RR.option_add("*Font","K2D 12")
myMenu =Menu()
RR.config(menu=myMenu)
menuitem = Menu()
def aa():
    newwindow = Tk()
    newwindow.title("หาพื้นที่รูปสี่เหลี่ยมจัตุรัส")
    newwindow.option_add("*Font","K2D 16")
    newwindow.geometry('700x1200');
    newwindow.configure(background="#D1EDE1")
    Label(newwindow,text='พื้นที่รปูสีเหลี่ยมจัตุรัส',bg="#AEE0DD").grid(row=1,column=1,padx=6,pady=20)
    number1 = IntVar()
    Label(newwindow,text='กรุณาใส่ด้าน',bg="white").grid(row=2,column=0,padx=5,pady=20)
    box1=Entry(newwindow,width=20,textvariable=number1)
    box1.grid(row=2,column=1,padx=5,pady=20)
    number2 = IntVar()
    Label(newwindow,text='กรุณาใส่ด้าน',bg="white").grid(row=3,column=0,padx=5,pady=20)
    box2=Entry(newwindow,width=20,textvariable=number2)
    box2.grid(row=3,column=1,padx=5,pady=20)
    Label(newwindow,text='แสดงผลลัพธ์',bg="white").grid(row=4,column=0,padx=5,pady=20)
    def God ():
        x = float(box1.get())
        y = float(box2.get())
        z = x*y
        Label(newwindow,text=z,bg="white").grid(row=4,column=1,padx=5,pady=20)
    def deletedata():
        box1.delete(0,END)
        box2.delete(0,END)
        Labe1(newwindow,text="คำว่าง",bg="white").grid(row=4,column=1,padx=5,pady=20)
    btn=Button(newwindow,text="คำนวณ",bg="#1D6A96",command=God).grid(row=5,column=0,padx=5,pady=20)
    btn=Button(newwindow,text="ลบข้อมูล",bg="#1D6A96",command=deletedata).grid(row=6,column=0,padx=5,pady=20)
    newwindow.mainloop
def bb():
    newwindow = Tk()
    newwindow.title("หาพื้นที่รูปสี่เหลี่ยมผืนผ้า")
    newwindow.option_add("*Font","K2D 16")
    newwindow.geometry('700x1200');
    newwindow.configure(background="#D1EDE1")
    Label(newwindow,text='พื้นที่ของรปูสีเหลี่ยมผืนผ้า',bg="#AEE0DD").grid(row=1,column=1,padx=6,pady=20)
    number1 = IntVar()
    Label(newwindow,text='กรุณาใส่ความกว้าง',bg="white").grid(row=2,column=0,padx=5,pady=20)
    box1=Entry(newwindow,width=20,textvariable=number1)
    box1.grid(row=2,column=1,padx=5,pady=20)
    number2 = IntVar()
    Label(newwindow,text='กรุณาใส่ความยาว',bg="white").grid(row=3,column=0,padx=5,pady=20)
    box2=Entry(newwindow,width=20,textvariable=number2)
    box2.grid(row=3,column=1,padx=5,pady=20)
    Label(newwindow,text='แสดงผลลัพธ์',bg="white").grid(row=4,column=0,padx=5,pady=20)
    def God ():
        x = float(box1.get())
        y = float(box2.get())
        z = x*y
        Label(newwindow,text=z,bg="white").grid(row=4,column=1,padx=5,pady=20)
    def deletedata():
        box1.delete(0,END)
        box2.delete(0,END)
        Labe1(newwindow,text="คำว่าง",bg="white").grid(row=4,column=1,padx=5,pady=20)
    btn=Button(newwindow,text="คำนวณ",bg="#1D6A96",command=God).grid(row=5,column=0,padx=5,pady=20)
    btn=Button(newwindow,text="ลบข้อมูล",bg="#1D6A96",command=deletedata).grid(row=6,column=0,padx=5,pady=20)
    newwindow.mainloop
def cc():
    newwindow = Tk()
    newwindow.title("หาพื้นที่รูปสามเหลี่ยม")
    newwindow.option_add("*Font","K2D 16")
    newwindow.geometry('700x1200');
    newwindow.configure(background="#D1EDE1")
    Label(newwindow,text='พื้นที่รปูสามเหลี่ยม',bg="#AEE0DD").grid(row=1,column=1,padx=6,pady=20)
    number1 = IntVar()
    Label(newwindow,text='กรุณาใส่ฐาน',bg="white").grid(row=2,column=0,padx=5,pady=20)
    box1=Entry(newwindow,width=20,textvariable=number1)
    box1.grid(row=2,column=1,padx=5,pady=20)
    number2 = IntVar()
    Label(newwindow,text='กรุณาใส่สูง',bg="white").grid(row=3,column=0,padx=5,pady=20)
    box2=Entry(newwindow,width=20,textvariable=number2)
    box2.grid(row=3,column=1,padx=5,pady=20)
    Label(newwindow,text='แสดงผลลัพธ์',bg="white").grid(row=4,column=0,padx=5,pady=20)
    def God ():
        x = float(box1.get())
        y = float(box2.get())
        z = 1/2*x*y
        Label(newwindow,text=z,bg="white").grid(row=4,column=1,padx=5,pady=20)
    def deletedata():
        box1.delete(0,END)
        box2.delete(0,END)
        Labe1(newwindow,text="คำว่าง",bg="white").grid(row=4,column=1,padx=5,pady=20)
    btn=Button(newwindow,text="คำนวณ",bg="#1D6A96",command=God).grid(row=5,column=0,padx=5,pady=20)
    btn=Button(newwindow,text="ลบข้อมูล",bg="#1D6A96",command=deletedata).grid(row=6,column=0,padx=5,pady=20)
    newwindow.mainloop
def dd():
    newwindow = Tk()
    newwindow.title("หาพื้นที่รูปวงกลม")
    newwindow.option_add("*Font","K2D 16")
    newwindow.geometry('700x1200');
    newwindow.configure(background="#D1EDE1")
    Label(newwindow,text='พื้นที่รปูวงกลม',bg="#AEE0DD").grid(row=1,column=1,padx=6,pady=20)
    number1 = IntVar()
    Label(newwindow,text='กรุณาใส่รัศมี',bg="white").grid(row=2,column=0,padx=5,pady=20)
    box1=Entry(newwindow,width=20,textvariable=number1)
    box1.grid(row=2,column=1,padx=5,pady=20)
    def God ():
        x = float(box1.get())
        z = 3.14*x*x
        Label(newwindow,text=z,bg="red").grid(row=4,column=1,padx=5,pady=20)
    def deletedata():
        box1.delete(0,END)
        Labe1(newwindow,text="คำว่าง",bg="white").grid(row=4,column=1,padx=5,pady=20)
    btn=Button(newwindow,text="คำนวณ",bg="#1D6A96",command=God).grid(row=5,column=0,padx=5,pady=20)
    btn=Button(newwindow,text="ลบข้อมูล",bg="#1D6A96",command=deletedata).grid(row=6,column=0,padx=5,pady=20)
    newwindow.mainloop
def ee() :
    newwindow = Tk()
    newwindow.title("หาพื้นที่รูปสี่เหลี่ยมด้านขนาน")
    newwindow.option_add("*Font","K2D 16")
    newwindow.geometry('700x1200');
    newwindow.configure(background="#D1EDE1")
    Label(newwindow,text='พื้นที่ของรปูสีเหลี่ยมด้านขนาน',bg="#AEE0DD").grid(row=1,column=1,padx=6,pady=20)
    number1 = IntVar()
    Label(newwindow,text='กรุณาใส่ฐาน',bg="white").grid(row=2,column=0,padx=5,pady=20)
    box1=Entry(newwindow,width=20,textvariable=number1)
    box1.grid(row=2,column=1,padx=5,pady=20)
    number2 = IntVar()
    Label(newwindow,text='กรุณาใส่สูง',bg="white").grid(row=3,column=0,padx=5,pady=20)
    box2=Entry(newwindow,width=20,textvariable=number2)
    box2.grid(row=3,column=1,padx=5,pady=20)
    Label(newwindow,text='แสดงผลลัพธ์',bg="white").grid(row=4,column=0,padx=5,pady=20)
    def God ():
        x = float(box1.get())
        y = float(box2.get())
        z = x*y
        Label(newwindow,text=z,bg="white").grid(row=4,column=1,padx=5,pady=20)
    def deletedata():
        box1.delete(0,END)
        box2.delete(0,END)
        Labe1(newwindow,text="คำว่าง",bg="white").grid(row=4,column=1,padx=5,pady=20)
    btn=Button(newwindow,text="คำนวณ",bg="#1D6A96",command=God).grid(row=5,column=0,padx=5,pady=20)
    btn=Button(newwindow,text="ลบข้อมูล",bg="#1D6A96",command=deletedata).grid(row=6,column=0,padx=5,pady=20)
    newwindow.mainloop
def ff():
    newwindow = Tk()
    newwindow.title("หาพื้นที่รูปสี่เหลี่ยมรูปว่าว")
    newwindow.option_add("*Font","K2D 16")
    newwindow.geometry('700x1200');
    newwindow.configure(background="#D1EDE1")
    Label(newwindow,text='พื้นที่ของรปูสีเหลี่ยมรูปว่าว',bg="#AEE0DD").grid(row=1,column=1,padx=6,pady=20)
    number1 = IntVar()
    Label(newwindow,text='กรุณาใส่ผลคูณของเส้นทแยงมุม',bg="white").grid(row=2,column=0,padx=5,pady=20)
    box1=Entry(newwindow,width=20,textvariable=number1)
    box1.grid(row=2,column=1,padx=5,pady=20)
    def God ():
        x = float(box1.get())
        z = x*1/2
        Label(newwindow,text=z,bg="white").grid(row=4,column=1,padx=5,pady=20)
    def deletedata():
        box1.delete(0,END)
        box2.delete(0,END)
        Labe1(newwindow,text="คำว่าง",bg="white").grid(row=4,column=1,padx=5,pady=20)
    btn=Button(newwindow,text="คำนวณ",bg="#1D6A96",command=God).grid(row=5,column=0,padx=5,pady=20)
    btn=Button(newwindow,text="ลบข้อมูล",bg="#1D6A96",command=deletedata).grid(row=6,column=0,padx=5,pady=20)
    newwindow.mainloop
def boxshow():
    tkinter.messagebox.showinfo("คณะผู้จัดทำ","นายกฤติน ไชยราบ\nนายภูริรักษ์ ลิ่มรุฑานนท์")
menuitem.add_command(label="หาพื้นที่รูปสี่เหลี่ยมจัตุรัส",command = aa)
menuitem.add_command(label="หาพื้นที่รูปสี่เหลี่ยมผืนผ้า",command = bb)
menuitem.add_command(label="หาพื้นที่รูปสามเหลี่ยม",command = cc)
menuitem.add_command(label="หาพื้นที่รูปวงกลม",command = dd)
menuitem.add_command(label="หาพื้นที่รูปสี่เหลี่ยมด้านขนาน",command = ee)
menuitem.add_command(label="หาพื้นทรูปสี่เหลี่ยมรูปว่าว",command = ff)
myMenu.add_cascade(label="หมวดหมู่",menu=menuitem)
myMenu.add_cascade(label="คณะผู้จัดทำ",command = boxshow)
photo = PhotoImage(file="aa.png")
btn=Button(RR,image = photo,bg="#FE7773",command=aa).grid(row=5,column=0,padx=5,pady = 20)
photo1 = PhotoImage(file="bb.png")
btn=Button(RR,image = photo1,bg="#85B8CB",command=bb).grid(row=5,column=1,padx=5,pady = 20)
photo2 = PhotoImage(file="cc.png")
btn=Button(RR,image = photo2,bg="#028C6A",command=cc).grid(row=5,column=2,padx=5,pady = 20)
photo3 = PhotoImage(file="dd.png")
btn=Button(RR,image = photo3,bg="#D1EDE1",command=dd).grid(row=6,column=0,padx=5,pady = 20)
photo4 = PhotoImage(file="ee.png")
btn=Button(RR,image = photo4,bg="#1D6A96",command=ee).grid(row=6,column=1,padx=5,pady = 20)
photo5 = PhotoImage(file="ff.png")
btn=Button(RR,image = photo5,bg="#FCDFF3",command=ff).grid(row=6,column=2,padx=5,pady = 20)
RR.mainloop()
