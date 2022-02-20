#!/usr/bin/python3
from multiprocessing import parent_process
from sre_parse import State
import numpy as np
import os
import sys
# sys.setrecursionlimit(2000)
class Node :
    def __init__(self):
        self.index = None
        self.parent = None
        self.state = None


def print_state(state):
    print(state.T.ravel())

def check_visited(state):
    visited=False
    for temp in visited_states:
        if(state.state==temp.state).all():
            visited=True
    return visited

def copy_node (node):
    copy = Node()
    copy.index = node.index
    copy.parent = node.parent
    copy.state = node.state.copy()
    return copy

def move_state(curr_state,direction):
    # state=curr_state.copy()
    state=copy_node(curr_state)
    zero_pos=np.argwhere(state.state==0)
    
    zero_pos=zero_pos[0]

    shiftY, shiftX = moveBindings[direction]

    new_zero_pos = np.array([zero_pos[0]+shiftY,zero_pos[1]+shiftX])

    # Check if movement is possible
    if(new_zero_pos[0] >= 0 and new_zero_pos[0]<3 and new_zero_pos[1] >= 0 and new_zero_pos[1]<3):
        # print("Swapping :",state[zero_pos[0],zero_pos[1]]," and ", state[new_zero_pos[0],new_zero_pos[1]])

        init_val=state.state[zero_pos[0],zero_pos[1]]
        swap_val=state.state[new_zero_pos[0],new_zero_pos[1]]
        state.state[zero_pos[0],zero_pos[1]] = swap_val
        state.state[new_zero_pos[0],new_zero_pos[1]] = init_val
        # print("original passed:\n",curr_state.state)
        # print("modified:\n",state.state)

        state.index=visited_states[-1].index + 1
        state.parent=curr_state.index

        if not check_visited(state):

            # visited_states.append(state)
            # curr_state = state
            
            return True, state
        else:
            # print("Already visited this one!")
            return False, curr_state
    
    else:
        # print("Cannot move in this direction ")
        return False, curr_state


# def add_to_visited_list(state=current_state,parent=parent_state):
#     visited_states.append(state)
path = []
def generate_path(end_state):
    

    while(end_state.parent!=None):
        path.append(end_state)
        end_state = copy_node(end_state)

        parent_index = end_state.parent
        found_node=Node()

        # which element in visited has parent as parent_index
        for node in visited_states:
            if(node.index==parent_index):
                found_node=copy_node(node)
                break
        end_state = found_node
    

def ActionMoveLeft(state):
    retval,new_state = move_state(state , 'l')
    return retval, new_state

def ActionMoveUp(state):
    retval,new_state = move_state(state , 'u')
    return retval, new_state

def ActionMoveRight(state):
    retval,new_state = move_state(state , 'r')
    return retval, new_state

def ActionMoveDown(state):
    retval,new_state = move_state(state , 'd')
    return retval, new_state

def bfs (state):
    open = False
    if (state.state==goal_state).all():
        print("REACHED GOAL!\n",state.state)
        visited_states.append(state)
        
        generate_path(state)
        return
    
    else:
        # Try and move left
        retval,new_state = ActionMoveLeft(state)
        if retval:
            visited_states.append(new_state)

            open_nodes.append(new_state)
            open = True
            
        if (new_state.state==goal_state).all():
            print("REACHED GOAL!\n",state.state)
            # visited_states.append(new_state)
            
            generate_path(new_state)
            return

        # try and move up
        retval,new_state = ActionMoveUp(state)
        if retval:
            visited_states.append(new_state)
            open_nodes.append(new_state)
            open = True

        if (new_state.state==goal_state).all():
            print("REACHED GOAL!\n",state.state)
            # visited_states.append(new_state)
            
            generate_path(new_state)
            
            return

        # try and move right
        retval,new_state = ActionMoveRight(state)
        if retval:
            visited_states.append(new_state)
            open_nodes.append(new_state)
            open = True

        if (new_state.state==goal_state).all():
            print("REACHED GOAL!\n",state.state)
            # visited_states.append(new_state)
            
            generate_path(new_state)

            return
            
        # try and move up
        retval,new_state = ActionMoveDown(state)
        if retval:
            visited_states.append(new_state)
            open_nodes.append(new_state)
            open = True

        if (new_state.state==goal_state).all():
            print("REACHED GOAL!\n",state.state)
          
            generate_path(new_state)

            return

        if(not open):
            open_nodes.pop(0)
        bfs(open_nodes[0])
        

def write_all_nodes(filename):
    file=open(filename,'w')
    for node in visited_states:
        file.write(str(node.state.ravel()) + '\n')

def write_all_nodes_info(filename):
    file=open(filename,'w')
    for node in visited_states:
        file.write(str(node.index) + "   " + str(node.parent)+ '\n')

def write_all_nodes_path(filename):
    file=open(filename,'w')
    for node in path:
        file.write(str(node.state.ravel())[1:-1] + '\n')

# ------ Global variables used --------------------
visited_states= []
open_nodes = []
moveBindings={'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
goal_state=np.array([[1,4,7],[2,5,8],[3,6,0]])
# -------------------------------------------------

if __name__=="__main__":
    current_state = Node()
    current_state.parent = None
    current_state.index = 0
    # test case 1:
    # current_state.state=np.array([[1,4,7],[5,0,8],[2,3,6]])
    # test case 2:
    current_state.state=np.array([[4,7,0],[1,2,8],[3,5,6]])

    visited_states.append(current_state)
    open_nodes.append(current_state)

    bfs(current_state)
    
    path.append(current_state)
    path.reverse()

    print("Path is:")
    for node in path:
        print(node.state)

    Nodesfile = './Nodes.txt'
    NodesInfofile = './NodesInfo.txt'

    NodesPath = './nodePath.txt'


    write_all_nodes(Nodesfile)
    write_all_nodes_info(NodesInfofile)

    write_all_nodes_path(NodesPath)




