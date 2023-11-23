

class HTMLCheckerPDA:
    def __init__(self):
        self.stack = []
        self.current_state = "start"

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

    def transition(self, input_symbol):
        if self.current_state == "start":
            if input_symbol == "<html>":
                self.push_to_stack("<html>")
                self.current_state = "inside_html"
            else:
                self.current_state = "error"

        elif self.current_state == "inside_html":
            if input_symbol == "<head>":
                self.push_to_stack("<head>")
                self.current_state = "inside_head"
            elif input_symbol == "</html>":
                if self.current_stack_top() == "<html>":
                    self.pop_from_stack()
                    self.current_state = "outside_html"
                else:
                    self.current_state = "error"
            else:
                self.current_state = "error"

        elif self.current_state == "inside_head":
            if input_symbol == "<title>":
                self.push_to_stack("<title>")
                self.current_state = "inside_title"
            elif input_symbol == "</head>":
                if self.current_stack_top() == "<head>":
                    self.pop_from_stack()
                    self.current_state = "inside_html"
                else:
                    self.current_state = "error"
            else:
                self.current_state = "error"

        # Add more state-specific transition rules for other parts of the HTML document
        # ...

    def check_correctness(self, input_string):
        for symbol in input_string:
            self.transition(symbol)

        # Check for acceptance or error state
        if self.current_state == "outside_html" and not self.stack:
            return "Valid HTML"
        else:
            return "Invalid HTML"

# Example usage:
html_checker = HTMLCheckerPDA()
input_string = "<html><head></head></html>"
result = html_checker.check_correctness(input_string)
print(result)
