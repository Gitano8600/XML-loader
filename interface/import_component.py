import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import typing
from threading import *

from interface.styling import *

from parsers.ofac import OfacParser

if typing.TYPE_CHECKING:
    from interface.root_component import Root


class ImportEditor(tk.Frame):
    def __init__(self, root: "Root", xml_data: OfacParser, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.root = root
        self._xmldata = xml_data
        self.root.logging_frame.add_log(f"Just test: {self._xmldata._xmlns}")

        # self._headers = ["this", "that"]

        # var = tk.StringVar()
        # var.set("Import new XML data")

        # label = tk.Label(self, textvariable= var, bg=BG_COLOR, pady=2)
        # label.pack()

        self._import_button = tk.Button(self, text="Import new GWL", command=self.threading, font=GLOBAL_FONT, bg=BG_COLOR_2, fg=FG_COLOR)
        self._import_button.pack(side=tk.TOP, anchor="nw")

    def threading(self):
        t1 = Thread(target=self.import_trigger)
        t1.start()

    def import_trigger(self):
        filetypes = (
            ('xml files', '*.xml'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/home/manuel/PycharmProjects/XML_loader/input/',
            filetypes=filetypes)

        self.root.logging_frame.add_log(f"File selected: {filename}")
        self.root.logging_frame.add_log(f"Starting to import new watch list data.")
        self._xmldata.parse_data(filename)
        self.root.logging_frame.add_log(f"Data successfully parsed.")
        self._xmldata.process_data()
        self.root.logging_frame.add_log(f"Data successfully processed.")



        '''showinfo(
            title='Selected File',
            message=filename
        )'''
