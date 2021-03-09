class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        total = len(nums)
        nums.sort()
        # print(nums)
        def find(ls, left, pos, k) :
    
            if(k == 2):
                head = pos
                tail = total - 1
                s = nums[head] + nums[tail]
                # print("s. :", s)
                while(True) :
                    # print("head, tail", head, tail, s, left)
                    if(s == left):
                        q = ls[0:]
                        q.append(nums[head])
                        q.append(nums[tail])
                        if(q not in ans):
                            ans.append(q)
                            
                        s = nums[head + 1] + nums[tail - 1]
                        head += 1
                        tail -= 1
                        
                        
                    
                    if (s > left) :
                        s = s - nums[tail] + nums[tail - 1]
                        tail = tail -1
                    elif(s < left) :
                        s = s - nums[head] + nums[head + 1]
                        head = head + 1
                    if(head >= tail):
                        break
                
                
            else:
                for i in range(pos, total - k + 1):
                    rs = ls[0:]
                    # print("num.  ", i, nums[i])
                    rs.append(nums[i])
                    find(rs, left - nums[i], i + 1, k - 1)
        
        find([], 0, 0, 3);
        return ans