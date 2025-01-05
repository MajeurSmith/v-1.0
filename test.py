import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Initialisation de la fenêtre principale
        self.setWindowTitle("QListWidget Item Click Detection")
        self.setGeometry(100, 100, 300, 200)

        # Layout principal
        layout = QVBoxLayout()

        # Création du QListWidget
        self.list_widget = QListWidget()
        
        # Ajouter des éléments à la liste
        self.list_widget.addItem("Item 1")
        self.list_widget.addItem("Item 2")
        self.list_widget.addItem("Item 3")

        # Création d'une étiquette pour afficher l'élément cliqué
        self.label = QLabel("Aucun élément sélectionné")

        # Connecter le signal itemClicked à la méthode qui gère le clic
        self.list_widget.itemClicked.connect(self.on_item_clicked)

        # Ajouter le QListWidget et l'étiquette au layout
        layout.addWidget(self.list_widget)
        layout.addWidget(self.label)

        # Appliquer le layout à la fenêtre
        self.setLayout(layout)

    """def on_item_clicked(self, item):
        # Cette méthode est appelée lorsque l'élément est cliqué
        self.label.setText(f"Vous avez cliqué sur : {item.text()}")"""

# Exécuter l'application
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
