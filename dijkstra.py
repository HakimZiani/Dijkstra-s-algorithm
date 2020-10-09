
graph = {'A':{'B':1,'D':7},
'B':{'A':1,'C':3,'E':1},
'C':{'B':3,'D':2,'E':8},
'D':{'A':7,'C':2,'E':1},
'E':{'D':1,'E':8,'B':1},
        }
def printGraph(graph):
    for x , y in graph.items():
        print(x + " in relation with : " + str(y))
printGraph(graph)
StartNode  = input("Enter Start Node : ")
EndNode = input("Enter End Node : ")

def getMinimalValue(d):
    min = 999999
    a = 'ERROR' # to view if the value don't change
    for x,y in d.items():
        if y[0] < min:
            a = x
            min = y[0]
    return a

# d = {'A':[0,''],'B':[9999,''],'C':[9999,''],'D':[9999,''],'E':[9999,''],'F':[9999,''],'G':[9999,'']
# ,'H':[9999,''],'I':[9999,'']}
def initList(graph,StartNode,EndNOde):
    d={}
    for x in graph.keys():
        if x == StartNode:
            d[x] = [0,'']
        else: 
            d[x] =[99999,''] 
    return d

d= initList(graph,StartNode,EndNode)
unvisited = initList(graph,StartNode,EndNode)
#d = {'A':[9999,''],'B':[9999,''],'C':[0,''],'D':[9999,''],'E':[9999,'']}
# unvisited =  {'A':[9999,''],'B':[9999,''],'C':[0,''],'D':[9999,''],'E':[9999,''],'F':[9999,''],'G':[9999,'']
# ,'H':[9999,''],'I':[9999,'']}

while(True):
    
    focus = getMinimalValue(unvisited)
    if focus == EndNode:
        break
    for x,y in graph[focus].items():
        #x = B and y = 1
        #x = C and y = 4
        if d[x][0] > d[focus][0]+y:
            d[x][0] = d[focus][0]+y
            d[x][1] = focus
            try:
                unvisited[x][0] = unvisited[focus][0]+y
                unvisited[x][1] = focus
            except:
                pass 
    del unvisited[focus]
road = []
node= EndNode
while (node != StartNode):
    road.append(node)
    node = d[node][1]
road.append(StartNode)    

print("The shortest road is : "+"-->".join(reversed(road)))