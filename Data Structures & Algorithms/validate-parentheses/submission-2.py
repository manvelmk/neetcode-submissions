class Solution:
    def isValid(self, s: str) -> bool:
        matches = {}
        matches["{"] = "}"
        matches["("] = ")"
        matches["["] = "]"
        
        brackets = []
        for char in s:
            if char in matches:
                brackets.append(char)
            elif brackets:
                openChar = brackets.pop()
                if not openChar:
                    return False
                elif matches[openChar] != char:
                    return False
            else:
                return False
                                    
        return len(brackets) == 0