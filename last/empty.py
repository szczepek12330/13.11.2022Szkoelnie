import tkinter

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label1 = tkinter.Label(self.main_window, text="Witaj świecie!")
        self.label2 = tkinter.Label(self.main_window, text="To jest program z GUI.")

        self.label1.pack(side='left')
        self.label2.pack(side='left') #top bottom left right

        tkinter.mainloop()


my_gui = MyGui()