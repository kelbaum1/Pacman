import sys

# Graph data stucture          {node: [{node : cost} , ...], ...}
#
def CreateGraph(nodeFileName, edgeFileName, heuristicsFileName):
	nodesFile = open(nodeFileName, 'r')
	nodes = nodesFile.readlines()
	nodesFile.close()

	graph = {}
	for nod in nodes:
		graph[nod[0]] = {}

	edgeFile = open(edgeFileName, 'r')
	edges = edgeFile.readlines()
	edgeFile.close()
	for edge in edges:
		edge = edge.strip()
		start = edge[0]
		end = edge[2]
		cost = int(edge[4:])
		if not start in graph:
			graph[start] = {}
		graph[start][end] = cost

	heuristics = {}
	heurFile = open(heuristicsFileName, 'r')
	heurlines = heurFile.readlines();

	for val in heurlines:
		node = val[0]
		h = int(val[2:])
		heuristics[node] = h
	return graph, heuristics


def BreadthFirst(graph, start, end, outputName):
	#dirst in first ou

	#list of objects to look at next 
	# {node : A, cost:#, parent:index into visted} append     pop off the end 
	searchList = []

	#nodes visted but may need to update cost
	# {node : A, cost:#, parent:C} 
	visited = []
	visitLetters = []

	searchList.append({'node': start, 'cost':0, 'parent':-1})
	#main loop
	foundGoal = False
	while not foundGoal and len(searchList) > 0:
		node = searchList[0]
		del searchList[0]
		
		#next nodes
		newNodes = graph[node['node']]
		letters = list(newNodes.keys())
		letters.sort()
		for newNode in letters:
			viewing = {}
			viewing['node'] = newNode
			viewing['cost'] = node['cost'] + newNodes[newNode]
			viewing['parent'] = len(visited)

			# if already been just update cost and parent
			if newNode in visitLetters :
				if visited[visitLetters.index(newNode)]['cost'] > viewing['cost']:
					visited[visitLetters.index(newNode)]['cost'] = viewing['cost']
					visited[visitLetters.index(newNode)]['parent'] > viewing['parent']
			else:
				#create new node
				searchList.append(viewing)
		visitLetters.append(node['node'])
		visited.append(node)

		if node['node'] == end:
			foundGoal = True

	node = visited[-1]
	parent = 0
	path = ''
	while  parent >= 0:
		parent = node['parent']
		path = node['node'] + path
		node = visited[parent]

	cost = visited[-1]['cost']
	writePath(path, cost, outputName)

def writePath(path, cost, outputName):
	output = open(outputName, 'w');
	for node in path:
		output.write(node + '\n')
	if cost != None:
		output.write(str(cost))
	output.close()

def DepthFirst(graph, start, end, outputName):

	#list of objects to look at next 
	# {node : A, cost:#, parent:index into visted} append     pop off the front
	searchList = []

	#nodes visted but may need to update cost
	# {node : A, cost:#, parent:C} 
	visited = []
	visitLetters = []

	searchList.append({'node': start, 'cost':0, 'parent':-1})
	#main loop
	foundGoal = False
	while not foundGoal and len(searchList) > 0:
		node = searchList[-1]
		del searchList[-1]
		
		#next nodes
		newNodes = graph[node['node']]
		letters = list(newNodes.keys())
		letters.sort()
		letters.reverse()
		for newNode in letters:
			viewing = {}
			viewing['node'] = newNode
			viewing['cost'] = node['cost'] + newNodes[newNode]
			viewing['parent'] = len(visited)

			# if already been just update cost and parent
			if newNode in visitLetters :
				if visited[visitLetters.index(newNode)]['cost'] > viewing['cost']:
					visited[visitLetters.index(newNode)]['cost'] = viewing['cost']
					visited[visitLetters.index(newNode)]['parent'] > viewing['parent']
			else:
				#create new node
				searchList.append(viewing)
		visitLetters.append(node['node'])
		visited.append(node)

		if node['node'] == end:
			foundGoal = True

	node = visited[-1]
	parent = 0
	path = ''
	while  parent >= 0:
		parent = node['parent']
		path = node['node'] + path
		node = visited[parent]
	cost = visited[-1]['cost']
	writePath(path, cost,outputName)

def UniformCost(graph, start, end, outputName):
	#list of objects to look at next 
	# {node : A, cost:#, parent:index into visted} append     pop off the front
	searchList = []

	#nodes visted but may need to update cost
	# {node : A, cost:#, parent:C} 
	visited = []
	visitLetters = []

	searchList.append({'node': start, 'cost':0, 'parent':-1})
	#main loop
	foundGoal = False
	while not foundGoal and len(searchList) > 0:
		#sort based on cost
		searchList = sorted(searchList, key = lambda k: k['cost'])
		node = searchList[0]
		del searchList[0]
		#next nodes
		newNodes = graph[node['node']]
		letters = list(newNodes.keys())
		letters.sort()
		letters.reverse()
		for newNode in letters:
			viewing = {}
			viewing['node'] = newNode
			viewing['cost'] = node['cost'] + newNodes[newNode]
			viewing['parent'] = len(visited)

			# if already been just update cost and parent
			searchList.append(viewing)
		visitLetters.append(node['node'])
		visited.append(node)

		if node['node'] == end:
			foundGoal = True

	node = visited[-1]
	parent = 0
	path = ''
	while  parent >= 0:
		parent = node['parent']
		path = node['node'] + path
		node = visited[parent]
	cost = visited[-1]['cost']
	writePath(path, cost,outputName)

def GreedyBestSearch(graph, heuristics, start, end, outputName):
	#list of objects to look at next 
	# {node : A, cost:#, parent:index into visted} append     pop off the front
	searchList = []

	#nodes visted but may need to update cost
	# {node : A, cost:#, parent:C} 
	visited = []
	visitLetters = []

	searchList.append({'node': start, 'cost':0, 'HofX':heuristics[start], 'parent':-1})
	#main loop
	foundGoal = False
	while not foundGoal and len(searchList) > 0:
		#sort based on cost
		searchList = sorted(searchList, key = lambda k: k['HofX'])
		node = searchList[0]
		del searchList[0]
		#next nodes
		newNodes = graph[node['node']]
		letters = list(newNodes.keys())
		letters.sort()
		letters.reverse()
		for newNode in letters:
			viewing = {}
			viewing['node'] = newNode
			viewing['cost'] = node['cost'] + newNodes[newNode]
			viewing['parent'] = len(visited)
			viewing['HofX'] = heuristics[newNode]
			searchList.append(viewing)
		visitLetters.append(node['node'])
		visited.append(node)

		if node['node'] == end:
			foundGoal = True

	node = visited[-1]
	parent = 0
	path = ''
	while  parent >= 0:
		parent = node['parent']
		path = node['node'] + path
		node = visited[parent]
	cost = visited[-1]['cost']
	writePath(path, cost,outputName)

def aStar(graph, heuristics, start, end, outputName):
	#list of objects to look at next 
	# {node : A, cost:#, parent:index into visted} append     pop off the front
	searchList = []

	#nodes visted but may need to update cost
	# {node : A, cost:#, parent:C} 
	visited = []
	visitLetters = []

	searchList.append({'node': start, 'cost':0, 'HofX':heuristics[start], 'parent':-1})
	#main loop
	foundGoal = False
	while not foundGoal and len(searchList) > 0:
		#sort based on cost
		searchList = sorted(searchList, key = lambda k: k['HofX'])
		node = searchList[0]
		del searchList[0]
		#next nodes
		newNodes = graph[node['node']]
		letters = list(newNodes.keys())
		letters.sort()
		letters.reverse()
		for newNode in letters:
			viewing = {}
			viewing['node'] = newNode
			viewing['cost'] = node['cost'] + newNodes[newNode]
			viewing['parent'] = len(visited)
			viewing['HofX'] = heuristics[newNode] + viewing['cost']
			searchList.append(viewing)
		visitLetters.append(node['node'])
		visited.append(node)

		if node['node'] == end:
			foundGoal = True

	node = visited[-1]
	parent = 0
	path = ''
	while  parent >= 0:
		parent = node['parent']
		path = node['node'] + path
		node = visited[parent]
	cost = visited[-1]['cost']
	writePath(path, cost,outputName)
def main():
	
	if len(sys.argv) != 8:
		print("Oops! Incorrect syntax..Lets try it again\npython search.py <algorithm_name> <node_file> <edge_file> <heuristics_file> <start_node> <end_node> <output_file>")
		exit(0)

	algorythm = sys.argv[1]
	nodef = sys.argv[2]
	edgef = sys.argv[3]
	heuristicf = sys.argv[4]
	start = sys.argv[5]
	end = sys.argv[6]
	outf = sys.argv[7]

	graph, heuristics = CreateGraph(nodef, edgef, heuristicf)
	
	if algorythm == 'breadth':
		BreadthFirst(graph, start, end, outf)
	elif algorythm =='depth':
		DepthFirst(graph, start, end, outf)
	elif algorythm == 'uniform':
		UniformCost(graph, start, end, outf)
	elif algorythm == 'greedy':
		GreedyBestSearch(graph, heuristics, start, end, outf)
	elif algorythm =='astar':
		aStar(graph, heuristics, start, end, outf)
main()