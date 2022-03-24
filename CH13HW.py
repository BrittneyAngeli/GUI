#Brittney Solorio
import tkinter
import tkinter.messagebox

from pip import main

class Pizza: 
    
    #Create the main window 
    def __init__(self):
        self.main_window = tkinter.Tk() 
        
        self.main_window.geometry('650x200')
        self.main_window.title('Place Pizza Order')
    
        font_tuple = ("Comic Sans MS", 13, "bold")

        #Setting up the frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.name_frame = tkinter.Frame(self.main_window)
        self.empty_frame = tkinter.Frame(self.main_window)
        self.toppings_frame = tkinter.Frame(self.main_window)
        self.crust_frame = tkinter.Frame(self.main_window)

        #Setting up the title and input labels 
        self.intro_msg = tkinter.Label(self.top_frame, text = """Welcome to Brittney's Pizzeria, what would you like to order?""")
        self.create_space  = tkinter.Label(self.empty_frame, text = " ")
        self.first_name = tkinter.Label(self.name_frame, text = 'First Name')
        self.fn_entry = tkinter.Entry(self.name_frame, width = 15)
        
        self.last_name = tkinter.Label(self.name_frame, text = 'Last Name')
        self.ln_entry = tkinter.Entry(self.name_frame, width = 15)


        #Setting up the check boxes for the toppings 
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

        #Set the topping options 
        self.toppings_msg = tkinter.Label(self.toppings_frame, text = "Toppings:")
        self.cb1 = tkinter.Checkbutton(self.toppings_frame, text = 'Pepperoni ($0.15)', variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.toppings_frame, text = 'Ham ($0.15)', variable = self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.toppings_frame, text = 'Pineapple ($0.20)', variable = self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.toppings_frame, text = 'Mushrooms ($0.25)', variable = self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.toppings_frame, text = 'Onions ($0.20)', variable = self.cb_var5)

        #Setting up the radio boxes for the crust type 
        self.radio_var = tkinter.StringVar()

        self.crust_msg = tkinter.Label(self.crust_frame, text = "Crust Type:")
        self.rb1 = tkinter.Radiobutton(self.crust_frame, text = 'Hand-tossed ($13.00)', variable = self.radio_var, value = 'Hand-Tossed')
        self.rb2 = tkinter.Radiobutton(self.crust_frame, text = 'Stuffed ($15.00)', variable = self.radio_var, value = 'Stuffed')
        self.rb3 = tkinter.Radiobutton(self.crust_frame, text = 'Thin ($12.00)', variable = self.radio_var, value = 'Thin')

        #Default choice is Hand-Tossed crust 
        self.rb1.select()

        #Set up the buttons 
        self.mybutton = tkinter.Button(self.main_window, text = 'Add to Cart', command = self.calc_total)
        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)      #Make sure to destroy the entire window 

        #Pack the intro and person entry info and change background color 
        self.intro_msg.pack(side = 'left')
        self.create_space.pack(side = 'left')
        self.first_name.pack(side = 'left')
        self.fn_entry.pack(side = 'left')        
        self.last_name.pack(side = 'left')
        self.ln_entry.pack(side = 'right')  

        self.intro_msg.configure(font = font_tuple)
        self.intro_msg.configure(bg = 'light salmon')
        self.create_space.configure(bg = 'light salmon')
        self.first_name.configure(bg = 'light salmon')
        self.fn_entry.pack(side = 'left')        
        self.last_name.configure(bg = 'light salmon')
        self.ln_entry.pack(side = 'right')  


        #Pack the toppings content and change background color 
        self.toppings_msg.configure(font = font_tuple)
        self.toppings_msg.pack(side = 'left')
        self.cb1.pack(side = 'left')
        self.cb2.pack(side = 'left')
        self.cb3.pack(side = 'left')
        self.cb4.pack(side = 'left')
        self.cb5.pack(side = 'left')

        self.toppings_msg.configure(bg = 'light salmon')
        self.cb1.configure(bg = 'light salmon')
        self.cb2.configure(bg = 'light salmon')
        self.cb3.configure(bg = 'light salmon')
        self.cb4.configure(bg = 'light salmon')
        self.cb5.configure(bg = 'light salmon')

        #Pack the crust content and change background color 
        self.crust_msg.pack(side = 'left')
        self.rb1.pack(side = 'left')
        self.rb2.pack(side = 'left')
        self.rb3.pack(side = 'left')

        self.crust_msg.configure(font = font_tuple)
        self.crust_msg.configure(bg = 'light salmon')
        self.rb1.configure(bg = 'light salmon')
        self.rb2.configure(bg = 'light salmon')
        self.rb3.configure(bg = 'light salmon')

        #Pack the frames and change background color 
        self.top_frame.pack(side = 'top')
        self.name_frame.pack(side = 'top')
        self.empty_frame.pack(side = 'top')
        self.toppings_frame.pack(side = 'top')
        self.crust_frame.pack(side = 'top')

        self.main_window.configure(bg = 'light salmon')
        self.top_frame.configure(bg = 'light salmon')
        self.name_frame.configure(bg = 'light salmon')
        self.empty_frame.configure(bg = 'light salmon')
        self.toppings_frame.configure(bg = 'light salmon')
        self.crust_frame.configure(bg = 'light salmon')

        #Pack the buttons
        self.mybutton.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        tkinter.mainloop()

    #Calculate the total pizza cost and display message 
    def calc_total(self):
        self.msg = "Toppings added: "
        self.price = 0
        first_name = self.fn_entry.get()
        last_name = self.ln_entry.get()

        #Check to see which toppings the customer selected 
        if self.cb_var1.get() == 1:
            self.msg += 'Pepperoni '
            self.price += 0.15
        if self.cb_var2.get() == 1: 
            self.msg += 'Ham '
            self.price += 0.15
        if self.cb_var3.get() == 1:
            self.msg += 'Pineapple '
            self.price += 0.20
        if self.cb_var4.get() == 1:
            self.msg += 'Mushrooms '
            self.price += 0.25
        if self.cb_var5.get() == 1:
            self.msg += 'Onions '
            self.price += 0.20

        #Check to see which pizza crust the customer selected 
        if self.radio_var.get() == 'Hand-Tossed':
            self.price += 13.00
        if self.radio_var.get() == 'Stuffed':
            self.price += 15.00
        if self.radio_var.get() == 'Thin':
            self.price += 12.00

        #Display the order 
        tkinter.messagebox.showinfo("Order Confirmation", 
                            "Name: " + first_name + ' ' + 
                            last_name + '\n' + 
                            self.msg +'\n' +"Crust Type: " + str(self.radio_var.get()) +'\n'
                            + 'Total Pizza Cost: ' + str(self.price))


my_pizza = Pizza()