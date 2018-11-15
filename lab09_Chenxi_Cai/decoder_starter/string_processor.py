from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def process_string(self, line):
        """Given a sentence, return the decoded sentence,
        String -> String"""
        stack = Stack()
        result_str = ""
        for ch in line:
            if ch not in "*^":
                stack.push(ch)
            elif ch == "*":
                if stack.peek():
                    result_str += stack.pop()
            elif ch == "^":
                if stack.peek():
                    result_str += stack.pop()
                    if stack.peek():
                        result_str += stack.pop()
        return result_str
