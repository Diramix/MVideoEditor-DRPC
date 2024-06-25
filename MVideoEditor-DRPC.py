from pypresence import Presence
import time
import pyautogui
import os

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

RPC = Presence(1243721758591418439)
RPC.connect()

TIME = time.time()

print('MVideoEditor-DRPC: Enabled')

RPC.update(
    state="AFK",
    large_image="icon",
    large_text="Movavi Video Editor",
)

while True:
    windows = pyautogui.getWindowsWithTitle("Movavi Video Editor –")
    for window in windows:
        if "Movavi Video Editor" in window.title:
            pos = window.title.find('–')
            project_name = window.title[pos + 1:]
            del_star = project_name.find('*')
            final_name = project_name[:del_star]
            
            clear()
            print('MVideoEditor-DRPC: Enabled')
            print("Editing –" + final_name)
            
            RPC.update(
                state="Editing –" + final_name,
                large_image="icon",
                large_text="Movavi Video Editor",
                start=TIME
            )
        time.sleep(1)