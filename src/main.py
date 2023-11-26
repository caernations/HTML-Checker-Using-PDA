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
═════════════════════
              
░ 1. Check HTML
░ 2. Help
░ 3. Exit
          
""")
    chooseMenu = str(input("░ Choose: ")).upper()
    if (chooseMenu == '1') or (chooseMenu == 'CHECK HTML'):
        while True:
            system('cls')
            try:
                print("""

█▀▀ █░█ █▀▀ █▀▀ █▄▀   █░█ ▀█▀ █▀▄▀█ █░░
█▄▄ █▀█ ██▄ █▄▄ █░█   █▀█ ░█░ █░▀░█ █▄▄
════════════════════════════════════════
                    """)
                html_file_name = input("Input HTML file name:\n>> " )
                html_input = htmlParser.parseHTML(html_file_name)
                # print(html_input)
                pda_file_name = input("\nInput PDA file name:\n>> ")
                html_pda = pda.HTMLCheckerPDA()
                html_pda.setPDA(*pda.txtPDAExtractor(pda_file_name))
                result = html_pda.check_correctness(html_input)
                print("""
                      

█▀█ █▀▀ █▀ █░█ █░░ ▀█▀
█▀▄ ██▄ ▄█ █▄█ █▄▄ ░█░
═══════════════════════""")
                if result == -1:
                    print("""
░ >> HTML IS VALID                
                """)
                else:
                    print(f"""
░ >> HTML IS INVALID)                
░ >> Error at line: {result}                
                    """)
                print()
                choice = input("Do you want to check another HTML file? (Y/N): ")
                if(choice.lower() == 'n'):
                    break
                continue 
            except FileNotFoundError:
                print("File not found. Please try again.") 
                system('pause')
                continue
            except Exception as e:
                print(f"An error occurred: {e}") 
                print(f"Chosen Menu: {chooseMenu}")
                continue

    elif (chooseMenu == '2') or (chooseMenu == 'HELP'):
            system('cls')
            while True:
                print("""
                    
█░█ █▀█ █░█░█   ▀█▀ █▀█   █░█ █▀ █▀▀
█▀█ █▄█ ▀▄▀▄▀   ░█░ █▄█   █▄█ ▄█ ██▄

                      
░ 1. Enter a valid HTML file name which is located in the 'test' folder.
░ 2. Enter a valid PDA file name which is located in the 'pda' folder.
░ 3. Wait for the result.
░ 4. Type 'back' to return to the main menu.
                      
    """)
                chooseHelp = str(input("░ ")).upper()
                print(chooseHelp)
                if chooseHelp == 'BACK' or chooseHelp == '4':
                    system('cls')
                    break
                else:
                    print("Invalid.")
                    system('cls')
    elif (chooseMenu == '3') or (chooseMenu == 'EXIT'):
        print("\n")
        sys.exit()
    else:
        print("Invalid.")
