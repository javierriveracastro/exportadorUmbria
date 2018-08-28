# coding=utf-8

"""
Modulo con un GUI para descargar Umbria
"""

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from .principalUi import Ui_MainWindow


class VentanaPrincipal(QMainWindow):
    """
    Ventana principal de la aplicacion
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.usuario, self.contrasena, self.slug, self.destino = \
            None, None, None, None
        # Señales
        self.ui.pushDescargar.clicked.connect(self.descargar)

    def descargar(self):
        """
        Pulsan descargar
        """
        self.usuario = str(self.ui.Usuario.text())
        self.contrasena = str(self.ui.Contrasena.text())
        self.slug = str(self.ui.Slug.text())
        self.destino = str(self.ui.Destino.text())
        self.close()


def main():
    """
    Bucle principal
    """
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec_()
    return ventana.usuario, ventana.contrasena, ventana.slug, ventana.destino
