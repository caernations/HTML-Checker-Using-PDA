from os import system

def parseHTML():
    parsedHTML = []
    file_directory = "../test/"

    while True:
        print("""
        
█▀▀ █░█ █▀▀ █▀▀ █▄▀   █░█ ▀█▀ █▀▄▀█ █░░
█▄▄ █▀█ ██▄ █▄▄ █░█   █▀█ ░█░ █░▀░█ █▄▄
            
            """)
        file_name = input("Input file name: ")
        file_path = file_directory + file_name

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

                for line_number, line in enumerate(lines, 1):
                    tag = ''
                    in_tag = False
                    in_comment = False
                    in_attribute_value = False
                    quote_char = ''

                    for char in line:
                        if char == '<':
                            tag += '<'
                            in_tag = True
                        elif char == '>':
                            tag += '>'
                            if in_tag:
                                if tag.startswith('<!--'):
                                    in_comment = True
                                    parsedHTML.append((line_number, '<!---->')) 
                                    tag = ''
                                elif in_comment and tag.endswith('-->'):
                                    in_comment = False
                                    parsedHTML.append((line_number, '<!---->'))
                                    tag = ''
                                else:
                                    in_tag = False
                                    tag = remove_attribute_contents(tag)
                                    parsedHTML.append((line_number, tag))
                                    tag = ''
                        elif in_tag:
                            if char in ('"', "'"):
                                if not in_attribute_value:
                                    in_attribute_value = True
                                    quote_char = char
                                    tag += char 
                                elif char == quote_char: 
                                    in_attribute_value = False
                                    tag += char 
                            elif not in_attribute_value or char == quote_char:
                                tag += char  

            return parsedHTML

        except FileNotFoundError:
            print("File not found. Please try again.")
            system('cls')

        except Exception as e:
            print(f"An error occurred: {e}")
            system('cls')

def remove_attribute_contents(tag):
    new_tag = ''
    in_quotes = False
    skip = False
    for char in tag:
        if char in ('"', "'") and not in_quotes:
            in_quotes = True
            new_tag += char
        elif char in ('"', "'") and in_quotes:
            in_quotes = False
            new_tag += char
        elif not in_quotes or skip:
            new_tag += char
        elif in_quotes:
            skip = True  
        elif char == '=':
            new_tag += char
            skip = False  
            
    return new_tag.strip()