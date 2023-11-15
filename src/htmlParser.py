def parseHTML(file_path):
    parsedHTML = []
    
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


file_path = input("Input file path: ")
result = parseHTML(file_path)
for r in result:
    print(r)
