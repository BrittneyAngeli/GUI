import tkinter
import tkinter.messagebox

from pip import main


class MyGUI:

    #Create the main window 
    def __init__(self):
        self.main_window = tkinter.Tk()     #This creates a dialog box 

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)

        self.test_score1 = tkinter.Label(self.frame1, text = 'Enter the score for test 1:')
        self.test1_entry = tkinter.Entry(self.frame1, width = 10)

        self.test_score2 = tkinter.Label(self.frame2, text = 'Enter the score for test 2:')
        self.test2_entry = tkinter.Entry(self.frame2, width = 10)        

        self.test_score3 = tkinter.Label(self.frame3, text = 'Enter the score for test 3:')
        self.test3_entry = tkinter.Entry(self.frame3, width = 10)  

        self.prompt_label4 = tkinter.Label(self.frame4, text = 'Average:')

        self.test_score1.pack(side = 'left')
        self.test1_entry.pack(side = 'left')

        self.test_score2.pack(side = 'left')
        self.test2_entry.pack(side = 'left')

        self.test_score3.pack(side = 'left')
        self.test3_entry.pack(side = 'left')

        self.prompt_label4.pack(side = 'left')

        self.frame1.pack(side = 'top')
        self.frame2.pack(side = 'top')
        self.frame3.pack(side = 'top')
        self.frame4.pack(side = 'top')
        self.frame5.pack(side = 'top')

        self.avg_button = tkinter.Button(
            self.frame5, text = 'Average', command = self.main_window.calc_avg
        )  

        self.quit_button = tkinter.Button(
            self.frame5, text = 'Quit', command = self.main_window.destroy
        )  

        self.avg_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        self.main_window.configure(background='green')

        tkinter.mainloop()
        
    def calc_avg(self):

        score1 = float(self.test_score1.get())
        score2 = float(self.test_score2.get())
        score3 = float(self.test_score3.get())
        
        test_avg = (score1 + score2 + score3) / 3
        self.avg_prompt = tkinter.Label(self.frame4, text = str)

my_gui = MyGUI()