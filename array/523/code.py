class Solution(object):
    def checkSubarraySum2(self, nums, k):
        if len(nums)<2:
            return False
        dic = {}
        sum_=0
        for i in range(len(nums)):
            sum_==i
            if k:
                cur = sum_ % k
            else:
                if sum_ ==0:
                    return True
            if cur in dic and dic[cur] - i > 1:
                return True
            else:
                dic[cur] = i
        return False

    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return  False
        # if k==0:
        #     return False
        buf = [nums[0]]
        for i in range(1,len(nums)):
            buf.append(nums[i]+buf[i-1])
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sum_=buf[j]-buf[i]+nums[i]
                if k == 0:
                    if sum_ == 0:
                        return True
                    else:
                        continue
                else:
                    if  sum_% k ==0 and k is not 0:
                        return True
        return False



if __name__ == '__main__':
    res = Solution().checkSubarraySum2([23, 2, 6, 4, 7],0)
    # res = Solution().checkSubarraySum([0,0],0)

    print(res)