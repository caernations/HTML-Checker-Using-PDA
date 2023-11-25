from os import system
from collections import Counter
from htmlParser import parseHTML

def txtPDAExtractor(filename):
    file_path = "../pda/" + filename
    with open(file_path, 'r') as file:
        lines = [line.split() for line in file.readlines()]
        states = lines[0]
        input_symbols = lines[1]
        stack_symbols = lines[2]
        starting_state = lines[3][0]
        starting_stack = lines[4]
        accepting_states = lines[5]
        accept_type = lines[6][0]
        transition_functions = lines[7:]
    return states, input_symbols, stack_symbols, starting_state, starting_stack, accepting_states, accept_type, transition_functions 

def checkHTML():
    results = parseHTML()
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


class HTMLCheckerPDA:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.stack_symbols = []
        self.current_state = ""
        self.stack = []
        self.accepting_states = []
        self.accept_type = ""
        self.transition_functions = []

    def setPDA(self,states, alphabet, stack_symbols, starting_state, starting_stack, accepting_states, accept_type, transition_functions):
        self.states = states
        self.alphabet = alphabet
        self.stack_symbols = stack_symbols
        self.current_state = starting_state
        self.stack = starting_stack
        self.accepting_states = accepting_states
        self.accept_type = accept_type
        self.transition_functions = transition_functions

    def push_to_stack(self, item):
        self.stack.append(item)

    def pop_from_stack(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def current_stack_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
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
    def transition(self, input_symbol):
        print("state sekarang:", self.current_state)
        for transition in self.transition_functions:
            if self.current_state == transition[0]:
                # print("input symbol html: ", input_symbol)
                # print("input symbol transisi: ", transition[1])
                # print("stack top html: ", self.current_stack_top())
                # print("stack top transisi: ", transition[2])
                if input_symbol == transition[1] and transition[2] == "epsilon":
                    if(transition[4] != "epsilon"):
                        self.push_to_stack(transition[4])
                    self.current_state = transition[3]
                    return True
                elif input_symbol == transition[1] and self.current_stack_top() == transition[2]:
                    if(transition[4] != "epsilon"):
                        self.push_to_stack(transition[4])
                    self.pop_from_stack()
                    self.current_state = transition[3]
                    return True # sending true if there is a transition function with the input_symbol
        return False # sending false if there is no transition function for the input_symbol

    def check_correctness(self, html_input_symbols):
        for symbol in html_input_symbols:
            print("symbol", symbol)
            print("stack", self.stack)
            if not (symbol[1] in self.alphabet):
                return symbol[0]
            else:
                status = self.transition(symbol[1])
                if status == False:
                    return symbol[0]
                else:
                    continue
        if (self.current_state in self.accepting_states) and not self.stack:
            return -1 # if html valid, it will return -1 because there is no line which the code is invalid
            



