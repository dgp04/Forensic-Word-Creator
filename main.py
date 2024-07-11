from PySide6.QtWidgets import QApplication, QDialog
from sistema import *
from PySide6.QtCore import QTranslator, QLibraryInfo 
class VentanaPrincipal(Ui_Dialog_sistema, QDialog):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setupUi(self)
        
app  = QApplication([])

# Envolvemos la aplicación con el traductor
translator = QTranslator(app)
# Recuperamos el directorio de traducciones
translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
# Cargamos la traducción en el traductor
translator.load("qt_es", translations)
# Instalamos el traductor a la aplicación
app.installTranslator(translator)

ventana = VentanaPrincipal()
ventana.show()
app.exec()