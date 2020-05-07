# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alice/Desktop/SporProje/AnaSayfa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1025, 717)
        MainWindow.setStyleSheet(".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 731, 331))
        self.groupBox.setObjectName("groupBox")
        self.cwDTarihi = QtWidgets.QCalendarWidget(self.groupBox)
        self.cwDTarihi.setGeometry(QtCore.QRect(310, 40, 321, 201))
        self.cwDTarihi.setGridVisible(True)
        self.cwDTarihi.setObjectName("cwDTarihi")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(310, 20, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 41, 16))
        self.label_8.setObjectName("label_8")
        self.lwBrans = QtWidgets.QListWidget(self.groupBox)
        self.lwBrans.setGeometry(QtCore.QRect(50, 220, 241, 111))
        self.lwBrans.setObjectName("lwBrans")
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 281, 198))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lneTCK = QtWidgets.QLineEdit(self.layoutWidget)
        self.lneTCK.setMaxLength(11)
        self.lneTCK.setObjectName("lneTCK")
        self.horizontalLayout.addWidget(self.lneTCK)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lneSporcuAdi = QtWidgets.QLineEdit(self.layoutWidget)
        self.lneSporcuAdi.setObjectName("lneSporcuAdi")
        self.horizontalLayout_2.addWidget(self.lneSporcuAdi)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lneSporcuSoyadi = QtWidgets.QLineEdit(self.layoutWidget)
        self.lneSporcuSoyadi.setObjectName("lneSporcuSoyadi")
        self.horizontalLayout_3.addWidget(self.lneSporcuSoyadi)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.cmbSporKulubu = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbSporKulubu.setObjectName("cmbSporKulubu")
        self.cmbSporKulubu.addItem("")
        self.cmbSporKulubu.addItem("")
        self.cmbSporKulubu.addItem("")
        self.cmbSporKulubu.addItem("")
        self.cmbSporKulubu.addItem("")
        self.cmbSporKulubu.addItem("")
        self.horizontalLayout_4.addWidget(self.cmbSporKulubu)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.spnKilo = QtWidgets.QSpinBox(self.layoutWidget)
        self.spnKilo.setMinimum(50)
        self.spnKilo.setMaximum(130)
        self.spnKilo.setObjectName("spnKilo")
        self.horizontalLayout_5.addWidget(self.spnKilo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.cmbCinsiyet = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbCinsiyet.setObjectName("cmbCinsiyet")
        self.cmbCinsiyet.addItem("")
        self.cmbCinsiyet.addItem("")
        self.horizontalLayout_6.addWidget(self.cmbCinsiyet)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.chkMedeniHal = QtWidgets.QCheckBox(self.layoutWidget)
        self.chkMedeniHal.setObjectName("chkMedeniHal")
        self.horizontalLayout_7.addWidget(self.chkMedeniHal)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.tblwSporcuBilgi = QtWidgets.QTableWidget(self.centralwidget)
        self.tblwSporcuBilgi.setGeometry(QtCore.QRect(10, 360, 961, 281))
        self.tblwSporcuBilgi.setRowCount(100)
        self.tblwSporcuBilgi.setColumnCount(10)
        self.tblwSporcuBilgi.setObjectName("tblwSporcuBilgi")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 650, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lblKayitSayisi = QtWidgets.QLabel(self.centralwidget)
        self.lblKayitSayisi.setGeometry(QtCore.QRect(110, 650, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblKayitSayisi.setFont(font)
        self.lblKayitSayisi.setText("")
        self.lblKayitSayisi.setObjectName("lblKayitSayisi")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(780, 30, 191, 291))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnEkle = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnEkle.setObjectName("btnEkle")
        self.verticalLayout_2.addWidget(self.btnEkle)
        self.btnSil = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnSil.setObjectName("btnSil")
        self.verticalLayout_2.addWidget(self.btnSil)
        self.btnAra = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnAra.setObjectName("btnAra")
        self.verticalLayout_2.addWidget(self.btnAra)
        self.btnGuncelle = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.verticalLayout_2.addWidget(self.btnGuncelle)
        self.btnListele = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnListele.setObjectName("btnListele")
        self.verticalLayout_2.addWidget(self.btnListele)
        self.btnCikis = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnCikis.setObjectName("btnCikis")
        self.verticalLayout_2.addWidget(self.btnCikis)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(760, 650, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lblOrtKilo = QtWidgets.QLabel(self.centralwidget)
        self.lblOrtKilo.setGeometry(QtCore.QRect(860, 650, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblOrtKilo.setFont(font)
        self.lblOrtKilo.setText("")
        self.lblOrtKilo.setObjectName("lblOrtKilo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1025, 21))
        self.menubar.setObjectName("menubar")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuHakkinda = QtWidgets.QAction(MainWindow)
        self.menuHakkinda.setObjectName("menuHakkinda")
        self.menuYard_m.addAction(self.menuHakkinda)
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        self.cmbSporKulubu.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Sporcu Bilgileri"))
        self.label_9.setText(_translate("MainWindow", "Doğum Tarihi:"))
        self.label_8.setText(_translate("MainWindow", "Branş:"))
        __sortingEnabled = self.lwBrans.isSortingEnabled()
        self.lwBrans.setSortingEnabled(False)
        item = self.lwBrans.item(0)
        item.setText(_translate("MainWindow", "Güreş"))
        item = self.lwBrans.item(1)
        item.setText(_translate("MainWindow", "Boks"))
        item = self.lwBrans.item(2)
        item.setText(_translate("MainWindow", "Karete"))
        item = self.lwBrans.item(3)
        item.setText(_translate("MainWindow", "Tekvando"))
        item = self.lwBrans.item(4)
        item.setText(_translate("MainWindow", "Aikido"))
        item = self.lwBrans.item(5)
        item.setText(_translate("MainWindow", "Judo"))
        self.lwBrans.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "TC Kimlik Numarası:"))
        self.label_2.setText(_translate("MainWindow", "Sporcu Adı:"))
        self.label_3.setText(_translate("MainWindow", "Sporcu Soyadı:"))
        self.label_4.setText(_translate("MainWindow", "Spor Kulübü:"))
        self.cmbSporKulubu.setItemText(0, _translate("MainWindow", "Galatasaray"))
        self.cmbSporKulubu.setItemText(1, _translate("MainWindow", "Fenerbahçe"))
        self.cmbSporKulubu.setItemText(2, _translate("MainWindow", "Beşiktaş"))
        self.cmbSporKulubu.setItemText(3, _translate("MainWindow", "Trabzonspor"))
        self.cmbSporKulubu.setItemText(4, _translate("MainWindow", "Eskişehirspor"))
        self.cmbSporKulubu.setItemText(5, _translate("MainWindow", "Bursaspor"))
        self.label_5.setText(_translate("MainWindow", "Sporcu Kilosu:"))
        self.label_6.setText(_translate("MainWindow", "Sporcu Cinsiyeti:"))
        self.cmbCinsiyet.setItemText(0, _translate("MainWindow", "Erkek"))
        self.cmbCinsiyet.setItemText(1, _translate("MainWindow", "Kadın"))
        self.label_7.setText(_translate("MainWindow", "Medeni Hal:"))
        self.chkMedeniHal.setText(_translate("MainWindow", "Evli"))
        self.label_10.setText(_translate("MainWindow", "Kayıt Sayısı:"))
        self.btnEkle.setText(_translate("MainWindow", "KAYIT EKLE"))
        self.btnSil.setText(_translate("MainWindow", "KAYIT SİL"))
        self.btnAra.setText(_translate("MainWindow", "KAYIT ARA"))
        self.btnGuncelle.setText(_translate("MainWindow", "GÜNCELLE"))
        self.btnListele.setText(_translate("MainWindow", "KAYIT LİSTELE"))
        self.btnCikis.setText(_translate("MainWindow", "ÇIKIŞ"))
        self.label_11.setText(_translate("MainWindow", "Kilo Ortalaması:"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.menuHakkinda.setText(_translate("MainWindow", "Hakkında"))

