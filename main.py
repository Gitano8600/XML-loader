import tkinter as tk
import logging

from interface.root_component import Root
from parsers.ofac import OfacParser

logger = logging.getLogger()

logger.setLevel(logging.INFO)  # set to DEBUG for debugging information in info.log

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    new_data = OfacParser()

    root = Root(new_data)

    root.mainloop()

