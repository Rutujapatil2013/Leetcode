class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={")":"(","}":"{","]":"["}
        for char in s:
            if char in d.values():
                stack.append(char)
            else: 
                # char in d.keys():
                if stack==[] or (d[char]!=stack.pop()):
                    return False
            # else:
            #     return False
        return stack==[]
    