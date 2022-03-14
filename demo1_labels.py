import tkinter

class MyGUI:

    #Create the main window 
    def __init__(self):
        self.main_window = tkinter.Tk()     #This creates a dialog box 

        #Configure the main window 
        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')
    
        self.label1 = tkinter.Label(self.main_window, text = 'Hello World!')

        self.label2 = tkinter.Label(self.main_window, text = 'This is my GUI program.')


        #Default is side = 'Top'
        self.label1.pack(side = 'top')
        self.label2.pack(side = 'bottom')

        tkinter.mainloop()


my_gui = MyGUI()

#This will print as soon as you exit out of the dialog box 
print("moving on.....")
