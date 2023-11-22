from os import system
import htmlParser
import sys


while True:
    print("""
              
═════════════════════════════════════════
              
█░█ ▀█▀ █▀▄▀█ █░░
█▀█ ░█░ █░▀░█ █▄▄

█▀▀ █░█ █▀▀ █▀▀ █▄▀ █▀▀ █▀█
█▄▄ █▀█ ██▄ █▄▄ █░█ ██▄ █▀▄

        
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
              
░ © 2023 | 13522131, 13522139, 13522140 ░
═════════════════════════════════════════
                                                                                            
""")
        
        
    print("""
█▀▄▀█ █▀▀ █▄░█ █░█ ▀
█░▀░█ ██▄ █░▀█ █▄█ ▄
              
░ 1. Check HTML
░ 2. Help
░ 3. Exit
          
""")
    chooseMenu = str(input("░ Choose: ")).upper()
    system('pause')
    system('cls')

    if (chooseMenu == '1') or (chooseMenu == 'CHECK HTML'):
        result = htmlParser.parseHTML()
        if result:
            for r in result:
                print(r)
            print("""
░ Result:
░ >> ACCEPTED                
        """)
        print()
        break 

    elif (chooseMenu == '2') or (chooseMenu == 'HELP'):
        while True:
            print("""
                  
█░█ █▀█ █░█░█   ▀█▀ █▀█   █░█ █▀ █▀▀
█▀█ █▄█ ▀▄▀▄▀   ░█░ █▄█   █▄█ ▄█ ██▄

░ 1. 
░ 2.
░ 3. 
                  
░ Type 'back' to return to the main menu.
""")

            chooseHelp = str(input("░ ")).upper()
            print(chooseHelp)
            if chooseHelp == 'BACK':
                system('cls')
                break
            else:
                print("Invalid.")
                system('cls')

    elif (chooseMenu == '3') or (chooseMenu == 'EXIT'):
        system('cls')
        sys.exit()

    else:
        print("Invalid.")        