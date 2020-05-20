#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[81]:


Node_State_i = [0, 0]
Node_Index_i = []
Parent_Node_Index_i = []
Initial_Node = []
Goal_Node = [[1,2,3],[4,5,6],[7,8,0]]   # Goal Node defined 
Queue = []                              # Used to store the nodes which are yet to be explored
Virtual_Node = []                       # Used to store the nodes that already have been visited
A = []                                  # Used to store the 1st node in Queue and then to find the all the other posible nodes
Xp = []                                 # Used to store all the new nodes after moving the blank tile
Incoming_Node = []


# In[82]:


# Taking input from user to create a 3D matrix
def InputNode():
    print("Enter Values in Row 1")
    a = [int(x) for x in input().split()]
    print("Enter Values in Row 2")
    b = [int(x) for x in input().split()]
    print("Enter Values in Row 3")
    c = [int(x) for x in input().split()]   
    return [a,b,c]

Initial_Node = InputNode()


# In[163]:


def BlankTileLocation(CurrentNode):
#  This function is used to find the x and y coordinates of the blank tile 
#  assuming the left top corner of the box, to be origin (0,0)
    for i in range(len(CurrentNode)):
        for j in range (len(CurrentNode)):
            if(CurrentNode[i][j] == 0):
                print ("The position of blank tile is", i , j)
                return [i, j]


# In[164]:


def ActionMoveLeft(CurrentNode, i, j):
# This function is used to add a node to the left side of the current node if possible
    NewNode = np.copy(CurrentNode)
    temp1 = NewNode[i,j]
    temp2 = NewNode[i,j-1]
    NewNode[i,j-1] = temp1
    NewNode[i,j] = temp2
    return NewNode


# In[165]:


def ActionMoveRight(CurrentNode, i, j):
# This function is used to add a node to the right side of the current node if possible
    NewNode = np.copy(CurrentNode)
    temp1 = NewNode[i,j]
    temp2 = NewNode[i,j+1]
    NewNode[i,j+1] = temp1
    NewNode[i,j] = temp2
    return NewNode


# In[166]:


def ActionMoveDown(CurrentNode, i, j):
# This function is used to add a node to the down side of the current node if possible
    NewNode = np.copy(CurrentNode)
    temp1 = NewNode[i,j]
    temp2 = NewNode[i+1,j]
    NewNode[i+1,j] = temp1
    NewNode[i,j] = temp2
    return NewNode


# In[167]:


def ActionMoveUp(CurrentNode, i, j):
# This function is used to add a node to the upper side of the current node if possible
    NewNode = np.copy(CurrentNode)
    temp1 = NewNode[i,j]
    temp2 = NewNode[i-1,j]
    NewNode[i-1,j] = temp1
    NewNode[i,j] = temp2
    return NewNode


# In[168]:


# Function used to check directional movements of blank tile
def Check_Values(x,y):
    if(x == 0 and y == 0):
        return 1
    if(x == 0 and y == 1):
        return 2
    if(x == 0 and y == 2):
        return 3
    if(x == 1 and y == 0):
        return 4
    if(x == 1 and y == 1):
        return 5
    if(x == 1 and y == 2):
        return 6
    if(x == 2 and y == 0):
        return 7
    if(x == 2 and y == 1):
        return 8
    if(x == 2 and y == 2):
        return 9
    else:
        print("Entry not possible")


# In[169]:


# Function to move the the blank tile
def Shift(CurrentNode, Value, x, y):
    if(Value == 1):
        New_Node1 = ActionMoveDown(CurrentNode, x, y)
        New_Node2 = ActionMoveRight(CurrentNode, x, y)
        Incoming_Node.append(New_Node1)
        Incoming_Node.append(New_Node2)
        return Incoming_Node
    if(Value == 2):
        New_Node1 = ActionMoveRight(CurrentNode, x, y)
        New_Node2 = ActionMoveLeft(CurrentNode, x, y)
        New_Node3 = ActionMoveDown(CurrentNode, x, y)
        Incoming_Node.append(New_Node1)
        Incoming_Node.append(New_Node2)
        Incoming_Node.append(New_Node3)
        return Incoming_Node
    if(Value == 3):
        New_Node1 = ActionMoveDown(CurrentNode, x, y)
        New_Node2 = ActionMoveLeft(CurrentNode, x, y)
        Incoming_Node.append(New_Node1)
        Incoming_Node.append(New_Node2)
        return Incoming_Node
    if(Value == 4):
        New_Node1 = ActionMoveRight(CurrentNode, x, y)
        New_Node2 = ActionMoveUp(CurrentNode, x, y)
        New_Node3 = ActionMoveDown(CurrentNode, x, y)
        Incoming_Node.append(New_Node1)
        Incoming_Node.append(New_Node2)
        Incoming_Node.append(New_Node3)
        return Incoming_Node
    if(Value == 5):
        New_Node1 = ActionMoveRight(CurrentNode, x, y)
        New_Node2 = ActionMoveUp(CurrentNode, x, y)
        New_Node3 = ActionMoveDown(CurrentNode, x, y)
        New_Node4 = ActionMoveLeft(CurrentNode, x, y)
        Incoming_Node.append(New_Node1)
        Incoming_Node.append(New_Node2)
        Incoming_Node.append(New_Node3)
        Incoming_Node.append(New_Node4)
        return Incoming_Node
    if(Value == 6):
        New_Node1 = ActionMoveLeft(CurrentNode, x, y)
        New_Node2 = ActionMoveUp(CurrentNode, x, y)
        New_Node3 = ActionMoveDown(CurrentNode, x, y)
        Incoming_Node.append(New_Node1)
        Incoming_Node.append(New_Node2)
        Incoming_Node.append(New_Node3)
        return Incoming_Node
    if(Value == 7):
        New_Node1 = ActionMoveRight(CurrentNode, x, y)
        New_Node2 = ActionMoveUp(CurrentNode, x, y)
        Incoming_Node.append(New_Node1)
        Incoming_Node.append(New_Node2)
        return Incoming_Node
    if(Value == 8):
        New_Node1 = ActionMoveRight(CurrentNode, x, y)
        New_Node2 = ActionMoveUp(CurrentNode, x, y)
        New_Node3 = ActionMoveLeft(CurrentNode, x, y)
        Incoming_Node.append(New_Node1)
        Incoming_Node.append(New_Node2)
        Incoming_Node.append(New_Node3)
        return Incoming_Node
    if(Value == 9):
        New_Node1 = ActionMoveLeft(CurrentNode, x, y)
        New_Node2 = ActionMoveUp(CurrentNode, x, y)
        Incoming_Node.append(New_Node1)
        Incoming_Node.append(New_Node2)
        return Incoming_Node
    else:
        print("Error")


# In[170]:


# Function to copmare the goal node with the nodes
def CompareNodes1(node1, node2):
    A = np.copy(node1)
    B = np.copy(node2)
    X = ""
    Y = ""
    X = str(A[0][0])+str(A[0][1])+str(A[0][2])+str(A[1][0])+str(A[1][1])+str(A[1][2])+str(A[2][0])+str(A[2][1])+str(A[2][2])
    Y = str(B[0][0])+str(B[0][1])+str(B[0][2])+str(B[1][0])+str(B[1][1])+str(B[1][2])+str(B[2][0])+str(B[2][1])+str(B[2][2])
    if (X == Y):
        return 1
    else:
        return 0


# In[171]:


# Function used to compare the Xprime with visited nodes
def CompareNodes2(node1, node2):
    flag = 0
    for i in range(len(node1)):
        for j in range(len(node2)):
            if(node1[i][j]==node2[i][j]):
                flag = 0
            else:
                flag = 1
                break
        if(flag==1):
            break
    return flag


# In[183]:


Queue.append(Initial_Node)                            
BackTracking = []
while(Queue!=[]):                             
    A = np.copy(Queue.pop(0))                       # Poping the initial node in Queue and storing in node A
    verify = False
    verify = CompareNodes1(A, Goal_Node)            # verifying if A is the goal state
    if verify == True :
        print("Match as goal node [1,2,3],[4,5,6],[7,8,0]")
        Solution = A
        break
    x, y = BlankTileLocation(A)
    value = Check_Values(x, y)
    print(value)
    Xp = Shift(A, value, x, y)
    for k in range(len(Xp)):
        B = []
        B.append(Xp[k])
        B.append(A)
        BackTracking.append(B)                              # storage of parent and child in Back_tracking
    for i in range(len(Xp)):
        y = 1
        for j in range(len(Virtual_Node)):
            y = CompareNodes2(Xp[i], Virtual_Node[j])       #verifying the exploration of new node
            if(y == 0):
                print("New value of X'")
                break

        if(y == 1):
            Virtual_Node.append(Xp[i])                      # In case the new node hasn't been explored storage is Virtual_Node
            Queue.append(Xp[i])                             # Storing the unexplored node in Queue
    del Xp[:]                                               # Emptying the Xp


# In[176]:


# Copying the explored nodes to a text document
f = open("Nodes.txt",'w')
for i in range(len(Virtual_Node)):
    for j in range(len(Virtual_Node[i])):
        Element1 = Virtual_Node[i][0][0]
        Element2 = Virtual_Node[i][0][1]
        Element3 = Virtual_Node[i][0][2]
        print(Element1,Element2,Element3)
        Element4 = Virtual_Node[i][1][0]
        Element5 = Virtual_Node[i][1][1]
        Element6 = Virtual_Node[i][1][2]
        print(Element4,Element5,Element6)
        Element7 = Virtual_Node[i][2][0]
        Element8 = Virtual_Node[i][2][1]
        Element9 = Virtual_Node[i][2][2]
        print(Element7,Element8,Element9)
        print(Virtual_Node[i])
        f.write("\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n "  %(Element1,Element2,Element3,Element4,Element5,Element6,Element7,Element8,Element9))
f.close()
print(Virtual_Node)


# In[177]:


# Funtion to print node path
def Print_Matrix(Element_State):
    print("-------------")
    print("|", end=" ")
    print(int(Element_State[0]), "|", int(Element_State[1]), "|", int(Element_State[2]), "|")
    print("-------------")
    print("|", end=" ")
    print(int(Element_State[3]), "|", int(Element_State[4]), "|", int(Element_State[5]), "|")
    print("-------------")
    print("|", end=" ")
    print(int(Element_State[6]), "|", int(Element_State[7]), "|", int(Element_State[8]), "|")
    print("-------------")


# In[189]:


# Code for backtracking
Back_Path = []
Back_Path.append(Solution)
for i in range(len(BackTracking)):
    L=0
    for j in range(len(BackTracking)):
        L = CompareNodes2(Back_Path[i],BackTracking[j][0])
        if(L == 0):
            Back_Path.append(BackTracking[j][1])
            break
    K = CompareNodes1(Initial_Node,BackTracking[j][1])       # Verifying if initial node has been acheived or not
    if(K == True):
        break

Node_Path = []                                 
for i in reversed(Back_Path):
    Node_Path.append(i)                         


# In[192]:


Node_Path = []                                     # creating a list to store the path
for i in reversed(Back_Path):
    Node_Path.append(i)                            # saving the path into the list

# Copying the node path to a text document
f = open("Nodepath.txt",'w')
for i in range(len(Node_Path)):
    Element1 = Node_Path[i][0][0]
    Element2 = Node_Path[i][0][1]
    Element3 = Node_Path[i][0][2]
    Element4 = Node_Path[i][1][0]
    Element5 = Node_Path[i][1][1]
    Element6 = Node_Path[i][1][2]
    Element7 = Node_Path[i][2][0]
    Element8 = Node_Path[i][2][1]
    Element9 = Node_Path[i][2][2]
    f.write("\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n "  %(Element1,Element2,Element3,Element4,Element5,Element6,Element7,Element8,Element9))
f.close()

# Display the node path
fname = 'Nodepath.txt'
data = np.loadtxt(fname)
if len(data[1]) is not 9:
    print("Text format is not correct, retry ")
else:
    for i in range(0, len(data)):
        if i == 0:
            print("Start Node")
        elif i == len(data)-1:
            print("Reached the Goal Node")
        else:
            print("Step ",i)
        Print_Matrix(data[i])
        print()
        print()


# In[197]:


#for creating NodesInfo text file
fnodeinfo = open('NodesInfo.txt', 'w')
for element in Incoming_Node:
        for i in range(0, 2):
            fnodeinfo.write(str(element[i]) + " ")
        fnodeinfo.write('\n')                              

fnodeinfo.close()



