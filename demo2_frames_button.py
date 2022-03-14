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

        self.top_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'bottom')

        self.label1 = tkinter.Label(self.top_frame, text = 'John')
        self.label2 = tkinter.Label(self.top_frame, text = 'Jill')
        self.label3 = tkinter.Label(self.top_frame, text = 'James')

        #Default is side = 'Top'
        self.label1.pack(side = 'top')
        self.label2.pack(side = 'top')
        self.label3.pack(side = 'top')



        self.label4 = tkinter.Label(self.top_frame, text = 'Jack')
        self.label5 = tkinter.Label(self.top_frame, text = 'Jim')
        self.label6 = tkinter.Label(self.top_frame, text = 'Jerry')

        self.label4.pack(side = 'left')
        self.label5.pack(side = 'left')
        self.label6.pack(side = 'left')



        self.mybutton = tkinter.Button(self.main_window, text = 'Click Me!', command = self.do_something)
        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)      #Make sure to destroy the entire window 

        self.mybutton.pack(side = 'left')
        self.quit_button.pack(side = 'right')
        
        tkinter.mainloop()
        
    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button!')
    

my_gui = MyGUI()

#This will print as soon as you exit out of the dialog box 
print("moving on.....")
