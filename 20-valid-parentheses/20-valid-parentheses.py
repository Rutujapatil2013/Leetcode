class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={")":"(","}":"{","]":"["}
        for char in s:
            if char in d.values():
                stack.append(char)
            else: 
                if stack==[] or (d[char]!=stack.pop()):
                    return False
        return stack==[]
    
    
##############################################################


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        matches = set([('(',')'),('{','}'),('[',']')])
        opening = set('{([')
        lst = []
        
        for i in s:
            if i in opening:
                lst.append(i)
            else:
                if len(lst)==0:
                    return False
                last_element = lst.pop()
                if (last_element,i) not in matches:
                    return False
        return len(lst)==0
    
    #######################################
    
    
    