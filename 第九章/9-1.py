#Dijkstra算法 最短路径问题
from collections import defaultdict
import sys

class Graph:									#Graph类

	def __init__(self):
		self.nodes = set()							#结点集合
		self.edges = defaultdict(list)					#边集合的字典
		self.distances = {}							#边的距离的集合
	
	def add_node(self, value):							#添加结点
		self.nodes.add(value)
	
	def add_edge(self, from_node, to_node, distance):		#添加边
		self.edges[from_node].append(to_node)
		self.distances[(from_node, to_node)] = distance

class Node:										#结点类

	def __init__(self, name):
		self.distance = sys.maxsize						#距离值
		self.predecessor = None						#前任结点
		self.name = name							#名称
	
	def set_distance(self, dist):						#设距离值
		self.distance = dist
	
	def set_predecessor(self, pred):					#设前任结点
		self.predecessor = pred
	
	def get_distance(self):							#得到距离值
		return self.distance
	
	def get_predecessor(self):							#得到前任结点
		return self.predecessor

def dijsktra(graph, initial, end):

	permanent = set()							#永久集合
	temporary = set()								#临时集合
	temporary.add(initial)					#起点加入临时集合
	initial.set_distance(0)					#设起点距离值为0
	
	while temporary : 						#只要临时集合不为空
		min_node = None

		for node in temporary:				#找临时集合中距离值最少的结点
			if min_node is None:
				min_node = node
			elif node.get_distance() < min_node.get_distance():
				min_node = node
		temporary.remove(min_node)			#把该结点从临时集合移除
		permanent.add(min_node)			#加结点到永久集合
		current_distance = min_node.get_distance()
		for neighbour in graph.edges[min_node]:		#遍历相邻结点
			new_distance = current_distance + graph.distances[(min_node, neighbour)]
			if neighbour not in permanent and new_distance < neighbour.get_distance():
				neighbour.set_distance(new_distance)		#更新
				neighbour.set_predecessor(min_node)
				temporary.add(neighbour)
def printPath(self,end):			#输出路线方法
	current = end
	path = [end.name]					#路线结点集合
	while current.predecessor != None:			#只要当前结点有前任结点
		path.append(current.predecessor.name)		#把前任结点加入集合
		current = current.predecessor		#更新当前结点
	path.reverse()						#翻转集合
	print (path)							#输出集合


g = Graph()

a=Node('A')
b=Node('B')
c=Node('C')
d=Node('D')
e=Node('E')
f=Node('F')

g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_node(d)
g.add_node(e)
g.add_node(f)
g.add_edge(a,b,10)
g.add_edge(a,c,15)
g.add_edge(a,e,30)
g.add_edge(b,d,5)
g.add_edge(b,e,14)
g.add_edge(c,d,12)
g.add_edge(c,e,12)
g.add_edge(d,f,10)
g.add_edge(e,f,20)

dijsktra(g,a,f)
printPath(g,f)

