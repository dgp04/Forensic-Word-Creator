# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ios.ui'
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

class Ui_Dialog_iOS(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(412, 294)
        
        double_validator = QDoubleValidator(self)
        double_validator.setDecimals(2)
        
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setKerning(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_bd = QLineEdit(Dialog)
        self.lineEdit_bd.setObjectName(u"lineEdit_bd")
        self.lineEdit_bd.setMaximumSize(QSize(231, 16777215))
        self.lineEdit_bd.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")
        self.lineEdit_bd.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_bd)

        self.btn_db = QPushButton(Dialog)
        self.btn_db.clicked.connect(self.select_file_sqlite)
        self.btn_db.setObjectName(u"btn_db")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_db.setFont(font1)
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

        self.horizontalLayout_3.addWidget(self.btn_db)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_nuevaCarpeta = QLineEdit(Dialog)
        self.lineEdit_nuevaCarpeta.setObjectName(u"lineEdit_nuevaCarpeta")
        self.lineEdit_nuevaCarpeta.setMaximumSize(QSize(231, 16777215))
        self.lineEdit_nuevaCarpeta.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")
        self.lineEdit_nuevaCarpeta.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_nuevaCarpeta)

        self.btn_nuevaCarpeta = QPushButton(Dialog)
        self.btn_nuevaCarpeta.clicked.connect(self.select_folder_nuevaCarpeta)
        self.btn_nuevaCarpeta.setObjectName(u"btn_nuevaCarpeta")
        self.btn_nuevaCarpeta.setFont(font1)
        self.btn_nuevaCarpeta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nuevaCarpeta.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_4.addWidget(self.btn_nuevaCarpeta)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_manifest = QLineEdit(Dialog)
        self.lineEdit_manifest.setObjectName(u"lineEdit_manifest")
        self.lineEdit_manifest.setMaximumSize(QSize(231, 16777215))
        self.lineEdit_manifest.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")
        self.lineEdit_manifest.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_manifest)

        self.btn_manifest = QPushButton(Dialog)
        self.btn_manifest.clicked.connect(self.select_file_manifest)
        self.btn_manifest.setObjectName(u"btn_manifest")
        self.btn_manifest.setFont(font1)
        self.btn_manifest.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_manifest.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_5.addWidget(self.btn_manifest)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_multimedia = QLineEdit(Dialog)
        self.lineEdit_multimedia.setObjectName(u"lineEdit_multimedia")
        self.lineEdit_multimedia.setMaximumSize(QSize(231, 16777215))
        self.lineEdit_multimedia.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")
        self.lineEdit_multimedia.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_multimedia)

        self.btn_multimedia = QPushButton(Dialog)
        self.btn_multimedia.clicked.connect(self.select_folder_multimedia)
        self.btn_multimedia.setObjectName(u"btn_multimedia")
        self.btn_multimedia.setFont(font1)
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

        self.horizontalLayout_6.addWidget(self.btn_multimedia)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_telefono = QLineEdit(Dialog)
        self.lineEdit_telefono.setValidator(double_validator)
        self.lineEdit_telefono.setMaxLength(11)
        self.lineEdit_telefono.setObjectName(u"lineEdit_telefono")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_telefono.sizePolicy().hasHeightForWidth())
        self.lineEdit_telefono.setSizePolicy(sizePolicy1)
        self.lineEdit_telefono.textChanged.connect(self.validar_numero_telefono)
        self.lineEdit_telefono.setMaximumSize(QSize(231, 16777215))
        self.lineEdit_telefono.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")

        self.horizontalLayout_7.addWidget(self.lineEdit_telefono)

        self.label_telefono = QLabel(Dialog)
        self.label_telefono.setObjectName(u"label_telefono")
        font2 = QFont()
        font2.setBold(True)
        self.label_telefono.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_telefono)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.label_tiene_multimedia_2 = QLabel(Dialog)
        self.label_tiene_multimedia_2.setObjectName(u"label_tiene_multimedia_2")

        self.horizontalLayout_9.addWidget(self.label_tiene_multimedia_2)

        self.btn_tiene_multimedia_2 = QPushButton(Dialog)
        self.btn_tiene_multimedia_2.clicked.connect(self.tiene_multimedia)
        self.btn_tiene_multimedia_2.setObjectName(u"btn_tiene_multimedia_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_tiene_multimedia_2.sizePolicy().hasHeightForWidth())
        self.btn_tiene_multimedia_2.setSizePolicy(sizePolicy2)
        self.btn_tiene_multimedia_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tiene_multimedia_2.setStyleSheet(u"QPushButton{\n"
"color: blue;\n"
"border: none;\n"
"background-color: transparent;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.btn_tiene_multimedia_2)

        self.horizontalSpacer_2 = QSpacerItem(75, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_copiar = QPushButton(Dialog)
        self.btn_copiar.clicked.connect(self.copiar_archivos)
        self.btn_copiar.setObjectName(u"btn_copiar")
        self.btn_copiar.setFont(font1)
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

        self.horizontalLayout.addWidget(self.btn_copiar)

        self.btn_reiniciar = QPushButton(Dialog)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.btn_reiniciar.setObjectName(u"btn_reiniciar")
        self.btn_reiniciar.setFont(font1)
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

        self.horizontalLayout.addWidget(self.btn_reiniciar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Word Creator - iOS", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Introduce los datos requeridos para copiar los archivos a la </p><p align=\"justify\">nueva carpeta y crear el Word:</p></body></html>", None))
        self.lineEdit_bd.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca ruta base de datos (.sqlite)...", None))
        self.btn_db.setText(QCoreApplication.translate("Dialog", u"Seleccionar archivo", None))
        self.lineEdit_nuevaCarpeta.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca ruta de nueva carpeta...", None))
        self.btn_nuevaCarpeta.setText(QCoreApplication.translate("Dialog", u"Seleccionar carpeta", None))
        self.lineEdit_manifest.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca la ruta de Manifest.db...", None))
        self.btn_manifest.setText(QCoreApplication.translate("Dialog", u"Seleccionar archivo", None))
        self.lineEdit_multimedia.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca ruta archivos multimedia...", None))
        self.btn_multimedia.setText(QCoreApplication.translate("Dialog", u"Seleccionar carpeta", None))
        self.lineEdit_telefono.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca n\u00famero de tel\u00e9fono...", None))
        self.label_telefono.setText("")
        self.label_tiene_multimedia_2.setText(QCoreApplication.translate("Dialog", u"\u00bfYa tienes la carpeta con la multimedia?", None))
        self.btn_tiene_multimedia_2.setText(QCoreApplication.translate("Dialog", u"Pulsa aqu\u00ed", None))
        self.btn_copiar.setText(QCoreApplication.translate("Dialog", u"Copiar archivos", None))
        self.btn_reiniciar.setText(QCoreApplication.translate("Dialog", u"Reiniciar", None))
    # retranslateUi

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

    def reiniciar(self):
        self.lineEdit_bd.clear()
        self.lineEdit_manifest.clear()
        self.lineEdit_multimedia.clear()
        self.lineEdit_nuevaCarpeta.clear()
        self.lineEdit_telefono.clear()
        
    # Método para elegir la ruta del fichero .sqlite
    def select_file_sqlite(self):
        # Abrir el cuadro de diálogo para seleccionar un archivo
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar Archivo")
        if file_path:
            self.lineEdit_bd.setText(file_path)
            
    # Método para elegir la ruta del fichero Manifest.db
    def select_file_manifest(self):
        # Abrir el cuadro de diálogo para seleccionar un archivo
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar Archivo")
        if file_path:
            self.lineEdit_manifest.setText(file_path)
            
    # Método para elegir la ruta de la carpeta que se va a crear
    def select_folder_nuevaCarpeta(self):
        # Abrir el cuadro de diálogo para seleccionar la carpeta que contiene los archivos
        folder_dialog = QFileDialog(self)
        folder_path = folder_dialog.getExistingDirectory(self, "Seleccionar Carpeta")
        if folder_path:
            self.lineEdit_nuevaCarpeta.setText(folder_path)
            
    # Método para elegir la ruta de la carpeta con los directorios de los archivos a copiar
    def select_folder_multimedia(self):
        # Abrir el cuadro de diálogo para seleccionar la carpeta que contiene los directorios de los archivos
        folder_dialog = QFileDialog(self)
        folder_path = folder_dialog.getExistingDirectory(self, "Seleccionar Carpeta")
        if folder_path:
            self.lineEdit_multimedia.setText(folder_path)
            
    def copiar_archivos(self):
        base_datos_manifest = self.lineEdit_manifest.text()
        directorio_archivos = self.lineEdit_multimedia.text()
        ruta_nueva_carpeta = self.lineEdit_nuevaCarpeta.text()
        numero = self.lineEdit_telefono.text()
        
        self.crear_carpeta(ruta_nueva_carpeta, 'Media')
        QMessageBox.information(self, 'Carpeta creada', f'Se ha creado la carpeta Media en {ruta_nueva_carpeta}')
        # Obtener archivos del Manifest.db para el número de teléfono dado
        archivos_manifest = self.obtener_archivos_manifest(numero, base_datos_manifest)
        
        ruta_completa_csv = os.path.join(ruta_nueva_carpeta, f'archivos_{numero}.csv')
        if os.path.exists(ruta_completa_csv):
            respuesta = QMessageBox.question(self, 'CSV existente en directorio', 'Se ha encontrado un CSV en el directorio. ¿Desea borrarlo y crear uno nuevo?', QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.Yes:
                self.guardar_csv(archivos_manifest, ruta_completa_csv)
                QMessageBox.information(self, 'CSV nuevo creado', 'Se ha eliminado el antiguo CSV y se ha creado uno nuevo en el directorio.')
            else:
                QMessageBox.information(self, 'CSV nuevo no creado', 'No se ha creado un nuevo CSV. El antiguo CSV se ha mantenido en el directorio.')
        else:
            self.guardar_csv(archivos_manifest, ruta_completa_csv)
            QMessageBox.information(self, 'CSV nuevo creado', 'Se ha creado un nuevo CSV para la copia de archivos.')

        QMessageBox.information(self, "Copiando archivos", "Copiando archivos. Este proceso puede tardar un momento. Se avisará cuando este acabe. Por favor, presione Aceptar y espere...")

        # Leer el archivo CSV y copiar los archivos mencionados
        with open(f'{ruta_completa_csv}', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                fileID, relativePath = row
                
                # Encuentra el archivo correspondiente en el directorio de origen
                for root, dirs, files in os.walk(directorio_archivos):
                    for filename in files:
                        if filename == fileID:
                            sourceFile = os.path.join(root, filename)

                            # Verifica si el archivo existe antes de intentar copiarlo
                            if os.path.exists(sourceFile):
                                destFileName = os.path.basename(relativePath)

                                # Muestra información de depuración
                                print("Archivo a copiar:", sourceFile)
                                print("Destino:", os.path.join(f'{ruta_nueva_carpeta}/Media', destFileName))

                                # Copia el archivo al destino
                                try:
                                    shutil.copy(sourceFile, os.path.join(f'{ruta_nueva_carpeta}/Media', destFileName))
                                    print("Copia exitosa del archivo.")
                                except IOError as e:
                                    QMessageBox.critical(self, 'Error', f"ERROR:{e}")
                            else:
                                QMessageBox.information(self, 'Archivo no encontrado', "Archivo con fileID", fileID, "no encontrado. Saltando al siguiente.")

        respuesta = QMessageBox.information(self, "Proceso completado", f'Los archivos han sido copiados a {ruta_nueva_carpeta}.\n\n¿Desea continuar y crear el Word?', QMessageBox.Yes | QMessageBox.No) 

        if respuesta == QMessageBox.Yes:
            # Leer los valores de los QLineEdit
            base_datos_whatsapp = self.lineEdit_bd.text()
            numero = self.lineEdit_telefono.text()
            sistema = 'ios'

            # Escribir los valores en un archivo JSON
            datos = {'base_datos_whatsapp': base_datos_whatsapp, 'numero': numero, 'sistema': sistema}
            with open(f'{ruta_nueva_carpeta}/Media/datos.json', 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo)
            self.ventanaWord = Ventana_Word()
            self.ventanaWord.show()
            self.accept()
        else: 
            self.reiniciar()

    def crear_carpeta(self, ruta, nombre):
        nueva_ruta = os.path.join(ruta, nombre)
        try:
            os.mkdir(nueva_ruta)
            print(f"Carpeta '{nombre}' creada correctamente en '{ruta}'.")
            return nueva_ruta
        except OSError as error:
            QMessageBox.critical(self, 'Error', f"No se pudo crear la carpeta '{nombre}' en '{ruta}': {error}")
            return None

    def obtener_archivos_manifest(self, numero_telefono, ruta_manifest_db):
        conexion = sqlite3.connect(ruta_manifest_db)
        cursor = conexion.cursor()
        
        # Obtener la ruta absoluta del directorio actual
        dir_actual = os.path.dirname(os.path.abspath(__file__))

        # Construir la ruta absoluta al archivo consultas.json
        ruta_json_consultas = os.path.join(dir_actual, 'consultas.json')
        
        with open(ruta_json_consultas, 'r', encoding='utf-8') as archivo:
            consultas = json.load(archivo)
        consulta_sql = consultas['consulta_ios']
        
        cursor.execute(consulta_sql, (f'%{numero_telefono}%',))
        resultados = cursor.fetchall()
        conexion.close()
        return resultados

    def guardar_csv(self, archivos, ruta_completa):
        with open(ruta_completa, 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)  # Escribir encabezados
            escritor_csv.writerows(archivos)

    def tiene_multimedia(self):
        self.ventana_word = Ventana_Word()
        self.ventana_word.show()
        self.accept()

class Ventana_Word(Ui_Dialog_Word, QDialog):
    def __init__(self):
        super(Ventana_Word, self).__init__()
        self.setupUi(self)