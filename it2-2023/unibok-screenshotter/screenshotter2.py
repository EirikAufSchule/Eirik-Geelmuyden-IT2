import webbrowser as wb #https://docs.python.org/3/library/webbrowser.html
import pyautogui #https://pyautogui.readthedocs.io/en/latest/keyboard.html#the-hotkey-function
import pyperclip #https://www.askpython.com/python-modules/pyperclip
import time
import os

def getPageNumber() -> int:
    """Velger søkefeltet, kopierer til clipboard, lukker søkefeltet"""
    pyautogui.hotkey('command', 'l')
    pyautogui.hotkey('command', 'c')
    pyautogui.press("esc")
    """leser clipboard, fjerner url-rooten, slik at kun sidetall står igjen"""
    url = pyperclip.paste()
    number = url[len(urlRoot): ]
    """konverterer til int"""
    try:
        number = int(number)
    #kjører igjen ved ValueError
    except ValueError:
        time.sleep(0.2)
        getPageNumber()
        print("ValueError")
    return number

chapter_names = ["kapittel1", "kapittel2", "kapittel3"] #skriv inn kapittelnavn for mappenavn

endOfBook = 423
firstPage = 41
urlRoot = r"https://les.unibok.no/#cappelendamm/p202117/3619/"
url =  urlRoot + str(firstPage)
wb.open(url)
time.sleep(4)
screenshot = pyautogui.screenshot(region=(2700,1600,260,200 ))
screenshot.save(r"/Users/eirikgeelmuyden/Desktop/helvete.png")
#flytter mus til side og klikker vekk navbar
pyautogui.moveTo(50, 500)
pyautogui.click()

for name in chapter_names:
    newpath = r"/Users/eirikgeelmuyden/Desktop/Eirik-Geelmuyden-IT2/unibok-screenshotter/sheit/" + name + r"/" 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    ssCount = 1
    imgFound = False
    while not imgFound:
        screenshot = pyautogui.screenshot(region=(850,150, 1170,1650))
        #R gjør om til 'raw string' - '/' leses som ren tekst
        screenshot.save(newpath + name + "-" + str(ssCount) + r".png")
        try:
            clickCoordinates = pyautogui.locateCenterOnScreen("unibok-neste-kap.png", grayscale = True, region= (2700,1600,260,200))
            print(clickCoordinates)
            pyautogui.moveTo(clickCoordinates)
            pyautogui.click()
            time.sleep(4)#vent på at neste side laster
            imgFound = True
        except:
            pyautogui.press("pagedown")
            ssCount += 1
            