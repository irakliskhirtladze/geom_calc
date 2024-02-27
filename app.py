import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QPixmap
import math

class MainWindow(QMainWindow):
    
    def __init__(self) -> None:
        """Initialize UI and connect buttons with methods"""
        super().__init__()
        self.ui = loadUi("ui/calc.ui", self)
        # App always srarts with home page
        self.stackedWidget.setCurrentIndex(0)
        
        # Clicking radiobuttons displays correcponding figure on home page
        self.ui.radioButton.clicked.connect(self.change_image)
        self.ui.radioButton_2.clicked.connect(self.change_image)
        self.ui.radioButton_3.clicked.connect(self.change_image)
        self.ui.radioButton_4.clicked.connect(self.change_image)
            
        # Go to specific figure page from home page
        self.ui.pushButton.clicked.connect(self.switch_page)
        
        # Return to home page from any other page
        self.ui.pushButton_8.clicked.connect(self.go_home)
        self.ui.pushButton_9.clicked.connect(self.go_home)
        self.ui.pushButton_7.clicked.connect(self.go_home)
        self.ui.pushButton_2.clicked.connect(self.go_home)

        # Calculate area and/or perimeter of every figure
        self.ui.pushButton_6.clicked.connect(self.calculate_circle)
        self.ui.pushButton_3.clicked.connect(self.calculate_triangle)
        self.ui.pushButton_4.clicked.connect(self.calculate_trapezoid)
        self.ui.pushButton_5.clicked.connect(self.calculate_square)
        
    def change_image(self) -> None:
        """Changes image on home page when radiobutton is clicked"""
        if self.ui.radioButton.isChecked():
            pixmap = QPixmap(f"resources/circle.png")
        elif self.ui.radioButton_2.isChecked():
            pixmap = QPixmap(f"resources/triangle.png")
        elif self.ui.radioButton_3.isChecked():
            pixmap = QPixmap(f"resources/trap.png")
        elif self.ui.radioButton_4.isChecked():
            pixmap = QPixmap(f"resources/rect.png")    
        self.ui.label.setPixmap(pixmap)

    def switch_page(self) -> None:
        """ Go to a selected figure's page when "Calculate figure" button is clicked" """
        if self.ui.radioButton.isChecked():
            self.stackedWidget.setCurrentIndex(1)
        elif self.ui.radioButton_2.isChecked():
            self.stackedWidget.setCurrentIndex(2)
        elif self.ui.radioButton_3.isChecked():
            self.stackedWidget.setCurrentIndex(3)
        elif self.ui.radioButton_4.isChecked():
            self.stackedWidget.setCurrentIndex(4)

    def go_home(self) -> None:   
        """Return to home page from any other page"""    
        self.stackedWidget.setCurrentIndex(0)

    def calculate_circle(self) -> None:
        """Try to calculate circle if radius is more than 0"""

        radius = float(self.ui.doubleSpinBox_9.text())

        if radius == 0:
            self.ui.label_5.setStyleSheet("color: red")
            self.ui.label_5.setText("Radius must be greater than 0")

            self.ui.label_42.setText('')
            self.ui.label_40.setText('')

        else: 
            area = math.pi * radius ** 2
            self.ui.label_42.setText(str(round(area,2)))

            circumference = radius * 2 * math.pi
            self.ui.label_40.setText(str(round(circumference, 2)))

            self.ui.label_5.setText("") 

    def calculate_triangle(self) -> None:
        """Calculates triangle if all sides are more than 0"""
        side_1 = float(self.ui.doubleSpinBox_2.text())
        side_2 = float(self.ui.doubleSpinBox_3.text())
        side_3 = float(self.ui.doubleSpinBox_4.text())

        if 0 in (side_1, side_2, side_3):
            self.ui.label_4.setStyleSheet("color: red")
            self.ui.label_4.setText("All sides must be greater than 0")    

            self.ui.label_15.setText('')
            self.ui.label_13.setText('')    

        else:
            perimeter = side_1 + side_2 + side_3
            self.ui.label_13.setText(str(round(perimeter, 2)))
            
            p = perimeter/2 # Half perimeter
            # Using Heron's formula
            area = math.sqrt(p*(p-side_1)*(p-side_2)*(p-side_3))
            self.ui.label_15.setText(str(round(area, 2)))

            self.ui.label_4.setText("") 

    def calculate_trapezoid(self) -> None:
        """Calculates trapezoid depending on known parameters"""

        base_1 = float(self.ui.doubleSpinBox_5.text())
        base_2 = float(self.ui.doubleSpinBox_6.text())
        side_1 = float(self.ui.doubleSpinBox.text())
        side_2 = float(self.ui.doubleSpinBox_10.text())
        height = float(self.ui.doubleSpinBox_7.text())
        
        # Calculate area and perimeter even when some parameters are 0
        perimeter = base_1 + base_2 + side_1 + side_2
        area = (base_1 + base_2) / 2 * height
        
        # If height is 0 but all sides are >0, calculate only perimeter
        if height == 0 and 0 not in (base_1, base_2, side_1, side_2):
            self.ui.label_24.setText(str(round(perimeter, 2)))

            self.ui.label_6.setStyleSheet("color: purple")
            self.ui.label_6.setText("Could not calculate area: Unknown height")

            self.ui.label_26.setText("")
        
        # If on of the sides is 0 but both bases and height is >0, calculate only area
        elif 0 in (side_1, side_2) and 0 not in (base_1, base_2, height):
            self.ui.label_26.setText(str(round(area, 2)))

            self.ui.label_6.setStyleSheet("color: purple")
            self.ui.label_6.setText("Could not calculate perimeter: Unknown sides")

            self.ui.label_24.setText("")

        # If all parameters are >0 then calculate both area and perimeter
        elif 0 not in (base_1, base_2, side_1, side_2, height):
            self.ui.label_24.setText(str(round(perimeter, 2)))
            self.ui.label_26.setText(str(round(area, 2)))

            self.ui.label_6.setText("")
        
        # In any other case do not calculate trapezoid
        else:
            self.ui.label_6.setStyleSheet("color: red")
            self.ui.label_6.setText("Neither area nor perimeter could be calculated") 

    def calculate_square(self) -> None:
        """Calculates square is a side is more than 0"""
        side = float(self.ui.doubleSpinBox_8.text())

        if side == 0:
            self.ui.label_7.setStyleSheet("color: red")
            self.ui.label_7.setText("Side must be greater than 0")

            self.ui.label_33.setText('')
            self.ui.label_35.setText('')

        else:
            area = side ** 2
            perimeter = side * 4

            self.ui.label_33.setText(str(round(perimeter, 2)))
            self.ui.label_35.setText(str(round(area, 2)))

            self.ui.label_7.setText("")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("TBC Academy")
    window.setWindowIcon(QIcon("resources/tbcicon.png"))
    window.show()

    sys.exit(app.exec_())