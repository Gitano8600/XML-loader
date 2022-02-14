import tkinter as tk
import logging

from interface.styling import *
from interface.logging_component import Logging
from interface.import_component import ImportEditor
from interface.feature_component import FeatureEditor

from parsers.ofac import OfacParser


logger = logging.getLogger()


class Root(tk.Tk):
    def __init__(self, xml_data: OfacParser):
        super().__init__()

        self.xml_data = xml_data

        self.title("XML loader V1.0 by Gitano")

        self.configure(bg=BG_COLOR)
        self.geometry("1000x500")
        self.resizable(False, False)

        self.logging_frame = Logging(self, bg=BG_COLOR, borderwidth=20)
        self.logging_frame.pack(side=tk.LEFT)

        #self._left_frame = tk.Frame(self, bg=BG_COLOR)
        #self._left_frame.pack(side=tk.LEFT)

        self._right_frame = tk.Frame(self, bg=BG_COLOR)
        self._right_frame.pack(side=tk.LEFT)

        #self.logging_frame = Logging(self._left_frame, bg=BG_COLOR, borderwidth=1)
        #self.logging_frame.pack(side=tk.TOP)

        self._import_frame = ImportEditor(self, self.xml_data, self._right_frame, bg=BG_COLOR, borderwidth=20)
        #self._import_frame.config(bd=1, relief=tk.SOLID, pady=20)
        self._import_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self._feature_frame = FeatureEditor(self, self._right_frame, bg=BG_COLOR)
        self._feature_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)


