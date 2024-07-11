# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'android.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QDoubleValidator)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget, QFileDialog, QMessageBox)
from creaWord import *
import os
import sqlite3
import csv
import shutil
import json

class Ui_Dialog_android(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(448, 242)
        
        double_validator = QDoubleValidator(self)
        double_validator.setDecimals(2)
        
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_db = QLineEdit(Dialog)
        self.lineEdit_db.setObjectName(u"lineEdit_db")
        self.lineEdit_db.setMaximumSize(QSize(231, 16777215))
        self.lineEdit_db.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")
        self.lineEdit_db.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_db)

        self.btn_db = QPushButton(Dialog)
        self.btn_db.clicked.connect(self.select_file_bd)
        self.btn_db.setObjectName(u"btn_db")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_db.sizePolicy().hasHeightForWidth())
        self.btn_db.setSizePolicy(sizePolicy)
        self.btn_db.setMaximumSize(QSize(231, 16777215))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_db.setFont(font)
        self.btn_db.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_db.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgb(74, 152, 255);\n"
"border-radius: 5px;\n"
"padding: 5px; \n"
"}\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"background-color: rgb(37, 77, 255)\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_db)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_nueva_carpeta = QLineEdit(Dialog)
        self.lineEdit_nueva_carpeta.setObjectName(u"lineEdit_nueva_carpeta")
        self.lineEdit_nueva_carpeta.setMaximumSize(QSize(231, 16777215))
        self.lineEdit_nueva_carpeta.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")
        self.lineEdit_nueva_carpeta.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_nueva_carpeta)

        self.btn_nueva_carpeta = QPushButton(Dialog)
        self.btn_nueva_carpeta.clicked.connect(self.select_folder_nuevaCarpeta)
        self.btn_nueva_carpeta.setObjectName(u"btn_nueva_carpeta")
        self.btn_nueva_carpeta.setFont(font)
        self.btn_nueva_carpeta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nueva_carpeta.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgb(74, 152, 255);\n"
"border-radius: 5px;\n"
"padding: 5px; \n"
"}\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"background-color: rgb(37, 77, 255)\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_nueva_carpeta)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_multimedia = QLineEdit(Dialog)
        self.lineEdit_multimedia.setObjectName(u"lineEdit_multimedia")
        self.lineEdit_multimedia.setMaximumSize(QSize(231, 16777215))
        self.lineEdit_multimedia.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")
        self.lineEdit_multimedia.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_multimedia)

        self.btn_multimedia = QPushButton(Dialog)
        self.btn_multimedia.clicked.connect(self.select_folder_multimedia)
        self.btn_multimedia.setObjectName(u"btn_multimedia")
        self.btn_multimedia.setFont(font)
        self.btn_multimedia.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_multimedia.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgb(74, 152, 255);\n"
"border-radius: 5px;\n"
"padding: 5px; \n"
"}\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"background-color: rgb(37, 77, 255)\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_multimedia)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_telefono = QLineEdit(Dialog)
        self.lineEdit_telefono.textChanged.connect(self.validar_numero_telefono)
        self.lineEdit_telefono.setValidator(double_validator)
        self.lineEdit_telefono.setMaxLength(11)
        self.lineEdit_telefono.setObjectName(u"lineEdit_telefono")
        self.lineEdit_telefono.setMaximumSize(QSize(231, 16777215))
        self.lineEdit_telefono.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_5.addWidget(self.lineEdit_telefono)

        self.label_telefono = QLabel(Dialog)
        self.label_telefono.setObjectName(u"label_telefono")
        font1 = QFont()
        font1.setBold(True)
        self.label_telefono.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_telefono)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.label_tiene_multimedia = QLabel(Dialog)
        self.label_tiene_multimedia.setObjectName(u"label_tiene_multimedia")

        self.horizontalLayout_8.addWidget(self.label_tiene_multimedia)

        self.btn_tiene_multimedia = QPushButton(Dialog)
        self.btn_tiene_multimedia.clicked.connect(self.tiene_multimedia)
        self.btn_tiene_multimedia.setObjectName(u"btn_tiene_multimedia")
        sizePolicy.setHeightForWidth(self.btn_tiene_multimedia.sizePolicy().hasHeightForWidth())
        self.btn_tiene_multimedia.setSizePolicy(sizePolicy)
        self.btn_tiene_multimedia.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tiene_multimedia.setStyleSheet(u"QPushButton{\n"
"color: blue;\n"
"border: none;\n"
"background-color: transparent;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.btn_tiene_multimedia)

        self.horizontalSpacer = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_copiar = QPushButton(Dialog)
        self.btn_copiar.clicked.connect(self.copiar)
        self.btn_copiar.setObjectName(u"btn_copiar")
        self.btn_copiar.setFont(font)
        self.btn_copiar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_copiar.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgb(74, 152, 255);\n"
"border-radius: 5px;\n"
"padding: 5px; \n"
"}\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"background-color: rgb(37, 77, 255)\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_copiar)

        self.btn_reiniciar = QPushButton(Dialog)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.btn_reiniciar.setObjectName(u"btn_reiniciar")
        self.btn_reiniciar.setFont(font)
        self.btn_reiniciar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reiniciar.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgb(74, 152, 255);\n"
"border-radius: 5px;\n"
"padding: 5px; \n"
"}\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"background-color: rgb(37, 77, 255)\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_reiniciar)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Word Creator - Android", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Introduce los datos requeridos para copiar los archivos a la \n"
"nueva carpeta y crear el Word:", None))
        self.lineEdit_db.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduce la base de datos (msgstore.db)...", None))
        self.btn_db.setText(QCoreApplication.translate("Dialog", u"Seleccionar archivo", None))
        self.lineEdit_nueva_carpeta.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca ruta de nueva carpeta...", None))
        self.btn_nueva_carpeta.setText(QCoreApplication.translate("Dialog", u"Seleccionar carpeta", None))
        self.lineEdit_multimedia.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca ruta archivos multimedia...", None))
        self.btn_multimedia.setText(QCoreApplication.translate("Dialog", u"Seleccionar carpeta", None))
        self.lineEdit_telefono.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca n\u00famero de tel\u00e9fono...", None))
        self.label_telefono.setText("")
        self.label_tiene_multimedia.setText(QCoreApplication.translate("Dialog", u"\u00bfYa tienes la carpeta con la multimedia?", None))
        self.btn_tiene_multimedia.setText(QCoreApplication.translate("Dialog", u"Pulsa aqu\u00ed", None))
        self.btn_copiar.setText(QCoreApplication.translate("Dialog", u"Copiar archivos", None))
        self.btn_reiniciar.setText(QCoreApplication.translate("Dialog", u"Reiniciar", None))
        pass
    # retranslateUi
    
    def reiniciar(self):
        self.lineEdit_db.clear()
        self.lineEdit_multimedia.clear()
        self.lineEdit_telefono.clear()
        self.lineEdit_nueva_carpeta.clear()
        
    def validar_numero_telefono(self):
        numero = self.lineEdit_telefono.text()

        # Verificar si el número de teléfono tiene el formato deseado (por ejemplo, 34637485912)
        if len(numero) == 11 and numero.isdigit() and numero.startswith('34'):
            self.label_telefono.setText("<font color='green'>Numero de telefono correcto</font>")
        else:
            if numero == '': 
                self.label_telefono.clear()
                return 
            self.label_telefono.setText("<font color='red'>Numero de telefono incorrecto</font>")
    
    # Método para elegir la ruta del fichero msgstore.db
    def select_file_bd(self):
        # Abrir el cuadro de diálogo para seleccionar un archivo
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar Archivo")
        if file_path:
            self.lineEdit_db.setText(file_path)
            
    # Método para elegir la ruta de la carpeta que se va a crear
    def select_folder_nuevaCarpeta(self):
        # Abrir el cuadro de diálogo para seleccionar la carpeta que contiene los archivos
        folder_dialog = QFileDialog(self)
        folder_path = folder_dialog.getExistingDirectory(self, "Seleccionar Carpeta")
        if folder_path:
            self.lineEdit_nueva_carpeta.setText(folder_path)
            
    # Método para elegir la ruta de la carpeta con los directorios de los archivos a copiar
    def select_folder_multimedia(self):
        # Abrir el cuadro de diálogo para seleccionar la carpeta que contiene los directorios de los archivos
        folder_dialog = QFileDialog(self)
        folder_path = folder_dialog.getExistingDirectory(self, "Seleccionar Carpeta")
        if folder_path:
            self.lineEdit_multimedia.setText(folder_path)
    
    def crear_carpeta(self, ruta, nombre):
        nueva_ruta = os.path.join(ruta, nombre)
        try:
            os.mkdir(nueva_ruta)
            print(f"Carpeta '{nombre}' creada correctamente en '{ruta}'.")
            return nueva_ruta
        except OSError as error:
            QMessageBox.critical(self, 'Error', f"No se pudo crear la carpeta '{nombre}' en '{ruta}': {error}")
            return None

    def guardar_csv(self, archivos, ruta_completa):
        with open(ruta_completa, 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)  # Escribir encabezados
            escritor_csv.writerows(archivos)
            
    def copiar(self):
        base_datos_whatsapp = self.lineEdit_db.text()
        numero = self.lineEdit_telefono.text()
        carpeta_medios = self.lineEdit_multimedia.text()
        ruta_nueva_carpeta = self.lineEdit_nueva_carpeta.text()
        
        self.crear_carpeta(ruta_nueva_carpeta, 'Media')
        QMessageBox.information(self, 'Carpeta creada', f'Se ha creado la carpeta Media en {ruta_nueva_carpeta}')
        
        # Obtener la ruta absoluta del directorio actual
        dir_actual = os.path.dirname(os.path.abspath(__file__))

        # Construir la ruta absoluta al archivo consultas.json
        ruta_json_consultas = os.path.join(dir_actual, 'consultas.json')
        
        # Definir la consulta SQL
        with open(ruta_json_consultas, 'r') as archivo:
            consultas = json.load(archivo)
        consulta_sql = consultas['consulta_android']
        
        ruta_completa_csv = os.path.join(ruta_nueva_carpeta, f'archivos_{numero}.csv')
        if os.path.exists(ruta_completa_csv):
            respuesta = QMessageBox.question(self, 'CSV existente en directorio', 'Se ha encontrado un CSV en el directorio. ¿Desea borrarlo y crear uno nuevo?', QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.Yes:
                self.obtener_contenido_multimedia(base_datos_whatsapp, numero, consulta_sql, ruta_completa_csv)
                QMessageBox.information(self, 'CSV nuevo creado', 'Se ha eliminado el antiguo CSV y se ha creado uno nuevo en el directorio.')
            else:
                QMessageBox.information(self, 'CSV nuevo no creado', 'No se ha creado un nuevo CSV. El antiguo CSV se ha mantenido en el directorio.')
        else:
            self.obtener_contenido_multimedia(base_datos_whatsapp, numero, consulta_sql, ruta_completa_csv)
            QMessageBox.information(self, 'CSV nuevo creado', 'Se ha creado un nuevo CSV para la copia de archivos.')

        QMessageBox.information(self, "Copiando archivos", "Copiando archivos. Este proceso puede tardar un momento. Se avisará cuando este acabe. Por favor, presione Aceptar y espere...")

        with open(f'{ruta_completa_csv}', 'r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            lista_archivos_originales = list(lector_csv)

        self.copiar_archivos(carpeta_medios, lista_archivos_originales, f'{ruta_nueva_carpeta}/Media')
        
        respuesta = QMessageBox.information(self, "Proceso completado", f'Los archivos han sido copiados a {ruta_nueva_carpeta}.\n\n¿Desea continuar y crear el Word?', QMessageBox.Yes | QMessageBox.No) 

        if respuesta == QMessageBox.Yes:
            # Leer los valores de los QLineEdit
            base_datos_whatsapp = self.lineEdit_db.text()
            numero = self.lineEdit_telefono.text()
            sistema = 'android'

            # Escribir los valores en un archivo JSON
            datos = {'base_datos_whatsapp': base_datos_whatsapp, 'numero': numero, 'sistema': sistema}
            with open(f'{ruta_nueva_carpeta}/Media/datos.json', 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo)
            self.ventanaWord = Ventana_Word()
            self.ventanaWord.show()
            self.accept()
        else: 
            self.reiniciar()
    
    def obtener_contenido_multimedia(self, base_datos, numero_telefono, consulta_sql, ruta_completa_csv):
        conexion = sqlite3.connect(base_datos)
        cursor = conexion.cursor()
        cursor.execute(consulta_sql, (numero_telefono,))
        resultados = cursor.fetchall()
        conexion.close()
        if resultados:
            with open(f'{ruta_completa_csv}', 'w', newline='', encoding='utf-8') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerows(resultados)
            print("Se ha escrito correctamente en el archivo CSV.")
        else:
            print("No se encontraron resultados para la consulta.")
    
    def copiar_archivos(self, ruta_origen, lista_archivos, ruta_destino):
        archivos_copiados = []
        for archivo in lista_archivos:
            ruta_origen_archivo = os.path.join(ruta_origen, archivo[0])
            if os.path.isfile(ruta_origen_archivo):
                shutil.copy(ruta_origen_archivo, ruta_destino)
                archivos_copiados.append(archivo)
                print(f"Archivo '{archivo[0]}' copiado a '{ruta_destino}'")
            else:
                print(f"¡El archivo '{archivo[0]}' no se encontró en la carpeta de medios!")
        return archivos_copiados
    
    def tiene_multimedia(self):
        self.ventana_word = Ventana_Word()
        self.ventana_word.show()
        self.accept()
    
class Ventana_Word(Ui_Dialog_Word, QDialog):
    def __init__(self):
        super(Ventana_Word, self).__init__()
        self.setupUi(self)