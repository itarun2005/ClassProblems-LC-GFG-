from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #using memoization
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        def recursion(i,j):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=recursion(i-1,j)
            left=recursion(i,j-1)
            dp[i][j]=up+left

            return dp[i][j]
        return recursion(m - 1, n - 1)








        #usuing recursion
        # @cache
        # def recursion(i,j):
        #     if i==0 and j==0:
        #         return 1
        #     if i<0 or j<0:
        #         return 0
        #     up=recursion(i-1,j)
        #     left=recursion(i,j-1)

        #     return up + left
        # return recursion(m - 1, n - 1)