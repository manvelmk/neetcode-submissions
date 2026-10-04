# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded back to the original list of strings.

from enum import Enum

class Solution:
    class ParseState(Enum):
        
        IDLE = 1
        LENGTH = 2
        TOKENS = 3

    def encode(self, strs: List[str]) -> str:
        
        output = ""
        for token in strs:
            output = output + '!' + str(len(token)) + '|' + token
        return output

    def decode(self, s: str) -> List[str]:
        
        output = []
        word = ""
        charsToMatchRaw = ""
        charsToMatch = -1
        currState = self.ParseState.IDLE
        
        for char in s:
            match currState:
                case self.ParseState.IDLE:
                    if char == "!":
                        currState = self.ParseState.LENGTH
                case self.ParseState.LENGTH:
                    if char.isdigit():
                        charsToMatchRaw += char
                    elif char == "|":
                        charsToMatch = int(charsToMatchRaw)
                        charsToMatchRaw = ""
                        if charsToMatch:
                            currState = self.ParseState.TOKENS
                        else:
                            output.append("")
                            
                case self.ParseState.TOKENS:
                    if charsToMatch > 0:
                        word += char
                        charsToMatch -= 1
                    
                    if charsToMatch <= 0:
                        output.append(word)
                        word = ""
                        charsToMatch = -1
                        currState = self.ParseState.IDLE
            
        return output