class Solution(object):
    def subarraySum(self, nums, k):
            sums = {0: 1}  # prefix sum array
            res = s = 0
            for n in nums:
                s += n  # increment current sum
                res += sums.get(s - k, 0)  # check if there is a prefix subarray we can take out to reach k
                sums[s] = sums.get(s, 0) + 1  # add current sum to sum count
            return res

    # inspire 523
    def subarraySum111(self, nums, k):
        if k ==0:
           return self.subarraySum1(nums,k)
        ans = 0
        sum = [0]
        for x in nums:
            sum.append((sum[-1] + x))
        k = abs(k)
        Dict = {}
        print(sum)
        for i in range(1, len(sum)):
            print(Dict)
            mod = sum[i]%k
            div = sum[i]//k
            if  mod in Dict:
                for j in Dict[mod]:
                    if abs(j[-1] - div) == 1:
                        ans+=1
                        print(j)
                        print(ans)
                Dict[mod].append([i,div])
            else:
                Dict[mod] = [[i,div]]

        return ans

    #TLE
    def subarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        buf = [nums[0]]
        for i in range(1, len(nums)):
            buf.append(nums[i] + buf[i - 1])
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sum_ = buf[j] - buf[i] + nums[i]
                if sum_ == k:
                    ans+=1
        return ans

if __name__ == '__main__':
    ans = Solution().subarraySum([1,1,1],2)
    # ans = Solution().subarraySum([-1,-1,1],1)

    print(ans)