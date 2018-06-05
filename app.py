import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
import fusee_launcher as fusee
import mock_arguments



class App(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.build_widgets()

        self.payload_path = ''
        self.device_found = False
        self.lbl_length   = 22
        self.usb_backend  = fusee.HaxBackend.create_appropriate_backend()

        root = self.winfo_toplevel()
        root.update()
        root.resizable(0, 0)

        self.do_update()



    def build_widgets(self):
        style = ttk.Style()
        style.configure('Horizontal.TProgressbar', background='#5eba21')

        self.progress = ttk.Progressbar(self, mode='indeterminate', maximum=50)
        self.progress.grid(row=0, columnspan=2, sticky=tk.W+tk.E)
        self.progress.start(30)

        self.lbl_look = ttk.Label(self, text="Looking for device...")
        self.lbl_look.grid(row=1, column=0, columnspan=2, pady=8)

        self.btn_open = ttk.Button(self, text="Select Payload", command=self.btn_open_pressed)
        self.btn_open.grid(row=2, column=0, padx=8)

        self.lbl_file = ttk.Label(self, text="No payload selected.    ", justify=tk.LEFT)
        self.lbl_file.grid(row=2, column=1, padx=8)

        self.btn_send = ttk.Button(self, text="Launch Fusée!", command=self.btn_send_pressed)
        self.btn_send.grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E, pady=8, padx=8)
        self.btn_send.state(('disabled',)) # trailing comma to define single element tuple



    def do_update(self):
        device = self.usb_backend.find_device()
        if device and not self.device_found:
            self.device_found = True
            self.lbl_look.configure(text='Device found!')
            self.progress.stop()
            self.progress.configure(mode='determinate', maximum=1000)
            self.progress.step(999)

        elif not device and self.device_found:
            self.device_found = False
            self.lbl_look.configure(text='Looking for device...')
            self.progress.configure(mode='indeterminate', maximum=50)
            self.start(30)

        self.after(333, self.do_update)



    def btn_open_pressed(self):
        path = askopenfilename(filetypes=[('Binary', '*.bin')], title='Select Payload')
        if path:
            excess = len(path)-self.lbl_length
            self.payload_path = path
            self.lbl_file.configure(text='..'+path[max(0, excess):])

        self.validate_form()



    def btn_send_pressed(self):
        args = mock_arguments.MockArguments()
        args.payload = self.payload_path
        fusee.do_hax(args)


    
    def validate_form(self):
        if self.payload_path and self.device_found:
            self.btn_send.state(('!disabled',))



my_app = App()
my_app.master.title('Fusée Launcher Interfacée')
my_app.mainloop()