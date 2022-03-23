import tkinter
import tkinter.messagebox

from pip import main

class Pizza: 
    
    #Create the main window 
    def __init__(self):
        self.main_window = tkinter.Tk() 
        
        
        self.main_window.geometry('500x200')
        self.main_window.title('Place Pizza Order')
    
        self.top_frame = tkinter.Frame(self.main_window)
        self.name_frame = tkinter.Frame(self.main_window)
        self.toppings_frame = tkinter.Frame(self.main_window)
        #self.frame3 = tkinter.Frame(self.main_window)
        #self.frame4 = tkinter.Frame(self.main_window)

        self.intro_msg = tkinter.Label(self.top_frame, text = """Welcome to Brittney's Pizzeria, what would you like to order?""")
        
        self.first_name = tkinter.Label(self.name_frame, text = 'First Name')
        self.fn_entry = tkinter.Entry(self.name_frame, width = 15)
        
        self.last_name = tkinter.Label(self.name_frame, text = 'Last Name')
        self.ln_entry = tkinter.Entry(self.name_frame, width = 15)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        #Set the default button 
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        
        self.toppings_msg = tkinter.Label(self.toppings_frame, text = "Toppings: ")
        self.cb1 = tkinter.Checkbutton(self.toppings_frame, text = 'Pepperoni', variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.toppings_frame, text = 'Ham', variable = self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.toppings_frame, text = 'Pineapple', variable = self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.toppings_frame, text = 'Mushrooms', variable = self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.toppings_frame, text = 'Onions', variable = self.cb_var5)

        
        self.intro_msg.pack(side = 'left')
        self.first_name.pack(side = 'left')
        self.fn_entry.pack(side = 'left')        
        self.last_name.pack(side = 'left')
        self.ln_entry.pack(side = 'right')  
        
        self.toppings_msg.pack(side = 'left')
        self.cb1.pack(side = 'left')
        self.cb2.pack(side = 'left')
        self.cb3.pack(side = 'left')
        self.cb4.pack(side = 'left')
        self.cb5.pack(side = 'left')

        self.top_frame.pack(side = 'top')
        self.name_frame.pack(side = 'top')
        self.toppings_frame.pack(side = 'top')

        tkinter.mainloop()

my_pizza = Pizza()