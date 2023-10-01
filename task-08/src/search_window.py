from PySide6.QtWidgets import QApplication,QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QPixmap
import requests
from pokemon_window import pokemon

class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        self.q=None

        self.background_label = QLabel(self)
        pixmap = QPixmap("../assets/landing.jpg")
        self.background_label.setPixmap(pixmap)
       
        self.w = None        
        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)

        self.setStyleSheet("""
             QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
            """)

        label1 = QLabel("Enter the name",self)
        label1.setGeometry(50, 30, 400, 10)
        
        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.connection)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.open_capture_pokemon)

        pushButton = QPushButton(parent=self, text='Display')
        pushButton.setGeometry(50, 400, 160, 43)
        pushButton.clicked.connect(self.open_pokemon_window)

        self.show()

    def connection(self,checked):
        def fetch_pokemon_data(pokemon):
            url = pokemon['url']
            resp = requests.get(url)
            if resp.status_code == 200:
                pok_data = resp.json()
                id = pok_data["id"]
                picture = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
                abilities = pok_data["abilities"]
                list_abilities=[]
                for i in range(len(abilities)):
                    list_abilities.append(abilities[i]['ability']['name'])
                stats = pok_data["stats"]
                list_stats=[]
                for j in stats:
                    list_stats.append(j["base_stat"])
                height = pok_data["height"]
                weight = pok_data["weight"]

                '''self.id_label.setText(f"id : {id}",self)
                self.id_label.setGeometry(50,50,50,50)

                self.height_label = QWidget.QLabel(self)
                self.height_label.setText(f"height : {height}")
                self.height_label.setGeometry(50,80,80,80)

                self.weight_label = QWidget.QLabel(self)
                self.weight_label.setText(f"height : {weight}")
                self.weight_label.setGeometry(50,110,110,110)'''

                len_abilities = len(list_abilities)+1

                print(f"Name: {pokemon['name']}")
                print(f"id: {id}")
                print(f"The picture is {picture}")
                print(f"Height: {height}")
                print(f"Weight: {weight}")
                print("Abilities:",list_abilities[0:len_abilities])
                print("Stats")
                print("hp:",list_stats[0])
                print("Attack:",list_stats[1])
                print("Defense:",list_stats[2])
                print("Special-attack:",list_stats[3])
                print("Specail-defense:",list_stats[4])
                print("Speed:",list_stats[5])

        text = self.textbox.text()

        file = open('input.txt','w')
        file.write(text)
        file.close()
     
        response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
        if response.status_code == 200:
            data = response.json()
            for pokemon in data['results']:
                if pokemon['name'] == text:
                    fetch_pokemon_data(pokemon)
        else:
            print('Error fetching data')


    def open_capture_pokemon(self):

        def capture_successful():
            msg = QMessageBox()
            msg.setWindowTitle("Pokemon capture")
            msg.setText("Pokemon captured successfully!")
            msg.exec()

            
        text = self.textbox.text()

        response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
        if response.status_code == 200:
            data = response.json()
            for pokemon in data['results']:
                if pokemon['name'] == text:
                    capture_successful()
        
            
    def open_pokemon_window(self,checked):
        if self.w is None:
            self.w = pokemon()
        self.w.show()
            
    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    # Add the background provided in assets

    # 2 #
    # Capture the Pokémon i.e. download the image.

    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
