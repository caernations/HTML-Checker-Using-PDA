from os import system

def parseHTML():
    parsedHTML = []
    file_directory = "../test/"

    def process_tag(tag):
        parts = tag.split()
        tag_name = parts[0]
        attributes = []

        for part in parts[1:]:
            attr = part.split('=')[0]
            if '=' in part and attr not in ['method', 'action', 'type']:
                attributes.append(f'{attr}=""')
            else:
                attributes.append(part)

        attr_str = ' '.join(attributes).rstrip('>')
        return (tag_name, attr_str if attr_str else None, '>' if attr_str else None)

    while True:
        print("HTML Parser Tool")
        file_name = input("Input file name: ")
        file_path = file_directory + file_name

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
                            in_tag = True
                        elif char == '>':
                            tag += '>'
                            if in_tag:
                                if tag.startswith('<!--'):
                                    in_comment = True
                                    parsedHTML.append((line_number, '<!---->'))
                                elif in_comment and tag.endswith('-->'):
                                    in_comment = False
                                    parsedHTML.append((line_number, '<!---->'))
                                else:
                                    in_tag = False
                                    tag_name, attrs, closing = process_tag(tag)
                                    parsedHTML.append((line_number, tag_name))
                                    if attrs:  
                                        parsedHTML.append((line_number, attrs))
                                    if closing is not None: 
                                        parsedHTML.append((line_number, closing))
                                    tag = ''
                        elif in_tag:
                            tag += char

            return parsedHTML

        except FileNotFoundError:
            print("File not found. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")