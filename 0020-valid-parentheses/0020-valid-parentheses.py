class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for par in s:
            if par == '(' or par == '[' or par == '{':
                stack.append(par)
            elif par == ')':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif par == ']':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif par == '}':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '{':
                    return False
                else:
                    stack.pop()


        if len(stack) == 0:
            return True
        else:
            return False    
                

        