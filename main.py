import os

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

while True:
    clear()
    
    print(
"""Please select language:
1) ru
2) en
"""
    )

    command = str(input("Select language:"))
    
    if command == "1":
        clear()
        from localization import ru
    
    elif command == "2":
        clear()
        from localization import en
        
    else:
        invalid_command = 1