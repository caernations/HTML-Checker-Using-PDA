from os import system
import htmlParser
import sys
import pda
while True:
    system('cls')
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
        print("HTML Parser")
        html_file_name = input("Input HTML filename (.html): ")
        html_input = htmlParser.parseHTML(html_file_name)
        print("HTML Input:")
        print(html_input)
        print("PDA Reader")
        pda_file_name = input("Input PDA filename (.txt): ")
        html_pda = pda.HTMLCheckerPDA()
        html_pda.setPDA(*pda.txtPDAExtractor(pda_file_name))
        result = html_pda.check_correctness(html_input)
        if result == -1:
            print("""
░ Result:
░ >> HTML IS VALID                
        """)
        else:
            print(f"""
░ Result:
░ >> HTML IS INVALID (error at line: {result})                
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

