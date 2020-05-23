def getdp2(arr):
   """
	:param arr:输入序列
	:return:计算结果,最长子序列长度，列表
   """
   n = len(arr)
   dp, ends = [0] * n, [0] * n
   ends[0], dp[0] = arr[0], 1
   right, l, r, m = 0, 0, 0, 0
   for i in range(1, n):
       l = 0
       r = right
       # 二分查找,若找不到则ends[l或r]是比arr[i]大而又最接近其的数
       # 若arr[i]比ends有效区的值都大，则l=right+1
       while l <= r:
           m = (l + r) // 2
           if arr[i] > ends[m]:
               l = m + 1
           else:
               r = m - 1
       right = max(right, l)
       ends[l] = arr[i]
       dp[i] = l + 1
   return dp

def generateLIS(arr, dp):
   """
	 :param arr:输入序列
	 :dp:最长子序列长度，列表
	 :return:最长子序列

   """
   n = max(dp)
   index = dp.index(n)
   lis = [0] * n
   n -= 1
   lis[n] = arr[index]
   # 从右向左
   for i in range(index, 0 - 1, -1):
       # 关键
       if arr[i] < arr[index] and dp[i] == dp[index] - 1:
           n -= 1
           lis[n] = arr[i]
           index = i
   return lis

arr = [6,7,8,9,10,11,12,1,2,3,4,5,6]
dp = getdp2(arr)
print( generateLIS(arr, dp))