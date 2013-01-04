import alphabet

Nodes = []


class Node(object):
	
	def __init__(self, name, num):
		self.name = name
		self.higher_nodes = []
		self.lower_nodes = []
		if(num == 1):
			self.tentative = 0
		else:
			self.tentative = 1000
		self.distances = {}
		self.num_lower = 0
		self.num_higher = 0
		
		
	def add(self, node, dis):
		self.higher_nodes.append(node)
		node.lower_nodes.append(self)
		self.distances[node.name] = dis
		node.num_lower += 1
		self.num_higher += 1

		
	
		
	def ShortestPath(self):
		for i in range(len(self.higher_nodes)):
			node = self.higher_nodes[i]
			d = self.distances[node.name]
			if(self.tentative + d < node.tentative):
				node.tentative = self.tentative + d
			node.ShortestPath()
				
	
	def mark(self,node):
		self.higher_nodes[node] = self.d, True
		
f = open('/users/ethan/python/MarkOfAWizard/input.txt','r')
line = int(f.readline().rstrip())

while(line != 0):
	marks = 0
	for l in range(1,line+1):
		letter = alphabet.letter(l).replace('\'','')
		letter = Node(alphabet.letter(l),l)
		Nodes.append(letter)
	for i in range(line):
		line2 = f.readline().rstrip()
		nodes = line2.split()
		for j in range(2,len(nodes),2):
			for k in range(len(Nodes)):
				if(Nodes[k].name == nodes[j]):
					Nodes[i].add(Nodes[k], int(nodes[j+1]))
	Nodes[0].ShortestPath()
	for i in range(len(Nodes)):
		if((i > 0 and i < len(Nodes)-1) and (len(Nodes[i].lower_nodes) == 0 or len(Nodes[i].higher_nodes) == 0)):
			continue
		remove = []
		for j in range(len(Nodes[i].higher_nodes)):
			if(Nodes[i].tentative + Nodes[i].distances[Nodes[i].higher_nodes[j].name] > Nodes[i].higher_nodes[j].tentative):
				remove.append(Nodes[i].higher_nodes[j])
				print Nodes[i].name + ' : ' + Nodes[i].higher_nodes[j].name
		for r in range(len(remove)):
			remove[r].lower_nodes.remove(Nodes[i])
			Nodes[i].higher_nodes.remove(remove[r])
	for i in range(len(Nodes)):
		if(Nodes[i].num_higher > len(Nodes[i].higher_nodes)):
			for q in range(len(Nodes[i].higher_nodes)):
				marks += 1
			
			
		
				
				
	print Nodes[len(Nodes)-1].tentative, marks
	Nodes = []
	line = int(f.readline().rstrip())
