import PySide6.QtCore
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap
import requests

class pokemon(QWidget):
    def __init__(self):
        super().__init__()
        self.w=None

        self.setWindowTitle("Pokemon")
        self.setFixedSize(600,500)

        file = open('input.txt','r')
        text = file.readline()

        list = []

        response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
        if response.status_code == 200:
            data = response.json()
            for pokemon in data['results']:
                if pokemon['name'] == text:
                    url = pokemon['url']
                    resp = requests.get(url)
                    if resp.status_code == 200:
                         pok_data = resp.json()
                         name = pokemon['name']
                         id = pok_data["id"]
                         url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png'
                         list.append(url)
                    
        previous_button = QPushButton("previous",self)
        previous_button.setGeometry(50,430,200,40)
        previous_button.clicked.connect(self.display_pokemon(list))

        next_button = QPushButton("next",self)
        next_button.setGeometry(350,430,200,40)
        next_button.clicked.connect(self.display_pokemon(list))

    def display_pokemon(self,list):
        for i in list:
            print(i)
            
    