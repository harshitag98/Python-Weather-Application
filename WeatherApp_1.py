# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import os
import gmplot
import json

urlp1='https://api.openweathermap.org/data/2.5/weather?'
urlCity='q='
urlp2='&APPID='                         #Place your Obtained openweathermap API Key Here next to 'APPID='. It is like 5b1625e2a9a935be9c3f96b63e556cc7
urlCordP1='lat={'
urlCordP2='}&lon={'
def reqData(city):
    print("Requesting data",city)
    url=urlp1+urlCity+city+urlp2
    response=requests.get(url)
    data=response.json()
    return data

class Ui_Dialog(object):
    def func(self):
        try:
            print("Weather Selected")
            city=self.lineEdit.text()
            if(city=='City'):
                self.cityDisp.setText("Please enter City Name")
                self.tempDisp.setText("")
                self.weathDisp.setText("")
                return
            getData=reqData(city)
            self.cityDisp.setText(city)
            self.tempDisp.setText(str(int(float((getData['main'])['temp'])-273.15)))
            self.weathDisp.setText((getData['weather'][0])['main']+","+(getData['weather'][0])['description'])
        except Exception as e:
            print(e)
            self.cityDisp.setText("There was some error!!!")
            self.tempDisp.setText("")
            self.weathDisp.setText("")

    def func2(self):
        try:
            print("Loc Weather Selected")
            locReq=requests.get('https://ipinfo.io/city/?token=')     # Place Your Obtained IpInfo API key here next to 'token='. It is like 8f5570cbc2cc02
            latLng=requests.get('https://ipinfo.io/loc/?token=')          # Place Your Obtained IpInfo API key here next to 'token='. It is like 8f5570cbc2cc02
            latLng=latLng.text.strip()
            [var1,var2]=latLng.split(',')
            global lat
            lat=var1
            global lng
            lng=var2
            self.latDisp.display(lat)
            self.longDisp.display(lng)
            cityData=locReq.text.strip()
            getData=reqData(cityData)
            self.cityDisp.setText(cityData)
            self.tempDisp.setText(str(int(float((getData['main'])['temp'])-273.15)))
            self.weathDisp.setText((getData['weather'][0])['main']+","+(getData['weather'][0])['description'])
        except Exception as e:
            print(e)

    def func3(self):
        try:
            print(lat,lng)
            gmap1=gmplot.GoogleMapPlotter(float(lat),float(lng),16)
            gmap1.marker(float(lat),float(lng))
            gmap1.draw('D:\\maps123.html')
            os.system('D:\\maps123.html')
        except:
            self.cityDisp.setText("First Locate yourself")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1446, 890)
        Dialog.setStyleSheet("QDialog{background-image:url(Background_1.jpg)}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 50, 862, 48))
        font = QtGui.QFont()
        font.setFamily("Castellar")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{color:rgb(255, 210, 221)}")
        self.label.setLineWidth(3)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.weathers = QtWidgets.QPushButton(Dialog)
        self.weathers.setGeometry(QtCore.QRect(70, 260, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(20)
        self.weathers.setFont(font)
        self.weathers.setObjectName("weathers")
        self.locWeathers = QtWidgets.QPushButton(Dialog)
        self.locWeathers.setGeometry(QtCore.QRect(470, 260, 351, 81))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(20)
        self.locWeathers.setFont(font)
        self.locWeathers.setObjectName("locWeathers")
        self.locPlot = QtWidgets.QPushButton(Dialog)
        self.locPlot.setGeometry(QtCore.QRect(1000, 260, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(20)
        self.locPlot.setFont(font)
        self.locPlot.setObjectName("locPlot")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 486, 34))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi Cond")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{color:rgb(170, 255, 255)}")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(550, 160, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.cityLabel = QtWidgets.QLabel(Dialog)
        self.cityLabel.setGeometry(QtCore.QRect(60, 390, 50, 31))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(20)
        self.cityLabel.setFont(font)
        self.cityLabel.setStyleSheet("QLabel{color:rgb(255, 0, 0)}")
        self.cityLabel.setObjectName("cityLabel")
        self.tempLabel = QtWidgets.QLabel(Dialog)
        self.tempLabel.setGeometry(QtCore.QRect(60, 450, 149, 31))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(20)
        self.tempLabel.setFont(font)
        self.tempLabel.setStyleSheet("QLabel{color:rgb(255, 0, 0)}")
        self.tempLabel.setObjectName("tempLabel")
        self.weathLabel = QtWidgets.QLabel(Dialog)
        self.weathLabel.setGeometry(QtCore.QRect(60, 540, 227, 31))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(20)
        self.weathLabel.setFont(font)
        self.weathLabel.setStyleSheet("QLabel{color:rgb(255, 0, 0)}")
        self.weathLabel.setObjectName("weathLabel")
        self.latLabel = QtWidgets.QLabel(Dialog)
        self.latLabel.setGeometry(QtCore.QRect(730, 390, 96, 31))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(20)
        self.latLabel.setFont(font)
        self.latLabel.setStyleSheet("QLabel{color:rgb(255, 210, 221)}")
        self.latLabel.setObjectName("latLabel")
        self.lonLabel = QtWidgets.QLabel(Dialog)
        self.lonLabel.setGeometry(QtCore.QRect(730, 450, 116, 31))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(20)
        self.lonLabel.setFont(font)
        self.lonLabel.setStyleSheet("QLabel{color:rgb(255, 210, 221)}")
        self.lonLabel.setObjectName("lonLabel")
        self.cityDisp = QtWidgets.QLineEdit(Dialog)
        self.cityDisp.setGeometry(QtCore.QRect(130, 390, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(20)
        self.cityDisp.setFont(font)
        self.cityDisp.setObjectName("cityDisp")
        self.tempDisp = QtWidgets.QLineEdit(Dialog)
        self.tempDisp.setGeometry(QtCore.QRect(240, 450, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(20)
        self.tempDisp.setFont(font)
        self.tempDisp.setObjectName("tempDisp")
        self.weathDisp = QtWidgets.QLineEdit(Dialog)
        self.weathDisp.setGeometry(QtCore.QRect(300, 530, 881, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(20)
        self.weathDisp.setFont(font)
        self.weathDisp.setText("")
        self.weathDisp.setObjectName("weathDisp")
        self.latDisp = QtWidgets.QLCDNumber(Dialog)
        self.latDisp.setGeometry(QtCore.QRect(870, 380, 221, 51))
        self.latDisp.setSmallDecimalPoint(True)
        self.latDisp.setProperty("value", 0.0000)
        self.latDisp.setObjectName("latDisp")
        self.longDisp = QtWidgets.QLCDNumber(Dialog)
        self.longDisp.setGeometry(QtCore.QRect(870, 440, 221, 51))
        self.longDisp.setSmallDecimalPoint(True)
        self.longDisp.setProperty("value", 0.0000)
        self.longDisp.setObjectName("longDisp")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.weathers.clicked.connect(self.func)
        self.locWeathers.clicked.connect(self.func2)
        self.locPlot.clicked.connect(self.func3)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Well,What\'s The Weather Today!!"))
        self.weathers.setText(_translate("Dialog", "Find City Weather"))
        self.locWeathers.setText(_translate("Dialog", "Find My Location\'s Weather"))
        self.locPlot.setText(_translate("Dialog", "Plot My Location On the Map"))
        self.label_2.setText(_translate("Dialog", "Enter the City Whose Weather you Want to Know"))
        self.lineEdit.setText(_translate("Dialog", "City"))
        self.cityLabel.setText(_translate("Dialog", "City:"))
        self.tempLabel.setText(_translate("Dialog", "Temperature:"))
        self.weathLabel.setText(_translate("Dialog", "Weather Conditions:"))
        self.latLabel.setText(_translate("Dialog", "Latitude:"))
        self.lonLabel.setText(_translate("Dialog", "Longitude:"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
