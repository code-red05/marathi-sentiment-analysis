import tweet_handler
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)  #
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget) #
        self.lineEdit.setGeometry(QtCore.QRect(230, 120, 331, 31))
        self.lineEdit.setObjectName("lineEdit")
    
        self.lineEdit.returnPressed.connect(self.on_press_enter)  #
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 351, 31))
        self.label.setStyleSheet("font: 14pt \"Calibri\";")
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 191, 31))
        self.label_2.setStyleSheet("font: 12pt \"Calibri\";")
        self.label_2.setObjectName("label_2")
        
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 370, 161, 31))
        self.label_3.setStyleSheet("font: 12pt \"Calibri\";")
        self.label_3.setObjectName("label_3")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(230, 370, 331, 121))
        self.textBrowser.setObjectName("textBrowser")
        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 120, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.on_press_enter)  #
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 200, 131, 31))
        self.label_5.setStyleSheet("font: 12pt \"Calibri\";")
        self.label_5.setObjectName("label_5")
        
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(230, 200, 331, 121))
        self.textBrowser_2.setObjectName("textBrowser_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)  #
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):    #
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NLP Project"))
        self.label.setText(_translate("MainWindow", "Marathi Review and Opinion Analyser"))
        self.label_2.setText(_translate("MainWindow", "Enter Search Keyword :"))
        self.label_3.setText(_translate("MainWindow", "Statistical Results :"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.label_5.setText(_translate("MainWindow", "Fetched Data : "))

    def on_press_enter(self):   #
        
        input_text = self.lineEdit.text()

        pos_percent, neg_percent, pos_count, neg_count = tweet_handler.main(input_text, ui)
        self.textBrowser.setPlainText("Positive = "+str(pos_percent)+"%\nNegative = "+str(neg_percent)+"%\n"+
        	"Positive Count: "+str(pos_count)+"\nNegative Count: "+str(neg_count)+"\nTotal Count: "+str(pos_count+neg_count))


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())