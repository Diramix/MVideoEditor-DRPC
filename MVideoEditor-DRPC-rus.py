from pypresence import Presence
import time
import pyautogui

RPC = Presence(1243721758591418439)
RPC.connect()

TIME = time.time()

print('MVideo-DRPC: Активирован')

while True:
    windows = pyautogui.getWindowsWithTitle("Movavi Video Editor –")
    for window in windows:
        if "Movavi Video Editor" in window.title:
            pos = window.title.find('–')
            project_name = window.title[pos + 1:]
            del_star = project_name.find('*')
            final_name = project_name[:del_star]
        
            RPC.update(
                state="Монтирует –" + final_name,
                large_image="icon",
                large_text="Movavi Video Editor",
                start=TIME
            )
        time.sleep(1)