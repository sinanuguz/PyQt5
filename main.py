# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:40:29 2020

@author: USER
"""



#----------------------KÜTÜPHANE--------------------------#
#---------------------------------------------------------#
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AnaSayfaUI import *
from HakkindaUI import *
#----------------------UYGULAMA OLUŞTUR-------------------#
#---------------------------------------------------------#
Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()

penHakkinda=QDialog()
ui2=Ui_Dialog()
ui2.setupUi(penHakkinda)




#----------------------VERİTABANI OLUŞTUR-----------------#
#---------------------------------------------------------#
import sqlite3
global curs
global conn

conn=sqlite3.connect('veritabani.db')
curs=conn.cursor()
sorguCreTblSpor=("CREATE TABLE IF NOT EXISTS spor(                 \
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,    \
                 TCNo TEXT NOT NULL UNIQUE,                        \
                 SporcuAdi TEXT NOT NULL,                          \
                 SporcuSoyadi TEXT NOT NULL,                       \
                 KulupAdi TEXT NOT NULL,                           \
                 Brans TEXT NOT NULL,                              \
                 Cinsiyet TEXT NOT NULL,                           \
                 DTarihi TEXT NOT NULL,                            \
                 MHal TEXT NOT NULL,                               \
                 Kilo TEXT NOT NULL)")
curs.execute(sorguCreTblSpor)
conn.commit()

#----------------------KAYDET-----------------------------#
#---------------------------------------------------------#
def EKLE():
    _lneTCK=ui.lneTCK.text()
    _lneSporcuAdi=ui.lneSporcuAdi.text()
    _lneSporcuSoyadi=ui.lneSporcuSoyadi.text()
    _cmbSporKulubu=ui.cmbSporKulubu.currentText()
    _lwBrans=ui.lwBrans.currentItem().text()
    _cmbCinsiyet=ui.cmbCinsiyet.currentText()
    _cwDTarihi=ui.cwDTarihi.selectedDate().toString(QtCore.Qt.ISODate)
        
    if ui.chkMedeniHal.isChecked():
        _medeniHal="Evli"
    else:
        _medeniHal="Bekar"
    _spnKilo=ui.spnKilo.value()
    
            
    curs.execute("INSERT INTO spor \
                     (TCNo,SporcuAdi,SporcuSoyadi,KulupAdi,Brans,Cinsiyet,DTarihi,MHal,Kilo) \
                      VALUES (?,?,?,?,?,?,?,?,?)", \
                      (_lneTCK,_lneSporcuAdi,_lneSporcuSoyadi,_cmbSporKulubu,_lwBrans,_cmbCinsiyet, \
                       _cwDTarihi,_medeniHal,_spnKilo))
    conn.commit()
    
    
    LISTELE()
#----------------------LİSTELE-----------------------------#
#---------------------------------------------------------#  
def LISTELE():
    
    ui.tblwSporcuBilgi.clear()
    
    ui.tblwSporcuBilgi.setHorizontalHeaderLabels(('No','TC Kimlik No','Sporcu Adı','Sporcu Soyadı', \
                                                  'Kulüp Adı', 'Branş', 'Cinsiyet', 'Doğum Tarihi', \
                                                  'Medeni Hal', 'Sporcu Kilosu'))
    
    ui.tblwSporcuBilgi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    curs.execute("SELECT * FROM spor")
    
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui.tblwSporcuBilgi.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
    ui.lneTCK.clear()
    ui.lneSporcuSoyadi.clear()
    ui.lneSporcuAdi.clear()
    ui.cmbSporKulubu.setCurrentIndex(-1)
    ui.spnKilo.setValue(55)
    
    curs.execute("SELECT COUNT(*) FROM spor")
    kayitSayisi=curs.fetchone()
    ui.lblKayitSayisi.setText(str(kayitSayisi[0]))
    
    curs.execute("SELECT AVG(Kilo) FROM spor")
    ortKilo=curs.fetchone()
    ui.lblOrtKilo.setText(str(ortKilo[0]))
    
   
    

LISTELE()

#----------------------ÇIKIŞ-----------------------------#
#---------------------------------------------------------#  
def CIKIS():
    cevap=QMessageBox.question(penAna,"ÇIKIŞ","Programdan çıkmak istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        conn.close()
        sys.exit(Uygulama.exec_())
    else:
        penAna.show()
        

#----------------------SİL-----------------------------#
#---------------------------------------------------------# 
def SIL():
    cevap=QMessageBox.question(penAna,"KAYIT SİL","Kaydı silmek istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        secili=ui.tblwSporcuBilgi.selectedItems()
        silinecek=secili[1].text()
        try:
            curs.execute("DELETE FROM spor WHERE TCNo='%s'" %(silinecek))
            conn.commit()
            
            LISTELE()
            
            ui.statusbar.showMessage("KAYIT SİLME İŞLEMİ BAŞARIYLA GERÇEKLEŞTİ...",10000)
        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı:"+str(Hata))
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi...",10000)
        
#----------------------ARAMA-----------------------------#
#---------------------------------------------------------# 

def ARA():
    aranan1=ui.lneTCK.text()
    aranan2=ui.lneSporcuAdi.text()
    aranan3=ui.lneSporcuSoyadi.text()
    curs.execute("SELECT * FROM spor WHERE TCNo=? OR SporcuAdi=? OR SporcuSoyadi=? OR (SporcuAdi=? AND SporcuSoyadi=?)",  \
                 (aranan1,aranan2,aranan3,aranan2,aranan3))
    conn.commit()
    ui.tblwSporcuBilgi.clear()
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui.tblwSporcuBilgi.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
    

#----------------------DOLDUR-----------------------------#
#---------------------------------------------------------#
def DOLDUR():
    secili=ui.tblwSporcuBilgi.selectedItems()
    ui.lneTCK.setText(secili[1].text())
    ui.lneSporcuAdi.setText(secili[2].text())
    ui.lneSporcuSoyadi.setText(secili[3].text())
    ui.cmbSporKulubu.setCurrentText(secili[4].text())
    if secili[5].text()=="Güreş":
        ui.lwBrans.item(0).setSelected(True)
        ui.lwBrans.setCurrentItem(ui.lwBrans.item(0))
    if secili[5].text()=="Boks":
        ui.lwBrans.item(1).setSelected(True)
        ui.lwBrans.setCurrentItem(ui.lwBrans.item(1))
    if secili[5].text()=="Karete":
        ui.lwBrans.item(2).setSelected(True)
        ui.lwBrans.setCurrentItem(ui.lwBrans.item(2))
    if secili[5].text()=="Tekvando":
        ui.lwBrans.item(3).setSelected(True)
        ui.lwBrans.setCurrentItem(ui.lwBrans.item(3))
    if secili[5].text()=="Aikido":
        ui.lwBrans.item(4).setSelected(True)
        ui.lwBrans.setCurrentItem(ui.lwBrans.item(4))
    if secili[5].text()=="Judo":
        ui.lwBrans.item(5).setSelected(True)
        ui.lwBrans.setCurrentItem(ui.lwBrans.item(5))
    
    ui.cmbCinsiyet.setCurrentText(secili[6].text())
    
    yil=int(secili[7].text()[0:4])
    ay=int(secili[7].text()[5:7])
    gun=int(secili[7].text()[8:10])
    ui.cwDTarihi.setSelectedDate(QtCore.QDate(yil,ay,gun))
    
    if secili[8].text()=="Evli":
        ui.chkMedeniHal.setChecked(True)
    else:
        ui.chkMedeniHal.setChecked(False)
    
    ui.spnKilo.setValue(int(secili[9].text()))
    
#----------------------GÜNCELLE-----------------------------#
#---------------------------------------------------------#
def GUNCELLE():
    cevap=QMessageBox.question(penAna,"KAYIT GÜNCELLE","Kaydı güncellemek istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        try:
            secili=ui.tblwSporcuBilgi.selectedItems()
            _Id=int(secili[0].text())
            _lneTCK=ui.lneTCK.text()
            _lneSporcuAdi=ui.lneSporcuAdi.text()
            _lneSporcuSoyadi=ui.lneSporcuSoyadi.text()
            _cmbSporKulubu=ui.cmbSporKulubu.currentText()
            _lwBrans=ui.lwBrans.currentItem().text()
            _cmbCinsiyet=ui.cmbCinsiyet.currentText()
            _cwDTarihi=ui.cwDTarihi.selectedDate().toString(QtCore.Qt.ISODate)
        
            if ui.chkMedeniHal.isChecked():
                _medeniHal="Evli"
            else:
                _medeniHal="Bekar"
            _spnKilo=ui.spnKilo.value()
            
            curs.execute("UPDATE spor SET TCNo=?, SporcuAdi=?, SporcuSoyadi=?, Kilo=?,   \
                         KulupAdi=?, Brans=?, Cinsiyet=?, DTarihi=?, MHal=? WHERE Id=?", \
                         (_lneTCK,_lneSporcuAdi,_lneSporcuSoyadi,_spnKilo,\
                          _cmbSporKulubu,_lwBrans,_cmbCinsiyet,_cwDTarihi,_medeniHal,_Id))
            conn.commit()
            
            LISTELE()
            
        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata meydana geldi"+str(Hata))
    else:
        ui.statusbar.showMessage("Güncellme iptal edildi",10000)


#----------------------HAKKINDA-----------------------------#
#---------------------------------------------------------#
def HAKKINDA():
    penHakkinda.show()


#----------------------SİNYAL-SLOT-----------------------------#
#---------------------------------------------------------#
ui.btnEkle.clicked.connect(EKLE)
ui.btnListele.clicked.connect(LISTELE)
ui.btnCikis.clicked.connect(CIKIS)
ui.btnSil.clicked.connect(SIL)
ui.btnAra.clicked.connect(ARA)
ui.tblwSporcuBilgi.itemSelectionChanged.connect(DOLDUR)
ui.btnGuncelle.clicked.connect(GUNCELLE)
ui.menuHakkinda.triggered.connect(HAKKINDA)



sys.exit(Uygulama.exec_())
