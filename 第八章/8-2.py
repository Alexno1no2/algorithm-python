#w个矿工挖n个金矿 g p分别为金矿价值和需要的矿工数
def goldMining(n, w, g, p):
	"""
	动态规划算法过程
	:param n:金矿个数
	:param w:旷工个数
	:param g:金矿价值，列表
	:param p:挖各个金矿需要的矿工 ，列表
	:return:不同的矿工个数对应的挖矿价值，列表
	"""
	results = []					#保存返回结果的数组
	preResults = []				#保存上一行结果的数组
	for i in range(0,w+1):			#填充边界格子的值，从左向右填充表格第一行的内容
		results.append(0)		#初始化结果数组,结果下标从1开始
		if  i < p[0]:
			preResults.append(0)	#若人数少于第一个金矿所需人数，黄金量为0
		else:
			preResults.append(g[0])	#若人数不少于第一个金矿所需人数，黄金量为g[0]

	for i in range(1,n):			#外层循环为金矿数量
		for j in range(1,w+1):		#外层循环为矿工数量
			if j < p[i]:
				results[j] = preResults[j]
			else:
				results[j] = max(preResults[j], preResults[j-p[i]] + g[i])
		preResults = results
	return results[1:]
n=4
w=10
g= [400,500, 200, 300]
p= [5 ,5 ,3, 4 ]
print( goldMining(n, w, g, p))