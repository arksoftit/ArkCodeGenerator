# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainQTMflw.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
import resources_rc
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindow.resize(825, 613)
        MainWindow.setMinimumSize(QSize(825, 544))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(825, 544))
        self.centralwidget.setMaximumSize(QSize(1980, 1080))
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frm_principal = QFrame(self.centralwidget)
        self.frm_principal.setObjectName(u"frm_principal")
        self.frm_principal.setMaximumSize(QSize(1980, 1080))
        self.frm_principal.setStyleSheet(u"")
        self.frm_principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_principal.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frm_principal)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frm_principal)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 45))
        self.frame_superior.setMaximumSize(QSize(16777215, 45))
        self.frame_superior.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}\n"
"")
        self.frame_superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Shadow.Raised)
        self.hly_frame_superior = QHBoxLayout(self.frame_superior)
        self.hly_frame_superior.setSpacing(2)
        self.hly_frame_superior.setObjectName(u"hly_frame_superior")
        self.hly_frame_superior.setContentsMargins(2, 2, 2, 2)
        self.btn_menu = QPushButton(self.frame_superior)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(200, 35))
        self.btn_menu.setMaximumSize(QSize(200, 35))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        self.btn_menu.setFont(font)
        self.btn_menu.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/rec/assets/icons/fi-sr-rectangle-list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(28, 28))

        self.hly_frame_superior.addWidget(self.btn_menu)

        self.horizontalSpacer = QSpacerItem(439, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hly_frame_superior.addItem(self.horizontalSpacer)

        self.btn_minimizar = QPushButton(self.frame_superior)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        self.btn_minimizar.setMinimumSize(QSize(35, 35))
        self.btn_minimizar.setMaximumSize(QSize(35, 35))
        self.btn_minimizar.setFont(font)
        self.btn_minimizar.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/rec/assets/icons/fi-sr-arrow-down-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_minimizar.setIcon(icon1)
        self.btn_minimizar.setIconSize(QSize(24, 24))

        self.hly_frame_superior.addWidget(self.btn_minimizar)

        self.btn_restaurar = QPushButton(self.frame_superior)
        self.btn_restaurar.setObjectName(u"btn_restaurar")
        self.btn_restaurar.setMinimumSize(QSize(35, 35))
        self.btn_restaurar.setMaximumSize(QSize(35, 35))
        self.btn_restaurar.setFont(font)
        self.btn_restaurar.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/rec/assets/icons/fi-sr-expand.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_restaurar.setIcon(icon2)
        self.btn_restaurar.setIconSize(QSize(24, 24))

        self.hly_frame_superior.addWidget(self.btn_restaurar)

        self.btn_maximizar = QPushButton(self.frame_superior)
        self.btn_maximizar.setObjectName(u"btn_maximizar")
        self.btn_maximizar.setMinimumSize(QSize(35, 35))
        self.btn_maximizar.setMaximumSize(QSize(35, 35))
        self.btn_maximizar.setFont(font)
        self.btn_maximizar.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/rec/assets/icons/fi-sr-expand-arrows.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_maximizar.setIcon(icon3)
        self.btn_maximizar.setIconSize(QSize(24, 24))

        self.hly_frame_superior.addWidget(self.btn_maximizar)

        self.btn_cerrar = QPushButton(self.frame_superior)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setMinimumSize(QSize(35, 35))
        self.btn_cerrar.setMaximumSize(QSize(35, 35))
        self.btn_cerrar.setFont(font)
        self.btn_cerrar.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/rec/assets/icons/fi-sr-cross-small.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QSize(35, 35))

        self.hly_frame_superior.addWidget(self.btn_cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.frm_principal)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setMinimumSize(QSize(825, 544))
        self.frame_inferior.setMaximumSize(QSize(1980, 1080))
        self.frame_inferior.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"   \n"
"}\n"
"")
        self.frame_inferior.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_inferior)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setEnabled(True)
        self.frame_menu.setMinimumSize(QSize(0, 0))
        self.frame_menu.setMaximumSize(QSize(200, 16777215))
        self.frame_menu.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}")
        self.frame_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frame_menu = QVBoxLayout(self.frame_menu)
        self.vly_frame_menu.setObjectName(u"vly_frame_menu")
        self.btn_info_hardware = QPushButton(self.frame_menu)
        self.btn_info_hardware.setObjectName(u"btn_info_hardware")
        self.btn_info_hardware.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color:qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/rec/assets/icons/PC01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_hardware.setIcon(icon5)
        self.btn_info_hardware.setIconSize(QSize(35, 35))

        self.vly_frame_menu.addWidget(self.btn_info_hardware)

        self.btn_info_red = QPushButton(self.frame_menu)
        self.btn_info_red.setObjectName(u"btn_info_red")
        self.btn_info_red.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/rec/assets/icons/Red01.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_red.setIcon(icon6)
        self.btn_info_red.setIconSize(QSize(35, 35))

        self.vly_frame_menu.addWidget(self.btn_info_red)

        self.btn_info_so = QPushButton(self.frame_menu)
        self.btn_info_so.setObjectName(u"btn_info_so")
        self.btn_info_so.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/rec/assets/icons/fi-sr-computer-classic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_so.setIcon(icon7)
        self.btn_info_so.setIconSize(QSize(35, 36))

        self.vly_frame_menu.addWidget(self.btn_info_so)

        self.btn_info_regional = QPushButton(self.frame_menu)
        self.btn_info_regional.setObjectName(u"btn_info_regional")
        self.btn_info_regional.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/rec/assets/icons/Regional01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info_regional.setIcon(icon8)
        self.btn_info_regional.setIconSize(QSize(35, 35))

        self.vly_frame_menu.addWidget(self.btn_info_regional)

        self.btn_limpiar = QPushButton(self.frame_menu)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/rec/assets/icons/Clear01.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_limpiar.setIcon(icon9)
        self.btn_limpiar.setIconSize(QSize(35, 35))

        self.vly_frame_menu.addWidget(self.btn_limpiar)

        self.vspacer_menu = QSpacerItem(20, 106, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vly_frame_menu.addItem(self.vspacer_menu)

        self.btn_operations = QPushButton(self.frame_menu)
        self.btn_operations.setObjectName(u"btn_operations")
        self.btn_operations.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/rec/assets/icons/filesettings_102180.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_operations.setIcon(icon10)
        self.btn_operations.setIconSize(QSize(28, 29))

        self.vly_frame_menu.addWidget(self.btn_operations)

        self.btn_config = QPushButton(self.frame_menu)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color:qlineargradient(\n"
"    spread:pad, \n"
"    x1:0, \n"
"    y1:0, \n"
"    x2:1, \n"
"    y2:0, \n"
"    stop:0 rgba(102, 178, 255, 255), \n"
"    stop:0.55 rgba(61, 148, 235, 255), \n"
"    stop:0.98 rgba(0, 0, 0, 255), \n"
"    stop:1 rgba(0, 0, 0, 0)\n"
");\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/rec/assets/icons/fi-sr-settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_config.setIcon(icon11)
        self.btn_config.setIconSize(QSize(35, 35))

        self.vly_frame_menu.addWidget(self.btn_config)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_consolas = QFrame(self.frame_inferior)
        self.frame_consolas.setObjectName(u"frame_consolas")
        self.frame_consolas.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_consolas.sizePolicy().hasHeightForWidth())
        self.frame_consolas.setSizePolicy(sizePolicy)
        self.frame_consolas.setMinimumSize(QSize(825, 544))
        self.frame_consolas.setMaximumSize(QSize(1920, 1080))
        self.frame_consolas.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"   \n"
"}")
        self.frame_consolas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_consolas.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frame_consolas = QVBoxLayout(self.frame_consolas)
        self.vly_frame_consolas.setSpacing(0)
        self.vly_frame_consolas.setObjectName(u"vly_frame_consolas")
        self.vly_frame_consolas.setContentsMargins(0, 0, 0, 0)
        self.sw_consolas = QStackedWidget(self.frame_consolas)
        self.sw_consolas.setObjectName(u"sw_consolas")
        self.sw_consolas.setEnabled(True)
        sizePolicy.setHeightForWidth(self.sw_consolas.sizePolicy().hasHeightForWidth())
        self.sw_consolas.setSizePolicy(sizePolicy)
        self.sw_consolas.setMinimumSize(QSize(825, 544))
        self.sw_consolas.setMaximumSize(QSize(1920, 1080))
        self.sw_consolas.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.sw_consolas.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.page_inicio.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.vly_page_inicio = QVBoxLayout(self.page_inicio)
        self.vly_page_inicio.setSpacing(0)
        self.vly_page_inicio.setObjectName(u"vly_page_inicio")
        self.vly_page_inicio.setContentsMargins(0, 0, 0, 0)
        self.frame_inicio_head = QFrame(self.page_inicio)
        self.frame_inicio_head.setObjectName(u"frame_inicio_head")
        self.frame_inicio_head.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_inicio_head.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frame_inicio_head = QVBoxLayout(self.frame_inicio_head)
        self.vly_frame_inicio_head.setObjectName(u"vly_frame_inicio_head")
        self.title_arktoolspc = QLabel(self.frame_inicio_head)
        self.title_arktoolspc.setObjectName(u"title_arktoolspc")
        self.title_arktoolspc.setEnabled(True)
        self.title_arktoolspc.setMinimumSize(QSize(40, 60))
        self.title_arktoolspc.setMaximumSize(QSize(1980, 40))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.title_arktoolspc.setFont(font1)
        self.title_arktoolspc.setStyleSheet(u"")
        self.title_arktoolspc.setFrameShadow(QFrame.Shadow.Sunken)
        self.title_arktoolspc.setTextFormat(Qt.TextFormat.PlainText)
        self.title_arktoolspc.setPixmap(QPixmap(u":/rec/assets/images/ArlToolsPC2.png"))
        self.title_arktoolspc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vly_frame_inicio_head.addWidget(self.title_arktoolspc)

        self.verticalSpacer_2 = QSpacerItem(20, 94, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vly_frame_inicio_head.addItem(self.verticalSpacer_2)


        self.vly_page_inicio.addWidget(self.frame_inicio_head)

        self.frame_inicio_middle = QFrame(self.page_inicio)
        self.frame_inicio_middle.setObjectName(u"frame_inicio_middle")
        self.frame_inicio_middle.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_inicio_middle.setFrameShadow(QFrame.Shadow.Plain)
        self.hly_frame_inicio_middle = QHBoxLayout(self.frame_inicio_middle)
        self.hly_frame_inicio_middle.setSpacing(1)
        self.hly_frame_inicio_middle.setObjectName(u"hly_frame_inicio_middle")
        self.hly_frame_inicio_middle.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hly_frame_inicio_middle.addItem(self.horizontalSpacer_2)

        self.label_logo_tools = QLabel(self.frame_inicio_middle)
        self.label_logo_tools.setObjectName(u"label_logo_tools")
        self.label_logo_tools.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_logo_tools.sizePolicy().hasHeightForWidth())
        self.label_logo_tools.setSizePolicy(sizePolicy1)
        self.label_logo_tools.setMinimumSize(QSize(164, 164))
        self.label_logo_tools.setMaximumSize(QSize(200, 200))
        self.label_logo_tools.setAutoFillBackground(False)
        self.label_logo_tools.setStyleSheet(u"")
        self.label_logo_tools.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_logo_tools.setPixmap(QPixmap(u":/rec/assets/images/ArkToolsPC_02.png"))
        self.label_logo_tools.setScaledContents(True)
        self.label_logo_tools.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hly_frame_inicio_middle.addWidget(self.label_logo_tools)

        self.horizontalSpacer_3 = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hly_frame_inicio_middle.addItem(self.horizontalSpacer_3)


        self.vly_page_inicio.addWidget(self.frame_inicio_middle)

        self.frame_inicio_pie = QFrame(self.page_inicio)
        self.frame_inicio_pie.setObjectName(u"frame_inicio_pie")
        self.frame_inicio_pie.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_inicio_pie.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frame_inicio_pie = QVBoxLayout(self.frame_inicio_pie)
        self.vly_frame_inicio_pie.setSpacing(6)
        self.vly_frame_inicio_pie.setObjectName(u"vly_frame_inicio_pie")
        self.vly_frame_inicio_pie.setContentsMargins(0, 0, 0, 9)
        self.verticalSpacer = QSpacerItem(20, 123, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vly_frame_inicio_pie.addItem(self.verticalSpacer)

        self.pie_arkinfo = QLabel(self.frame_inicio_pie)
        self.pie_arkinfo.setObjectName(u"pie_arkinfo")
        self.pie_arkinfo.setMinimumSize(QSize(40, 40))
        self.pie_arkinfo.setMaximumSize(QSize(16777215, 40))
        self.pie_arkinfo.setFont(font1)
        self.pie_arkinfo.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")
        self.pie_arkinfo.setFrameShadow(QFrame.Shadow.Sunken)
        self.pie_arkinfo.setTextFormat(Qt.TextFormat.PlainText)
        self.pie_arkinfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vly_frame_inicio_pie.addWidget(self.pie_arkinfo)

        self.vly_frame_inicio_pie.setStretch(0, 1)
        self.vly_frame_inicio_pie.setStretch(1, 1)

        self.vly_page_inicio.addWidget(self.frame_inicio_pie)

        self.vly_page_inicio.setStretch(0, 1)
        self.vly_page_inicio.setStretch(1, 1)
        self.vly_page_inicio.setStretch(2, 1)
        self.sw_consolas.addWidget(self.page_inicio)
        self.page_inf_hardware = QWidget()
        self.page_inf_hardware.setObjectName(u"page_inf_hardware")
        self.page_inf_hardware.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.vly_page_inf_hardware = QVBoxLayout(self.page_inf_hardware)
        self.vly_page_inf_hardware.setObjectName(u"vly_page_inf_hardware")
        self.textEdit_info_hw = QTextEdit(self.page_inf_hardware)
        self.textEdit_info_hw.setObjectName(u"textEdit_info_hw")
        self.textEdit_info_hw.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")

        self.vly_page_inf_hardware.addWidget(self.textEdit_info_hw)

        self.label_info_hw = QLabel(self.page_inf_hardware)
        self.label_info_hw.setObjectName(u"label_info_hw")
        self.label_info_hw.setMinimumSize(QSize(80, 80))
        self.label_info_hw.setMaximumSize(QSize(80, 80))
        self.label_info_hw.setPixmap(QPixmap(u":/rec/assets/icons/sys01.svg"))
        self.label_info_hw.setScaledContents(True)

        self.vly_page_inf_hardware.addWidget(self.label_info_hw)

        self.sw_consolas.addWidget(self.page_inf_hardware)
        self.page_inf_config = QWidget()
        self.page_inf_config.setObjectName(u"page_inf_config")
        self.page_inf_config.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.vly_page_inf_config = QVBoxLayout(self.page_inf_config)
        self.vly_page_inf_config.setObjectName(u"vly_page_inf_config")
        self.frame_config = QFrame(self.page_inf_config)
        self.frame_config.setObjectName(u"frame_config")
        self.frame_config.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_config.setFrameShadow(QFrame.Shadow.Raised)
        self.hly_frame_config = QHBoxLayout(self.frame_config)
        self.hly_frame_config.setSpacing(0)
        self.hly_frame_config.setObjectName(u"hly_frame_config")
        self.hly_frame_config.setContentsMargins(0, 0, 0, 0)
        self.frame_btns_config = QFrame(self.frame_config)
        self.frame_btns_config.setObjectName(u"frame_btns_config")
        self.frame_btns_config.setMinimumSize(QSize(200, 0))
        self.frame_btns_config.setMaximumSize(QSize(200, 16777215))
        self.frame_btns_config.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: rgb(85, 170, 255);\n"
"   \n"
"}")
        self.frame_btns_config.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_btns_config.setFrameShadow(QFrame.Shadow.Raised)
        self.vly_frame_btns_config = QVBoxLayout(self.frame_btns_config)
        self.vly_frame_btns_config.setObjectName(u"vly_frame_btns_config")
        self.btn_cambio_regional = QPushButton(self.frame_btns_config)
        self.btn_cambio_regional.setObjectName(u"btn_cambio_regional")
        self.btn_cambio_regional.setMinimumSize(QSize(170, 90))
        self.btn_cambio_regional.setMaximumSize(QSize(170, 90))
        font2 = QFont()
        font2.setBold(True)
        self.btn_cambio_regional.setFont(font2)
        self.btn_cambio_regional.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px; /* Un padding uniforme puede ayudar a centrarlo */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center; /* Justifica el texto al centro */\n"
"}\n"
"\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.btn_cambio_regional.setIcon(icon8)
        self.btn_cambio_regional.setIconSize(QSize(35, 35))

        self.vly_frame_btns_config.addWidget(self.btn_cambio_regional)

        self.btn_config_sql_tools = QPushButton(self.frame_btns_config)
        self.btn_config_sql_tools.setObjectName(u"btn_config_sql_tools")
        self.btn_config_sql_tools.setMinimumSize(QSize(170, 90))
        self.btn_config_sql_tools.setMaximumSize(QSize(170, 90))
        self.btn_config_sql_tools.setFont(font2)
        self.btn_config_sql_tools.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px; /* Un padding uniforme puede ayudar a centrarlo */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center; /* Justifica el texto al centro */\n"
"}\n"
"\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/rec/assets/icons/fi-sr-sql-server.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_config_sql_tools.setIcon(icon12)
        self.btn_config_sql_tools.setIconSize(QSize(35, 35))

        self.vly_frame_btns_config.addWidget(self.btn_config_sql_tools)

        self.btn_config_tools = QPushButton(self.frame_btns_config)
        self.btn_config_tools.setObjectName(u"btn_config_tools")
        self.btn_config_tools.setMinimumSize(QSize(170, 90))
        self.btn_config_tools.setMaximumSize(QSize(170, 90))
        self.btn_config_tools.setStyleSheet(u"/* Estilo base del bot\u00f3n */\n"
"QPushButton {\n"
"    background-color: #007BFF;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"/* Estilo cuando el mouse pasa por encima */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"/* Estilo cuando el bot\u00f3n es presionado */\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}\n"
"")
        self.btn_config_tools.setIcon(icon10)
        self.btn_config_tools.setIconSize(QSize(35, 35))

        self.vly_frame_btns_config.addWidget(self.btn_config_tools)


        self.hly_frame_config.addWidget(self.frame_btns_config)

        self.textEdit_info_config = QTextEdit(self.frame_config)
        self.textEdit_info_config.setObjectName(u"textEdit_info_config")
        self.textEdit_info_config.setEnabled(False)
        self.textEdit_info_config.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.textEdit_info_config.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: rgb(170, 170, 127);")

        self.hly_frame_config.addWidget(self.textEdit_info_config)


        self.vly_page_inf_config.addWidget(self.frame_config)

        self.frame_pie_config = QFrame(self.page_inf_config)
        self.frame_pie_config.setObjectName(u"frame_pie_config")
        self.frame_pie_config.setMinimumSize(QSize(0, 85))
        self.frame_pie_config.setMaximumSize(QSize(16777215, 85))
        self.frame_pie_config.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pie_config.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_pie_config)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_info_config = QLabel(self.frame_pie_config)
        self.label_info_config.setObjectName(u"label_info_config")
        self.label_info_config.setMinimumSize(QSize(40, 40))
        self.label_info_config.setMaximumSize(QSize(80, 80))
        self.label_info_config.setPixmap(QPixmap(u":/rec/assets/icons/confi01.svg"))
        self.label_info_config.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.label_info_config)


        self.vly_page_inf_config.addWidget(self.frame_pie_config)

        self.sw_consolas.addWidget(self.page_inf_config)
        self.page_forms = QWidget()
        self.page_forms.setObjectName(u"page_forms")
        sizePolicy.setHeightForWidth(self.page_forms.sizePolicy().hasHeightForWidth())
        self.page_forms.setSizePolicy(sizePolicy)
        self.page_forms.setMinimumSize(QSize(825, 544))
        self.page_forms.setMaximumSize(QSize(1920, 1080))
        self.page_forms.setStyleSheet(u"")
        self.hly_page_forms = QHBoxLayout(self.page_forms)
        self.hly_page_forms.setSpacing(4)
        self.hly_page_forms.setObjectName(u"hly_page_forms")
        self.hly_page_forms.setContentsMargins(0, 0, 0, 0)
        self.sw_consolas.addWidget(self.page_forms)
        self.page_inf_red = QWidget()
        self.page_inf_red.setObjectName(u"page_inf_red")
        self.page_inf_red.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.vly_page_inf_red = QVBoxLayout(self.page_inf_red)
        self.vly_page_inf_red.setObjectName(u"vly_page_inf_red")
        self.textEdit_info_red = QTextEdit(self.page_inf_red)
        self.textEdit_info_red.setObjectName(u"textEdit_info_red")
        self.textEdit_info_red.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")

        self.vly_page_inf_red.addWidget(self.textEdit_info_red)

        self.label_info_red = QLabel(self.page_inf_red)
        self.label_info_red.setObjectName(u"label_info_red")
        self.label_info_red.setMinimumSize(QSize(40, 40))
        self.label_info_red.setMaximumSize(QSize(80, 80))
        self.label_info_red.setPixmap(QPixmap(u":/rec/assets/icons/Red01.png"))
        self.label_info_red.setScaledContents(True)
        self.label_info_red.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vly_page_inf_red.addWidget(self.label_info_red)

        self.sw_consolas.addWidget(self.page_inf_red)
        self.page_inf_so = QWidget()
        self.page_inf_so.setObjectName(u"page_inf_so")
        self.page_inf_so.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.vly_page_inf_so = QVBoxLayout(self.page_inf_so)
        self.vly_page_inf_so.setObjectName(u"vly_page_inf_so")
        self.textEdit_info_so = QTextEdit(self.page_inf_so)
        self.textEdit_info_so.setObjectName(u"textEdit_info_so")
        self.textEdit_info_so.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")

        self.vly_page_inf_so.addWidget(self.textEdit_info_so)

        self.label_info_so = QLabel(self.page_inf_so)
        self.label_info_so.setObjectName(u"label_info_so")
        self.label_info_so.setMinimumSize(QSize(40, 40))
        self.label_info_so.setMaximumSize(QSize(80, 80))
        self.label_info_so.setPixmap(QPixmap(u":/rec/assets/icons/OS02.svg"))
        self.label_info_so.setScaledContents(True)
        self.label_info_so.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vly_page_inf_so.addWidget(self.label_info_so)

        self.sw_consolas.addWidget(self.page_inf_so)
        self.page_inf_regional = QWidget()
        self.page_inf_regional.setObjectName(u"page_inf_regional")
        self.page_inf_regional.setStyleSheet(u"/* Estilo del marco */\n"
"QFrame {\n"
"    background-color: #F8F9FA;\n"
"    }\n"
"")
        self.vly_page_inf_regional = QVBoxLayout(self.page_inf_regional)
        self.vly_page_inf_regional.setObjectName(u"vly_page_inf_regional")
        self.textEdit_info_regional = QTextEdit(self.page_inf_regional)
        self.textEdit_info_regional.setObjectName(u"textEdit_info_regional")
        self.textEdit_info_regional.setStyleSheet(u"font: 9pt \"Consolas\";\n"
"color: #000000; \n"
"background-color: #f0f0f0;")

        self.vly_page_inf_regional.addWidget(self.textEdit_info_regional)

        self.label_info_regional = QLabel(self.page_inf_regional)
        self.label_info_regional.setObjectName(u"label_info_regional")
        self.label_info_regional.setMinimumSize(QSize(80, 80))
        self.label_info_regional.setMaximumSize(QSize(80, 80))
        self.label_info_regional.setPixmap(QPixmap(u":/rec/assets/icons/filesettings_102180.svg"))
        self.label_info_regional.setScaledContents(True)
        self.label_info_regional.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vly_page_inf_regional.addWidget(self.label_info_regional)

        self.sw_consolas.addWidget(self.page_inf_regional)

        self.vly_frame_consolas.addWidget(self.sw_consolas)


        self.horizontalLayout.addWidget(self.frame_consolas)


        self.verticalLayout_2.addWidget(self.frame_inferior)


        self.horizontalLayout_2.addWidget(self.frm_principal)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimizar, self.btn_restaurar)
        QWidget.setTabOrder(self.btn_restaurar, self.btn_maximizar)
        QWidget.setTabOrder(self.btn_maximizar, self.btn_cerrar)
        QWidget.setTabOrder(self.btn_cerrar, self.btn_info_hardware)
        QWidget.setTabOrder(self.btn_info_hardware, self.btn_info_red)
        QWidget.setTabOrder(self.btn_info_red, self.btn_info_so)
        QWidget.setTabOrder(self.btn_info_so, self.btn_info_regional)
        QWidget.setTabOrder(self.btn_info_regional, self.btn_limpiar)
        QWidget.setTabOrder(self.btn_limpiar, self.btn_menu)
        QWidget.setTabOrder(self.btn_menu, self.btn_operations)
        QWidget.setTabOrder(self.btn_operations, self.btn_config)
        QWidget.setTabOrder(self.btn_config, self.textEdit_info_hw)
        QWidget.setTabOrder(self.textEdit_info_hw, self.btn_cambio_regional)
        QWidget.setTabOrder(self.btn_cambio_regional, self.btn_config_sql_tools)
        QWidget.setTabOrder(self.btn_config_sql_tools, self.btn_config_tools)
        QWidget.setTabOrder(self.btn_config_tools, self.textEdit_info_config)
        QWidget.setTabOrder(self.textEdit_info_config, self.textEdit_info_red)
        QWidget.setTabOrder(self.textEdit_info_red, self.textEdit_info_so)
        QWidget.setTabOrder(self.textEdit_info_so, self.textEdit_info_regional)

        self.retranslateUi(MainWindow)

        self.sw_consolas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"     Men\u00fa", None))
        self.btn_minimizar.setText("")
        self.btn_restaurar.setText("")
        self.btn_maximizar.setText("")
        self.btn_cerrar.setText("")
        self.btn_info_hardware.setText(QCoreApplication.translate("MainWindow", u"      Hardware", None))
        self.btn_info_red.setText(QCoreApplication.translate("MainWindow", u"      Red", None))
        self.btn_info_so.setText(QCoreApplication.translate("MainWindow", u"      Sistema", None))
        self.btn_info_regional.setText(QCoreApplication.translate("MainWindow", u"      Regional", None))
#if QT_CONFIG(shortcut)
        self.btn_info_regional.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_limpiar.setText(QCoreApplication.translate("MainWindow", u"      Limpiar", None))
        self.btn_operations.setText(QCoreApplication.translate("MainWindow", u"  Operaciones", None))
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"  Configuraci\u00f3n", None))
        self.title_arktoolspc.setText("")
#if QT_CONFIG(accessibility)
        self.label_logo_tools.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_logo_tools.setText("")
        self.label_info_hw.setText("")
        self.btn_cambio_regional.setText(QCoreApplication.translate("MainWindow", u"  Cambiar \n"
"  Configuraci\u00f3n \n"
"  Regional", None))
        self.btn_config_sql_tools.setText(QCoreApplication.translate("MainWindow", u"  Consultar\n"
"  Conexi\u00f3n\n"
"  SQLite", None))
        self.btn_config_tools.setText(QCoreApplication.translate("MainWindow", u"  Consultar\n"
"  Configuraci\u00f3n\n"
"  Actual", None))
        self.label_info_config.setText("")
        self.label_info_red.setText("")
        self.label_info_so.setText("")
        self.label_info_regional.setText("")
    # retranslateUi

