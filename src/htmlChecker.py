from os import system
from collections import Counter
from htmlParser import parseHTML

def transition(lines, state, word, stacks):
        for line_number, line in enumerate(lines, 1):
            if line_number < 10: continue
            else:
                elements = line
                if elements[0] == state and elements[1] == word:
                    print("TEST 1")
                    if elements[2] != 'e':
                        stacks.remove(elements[2])
                    if elements[4] != 'e':
                        stacks.append(elements[4])
                    state = elements[3] 
                    break
                elif elements[0] != state and elements[1] == word:
                    print("TEST 2")
                    return stacks, True
                elif len(lines) == line_number:
                    stacks.append(word)
                    print("TEST 3")
                    return stacks, False
        return stacks, state

def checkHTML():
    results = parseHTML()
    with open("pda.txt", 'r') as file:
        lines = [line.split() for line in file.readlines()]
        symbol = lines[1]
        state = lines[3][0]
        lines = lines[9:]
        stacks = []

    for i in range(len(results)):
        stacks, state = transition(lines, state, results[i][1], stacks)
        print("Stacks:", stacks, "State:", state)
        if state == False:
            print(stacks)
            if stacks[-1] in symbol:
                print("Syntax error in line", results[i][0], "\nInvalid placement:", results[i][1], " inside tag ", '<',stacks[-2],'>', sep='')
            else:
                print("Syntax error in line", results[i][0], "\nUnrecognized word:", results[i][1])
            system("pause")
            system("cls")
        elif state == True:
            require = ['html', 'head', 'body']
            results = [item for sublist in results for item in sublist]
            results = ([element.replace('<', '').replace('>', '').replace('/', '') for element in results if isinstance(element, str) and not element.isdigit()])
            print("results=",results)
            print("stacks", stacks)
            missing = [x for x in require if x not in stacks and x not in results]
            print("missing", missing)
            if len(missing) == 0:
                print('''Check your tag nesting!
Correct code:
<html>
    <head>
    </head>
    <body>
    </body>
</html>''')
            else:
                print("You're missing a required tag")
                print("Missing tag: ", missing)
            system("pause")
            system("cls")
        skip += 1

    print("FS", state, stacks)

    #FINISHING HANDLE
    if len(stacks) == 0:
        if state == 'F':
            print("Accepted")
        else:
            print("NOT HANDLED state=", state, "stacks=", stacks)
    else:
        error = [x for x in results if x[1] == '<' + stacks[0] + '>' or x[1] == stacks[0]]
        print("Syntax error in line", error[0][0])
        if len(stacks) != len(set(stacks)):
            duplicate = [item for item, count in Counter(stacks).items() if count > 1]
            print("There is no closing tag for", (", ".join(str(item) for item in duplicate)))
        else:
            print("NOT HANDLED")

checkHTML()