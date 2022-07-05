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
    
    C++

class Solution {
public:
    bool isValid(string s) {
        int n=s.length();
        stack<char> ss;
        for(int i = 0; i < n; i++) {
            if(ss.empty()) {
                if(s[i]=='(' || s[i]=='{' || s[i]=='[') ss.push(s[i]);
                else return false;
            }
            else if(s[i]=='(' || s[i]=='{' || s[i]=='[') ss.push(s[i]);
            else {
                if(ss.top()=='(' && s[i]==')') ss.pop();
                else if(ss.top()=='[' && s[i]==']') ss.pop();
                else if(ss.top()=='{' && s[i]=='}') ss.pop();
                else return false;
            }
        }
        if(ss.empty()) return true;
        return false;
    }
};

###########################################################################
    
    
    
