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
                                    tag = remove_attribute_contents(tag)
                                    parsedHTML.append((line_number, tag))
                                tag = ''
                        elif in_tag or in_comment:
                            if not in_comment:
                                if char == '"' and in_tag:
                                    in_attribute_value = not in_attribute_value
                                    tag += char
                                elif not in_attribute_value:
                                    tag += char

            return parsedHTML

        except FileNotFoundError:
            print("File not found. Please try again.")
            system('cls')

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

def remove_attribute_contents(tag):
    new_tag = ''
    in_quotes = False
    for char in tag:
        if char == '"' and not in_quotes:
            in_quotes = True
            new_tag += char
        elif char == '"' and in_quotes:
            in_quotes = False
            new_tag += char
        elif not in_quotes:
            new_tag += char
    return new_tag