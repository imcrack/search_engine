import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.browser= QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navigation
        navigation=QToolBar()
        self.addToolBar(navigation)
        
        #buttons
        back=QAction('<', self)
        back.triggered.connect(self.browser.back)
        navigation.addAction(back)

        
        forward=QAction('>', self)
        forward.triggered.connect(self.browser.forward)
        navigation.addAction(forward)

        reload=QAction('🔃', self)
        reload.triggered.connect(self.browser.reload)
        navigation.addAction(reload)

        home=QAction('🏠', self)
        home.triggered.connect(self.navigate_home)
        navigation.addAction(home)

        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigation.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)
        
    
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://googl.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, a):
        self.url_bar.setText(a.toString())


app=QApplication(sys.argv)
QApplication.setApplicationName("LAALM")
window= MainWindow()
app.exec_()
