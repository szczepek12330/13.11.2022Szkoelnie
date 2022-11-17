import tkinter
import tkinter.messagebox


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Tytuł okna')
        self.main_window.geometry('400x400')

        self.my_button = tkinter.Button(self.main_window, text="Kliknij!", command=self.do_something)

        self.my_button2 = tkinter.Button(self.main_window, text="Kliknij mnie też!",
                                         command=lambda: self.do_something2("Testowu tytuł"))
        self.my_button3 = tkinter.Button(self.main_window, text="Zakończ!", command=self.main_window.destroy)

        self.my_button.pack()
        self.my_button2.pack()
        self.my_button3.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Tytuł', 'Dziękujemy za kliknięcie!')

    def do_something2(self, text):
        tkinter.messagebox.showinfo(f'{text}', 'Dziękujemy za kliknięcie!')


my_gui = MyGui()
