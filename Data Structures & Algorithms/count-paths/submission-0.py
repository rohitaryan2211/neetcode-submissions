class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        area = [[0 for i in range(n)] for j in range(m)]
            
        # print(area)

        # area [2][2] = 1
        
        for i in range(n):
            area[m-1][i] = 1  
            # print(m-1," ", i)
       
        print(area)

        for i in range(m):
            area[i][n-1] = 1

        print(area)

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                area[i][j] += area[i+1][j] + area[i][j+1]

        print(area)
        
        return area[0][0]


