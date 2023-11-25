import re # to read whitespace in attribute value


def isTokenExist(array,token):
    for tuple in array:
        if tuple[1] == token:
            return True
    return False

def parseHTML(filename):
    parsedHTML = []
    file_directory = "../test/"
    file_path = file_directory + filename

    def process_tag(tag, line_number):
        

        if tag.startswith('<!--'):
            end_comment_index = tag.find('-->')
            if end_comment_index != -1:
                parsedHTML.append((line_number, '<!---->'))
            else:
                parsedHTML.append((line_number, 'INVALID COMMENT'))
            return 

        if tag.startswith('</'):
            tag = tag.replace('\n', '').replace(' ', '').replace('\t', '')
            parsedHTML.append((line_number, (tag).lower()))
            return

        space_index = tag.find(' ')
        close_index = tag.find('>')

        if 0 < space_index < close_index:
            tag_name = (tag[1:space_index]).strip()
            attrs = tag[space_index + 1:close_index]

            attrs_list = re.findall(r'\w+="[^"]+"|\w+=\w+|\w+', attrs)
            parsedHTML.append((line_number, (f'<{(tag_name.strip(" ")).lower()}')))
            for attr in attrs_list:
                attr_name, equal, attr_value = attr.partition('=')
                if attr_name.lower() in ['method', 'type'] and equal:
                    parsedHTML.append((line_number, f'{(attr_name).lower()}={(attr_value).lower()}'))
                elif not equal and attr_name: 
                    parsedHTML.append((line_number, f'{(attr_name).lower()}'))
                else:  
                    parsedHTML.append((line_number, f'{(attr_name).lower()}=""'))
        else:
            tag_name = tag[1:close_index]
            parsedHTML.append((line_number, f'<{(tag_name).lower()}'))

        parsedHTML.append((line_number, '>'))

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
                    else:
                        if not isTokenExist(parsedHTML, '<html')  or isTokenExist(parsedHTML, '</html>'):
                            parsedHTML.append((line_number, 'INVALID STRING'))
               


        return parsedHTML

    except FileNotFoundError:
        print("File not found. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")