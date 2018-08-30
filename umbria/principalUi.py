# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/javier/Dropbox/Programas/spikes/exportadorUmbria/umbria/resources/principal.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 285)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagenes/notificadorLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.Contrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.Contrasena.setObjectName("Contrasena")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Contrasena)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.Slug = QtWidgets.QLineEdit(self.centralwidget)
        self.Slug.setObjectName("Slug")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Slug)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Destino = QtWidgets.QLineEdit(self.centralwidget)
        self.Destino.setObjectName("Destino")
        self.horizontalLayout.addWidget(self.Destino)
        self.pushDirectorio = QtWidgets.QPushButton(self.centralwidget)
        self.pushDirectorio.setObjectName("pushDirectorio")
        self.horizontalLayout.addWidget(self.pushDirectorio)
        self.formLayout.setLayout(11, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.Usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.Usuario.setObjectName("Usuario")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Usuario)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushDescargar = QtWidgets.QPushButton(self.centralwidget)
        self.pushDescargar.setObjectName("pushDescargar")
        self.verticalLayout.addWidget(self.pushDescargar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Descargar Umbria"))
        self.label_3.setText(_translate("MainWindow", "Slug"))
        self.pushDirectorio.setText(_translate("MainWindow", "Buscar"))
        self.label.setText(_translate("MainWindow", "Usuario"))
        self.label_2.setText(_translate("MainWindow", "Contraseña"))
        self.label_4.setText(_translate("MainWindow", "Destino"))
        self.pushDescargar.setText(_translate("MainWindow", "Descargar"))

from . import resources_rc
