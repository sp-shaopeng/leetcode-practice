class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        ptr = 0
        for i in range(len(pushed)) :
            if(pushed[i] == popped[ptr]) :
                ptr += 1
                while(ptr < len(popped) and stack != [] and popped[ptr] == stack[-1]) :
                    stack.pop()
                    ptr += 1
                
            else:
                stack.append(pushed[i])
        if(ptr == len(popped)) :
            return True
        
        while(len(stack) > 0) :
            v = stack.pop()
            if(v != popped[ptr]) :
                return False
            ptr += 1
        return True