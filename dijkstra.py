#----------------------------------------------------------------------
# Implementation of the Dijkstra's Algorithm
# This program requires no libraries like pandas, numpy...
# and the graph DataStructure is a dictionary of dictionaries
#
# Created by [HakimZiani - zianianakim@gmail.com]
#----------------------------------------------------------------------


# the key in the graph dic is the node and the value is its neighbors
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
# Initialize the Start and End node
StartNode  = input("Enter Start Node : ")
EndNode = input("Enter End Node : ")
# initList function for crating the queues of unvesited nodes
# and data
# The Structure is : {'node':[Distance,'prev-node']}
def initList(graph,StartNode,EndNOde):
    d={}
    for x in graph.keys():
        if x == StartNode:
            d[x] = [0,'']
        else: 
            d[x] =[99999,''] 
    return d
# getMinimalValue function to return the label of the node that 
# has the minimal value  
def getMinimalValue(d):
    min = 999999
    a = 'ERROR' # to see if the value don't change
    for x,y in d.items():
        if y[0] < min:
            a = x
            min = y[0]
    return a

d= initList(graph,StartNode,EndNode)
unvisited = initList(graph,StartNode,EndNode)
while(True):
    #get the node to work with    
    focus = getMinimalValue(unvisited)
    # Break if it's the destination 
    if focus == EndNode:
        break
    # Setting the Data queue 
    for x,y in graph[focus].items():
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
# d now contains the final data queue we need
# All we have to do is getting the right path from the EndNode
# to the StartNode using the prev states stored in d 
while (node != StartNode):
    road.append(node)
    node = d[node][1]
road.append(StartNode)    
# Showing the result 
print("The shortest road is : "+"-->".join(reversed(road)))
