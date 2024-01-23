# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QFile, Slot
from PySide6.QtUiTools import QUiLoader


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.bags_widget = None  # Initialize bags_widget as None
        self.clothing_widget = None
        self.shoes_widget = None
        self.beautyproducts_widget = None
        self.wigs_widget = None
        self.accessories_widget = None
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

        self.bagsBtn = self.findChild(QPushButton, "bags")
        self.bagsBtn.clicked.connect(self.showBags)

        self.clothingBtn = self.findChild(QPushButton, "clothing")
        self.clothingBtn.clicked.connect(self.showClothing)

        self.shoesBtn = self.findChild(QPushButton, "shoes")
        self.shoesBtn.clicked.connect(self.showShoes)

        self.beautyproductsBtn = self.findChild(QPushButton, "beautyproducts")
        self.beautyproductsBtn.clicked.connect(self.showBeautyproducts)

        self.wigsBtn = self.findChild(QPushButton, "wigs")
        self.wigsBtn.clicked.connect(self.showWigs)

        self.accessoriesBtn = self.findChild(QPushButton, "accessories")
        self.accessoriesBtn.clicked.connect(self.showAccessories)




    @Slot()
    def showBags(self):
        if not self.bags_widget:  # Create bags_widget only if it doesn't exist
            loader = QUiLoader()
            path = os.fspath(Path(__file__).resolve().parent / "bags.ui")
            ui_file = QFile(path)
            ui_file.open(QFile.ReadOnly)
            self.bags_widget = loader.load(ui_file)
            ui_file.close()
        self.bags_widget.show()

    @Slot()
    def showClothing(self):
        if not self.clothing_widget:  # Create bags_widget only if it doesn't exist
            loader = QUiLoader()
            path = os.fspath(Path(__file__).resolve().parent / "clothing.ui")
            ui_file = QFile(path)
            ui_file.open(QFile.ReadOnly)
            self.clothing_widget = loader.load(ui_file)
            ui_file.close()
        self.clothing_widget.show()

    @Slot()
    def showShoes(self):
        if not self.shoes_widget:  # Create bags_widget only if it doesn't exist
            loader = QUiLoader()
            path = os.fspath(Path(__file__).resolve().parent / "shoes.ui")
            ui_file = QFile(path)
            ui_file.open(QFile.ReadOnly)
            self.shoes_widget = loader.load(ui_file)
            ui_file.close()
        self.shoes_widget.show()

    @Slot()
    def showBeautyproducts(self):
        if not self.beautyproducts_widget:  # Create bags_widget only if it doesn't exist
            loader = QUiLoader()
            path = os.fspath(Path(__file__).resolve().parent / "beautyproducts.ui")
            ui_file = QFile(path)
            ui_file.open(QFile.ReadOnly)
            self.beautyproducts_widget = loader.load(ui_file)
            ui_file.close()
        self.beautyproducts_widget.show()

    @Slot()
    def showWigs(self):
        if not self.wigs_widget:  # Create bags_widget only if it doesn't exist
            loader = QUiLoader()
            path = os.fspath(Path(__file__).resolve().parent / "wigs.ui")
            ui_file = QFile(path)
            ui_file.open(QFile.ReadOnly)
            self.wigs_widget = loader.load(ui_file)
            ui_file.close()
        self.wigs_widget.show()

    @Slot()
    def showAccessories(self):
        if not self.accessories_widget:  # Create bags_widget only if it doesn't exist
            loader = QUiLoader()
            path = os.fspath(Path(__file__).resolve().parent / "accessories.ui")
            ui_file = QFile(path)
            ui_file.open(QFile.ReadOnly)
            self.accessories_widget = loader.load(ui_file)
            ui_file.close()
        self.accessories_widget.show()


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
