class Solution:
    def isValid(self, s: str) -> bool:
        hm = {']': '[','}' : '{',')':'('}
        stack = []
        for ch in s:
            if ch in hm.values():
                stack.append(ch)
            
            elif len(stack) == 0 or stack.pop() != hm[ch]:
                return False
        
        return len(stack) == 0
           
            #elif ch == ')':
               # if len(stack) == 0 or stack.pop() == '(':
                 #   return False
                
            #elif ch == ']':
                #if len(stack) == 0 or stack.pop() == '[':
                  #  return False
           # elif ch == '}':
               # if len(stack) == 0 or stack.pop() == '{':
                   # return False
