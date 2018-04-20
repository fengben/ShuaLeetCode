class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        buildPoints = []
        for b in buildings:
            buildPoints.append([b[0], b[2]])
            buildPoints.append([b[1], -b[2]])
        buildPoints.sort()
        print(buildPoints)
        import heapq
        hp=[0]
        # heapq.heappush(hp,0)
        min_ = hp[0]
        for i in buildPoints:
            if i[1]>0:
                hp.append(-i[1])
                # heapq.heappush(hp,-i[1])
            else:
                hp.remove(i[1])
                # heapq.heappop(hp)
            cur = min(hp)
            print(hp)
            if cur != min_:
                ans.append([i[0],cur])
                min_=cur
        return ans
        from queue import PriorityQueue
if __name__ == '__main__':
    res=Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
    print(res)