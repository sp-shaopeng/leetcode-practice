class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        print(l1, l2)
        if(l1 == 0 and l2 == 0) :
            return 0
        if(l1 == 0) :
            return self.find(nums2)
        
        if(l2 == 0):
            return self.find(nums1)
        
        
        
        mid = (l1 + l2) / 2
        mid = mid + 1
        
        p1 = 0;
        p2 = 0;
        
        tail = 1
        tailtail = 1
        
        last = 0
        lastlast = 0
        for i in range(mid):
            if(p1 > l1 - 1) :
                lastlast = last
                last = p2
                p2 = p2 + 1
                tailtail = tail
                tail = 2
                
            elif (p2 > l2 - 1) :
                lastlast = last
                last = p1
                p1 = p1 + 1
                tailtail = tail
                tail = 1
                
            else :
                
                if(nums1[p1] < nums2[p2]):
                    lastlast = last
                    last = p1
                    p1 = p1 + 1
                    tailtail = tail
                    tail = 1
                    
                else :
                    lastlast = last
                    last = p2
                    p2 = p2 + 1
                    tailtail = tail
                    tail = 2
                    
        
        
        if((l1+l2) % 2 == 0) :
            if(tail == 1 and tailtail == 1) :
                return (nums1[last] + nums1[lastlast])/2.0
            if(tail == 1 and tailtail == 2) :
                return (nums1[last] + nums2[lastlast])/2.0
            if(tail == 2 and tailtail == 1) :
                return (nums2[last] + nums1[lastlast])/2.0
            if(tail == 2 and tailtail == 2) :
                return (nums2[last] + nums2[lastlast])/2.0
        else :
            if(tail == 1) :
                return nums1[last]
            else :
                return nums2[last]    
            
            
    def find(self, nums):
        l = len(nums)
        if(l%2 == 1) :
            return nums[(l/2)]
        else:
            return (nums[(l/2) - 1] + nums[(l/2)]) / 2.0
                
                