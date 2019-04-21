from tkinter import * # Import tkinter
import tkinter as ttk
from PIL import ImageTk, Image

class ShoppingCart:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Glamping World Shopping Cart") # Set title of a window
        window.geometry("650x450")
        window.configure(background = 'white')

        self.Yes = IntVar()
       


        tkvar = StringVar(window)
        tkvar2 = StringVar(window)
        tkvar3 = StringVar(window)
        tkvar4 = StringVar(window)
        tkvar5 = StringVar(window)

        #set up labels for the loan calculator in the left column of the window, align labels left (Sticky=W)
        choices = {'Sleeping Bag', "Lantern", "Tent"}
        tkvar.set('Choose Product')
        popupMenu = OptionMenu(window, tkvar, *choices)
        Label(window, text = "Choose Product", bg='white').grid(row = 2, column = 1, sticky = W)
        popupMenu.grid(row = 2, column = 3)

        choices2 = {'Sleeping Bag', 'Lantern', 'Tent'}
        tkvar2.set('Choose Product 2')
        popupMenu = OptionMenu(window, tkvar2, *choices2)
        Label(window, text = "Choose Product 2", bg='white').grid(row = 5, column = 1, sticky = W)
        popupMenu.grid(row = 5, column = 3)

        Label(window, text = "Quantity", bg='white').grid(row = 3, column = 1, sticky = W)
        self.Quantity = IntVar()
        Entry(window, textvariable = self.Quantity, justify = RIGHT).grid(row = 3, column = 3, sticky = E)
        
        Label(window, text = "Customer ID", bg='white').grid(row = 1, column = 1, sticky = W)
        self.CustomerID = StringVar()
        Entry(window, textvariable = self.CustomerID, justify = RIGHT).grid(row = 1, column = 3, sticky = E)
        
        Label(window, text = "Price of Product", bg='white').grid(row = 4, column = 1, sticky = W)
        self.Price = StringVar()
        Entry(window, textvariable = self.Price, justify = RIGHT).grid(row = 4, column = 3, sticky = E)


        Label(window, text = 'Quantity', bg='white').grid(row=6, column = 1, sticky = W)
        self.Quantity2 = IntVar()
        Entry(window, textvariable = self.Quantity2, justify = RIGHT).grid(row=6, column = 3, sticky = E )

        Label(window, text = "Price of Product", bg='white').grid(row = 7, column = 1, sticky = W)
        self.Price2 = StringVar()
        Entry(window, textvariable = self.Price2, justify = RIGHT).grid(row = 7, column = 3, sticky = E)

        Label(window, text = "Discount (2% for item in stock over 120 days)", bg='white').grid(row = 8, column = 1, sticky = W)

        Label(window, text = "Sales Tax 13% ($)", bg='white').grid(row = 10 , column = 1, sticky = W)

        Label(window, text = "SubTotal ($)", bg='white').grid(row = 9, column = 1, sticky = W)

        Label(window, text = "Total Order Cost ($)", bg='white').grid(row = 11, column = 1, sticky = W)
        
       

        

        #set up the output area for the calculator below the input area, using two labels and a button; the button calls the function computePayment when it's clicked
        self.SalesTax = StringVar()
        Label(window, textvariable = self.SalesTax, bg='white').grid(row = 10, column = 3, sticky = E)
        self.SubTotal = StringVar()
        Label(window, textvariable = self.SubTotal, bg='white').grid(row = 9, column = 3, sticky = E)
        self.TotalCost = StringVar()
        Label(window, textvariable = self.TotalCost, bg='white').grid(row = 11, column = 3, sticky = E)


       
        Button(window, text="Help?", bg="Yellow").grid(row=12, column = 1, sticky= W)

        C1 = Checkbutton(window, text="Yes", command = self.Yes, onvalue = 1, offvalue = 0).grid(row = 8, column = 3, sticky = N)
        
        
       
        Button(window, text = "Compute Payment", bg="cornsilk1", command = self.computePayment).grid(row = 12, column = 3, sticky = E)
        photo = PhotoImage(file="C:\\Users\\Teddy Fotos\\Desktop\\python (1)\\GWlogo.gif")
        imglabel = Label(window, image=photo).grid(row = 0, column = 1)

        window.mainloop() # Create an event loop to display the window

    def computePayment(self):
        SalesTax = float(self.Price.get()) * int(self.Quantity.get()) * .13 + float(self.Price2.get()) * int(self.Quantity2.get()) * .13
        self.SalesTax.set(format(SalesTax, '10.2f')) #assign the value and format the monthlyPaymentVar to the value of monthlyPayment returned from getMonthlyPayment function
        SubTotal = float(self.Price.get()) * int(self.Quantity.get())  + float(self.Price2.get()) * int(self.Quantity2.get())  #calculate totalPayment 
        self.SubTotal.set(format(SubTotal, '10.2f'))   #output totalPayment formatted to two decimal places in the totalPaymentVar
        TotalCost = float(self.Price.get()) * int(self.Quantity.get()) * .13 + float(self.Price.get()) * int(self.Quantity.get()) + float(self.Price2.get()) * int(self.Quantity2.get()) * .13 + float(self.Price2.get()) * int(self.Quantity2.get())
        self.TotalCost.set(format(TotalCost, '10.2f'))

  

    def Yes(self):
        if self.Yes.get() == 1:
            SubTotal = float(self.Price.get()) * int(self.Quantity.get()) - float(self.Price.get()) * int(self.Quantity.get()) * .02
            self.Subtotal.set(format(Subtotal, '10.2f'))
      
 
    
ShoppingCart()  # Create GUI 