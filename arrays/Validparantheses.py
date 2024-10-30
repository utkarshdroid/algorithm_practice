class Solution:
    def isValid(self, s: str) -> bool:
        bracs_dict = {
            "{":"}", "(":")","[":"]"
        }
        open_brac_stack = []
        for i in s:
            if i in bracs_dict:
                open_brac_stack.append(i)
            else: 
                if len(open_brac_stack)>0:
                    if bracs_dict[open_brac_stack.pop()]!= i:
                        return False 
                else : 
                    return False
        return True and len(open_brac_stack)==0