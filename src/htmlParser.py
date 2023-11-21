from os import system

def parseHTML():
    parsedHTML = []
    file_path = input("Input file path: ")

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            for line_number, line in enumerate(lines, 1):
                tag = ''
                in_tag = False  

                for char in line:
                    if char == '<':  
                        in_tag = True
                        tag += '<' 
                    elif char == '>':  
                        tag += '>'
                        parsedHTML.append((line_number, tag))
                        tag = '' 
                        in_tag = False
                    elif in_tag: 
                        tag += char
        return parsedHTML
    
    except FileNotFoundError:
        print("File not found. Please try again.")
        system('pause')
        system('cls')
        return None
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

result = parseHTML()
if result:
    for r in result:
        print(r)