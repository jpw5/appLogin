import pyautogui
import time
import customtkinter as ctk
from info import PASSWORDS


def moms():
    username = PASSWORDS["MOMS"]["username"]
    password = PASSWORDS["MOMS"]["password"]
    time.sleep(2)
    pyautogui.write(f'{username}')
    pyautogui.hotkey('tab')
    pyautogui.write(f'{password}')
    pyautogui.hotkey('enter')


def admin():
    username = PASSWORDS["ADMIN"]["username"]
    password = PASSWORDS["ADMIN"]["password"]
    time.sleep(2)
    pyautogui.write(f'{username}')
    pyautogui.hotkey('tab')
    pyautogui.write(f'{password}')
    pyautogui.hotkey('enter')


def orion():
    username = PASSWORDS["ORION"]["username"]
    password = PASSWORDS["ORION"]["password"]
    time.sleep(2)
    pyautogui.write(f'{username}')
    pyautogui.hotkey('tab')
    pyautogui.write(f'{password}')
    pyautogui.hotkey('enter')


def scada():
    username = PASSWORDS["SCADA"]["username"]
    password = PASSWORDS["SCADA"]["password"]
    time.sleep(2)
    pyautogui.write(f'{username}')
    pyautogui.hotkey('tab')
    pyautogui.write(f'{password}')
    pyautogui.hotkey('enter')


def wiw():
    username = PASSWORDS["WIW"]["username"]
    password = PASSWORDS["WIW"]["password"]
    time.sleep(2)
    pyautogui.write(f'{username}')
    pyautogui.hotkey('tab')
    pyautogui.write(f'{password}')
    pyautogui.hotkey('enter')


def vps():
    username = PASSWORDS["VPS"]["username"]
    password = PASSWORDS["VPS"]["password"]
    time.sleep(2)
    pyautogui.write(f'{username}')
    pyautogui.hotkey('tab')
    pyautogui.write(f'{password}')
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')


def oms():
    username = PASSWORDS["OMS"]["username"]
    password = PASSWORDS["OMS"]["password"]
    time.sleep(2)
    pyautogui.write(f'{username}')
    pyautogui.hotkey('tab')
    pyautogui.write(f'{password}')
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')


def mcc():
    username = PASSWORDS["MCC"]["username"]
    password = PASSWORDS["MCC"]["password"]
    time.sleep(2)
    pyautogui.write(f'{username}')
    pyautogui.hotkey('tab')
    pyautogui.write(f'{password}')
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')


def p2000():
    username = PASSWORDS["P2000"]["username"]
    password = PASSWORDS["P2000"]["password"]
    time.sleep(2)
    pyautogui.write(f'{username}')
    pyautogui.hotkey('tab')
    pyautogui.write(f'{password}')
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')


def avigilon():
    username = PASSWORDS["AVIGILON"]["username"]
    password = PASSWORDS["AVIGILON"]["password"]
    time.sleep(2)
    pyautogui.write(f'{username}')
    pyautogui.hotkey('tab')
    pyautogui.write(f'{password}')
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')


root = ctk.CTk()
root.title('App Login')
root.geometry('450x200')
root.resizable(False, False)
ctk.set_appearance_mode('dark')

# First Row
moms_button = ctk.CTkButton(root, text='MOMS', font=ctk.CTkFont(size=20, weight='bold'), command=moms)
moms_button.grid(row=0, column=0, padx=5, pady=10)

admin_button = ctk.CTkButton(root, text='ADMIN', font=ctk.CTkFont(size=20, weight='bold'), command=admin)
admin_button.grid(row=0, column=1, padx=5, pady=10)

orion_button = ctk.CTkButton(root, text='ORION', font=ctk.CTkFont(size=20, weight='bold'), command=orion)
orion_button.grid(row=0, column=2, padx=5, pady=10)

# Second Row
scada_button = ctk.CTkButton(root, text='SCADA', font=ctk.CTkFont(size=20, weight='bold'), command=scada)
scada_button.grid(row=1, column=0, padx=5, pady=10)

wiw_button = ctk.CTkButton(root, text='WIW', font=ctk.CTkFont(size=20, weight='bold'), command=wiw)
wiw_button.grid(row=1, column=1, padx=5, pady=10)

vps_button = ctk.CTkButton(root, text='VPS', font=ctk.CTkFont(size=20, weight='bold'), command=vps)
vps_button.grid(row=1, column=2, padx=5, pady=10)

# Third Row
oms_button = ctk.CTkButton(root, text='OMS', font=ctk.CTkFont(size=20, weight='bold'), command=oms)
oms_button.grid(row=2, column=0, padx=5, pady=10)

mcc_button = ctk.CTkButton(root, text='MCC', font=ctk.CTkFont(size=20, weight='bold'), command=mcc)
mcc_button.grid(row=2, column=1, padx=5, pady=10)

p2000_button = ctk.CTkButton(root, text='P2000', font=ctk.CTkFont(size=20, weight='bold'), command=p2000)
p2000_button.grid(row=2, column=2, padx=5, pady=10)

# Fourth Row
avigilon_button = ctk.CTkButton(root, text='AVIGILON', font=ctk.CTkFont(size=20, weight='bold'), command=avigilon)
avigilon_button.grid(row=3, column=0, padx=5, pady=10)

root.mainloop()

