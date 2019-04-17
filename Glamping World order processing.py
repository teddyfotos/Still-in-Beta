from tkinter import * # Import tkinter
import tkinter as ttk
from PIL import ImageTk, Image

class ShoppingCart:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Glamping World Shopping Cart") # Set title of a window
        window.geometry("625x450")
        window.configure(background = 'white')

        var1 = IntVar()
        var2 = IntVar()
       


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

        choices2 = {'Sleeping Bag - 0001', 'Lantern - 0002', 'Tent - 0003'}
        tkvar2.set('Select Product ID')
        popupMenu = OptionMenu(window, tkvar2, *choices2)
        Label(window, text = "Product ID", bg='white').grid(row = 3, column = 1, sticky = W)
        popupMenu.grid(row = 3, column = 3)

        Label(window, text = "Quantity", bg='white').grid(row = 4, column = 1, sticky = W)
        self.Quantity = IntVar()
        Entry(window, textvariable = self.Quantity, justify = RIGHT).grid(row = 4, column = 3, sticky = E)
        
        Label(window, text = "Customer ID", bg='white').grid(row = 1, column = 1, sticky = W)
        self.CustomerID = StringVar()
        Entry(window, textvariable = self.CustomerID, justify = RIGHT).grid(row = 1, column = 3, sticky = E)
        
        Label(window, text = "Price of Product", bg='white').grid(row = 5, column = 1, sticky = W)
        self.Price = StringVar()
        Entry(window, textvariable = self.Price, justify = RIGHT).grid(row = 5, column = 3, sticky = E)

        Label(window, text = "Discount (2% for item in stock over 120 days)", bg='white').grid(row = 6, column = 1, sticky = W)

        Label(window, text = "Sales Tax (13%)", bg='white').grid(row = 7 , column = 1, sticky = W)

        Label(window, text = "Total Cost ($)", bg='white').grid(row = 8, column = 1, sticky = W)
        
       

        

        #set up the output area for the calculator below the input area, using two labels and a button; the button calls the function computePayment when it's clicked
        self.SalesTax = StringVar()
        Label(window, textvariable = self.SalesTax, bg='white').grid(row = 7, column = 3, sticky = E)
        self.TotalCost = StringVar()
        Label(window, textvariable = self.TotalCost, bg='white').grid(row = 8, column = 3, sticky = E)

        Button(window, text="Close", bg="firebrick1",command = window.destroy).grid(row = 0, column = 8, sticky = E)
        Button(window, text="Help?", bg="Yellow").grid(row=12, column = 1, sticky= W)

        Checkbutton(window, text="Yes", variable = var1).grid(row = 6, column = 3, sticky = N)
        Checkbutton(window, text="No", variable = var2).grid(row = 6, column = 3, sticky = E)

        self.AddtoCart = Button
        Button(window, text = 'Add to Cart', bg = 'green', command = self.AddtoCart).grid(row = 10, column = 2, sticky = W)
        Button(window, text = "Compute Payment", bg="cornsilk1", command = self.computePayment).grid(row = 10, column = 3, sticky = E)
        photo = PhotoImage(file="C:\\Users\\Teddy Fotos\\Desktop\\python (1)\\GWlogo.gif")
        imglabel = Label(window, image=photo).grid(row = 0, column = 1)
        
        window.mainloop() # Create an event loop to display the window

    # function computePayment calls the getMonthlyPayment function with arguments assigned the values from the user

    def computePayment(self):
        SalesTax = self.getSalesTax(
            float(self.Price.get()), 
            int(self.Quantity.get()) * .13)
        self.SalesTax.set(format(SalesTax, '10.2f')) #assign the value and format the monthlyPaymentVar to the value of monthlyPayment returned from getMonthlyPayment function
        TotalCost = float(self.Price.get()) * int(self.Quantity.get() * .13) + float(self.Price.get()) * int(self.Quantity.get())   #calculate totalPayment 
        self.TotalCost.set(format(TotalCost, '10.2f'))   #output totalPayment formatted to two decimal places in the totalPaymentVar
    
    #calculate Monthly Payment using  the formula provided    
    def getSalesTax(self,Price, Quantity):
        SalesTax = (Price * Quantity)
        return SalesTax 
    
ShoppingCart()  # Create GUI 