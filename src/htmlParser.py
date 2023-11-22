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
                in_comment = False

                for char in line:
                    if char == '<': 
                        tag += '<'
                        if not in_comment:
                            in_tag = True
                    elif char == '>': 
                        tag += '>'
                        if in_tag:
                            if tag.startswith('<!--'):
                                in_comment = True
                                in_tag = False
                                tag = '<!---->'
                            elif in_comment and tag.endswith('-->'):
                                in_comment = False
                            else:
                                in_tag = False
                            parsedHTML.append((line_number, tag))
                            tag = ''
                    elif in_tag or in_comment:
                        if not in_comment:
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