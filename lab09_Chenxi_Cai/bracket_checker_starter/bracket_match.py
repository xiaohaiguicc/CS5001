from stack import Stack


class BracketMatch:
    """Class for evaluating parenthetical strings"""
    # TODO: Implement bracket matching functionality
    # as required by bracket_checker.py and by
    # bracket_match_test.py

    def brackets_match(self, line):
        """Given a string and return the brackets are paired or not.
        String -> Boolean"""
        stack = Stack()
        bracket_left = ["(", "[", "{"]
        bracket_right = [")", "]", "}"]
        for ch in line:
            if ch in bracket_left:
                stack.push(ch)
            if ch in bracket_right:
                ch_left = stack.pop()
                index = bracket_right.index(ch)
                if bracket_left[index] != ch_left:
                    return False
        if stack.items:
            return False
        else:
            return True
