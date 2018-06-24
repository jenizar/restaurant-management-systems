%config IPCompleter.greedy=True
from tkinter import*
from tkinter import messagebox
import random
import time;
import datetime
import psycopg2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A6
from decimal import Decimal

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management Systems")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width = 1600,height = 50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800,height = 700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300,height = 700, relief=SUNKEN)
f2.pack(side=RIGHT)

#====================================================Time==================================================
localtime=time.asctime(time.localtime(time.time()))  # Date time Function
#====================================================Info==================================================
lblDateTime = Label(Tops, font=('arial',15, 'bold'), text=localtime,fg="black", bd=10, anchor='w')
lblDateTime.grid(row=0,column=1)
lblDateTime = Label(Tops, font=('arial',11, 'bold'), text="User : John Eswin Nizar",fg="black", bd=10, anchor='w')
lblDateTime.grid(row=1,column=1)
lblInfo = Label(Tops, font=('arial',50, 'bold'), text="              Halal Resto                  ",fg="sienna", bd=10, anchor='w')
lblInfo.grid(row=2,column=0)
#====================================================Calculator=============================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
    
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():    
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)    
    operator=""
    
def Ref():   
    CoF = float(Fries.get())
    CoD = float(Drinks.get())
    CoFilet = float(Filet.get())
    CoBurger = float(Burger.get())
    CoChicBurger = float(Chicken_Burger.get())
    CoCheeseBurger = float(Cheese_Burger.get())
    
    CostofFries = CoF * 0.99
    CostofFries = round(CostofFries,2)
    CostofDrinks = CoD * 1.00
    CostofDrinks = round(CostofDrinks,2)
    CostofFilet = CoFilet * 2.99
    CostofFilet = round(CostofFilet,2)
    CostofBurger = CoBurger * 2.87
    CostofBurger = round(CostofBurger,2)
    CostChicken_Burger = CoChicBurger * 2.89
    CostChicken_Burger = round(CostChicken_Burger,2)
    CostCheese_Burger = CoCheeseBurger * 2.69
    CostCheese_Burger = round(CostCheese_Burger,2)
    
    Itm1.set(CostofFries)
    Itm2.set(CostofBurger)
    Itm3.set(CostofFilet)
    Itm4.set(CostChicken_Burger)
    Itm5.set(CostCheese_Burger)
    Itm6.set(CostofDrinks)    
    
    CostofMeal = "$", str('%.2f' % (CostofFries + CostofDrinks + CostofFilet + CostofBurger 
                                    + CostChicken_Burger + CostCheese_Burger))
    
    PayTax = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger 
                                    + CostChicken_Burger + CostCheese_Burger) * 0.2)
    
    PayTax = round(PayTax,2)
    
    TotalCost = (CostofFries + CostofDrinks + CostofFilet + CostofBurger 
                 + CostChicken_Burger + CostCheese_Burger)
    
    TotalCost = round(TotalCost,2)
    
    Ser_Charge = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger 
                 + CostChicken_Burger + CostCheese_Burger) * 0.1)
    
    Ser_Charge = round(Ser_Charge,2)
    
    Service = "$", str('%2.f' % Ser_Charge)
    
    OverAllCost = "$", str('%2.f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax = "$", str('%2.f' % PayTax)
    Service_Charge.set(Service) 
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
   
    Cost1.set(TotalCost)
    Cost2.set(PayTax)
    Cost3.set(Ser_Charge)
    Cost4 = PayTax + TotalCost + Ser_Charge  
    Cost4 = round(Cost4,2)
    Cost5.set(Cost4)
    
def sSave():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)
    
#==========================================PostgreSQL - save to database===========================================================    
    vbl1 = datetime.date.today()
    conn = psycopg2.connect(database = "resto", user = "admin", password = "admin", host = "127.0.0.1", port = "5432")
    print ("Opened database successfully")
    
    cur = conn.cursor()
    sql = "INSERT INTO sales.receipt VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    data = (rand.get(), vbl1, Fries.get(), Burger.get(), Filet.get(), 
              Chicken_Burger.get(), Cheese_Burger.get(), Drinks.get(), Cost1.get(), Cost2.get(), Cost3.get(), Cost5.get())    
        
    cur.execute(sql, data)    

    conn.commit()
    conn.close()      

#==========================================save to pdf===========================================================    
    ldate = DateofOrder.get()[:2] + DateofOrder.get()[3:5] + DateofOrder.get()[6:10]
    filename1 = 'BILL' + rand.get() + '_' + ldate + '.pdf' 
    c = canvas.Canvas(filename1, pagesize=A6)
    c.setFont('Helvetica', 8)
    c.drawString(55,400,"Halal Resto")
    c.drawString(15,390,"Receipt Ref:")
    c.drawString(65,390,rand.get())
    c.drawString(135,390,DateofOrder.get())
    c.drawString(15,380,"----------------------------------------------------------------")
    c.drawString(15,370,"Large Fries:")
    c.drawString(135,370,Fries.get())
    c.drawString(150,370,Itm1.get())   
    c.drawString(15,360,"Burger Meal:")
    c.drawString(135,360,Burger.get())
    c.drawString(150,360,Itm2.get())   
    c.drawString(15,350,"Filet_o_Meal:")
    c.drawString(135,350,Filet.get())
    c.drawString(150,350,Itm3.get())   
    c.drawString(15,340,"Chicken Meal:")
    c.drawString(135,340,Chicken_Burger.get())
    c.drawString(150,340,Itm4.get())   
    c.drawString(15,330,"Cheese Meal:")
    c.drawString(135,330,Cheese_Burger.get())
    c.drawString(150,330,Itm5.get())   
    c.drawString(15,320,"Drinks:")
    c.drawString(135,320,Drinks.get())
    c.drawString(150,320,Itm6.get())   
    c.drawString(15,310,"----------------------------------------------------------------") 
    c.drawString(15,300,"Sub Total:")
    c.drawString(85,300,'$')
    c.drawString(95,300,Cost1.get())
    c.drawString(15,290,"Tax:")
    c.drawString(85,290,'$')
    c.drawString(95,290,Cost2.get()) 
    c.drawString(15,280,"Service Charge:")
    c.drawString(85,280,'$')
    c.drawString(95,280,Cost3.get())
    c.drawString(15,270,"Total Cost:")
    c.drawString(85,270,'$')
    c.drawString(95,270,Cost5.get()) 
    c.showPage()
    c.save()    
     
def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy() 
        return  
    
def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    Chicken.set("")
    Cheese.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")    
    
    Fries.set("0")
    Burger.set("0")
    Filet.set("0")
    Chicken.set("0")
    Cheese.set("0")
    Drinks.set("0")
    Chicken_Burger.set("0")
    Cheese_Burger.set("0")       
    
txtDisplay = Entry(f2,font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, 
                   insertwidth=4, bg="seashell2", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="7", bg="seashell2", command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="8", bg="seashell2", command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="9", bg="seashell2", command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="+", bg="seashell2", command=lambda: btnClick("+")).grid(row=2,column=3)
#===============================================================================================
btn4=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="4", bg="seashell2", command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="5", bg="seashell2", command=lambda: btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="6", bg="seashell2", command=lambda: btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="-", bg="seashell2", command=lambda: btnClick("-")).grid(row=3,column=3)
#================================================================================================
btn1=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="1", bg="seashell2", command=lambda: btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="2", bg="seashell2", command=lambda: btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="3", bg="seashell2", command=lambda: btnClick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="*", bg="seashell2", command=lambda: btnClick("*")).grid(row=4,column=3)
#================================================================================================
btn0=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="0", bg="seashell2", command=lambda: btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="C", bg="seashell2", command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="=", bg="seashell2", command=btnEqualsInput).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=16, fg="black", font=('arial',20,'bold'),
            text="/", bg="seashell2", command=lambda: btnClick("/")).grid(row=5,column=3)
#======================================Restaurant Info 1===========================================
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
Chicken = StringVar()
Cheese = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()

Fries.set("0")
Burger.set("0")
Filet.set("0")
Chicken.set("0")
Cheese.set("0")
Drinks.set("0")
Chicken_Burger.set("0")
Cheese_Burger.set("0") 

# PostgreSQL
Cost1 = StringVar()
Cost2 = StringVar()
Cost3 = StringVar()
Cost5 = StringVar()

# Pdf
Itm1 = StringVar()
Itm2 = StringVar()
Itm3 = StringVar()
Itm4 = StringVar()
Itm5 = StringVar()
Itm6 = StringVar()

DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%Y"))

lblReference = Label(f1,font=('arial', 16,'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0,column=0)
txtReference = Entry(f1,font=('arial', 16,'bold'), textvariable=rand, bd=10, 
                     insertwidth=4, bg="gray82", justify='right')
txtReference.grid(row=0,column=1)

lblFries = Label(f1,font=('arial', 16,'bold'), text="Large Fries", bd=16, anchor='w')
lblFries.grid(row=1,column=0)
txtFries = Entry(f1,font=('arial', 16,'bold'), textvariable=Fries, bd=10, 
                     insertwidth=4, bg="pale green", justify='right')
txtFries.grid(row=1,column=1)

lblBurger = Label(f1,font=('arial', 16,'bold'), text="Burger Meal", bd=16, anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger = Entry(f1,font=('arial', 16,'bold'), textvariable=Burger, bd=10, 
                     insertwidth=4, bg="pale green", justify='right')
txtBurger.grid(row=2,column=1)

lblFilet = Label(f1,font=('arial', 16,'bold'), text="Filet_o_Meal", bd=16, anchor='w')
lblFilet.grid(row=3,column=0)
txtFilet = Entry(f1,font=('arial', 16,'bold'), textvariable=Filet, bd=10, 
                     insertwidth=4, bg="pale green", justify='right')
txtFilet.grid(row=3,column=1)

lblChicken = Label(f1,font=('arial', 16,'bold'), text="Chicken Meal", bd=16, anchor='w')
lblChicken.grid(row=4,column=0)
txtChicken = Entry(f1,font=('arial', 16,'bold'), textvariable=Chicken_Burger, bd=10, 
                     insertwidth=4, bg="pale green", justify='right')
txtChicken.grid(row=4,column=1)

lblCheese = Label(f1,font=('arial', 16,'bold'), text="Cheese Meal", bd=16, anchor='w')
lblCheese.grid(row=5,column=0)
txtCheese = Entry(f1,font=('arial', 16,'bold'), textvariable=Cheese_Burger, bd=10, 
                     insertwidth=4, bg="pale green", justify='right')
txtCheese.grid(row=5,column=1)

#======================================Restaurant Info 2=====================================================
lblDrinks = Label(f1,font=('arial', 16,'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('arial', 16,'bold'), textvariable=Drinks, bd=10, 
                  insertwidth=4, bg="pale green", justify='right')
txtDrinks.grid(row=0,column=3)

lblCost = Label(f1,font=('arial', 16,'bold'), text="Cost of Meal", bd=16, anchor='w')
lblCost.grid(row=1,column=2)
txtCost = Entry(f1,font=('arial', 16,'bold'), textvariable=Cost, bd=10, 
                insertwidth=4, bg="#ffffff", justify='right')
txtCost.grid(row=1,column=3)

lblSubTotal = Label(f1,font=('arial', 16,'bold'), text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=2,column=2)
txtSubTotal = Entry(f1,font=('arial', 16,'bold'), textvariable=SubTotal, bd=10, 
                    insertwidth=4, bg="#ffffff", justify='right')
txtSubTotal.grid(row=2,column=3)

lblService = Label(f1,font=('arial', 16,'bold'), text="Service Charge", bd=16, anchor='w')
lblService.grid(row=3,column=2)
txtService = Entry(f1,font=('arial', 16,'bold'), textvariable=Service_Charge, bd=10, 
                   insertwidth=4, bg="#ffffff", justify='right')
txtService.grid(row=3,column=3)

lblStateTax = Label(f1,font=('arial', 16,'bold'), text="Tax", bd=16, anchor='w')
lblStateTax.grid(row=4,column=2)
txtStateTax = Entry(f1,font=('arial', 16,'bold'), textvariable=Tax, bd=10, 
                    insertwidth=4, bg="#ffffff", justify='right')
txtStateTax.grid(row=4,column=3)

lblTotalCost = Label(f1,font=('arial', 16,'bold'), text="Total Cost", bd=16, anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost = Entry(f1,font=('arial', 16,'bold'), textvariable=Total, bd=10, 
                     insertwidth=4, bg="#ffffff", justify='right')
txtTotalCost.grid(row=5,column=3)

#======================================Button=====================================================
btnTotal=Button(f1,padx=16,pady=8, bd=14, fg="black",font=('arial', 12,'bold'), width=10, 
               text="Total", bg="green", command = Ref).grid(row=7, column=0) 
btnSave=Button(f1,padx=16,pady=8, bd=14, fg="black",font=('arial', 12,'bold'), width=10, 
               text="Save", bg="yellow", command = sSave).grid(row=7, column=1)
btnReset=Button(f1,padx=16,pady=8, bd=14, fg="black",font=('arial', 12,'bold'), width=10, 
               text="Reset", bg="lavender", command = Reset).grid(row=7, column=2)
btnExit=Button(f1,padx=16,pady=8, bd=14, fg="black",font=('arial', 12,'bold'), width=10, 
               text="Exit", bg="red", command = qExit).grid(row=7, column=3)
root.mainloop()
