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
    number = url[len(urlStart): ]
    """konverterer til int"""
    try:
        number = int(number)
    #kjører igjen ved ValueError
    except ValueError:
        time.sleep(0.2)
        getPageNumber()
        print("ValueError")
    return number

#sidetall for start på hvert kapittel
chapter_starts = {
    "kapittel_1": 7,
    "kapittel_2": 42, 
    "kapittel_3": 82,
    "kapittel_4": 118,
    "kapittel_5": 162,
    "kapittel_6": 208,
    "mellomside":252,
    "oppgaver_1": 253,
    "oppgaver_2": 265,
    "oppgaver_3": 291,
    "oppgaver_4": 314,
    "oppgaver_5": 336,
    "oppgaver_6": 367,
    "fasit-teoridel": 394,
    "fasit-oppgaver": 420,
    "stikkord":423,
}

urlStart = "https://les.unibok.no/#cappelendamm/p202117/3619/"

pageNumbersKeys = list(chapter_starts.keys())

for i in range(len(chapter_starts)):
    #lager ny mappe med filplass, med navnet til den aktuelle nøkkelen
    newpath = r"/Users/eirikgeelmuyden/Desktop/Eirik-Geelmuyden-IT2/unibok-screenshotter/1p-bok/" + str(pageNumbersKeys[i]) + r"/" 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    #sidetallet i boken vi vil ha i URL-en
    page = str(chapter_starts[pageNumbersKeys[i]])
    #setter sammen med URL-roten
    url = urlStart + page
    wb.open(url)
    time.sleep(3)
    #flytter mus til side og klikker vekk navbar
    pyautogui.moveTo(50, 500)
    pyautogui.click()

    #initierer siste side av kapittelet
    lastPage = chapter_starts[pageNumbersKeys[i+1]] - 1
    currentPage = getPageNumber()
    ssCount = 1
    while currentPage != lastPage and ssCount <100:
        currentPage = getPageNumber()
        screenshot = pyautogui.screenshot(region=(850,150, 1170,1650))
        #R gjør om til 'raw string' - '/' leses som ren tekst
        screenshot.save(newpath + pageNumbersKeys[i] + r"-" + str(ssCount) + r".png")
        time.sleep(0.2)
        pyautogui.press('pagedown')
        time.sleep(1.3)
        ssCount += 1

    pyautogui.hotkey('command', 'w')





