# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'creaWord.ui'
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
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget, QFileDialog, QMessageBox)
import os
import subprocess
import requests
import json

class Ui_Dialog_Word(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(452, 204)
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
        self.lineEdit_copiados = QLineEdit(Dialog)
        self.lineEdit_copiados.setObjectName(u"lineEdit_copiados")
        self.lineEdit_copiados.setMaximumSize(QSize(231, 16777215))
        self.lineEdit_copiados.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")
        self.lineEdit_copiados.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_copiados)

        self.btn_copiados = QPushButton(Dialog)
        self.btn_copiados.clicked.connect(self.select_folder_archivosCopiados)
        self.btn_copiados.setObjectName(u"btn_copiados")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_copiados.setFont(font1)
        self.btn_copiados.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_copiados.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_3.addWidget(self.btn_copiados)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_php = QLineEdit(Dialog)
        self.lineEdit_php.setObjectName(u"lineEdit_php")
        self.lineEdit_php.setMaximumSize(QSize(231, 16777215))
        self.lineEdit_php.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")
        self.lineEdit_php.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_php)

        self.btn_php = QPushButton(Dialog)
        self.btn_php.clicked.connect(self.select_file_php)
        self.btn_php.setObjectName(u"btn_php")
        self.btn_php.setFont(font1)
        self.btn_php.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_php.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_4.addWidget(self.btn_php)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_word = QLineEdit(Dialog)
        self.lineEdit_word.setObjectName(u"lineEdit_word")
        self.lineEdit_word.setMaximumSize(QSize(231, 16777215))
        self.lineEdit_word.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"border-bottom: 1px solid black;\n"
"background-color: transparent;\n"
"}")
        self.lineEdit_word.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_word)

        self.btn_word = QPushButton(Dialog)
        self.btn_word.clicked.connect(self.select_folder_guardarWord)
        self.btn_word.setObjectName(u"btn_word")
        self.btn_word.setFont(font1)
        self.btn_word.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_word.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_5.addWidget(self.btn_word)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_confirma_multimedia = QLabel(Dialog)
        self.label_confirma_multimedia.setObjectName(u"label_confirma_multimedia")

        self.horizontalLayout_6.addWidget(self.label_confirma_multimedia)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.checkBox_confirma_multimedia = QCheckBox(Dialog)
        self.checkBox_confirma_multimedia.setObjectName(u"checkBox_confirma_multimedia")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_confirma_multimedia.sizePolicy().hasHeightForWidth())
        self.checkBox_confirma_multimedia.setSizePolicy(sizePolicy1)
        self.checkBox_confirma_multimedia.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox_confirma_multimedia.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.checkBox_confirma_multimedia)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_creaWord = QPushButton(Dialog)
        self.btn_creaWord.clicked.connect(self.crear_word)
        self.btn_creaWord.setObjectName(u"btn_creaWord")
        self.btn_creaWord.setFont(font1)
        self.btn_creaWord.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_creaWord.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.btn_creaWord)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Creaci\u00f3n del Word - Word Creator", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Introduce los datos requeridos para crear el Word:</p></body></html>", None))
        self.lineEdit_copiados.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca carpeta de archivo copiados...", None))
        self.btn_copiados.setText(QCoreApplication.translate("Dialog", u"Seleccionar carpeta", None))
        self.lineEdit_php.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca archivo PHP para crear tabla...", None))
        self.btn_php.setText(QCoreApplication.translate("Dialog", u"Seleccionar archivo", None))
        self.lineEdit_word.setPlaceholderText(QCoreApplication.translate("Dialog", u"Introduzca la ruta para guardar el Word...", None))
        self.btn_word.setText(QCoreApplication.translate("Dialog", u"Seleccionar archivo", None))
        self.label_confirma_multimedia.setText(QCoreApplication.translate("Dialog", u"\u00bfDesea incluir multimedia en el archivo Word?", None))
        self.checkBox_confirma_multimedia.setText(QCoreApplication.translate("Dialog", u"Si, a\u00f1adir multimedia", None))
        self.btn_creaWord.setText(QCoreApplication.translate("Dialog", u"Crear Word", None))
        self.btn_reiniciar.setText(QCoreApplication.translate("Dialog", u"Reiniciar", None))
    # retranslateUi

    # Método para elegir la ruta del fichero PHP
    def select_file_php(self):
        # Abrir el cuadro de diálogo para seleccionar un archivo
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar Archivo")
        if file_path:
            self.lineEdit_php.setText(file_path)
            
    # Método para elegir la ruta de la carpeta con los archivos copiados
    def select_folder_archivosCopiados(self):
        # Abrir el cuadro de diálogo para seleccionar la carpeta que contiene los archivos
        folder_dialog = QFileDialog(self)
        folder_path = folder_dialog.getExistingDirectory(self, "Seleccionar Carpeta")
        if folder_path:
            self.lineEdit_copiados.setText(folder_path)
            
    # Método para elegir la ruta de la carpeta donde se quiere guardar el Word
    def select_folder_guardarWord(self):
        # Abrir el cuadro de diálogo para seleccionar la carpeta que contiene los archivos
        folder_dialog = QFileDialog(self)
        folder_path = folder_dialog.getExistingDirectory(self, "Seleccionar Carpeta")
        if folder_path:
            self.lineEdit_word.setText(folder_path)
            
    def reiniciar(self):
        self.lineEdit_copiados.clear()
        self.lineEdit_php.clear()
        self.lineEdit_word.clear()
        self.checkBox_confirma_multimedia.setChecked(False)
        
    def crear_word(self):
        # Leer los valores del archivo JSON
        ruta_json = f'{self.lineEdit_copiados.text()}/datos.json'
        with open(f'{ruta_json}', 'r') as archivo:
            datos = json.load(archivo)

        # Usar los valores según sea necesario
        base_datos_whatsapp = datos['base_datos_whatsapp']
        numero = datos['numero']
        sistema = datos['sistema']
        
        # Definir la URL del servidor PHP 
        media_folder = self.lineEdit_copiados.text() + '/'
        archivo_php = self.lineEdit_php.text()
        puerto = 8000    
        url_php = f'http://localhost:{puerto}/{os.path.basename(archivo_php)}'
        directorio_php = os.path.dirname(archivo_php)
        ruta_word = self.lineEdit_word.text()
        nombre_word = f'mensajes_{numero}.doc'
        archivo_word = ruta_word + '/' + nombre_word 
        print(archivo_word)
        incluirMultimedia = self.checkBox_confirma_multimedia.isChecked()
        if incluirMultimedia == True:
            multimedia = 'si'
        else:
            multimedia = 'no'
        # Cambiar al directorio que contiene el archivo PHP
        os.chdir(directorio_php)

        # Ejecutar el servidor PHP integrado en un proceso secundario
        servidor_php = subprocess.Popen(['php', '-S', f'localhost:{puerto}'])

        # Realizar una solicitud HTTP al servidor local para obtener la salida del archivo PHP
        respuesta = requests.get(url_php, params={'media_folder': media_folder, 'database': base_datos_whatsapp, 
                                                'numero': numero, 'multimedia': multimedia, 'sistema': sistema})

        # Guardar la respuesta en un archivo Word
        if os.path.exists(archivo_word):
            reply = QMessageBox.question(self, 'Archivo Word existente', f'Ya existe el archivo {nombre_word} en la ruta {ruta_word}\n\n¿Desea eliminar este archivo y crear uno nuevo?', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                os.remove(archivo_word)
                with open(archivo_word, 'wb') as f: 
                    f.write(respuesta.content)

                # Terminar el servidor PHP integrado
                servidor_php.terminate()

                QMessageBox.information(self, 'Word creado', f'Archivo Word guardado como {archivo_word}.')  
                self.reiniciar()
                os.system(f'start {archivo_word}')
                self.close()
            elif reply == QMessageBox.No:
                QMessageBox.critical(self, 'Error', f'No se ha podido completar el proceso porque ya existe el archivo {nombre_word} en la ruta {ruta_word}. Por favor elimínelo y pruebe de nuevo.')
        else: 
            with open(archivo_word, 'wb') as f: 
                f.write(respuesta.content)

            # Terminar el servidor PHP integrado
            servidor_php.terminate()

            QMessageBox.information(self, 'Word creado', f'Archivo Word guardado como {archivo_word}.')  
            self.reiniciar()
            os.system(f'start {archivo_word}')
            self.close()
        