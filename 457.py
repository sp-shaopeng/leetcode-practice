Qns 457             
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        
        def convert(x):
            if(x < 0) :
                return convert(l  + x)
            elif( x >= l):
                return convert(x - l)
            else:
                return x
        
        for i in range(l) :
            loop = []
            length = 0.00
            p = i
            a = l + l
            for h in range(l + 1):
                if(length/nums[p] < 0):
                    break
                if( a == p):
                    break;
                length += nums[p]
                if( (length > l or length < -l) and p in loop):
                    if(p == i):
                        return True
                    break
                elif(p in loop):
                    break
                loop.append(p)
                a = p
           
                p = convert(p + nums[p])
        return False
                