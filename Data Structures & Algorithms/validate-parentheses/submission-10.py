class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for char in s:
            if char in list(closeToOpen.values()):
                stack.append(char)
                continue
            
            if len(stack) == 0:
                return False
            
            latest = stack[-1]
            if closeToOpen[char] != latest:
                return False
            
            stack.pop()
                
        
        return len(stack) == 0

            
        
        