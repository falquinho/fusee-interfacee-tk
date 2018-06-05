import tkinter as tk
import tkinter.ttk as ttk


class App(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.build_widgets()



    def build_widgets(self):
        self.progress = ttk.Progressbar(self, mode='indeterminate', maximum=50)
        self.progress.grid(row=0, columnspan=2, sticky=tk.W+tk.E)
        self.progress.start(30)

        self.lbl_look = ttk.Label(self, text="Looking for device...")
        self.lbl_look.grid(row=1, column=0, columnspan=2, pady=8)

        self.btn_open = ttk.Button(self, text="Select Payload", command=self.btn_open_pressed)
        self.btn_open.grid(row=2, column=0, padx=8)

        self.lbl_file = ttk.Label(self, text="No payload selected.", justify=tk.LEFT)
        self.lbl_file.grid(row=2, column=1, padx=8)

        self.btn_send = ttk.Button(self, text="Launch Fusée!", command=self.btn_send_pressed, state=tk.DISABLED)
        self.btn_send.grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E, pady=8, padx=8)



    def btn_open_pressed(self):
        print('btn_open_pressed()')



    def btn_send_pressed(self):
        print('btn_send_pressed()')



my_app = App()
my_app.master.title('Fusée Launcher Interfacée')
my_app.mainloop()