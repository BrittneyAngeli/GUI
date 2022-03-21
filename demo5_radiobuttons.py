import tkinter
import tkinter.messagebox


class KiloConverterGUI:

    #Create the main window 
    def __init__(self):
        self.main_window = tkinter.Tk()     #This creates a dialog box 

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        self.rb1 = tkinter.Radiobutton(self.top_frame, text = 'Option1', variable = self.radio_var, value = 10)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text = 'Option2', variable = self.radio_var, value = 20)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text = 'Option1', variable = self.radio_var, value = 30)

        #Set the default button 
        self.rb2.select()
        
        #Pack the radio buttons 
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Yes, we have to pack the frames too!
        self.top_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'top')
        
        self.okbutton = tkinter.Button(
            self.bottom_frame, text = 'OK', command = self.show_choice
        )
        
        self.resetbutton = tkinter.Button(
            self.bottom_frame, text = 'Reset', command = self.rb1.select
        )        


        self.quit_button = tkinter.Button(
            self.bottom_frame, text = 'Quit', command = self.main_window.destroy
        )      #Make sure to destroy the entire window 

        self.okbutton.pack(side = 'left')
        self.resetbutton.pack(side = 'left')
        self.quit_button.pack(side = 'bottom')

        tkinter.mainloop()
        
    def show_choice(self):
        tkinter.messagebox.showinfo("Selection", "You have selected option" + str(self.radio_var.get()))
    

kilo_conv = KiloConverterGUI()