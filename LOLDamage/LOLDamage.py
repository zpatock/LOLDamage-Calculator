import pyautogui
import pytesseract
import numpy as np
from PIL import Image, ImageGrab, ImageOps
import sys
import time
import cv2
import json
import tkinter as tk
import threading
import keyboard as ks
from pynput.keyboard import Key, Listener, KeyCode
from pynput import keyboard
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
import imgcompare


pytesseract.pytesseract.tesseract_cmd = r'.\Tesseract-OCR\tesseract.exe'

#while True:
    #w = pyautogui.position()
    #x_mouse = w.x
    #y_mouse = w.y
    #print(x_mouse, y_mouse)


#To find level and which ability leveled, wait for key press such and middle mouse button and q w e r
class ocr():
    
    def __init__(self):
        pass
        
    def refData():

        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        eArmor = ImageGrab.grab(bbox =(30,41,65,63)) 
        eArmor.save(r'.\eArmor.png')
        eArmor = cv2.imread(r'.\eArmor.png', cv2.IMREAD_GRAYSCALE)
        #cv2.imrwrite(eArmor, 'eArmor.png')
        #eArmor = Image.open(r'C:\Users\Zac\Documents\Visual Studio 2019\Projects\LOLDamage\LOLDamage\eArmor.png')
        strImg = pytesseract.image_to_string(eArmor)
        conStrImg = json.dumps(strImg)
        i = 1
        newStr1 = ""
        while (i < 4):
            newStr1 = newStr1 + conStrImg[i]
            i = i + 1
        cmpStr = 2
        if (newStr1[cmpStr] == '\"' or newStr1[cmpStr] == '\\'):
            newStr1 = newStr1[:-1]
        
        try:
            eAint = int(newStr1) 
        except ValueError:
            print("Not an int")
            eAint = 0
        
    
             
        
        eMr = ImageGrab.grab(bbox =(89,38,120,60)) 
        eMr.save(r'.\eMr.png')
        eMr = cv2.imread(r'.\eMr.png',cv2.IMREAD_GRAYSCALE)
        #eMr = Image.open(r'C:\Users\Zac\Documents\Visual Studio 2019\Projects\LOLDamage\LOLDamage\eMr.png')
        strImg2 = pytesseract.image_to_string(eMr)
        conStrImg2 = json.dumps(strImg2)
        i = 1
        newStr2 = ""
        while (i<4):
            newStr2 = newStr2 + conStrImg2[i]
            i = i + 1
 
        if (newStr2[cmpStr] == '\"' or newStr2[cmpStr] == '\\'):
            newStr2 = newStr2[:-1]
        
        try:
            eMrint = int(newStr2)
        except ValueError:
            print("Not an int")
            eMrint = 0
    


            #485,940,525,998 fuctioning for 3 digit ap   485,854,513,1500))
        ap = ImageGrab.grab(bbox =(485,940,525,1000))
        ap.save(r'.\ap.png')
        ap = cv2.imread(r'.\ap.png',cv2.IMREAD_GRAYSCALE)
        #ap = Image.open(r'C:\Users\Zac\Documents\Visual Studio 2019\Projects\LOLDamage\LOLDamage\ap.png')
        strImg3 = pytesseract.image_to_string(ap)
        conStrImg3 = json.dumps(strImg3)
        i = 1
        newStr3 = ""
        while (i<4):
            newStr3 = newStr3 + conStrImg3[i]
            i = i + 1

        if (newStr3[cmpStr] == '\"' or newStr3[cmpStr] == '\\'):
            newStr3 = newStr3[:-1]
        
        try:
            eApint = int(newStr3)
        except ValueError:
            print("Not an int")
            eApint = 13

    


        ad = ImageGrab.grab(bbox =(390,947,528,1071)) 
        ad.save(r'.\ad.png')
        ad = cv2.imread(r'.\ad.png', cv2.IMREAD_GRAYSCALE)
        #ad = Image.open(r'C:\Users\Zac\Documents\Visual Studio 2019\Projects\LOLDamage\LOLDamage\ad.png')
        strImg4 = pytesseract.image_to_string(ad)
        conStrImg4 = json.dumps(strImg4)
        i = 1
        newStr4 = ""
        while (i<4):
            newStr4 = newStr4 + conStrImg4[i]
            i = i + 1
        
        if (newStr4[cmpStr] == '\"' or newStr4[cmpStr] == '\\'):
            newStr4 = newStr4[:-1]
            
        try:
            eAdint = int(newStr4)
        except ValueError:
            print("Not an int") 
            eAdint = 0



        eH = ImageGrab.grab(bbox =(230, 41, 272, 80)) 
        eH.save(r'.\eH.png')
        eH = cv2.imread(r'.\eH.png')
        img = cv2.cvtColor(eH, cv2.COLOR_BGR2GRAY)
        x, img = cv2.threshold(img, 150,255, cv2.THRESH_BINARY)
        #ad = Image.open(r'C:\Users\Zac\Documents\Visual Studio 2019\Projects\LOLDamage\LOLDamage\ad.png')
        strImg5 = pytesseract.image_to_string(img)
        conStrImg5 = json.dumps(strImg5)
        i = 1
        newStr5 = ""
        while (i < len(conStrImg5)):
            newStr5 = newStr5 + conStrImg5[i]
            i = i + 1
        try:
            newStr5 = newStr5[0] + newStr5[1] + newStr5[2] + newStr5[3]
        except:
            pass
        try:
            if (newStr5[cmpStr] == '\"' or newStr5[cmpStr] == '\\' or newStr5[3] == ' '):
                newStr5 = newStr5[:-1]
        except:
            pass
            
        try:
            eHint = int(newStr5)
        except ValueError:
            #print(newStr5) 
            eHint = 0

        return [eAint, eMrint, eApint, eAdint, eHint]     


            
class lvl(object):
   
    def __init__(self):
        self.qlvl = 0
        self.wlvl = 0
        self.elvl = 0
        self.rlvl = 0
    
    def incQ(self):
        if (self.qlvl == 5):
            pass
        else:
            self.qlvl += 1

    def incW(self):
        if (self.wlvl == 5):
            pass
        else:
            self.wlvl += 1

    def incE(self):
        if (self.elvl == 5):
            pass
        else:
            self.elvl += 1

    def incR(self):
        if (self.rlvl == 3):
            pass
        else:
            self.rlvl += 1

        
class champs(object):
    
    def __init__(self, name, qratio, q1, q2, q3, q4, q5, wratio, w1, w2, w3, w4, w5, eratio, e1, e2, e3, e4, e5, rratio, r1, r2, r3):
        self.name = name
        self.qratio = qratio
        self.ql1 = q1
        self.ql2 = q2
        self.ql3 = q3
        self.ql4 = q4
        self.ql5 = q5
        self.wratio = wratio
        self.wl1 = w1
        self.wl2 = w2
        self.wl3 = w3
        self.wl4 = w4
        self.wl5 = w5
        self.eratio = eratio
        self.el1 = e1
        self.el2 = e2
        self.el3 = e3
        self.el4 = e4
        self.el5 = e5
        self.rratio = rratio
        self.rl1 = r1
        self.rl2 = r2
        self.rl3 = r3

class createChamps(object):
    def __init__(self):
        pass

    def diana():
        ch = champs("Diana", 0.7, 60, 95, 130, 165, 200, 0.15, 18, 30, 42, 54, 66, 0.4, 40, 60, 80, 100 , 120, 0.6, 200, 300, 400)
        return ch

    def corki():
        return None


#currItems = ocrItem()

class ocrItem():

    def __init__(self, list):
        self.list = list[6]

    def getList(self):
        return self.list

    def ocrItems(self):
        iSlot1 = ImageGrab.grab(bbox =(1132, 948, 1166, 986))
        iSlot1 = ImageOps.grayscale(iSlot1)

        iSlot2 = ImageGrab.grab(bbox =(1184, 948, 1218, 986))
        iSlot2 = ImageOps.grayscale(iSlot2)

        iSlot3 = ImageGrab.grab(bbox =(1234, 948, 1268, 986))
        iSlot3 = ImageOps.grayscale(iSlot3)

        iSlot4 = ImageGrab.grab(bbox =(1132, 996, 1166, 1032))
        iSlot4 = ImageOps.grayscale(iSlot4)

        iSlot5 = ImageGrab.grab(bbox =(1184, 996, 1218, 1032))
        iSlot5 = ImageOps.grayscale(iSlot5)

        iSlot6 = ImageGrab.grab(bbox =(1234, 996, 1268, 1032))
        iSlot6 = ImageOps.grayscale(iSlot6)

        images = [iSlot1, iSlot2, iSlot3, iSlot4, iSlot5, iSlot6]

        #itemList = set()
        self.list.clear()
        index = 0
        
        count = 1
        for i in range(len(images)):
            path = r".\NightHarvester\iSlot" + str(count) + ".png"
            is_same = imgcompare.is_equal(path, images[i], tolerance=2.5)
            if is_same == True:
                nh = items(125, 1.15, 0.0, 0, 0)
                self.list[index] = nh
                index += 1
                break
            else:
                count  += 1

        count = 1
        for i in range(len(images)):
            path = r".\Liandrys\iSlot" + str(count) + ".png"
            is_same = imgcompare.is_equal(path, images[i], tolerance=2.5)
            if is_same == True:
                li = items(60, 1.06, 1.04, 0, 0)
                self.list[index] = li
                index += 1
                break
            else:
                count  += 1

        count = 1
        for i in range(len(images)):
            path = r".\Ludens\iSlot" + str(count) + ".png"
            is_same = imgcompare.is_equal(path, images[i], tolerance=2.5)
            if is_same == True:
                lud = items(100, 1.10, 0.0, 0, 0)
                self.list[index] = lud
                index += 1
                break
            else:
                count  += 1

        count = 1
        for i in range(len(images)):
            path = r".\Rocketbelt\iSlot" + str(count) + ".png"
            is_same = imgcompare.is_equal(path, images[i], tolerance=2.5)
            if is_same == True:
                rb = items(125, 1.15, 0.0, 0, 0)
                self.list[index] = rb
                index += 1
                break
            else:
                count  += 1

        count = 1
        for i in range(len(images)):
            path = r".\Everfrost\iSlot" + str(count) + ".png"
            is_same = imgcompare.is_equal(path, images[i], tolerance=2.5)
            if is_same == True:
                ef = items(125, 1.35, 0.0, 0, 0)
                self.list[index] = ef
                index += 1
                break
            else:
                count  += 1

        
        self.list[0] = items(125, 1.35, 0.0, 0, 0)

class items():

    def __init__(self, dmg, scl, dmgHth, mrpenflat, mrpenper):
        self.dmg = dmg
        self.scl = scl
        self.dmgHth = dmgHth
        self.mrPenFlat = mrpenflat
        self.mrPenPer = mrpenper
    

    
class calcSpellDmg(object):
    
    
    def calcDmg(eA, eM, ap, ad):
        #item = items()
        #if (hasVoid == True):
            #mpenper = item.voidStaff
        #if (hasSorcs == True):
            #mpenflat = item.sorShoes   
        
        #if hasVoid == True or hasSorcs == True:
           # mr = eM * (1 - mpenper) - mpenflat
        #else:
        mr = 0
        
        if l.qlvl == 0:
            dmgq = 0
        if l.qlvl == 1:
            dmgq = (currentChamp.ql1 + (ap * currentChamp.qratio)) * (100/(mr+100))
        if l.qlvl == 2:
            dmgq = (currentChamp.ql2 + (ap * currentChamp.qratio)) * (100/(mr+100))
        if l.qlvl == 3:
            dmgq = (currentChamp.ql3 + (ap * currentChamp.qratio)) * (100/(mr+100))
        if l.qlvl == 4:
            dmgq = (currentChamp.ql4 + (ap * currentChamp.qratio)) * (100/(mr+100))
        if l.qlvl == 5:
            dmgq = (currentChamp.ql5 + (ap * currentChamp.qratio)) * (100/(mr+100))

        if l.wlvl == 0:
            dmgw = 0
        if l.wlvl == 1:
            dmgw = (currentChamp.wl1 + (ap * currentChamp.wratio)) * (100/(mr+100))
        if l.wlvl == 2:
            dmgw = (currentChamp.wl2 + (ap * currentChamp.wratio)) * (100/(mr+100))
        if l.wlvl == 3:
            dmgw = (currentChamp.wl3 + (ap * currentChamp.wratio)) * (100/(mr+100))
        if l.wlvl == 4:
            dmgw = (currentChamp.wl4 + (ap * currentChamp.wratio)) * (100/(mr+100))
        if l.wlvl == 5:
            dmgw = (currentChamp.wl5 + (ap * currentChamp.wratio)) * (100/(mr+100))

        if l.elvl == 0:
            dmge = 0
        if l.elvl == 1:
            dmge = (currentChamp.el1 + (ap * currentChamp.eratio)) * (100/(mr+100))
        if l.elvl == 2:
            dmge = (currentChamp.el2 + (ap * currentChamp.eratio)) * (100/(mr+100))
        if l.elvl == 3:
            dmge = (currentChamp.el3 + (ap * currentChamp.eratio)) * (100/(mr+100))
        if l.elvl == 4:
            dmge = (currentChamp.el4 + (ap * currentChamp.eratio)) * (100/(mr+100))
        if l.elvl == 5:
            dmge = (currentChamp.el5 + (ap * currentChamp.eratio)) * (100/(mr+100))

        if l.rlvl == 0:
            dmgr = 0
        if l.rlvl == 1:
            dmgr = (currentChamp.rl1 + (data[2] * currentChamp.rratio)) * (100/(mr+100))
        if l.rlvl == 2:
            dmgr = (currentChamp.rl1 + (data[2] * currentChamp.rratio)) * (100/(mr+100))
        if l.rlvl == 3:
            dmgr = (currentChamp.rl1 + (data[2] * currentChamp.rratio)) * (100/(mr+100))
        if l.rlvl == 4:
            dmgr = (currentChamp.rl1 + (data[2] * currentChamp.rratio)) * (100/(mr+100))
        if l.rlvl == 5:
            dmgr = (currentChamp.rl1 + (data[2] * currentChamp.rratio)) * (100/(mr+100))
        
        
        try:
            global itemlist
            print(itemList[0].dmg)
        except:
            print("no item in list")

        return dmgq + dmgw + dmge + dmgr

        

class calcDmgAd(object):
    pass

class gameLoop(object):
    def __init__(self):
        pass


    @staticmethod
    def gameloop():
        #ocrC = ocr()
        lvlC = lvl()
        global hasVoid
        hasVoid = False
        global hasSorcs
        hasSorcs = False
        global l
        l = lvl()
        eArm = 0
        eMag = 0
        mAp  = 0
        mAd  = 0
        inc = 0
        #frontEndThread = threading.Thread(target=gui.liveGui)
        #frontEndThread.start()
        app = QApplication(sys.argv)
        win = QMainWindow()
        win.setGeometry(500, 300, 500, 500)
        win.setWindowTitle("Tig Ol Bitties")
        dmg = 0

        label = QtWidgets.QLabel(win)
        label.setText("Damage Output =")
        label.move(5,5)

        label2 = QtWidgets.QLabel(win)
        label2.setText(str(dmg))
        label2.move(100, 5)

        eHLabel = QtWidgets.QLabel(win)
        eHLabel.setText("Current Enemy Health = ")
        eHLabel.setGeometry(5, 40, 300, 50)
        #eHLabel.move(5, 50)

        eHLabel = QtWidgets.QLabel(win)
        eHLabel.setText(str(0))
        eHLabel.move(150, 50)

        yellow = QtWidgets.QLabel(win)
        yellow.setText("Background will turn yellow if damage is within 10% of enemy's total health!")
        yellow.setGeometry(5, 200, 400, 50)

        red = QtWidgets.QLabel(win)
        red.setText("Background will turn red if damage is guaranteed to kill!")
        red.setGeometry(5, 250, 400, 50)
        
        p = win.palette()

        p.setColor(QtGui.QPalette.Window, QtGui.QColor(0, 255, 0))
        win.setPalette(p)

        win.show()
        currItems = None
        while True:
            #print(cham)
            
            global data
            
            data = ocr.refData()
            eHLabel.setText(str(data[4]))
            print(data)

            if (eArm != data[0] and data[0] != 0):
                eArm = data[0]

            if (eMag != data[1] and data[1] != 0):
                eMag = data[1]

            if (mAp != data[2] and data[2] != 13):
                mAp  = data[2]

            if (mAd != data[3] and data[3] != 0):
                mAd  = data[3]

            
            dmg = calcSpellDmg.calcDmg(eArm, eMag, mAp, mAd)
            print(dmg)
            label2.setText(str(dmg))

            if dmg < data[4]:
                p.setColor(QtGui.QPalette.Window, QtGui.QColor(0, 255, 0))
                win.setPalette(p)
            elif dmg > (data[4] * 0.9):
                p.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 255, 0))
                win.setPalette(p)
            elif dmg > data[4]:
                p.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 0, 0))
                win.setPalette(p)
            
            #items.ocrItems()
            
            app.processEvents()
            
            #gui.liveGui(dmg)
    
    def listener():
        COMBINATIONS = [
    {keyboard.KeyCode(char='q'), keyboard.Key.alt_l}

]
        COMBINATIONS2 = [
    {keyboard.KeyCode(char='w'), keyboard.Key.alt_l}

]
        COMBINATIONS3 = [
    {keyboard.KeyCode(char='e'), keyboard.Key.alt_l}

]
        COMBINATIONS4 = [
    {keyboard.KeyCode(char='r'), keyboard.Key.alt_l}

]

        current = set()
        
        
        def on_press(key):
        
            if any(key in COMBO for COMBO in COMBINATIONS):
                current.add(key)
                if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                    l.incQ()

            if any(key in COMBO for COMBO in COMBINATIONS2):
                current.add(key)
                if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS2):
                    l.incW()

            if any(key in COMBO for COMBO in COMBINATIONS3):
                current.add(key)
                if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS3):
                    l.incE()

            if any(key in COMBO for COMBO in COMBINATIONS4):
                current.add(key)
                if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS4):
                    l.incR()
            
            #if key.char == 'v':
                #items.ocrItems()
            
            #print('{0} pressed'.format(
            #key))
            
                

           
        def on_release(key):
            try:
                if any([key in COMBO for COMBO in COMBINATIONS]):
                    current.remove(key)
                if any([key in COMBO for COMBO in COMBINATIONS2]):
                    current.remove(key)
                if any([key in COMBO for COMBO in COMBINATIONS3]):
                    current.remove(key)
                if any([key in COMBO for COMBO in COMBINATIONS4]):
                    current.remove(key)
            except KeyError:
                pass

          # Collect events until released
        #listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        #listener.start()
        with Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
    
  
           
class gui():

        
   
    def tryForChamp():
        global currentChamp
        newStr = champSelect.get().lower()
        if (newStr == "diana"):
            currentChamp = createChamps.diana()
            root.destroy()
            gameLoop.gameloop()
        #else:
            #root.destroy()
            #gui.window()
        
        

    def window(): 
        global root
        root = tk.Tk()
        root.title("Tig Ol Bitties")
        champLabel = tk.Label(root, text = "Select Your Champion by Writing their name!")
        champLabel.pack()
        #canvas1 = tk.Canvas(window, width = 400, height = 300)
        global champSelect 
        champSelect = tk.Entry(root, bd= 2) 
        champSelect.pack()
        tk.Button(root, text="Next", command= gui.tryForChamp).pack()
        root.mainloop()
    


#lock = threading.Lock()
secThread = threading.Thread(target=gameLoop.listener)
secThread.start()
gui.window()
#gameLoop.gameloop()






