class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        def find(token) :
            if(len(token) == 0):
                return 1
            
            if(token[-1] == "/") :
                tokens.pop()
                bottom = find(token)
                top = find(token)
                return int(top/bottom)
            if(tokens[-1] == "*") :
                tokens.pop()
                lhs =  find(token) 
                rhs =  find(token)
                v = rhs * lhs
                return v
            if(tokens[-1] == "+") :
                tokens.pop()
                lhs =  find(token) 
                rhs =  find(token)
                v = rhs + lhs
                return v
            if(tokens[-1] == "-") :
                tokens.pop()
                before = find(token)
                after = find(token)
                return after - before
            lhs = int(token[-1])
            token.pop()
            return lhs 
        
        return find(tokens)