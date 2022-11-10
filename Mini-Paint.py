from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow): 
    def __init__(self):   
        # Avoids referring to the base class explicitly
        super().__init__() 

        # Title of the window
        self.setWindowTitle("Paint")
        # Geometry of the main window
        self.setGeometry(100, 100, 800, 600)

        # Icon for the Main window 
        self.setWindowIcon(QIcon('icon.webp'))

        # Creating image object
        self.image = QImage(self.size(), QImage.Format_RGB32)
        
        # Filling the image with white color
        self.image.fill(Qt.white) 

        # Variables
        # Drawing Flag
        self.drawing = False

        # Default Brush Size
        self.brushSize = 2

        # Default Color
        self.brushColor = Qt.black

        # QPoint object to define points in a plane
        self.lastPoint = QPoint()

        # Menubar
        mainMenu = self.menuBar()
        # File Menu
        fileMenu = mainMenu.addMenu("File")

        # Adding Brush-Size to main-menu
        brush_size = mainMenu.addMenu("Brush Size")
        # Adding Brush-color to main-menu
        brush_color = mainMenu.addMenu("Brush Color")

        # Creating Save Action
        save_act = QAction("Save", self) 
        # Adding short-cut for saving
        save_act.setShortcut("Ctrl + S") 
        # Adding save to file-menu
        fileMenu.addAction(save_act)
        # Triggering action to save
        save_act.triggered.connect(self.save) 

        # Creating Clear Action
        clear_act = QAction("Clear", self) 
        # Adding short-cut for clearing
        clear_act.setShortcut("Ctrl + C") 
        # Adding clear to file-menu
        fileMenu.addAction(clear_act)
        # Triggering action to clear
        clear_act.triggered.connect(self.clear) 

        # Creating options for brush sizes
        # Creating action to change the pixel size
        # Adding action to the brush size
        pix_2 = QAction("2px", self)
        brush_size.addAction(pix_2)
        pix_2.triggered.connect(self.Pixel_2)

        pix_4 = QAction("4px", self)
        brush_size.addAction(pix_4)
        pix_4.triggered.connect(self.Pixel_4)

        pix_6 = QAction("6px", self) 
        brush_size.addAction(pix_6) 
        pix_6.triggered.connect(self.Pixel_6) 
  
        pix_8 = QAction("8px", self) 
        brush_size.addAction(pix_8) 
        pix_8.triggered.connect(self.Pixel_8)

        pix_10 = QAction("10px", self)
        brush_size.addAction(pix_10)
        pix_10.triggered.connect(self.Pixel_10) 
  
        pix_12 = QAction("12px", self) 
        brush_size.addAction(pix_12) 
        pix_12.triggered.connect(self.Pixel_12)

        # Creating options for brush color
        # Creating and Adding actions for colors
        black = QAction("Black",self)
        brush_color.addAction(black)
        black.triggered.connect(self.blackColor) 
        
        white = QAction("White",self)
        brush_color.addAction(white)
        white.triggered.connect(self.whiteColor)
        
        green = QAction("Green",self)
        brush_color.addAction(green)
        green.triggered.connect(self.greenColor)
        
        yellow = QAction("Yellow",self)
        brush_color.addAction(yellow)
        yellow.triggered.connect(self.yellowColor)
        
        red = QAction("Red",self)
        brush_color.addAction(red)
        red.triggered.connect(self.redColor)

        blue = QAction("Blue",self)
        brush_color.addAction(blue)
        blue.triggered.connect(self.blueColor)

        cyan = QAction("Cyan",self)
        brush_color.addAction(cyan)
        cyan.triggered.connect(self.cyanColor)
    
    # Mouse Clicks
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
        
    # Tracking Mouse Movement
    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            # Setting the pen
            painter.setPen(QPen(self.brushColor, self.brushSize,  Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)) 
                
            # Drawing the line
            painter.drawLine(self.lastPoint,event.pos())

            # Change the last point
            self.lastPoint = event.pos()
            self.update()
        
    # Mouse Release event
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
        
    # Paint event
    def paintEvent(self, event):
        # create a canvas 
        canvasPainter = QPainter(self)  
        # draw rectangle  on the canvas 
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
        
    # Saving event
    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ") 
        if filePath == "": 
            return
        self.image.save(filePath) 
        
    # Clearing event 
    def clear(self):
        self.image.fill(Qt.white)
        self.update()
        
    # Defining pixel sizes
    def Pixel_2(self):
        self.brushSize = 2

    def Pixel_4(self):
        self.brushSize = 4
        
    def Pixel_6(self): 
        self.brushSize = 6
  
    def Pixel_8(self): 
        self.brushSize = 8

    def Pixel_10(self): 
        self.brushSize = 10 
  
    def Pixel_12(self): 
        self.brushSize = 12
        
    # Defining brush color
    def blackColor(self): 
        self.brushColor = Qt.black 
        
    def whiteColor(self): 
        self.brushColor = Qt.white 
        
    def greenColor(self): 
        self.brushColor = Qt.green 
        
    def yellowColor(self): 
        self.brushColor = Qt.yellow 
        
    def redColor(self): 
        self.brushColor = Qt.red
    
    def blueColor(self): 
        self.brushColor = Qt.blue
    
    def cyanColor(self): 
        self.brushColor = Qt.cyan
        
# Creating the GUI
App = QApplication(sys.argv) 
window = Window() 
window.show() 
sys.exit(App.exec())
