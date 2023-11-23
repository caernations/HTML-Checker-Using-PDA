def parseHTML():
    parsedHTML = []
    file_directory = "../test/"

    def process_tag(tag, line_number):
        if tag.startswith('<!--'):
            end_comment_index = tag.find('-->')
            if end_comment_index != -1:
                parsedHTML.append((line_number, '<!---->'))
            else:
                parsedHTML.append((line_number, 'INVALID COMMENT'))
            return

        if tag.startswith('</'):
            parsedHTML.append((line_number, tag))
            return

        space_index = tag.find(' ')
        close_index = tag.find('>')

        if 0 < space_index < close_index:
            tag_name = tag[1:space_index]
            attrs = tag[space_index + 1:close_index].strip()
            parsedHTML.append((line_number, f'<{tag_name}'))
            for attr in attrs.split():
                attr_name, equal, attr_value = attr.partition('=')
                if attr_name.lower() in ['method', 'action', 'type'] and equal:
                    parsedHTML.append((line_number, f'{attr_name}={attr_value}'))
                elif equal: 
                    parsedHTML.append((line_number, f'{attr_name}=""'))
        else:
            tag_name = tag[1:close_index]
            parsedHTML.append((line_number, f'<{tag_name}'))

        parsedHTML.append((line_number, '>'))

    print("HTML Parser Tool")
    file_name = input("Input file name: ")
    file_path = file_directory + file_name

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            line_number = 1
            tag = ''
            in_tag = False
            for line in lines:
                for char in line:
                    if char == '\n':
                        line_number += 1
                    elif char == '<':
                        in_tag = True
                        tag = '<'
                    elif char == '>' and in_tag:
                        tag += '>'
                        process_tag(tag, line_number)
                        tag = ''
                        in_tag = False
                    elif in_tag:
                        tag += char

        return parsedHTML

    except FileNotFoundError:
        print("File not found. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")