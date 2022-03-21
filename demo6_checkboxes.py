import tkinter
import tkinter.messagebox


class MyGUI:

    #Create the main window 
    def __init__(self):
        self.main_window = tkinter.Tk()     #This creates a dialog box 

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        #Set the default button 
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)


        self.cb1 = tkinter.Checkbutton(self.top_frame, text = 'Option1', variable = self.cb_var1)

        self.cb2 = tkinter.Checkbutton(self.top_frame, text = 'Option2', variable = self.cb_var2)

        self.cb3 = tkinter.Checkbutton(self.top_frame, text = 'Option3', variable = self.cb_var3)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        
        self.okbutton = tkinter.Button(
            self.bottom_frame, text = 'OK', command = self.show_choice
        )    


        self.quit_button = tkinter.Button(
            self.bottom_frame, text = 'Quit', command = self.main_window.destroy
        )      #Make sure to destroy the entire window 


        # Yes, we have to pack the frames too!
        self.top_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'top')

        self.okbutton.pack(side = 'left')
        self.quit_button.pack(side = 'bottom')

        tkinter.mainloop()
        
    def show_choice(self):
        self.message = 'You have selected:\n'

        if self.cb_var1.get() == 1:
            self.message += '1\n'
        if self.cb_var2.get() == 1:
            self.message += '2\n'
        if self.cb_var3.get() == 1:
            self.message += '3\n'

        tkinter.messagebox.showinfo("Response", self.message)
    

my_gui = MyGUI()