import tkinter
import tkinter.messagebox

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Tytuł okna')
        self.main_window.geometry('400x400')
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
        myFont = tkinter.font.Font(family='Helvetica', size=18, weight='bold')
        self.canvas.create_text(100, 100, text='Testowy', anchor=tkinter.SW, font=myFont)

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        self.cb_var = tkinter.IntVar()
        self.cb_var.set(0)

        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Opcja 1', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Opcja 2', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Opcja 3', variable=self.radio_var, value=3)
        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Opcja 4', variable=self.cb_var)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.cb1.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.show_choice)

        self.ok_button.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.canvas.pack()

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo('Wybór', 'Wybrałeś opcje: ' + str(self.radio_var.get()))
        if self.cb_var.get() == 1:
            tkinter.messagebox.showinfo('Wybór', 'Zaznaczyłeś kwadracik')

gui = MyGui()
