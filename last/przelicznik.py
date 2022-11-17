import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Tytuł okna')
        self.main_window.geometry('400x200')
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text='podaj odleglosc w kilometrach:')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.descr_label = tkinter.Label(self.mid_frame, text= 'Po konwersji na mile:')
        self.value = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        self.calc_button = tkinter.Button(self.bottom_frame, text='konwertuj', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Zakończ', command=self.main_window.destroy)

        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.mid_frame.pack()
        tkinter.mainloop()

    def convert(self):
            kilo = float(self.kilo_entry.get())
            miles = kilo * 0.6214
            self.value.set(miles)


kilo = KiloConverterGUI()
