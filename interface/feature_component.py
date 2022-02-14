import tkinter as tk
import typing

from interface.styling import *

if typing.TYPE_CHECKING:
    from interface.root_component import Root


class FeatureEditor(tk.Frame):
    def __init__(self, root: "Root", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.root = root

        self._button1 = tk.Button(self, text="Add feature 1", font=GLOBAL_FONT, bg=BG_COLOR_2, fg=FG_COLOR)
        self._button1.pack(side=tk.TOP, anchor="nw", pady=10)

        self._button2 = tk.Button(self, text="Add feature 2", font=GLOBAL_FONT, bg=BG_COLOR_2, fg=FG_COLOR)
        self._button2.pack(side=tk.TOP, anchor="nw", pady=10)

        self._button3 = tk.Button(self, text="Add feature 3", font=GLOBAL_FONT, bg=BG_COLOR_2, fg=FG_COLOR)
        self._button3.pack(side=tk.TOP, anchor="nw", pady=10)