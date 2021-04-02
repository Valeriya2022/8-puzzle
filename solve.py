import sys
import copy
import collections
import time


goalState=[[1,2,3],[8,0,4],[7,6,5]]
dfsGoalstate= [1,2,3,8,0,4,7,6,5]
startState=[]

class dfsNode:

    def __init__(self,state,parent,movement,depth):
        self.state = state
        self.parent = parent
        self.movement = movement
        self.depth = depth
#Node Structure for all algorithms other than dfs
class Node:
    def __init__(self,starts=None,d=None,path=None,move=None,h=None):
        self.state=starts
        self.depth=d
        self.curPath=path
        self.operation=move
        self.hValue=h


#generating and returning children of a state with moves in 4 directions
    def generatechildren(self,parent,visited,h=None,totalNodes=None):
        children=[]
        xpos,ypos=None, None
        for i in range(0,3):
            for j in range(0,3):
                if(parent.state[i][j]==0 ):
                    xpos=i
                    ypos=j
                    break
            if xpos is not None:
                break

        if xpos is not 2:  # move down
            tpath = copy.deepcopy(parent.curPath)
            tpath.append("DOWN")
            child = Node(copy.deepcopy(parent.state), parent.depth + 1, tpath, "DOWN",h)
            child.state[xpos + 1][ypos], child.state[xpos][ypos] = child.state[xpos][ypos], child.state[xpos + 1][ypos]
            if (self.toString(child.state) not in visited):
                children.append(child)
                totalNodes+=1

        if ypos is not 0 : #move left
            tpath=copy.deepcopy(parent.curPath)
            tpath.append("LEFT")
            child=Node(copy.deepcopy(parent.state),parent.depth+1,tpath,"LEFT",h)
            child.state[xpos][ypos-1],child.state[xpos][ypos]=child.state[xpos][ypos],child.state[xpos][ypos-1]
            if (self.toString(child.state) not in visited):
                children.append(child)
                totalNodes+=1

        if ypos is not 2:  # move right
            tpath = copy.deepcopy(parent.curPath)
            tpath.append("RIGHT")
            child = Node(copy.deepcopy(parent.state), parent.depth + 1,tpath, "RIGHT",h)
            child.state[xpos][ypos+1], child.state[xpos][ ypos] = child.state[xpos][ypos], child.state[xpos][ypos+1]
            if (self.toString(child.state) not in visited):
                children.append(child)
                totalNodes+=1

        if xpos is not 0:  # move top
            tpath = copy.deepcopy(parent.curPath)
            tpath.append("UP")
            child = Node(copy.deepcopy(parent.state), parent.depth + 1,tpath, "TOP",h)
            child.state[xpos-1][ypos], child.state[xpos][ ypos] = child.state[xpos][ypos], child.state[xpos-1][ypos]
            if (self.toString(child.state) not in visited):
                children.append(child)
                totalNodes+=1

        return children,totalNodes


    def toString(self,tempState):
        s=''
        for i in tempState:
            for j in i:
                s+=str(j)
        return s

    #BFS
    def bfs(self):
        timeFlag=0
        maxListSize=float("inf")
        totalNodes=0
        start_time = time.time()
        q = collections.deque()
        visited = set()
        startNode = Node(startState, 1, [])
        q.append(startNode)
        flag = 0
        while (q):
            if len(q)>maxListSize:
                maxListSize=len(q)
            temp_time = time.time()
            if (temp_time - start_time >= 30):
                timeFlag = 1
                break
            currentNode = q.popleft()
            stateString = self.toString(currentNode.state)
            visited.add(stateString)
            #print len(visited)
            if (currentNode.state == goalState):
                print ("Moves="+str(len(currentNode.curPath)))
                print (currentNode.curPath)
                flag = 1
                print ('')
                print ("Total Nodes Visited="+str(totalNodes))
                print ("BFS Time"+ str(time.time()-start_time))
                print ("Max List Size="+str(maxListSize))

            if flag is 1:
                break
            tchilds,totalNodes=self.generatechildren(currentNode, visited, None,totalNodes)
            q.extend(tchilds)# Adding the expanded chidrens to the list
        if timeFlag is 1:
            print ("Total Nodes Visited=" + str(totalNodes))
            print ("BFS terminated due to TimeOut")



    

def mainfunction():

    print ("Please input the  Start state in the form '(1 2 3 4 5 6 7 8 0)")
    inStartState=(input())
    inStartState=inStartState.replace('(',' ( ')
    inStartState = inStartState.replace(')', ' ) ')
    for i in range(0,len(inStartState)):
        if inStartState[i] is '(':
            start=i+1
        elif inStartState[i]==')':
            end=i
    inStartState=inStartState[start:end]
    inStartState=inStartState.split()
    inStartState= [int(i) for i in inStartState]
    k=0
    for i in range(0,3):
        temp=[]
        for j in range(0,3):

            temp.append(inStartState[k])
            k+=1
        startState.append(temp)

    obj = Node()
    obj.bfs()


if __name__ == "__main__":
    mainfunction()
