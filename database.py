from tinydb import TinyDB, Query,where
from colorama import Fore, Back, Style, init



class dataset:
    def __init__(self, file="data.json"):
        self.file = file
        self.electrical_db = TinyDB(self.file)
        self.electrical = self.electrical_db.table('electricalData')
