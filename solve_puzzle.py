#!/usr/bin/python3
from multiprocessing import parent_process
from sre_parse import State
import numpy as np
import os
import sys
sys.setrecursionlimit(2000)
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


        if not check_visited(state):

            visited_states.append(state)
            # curr_state = state
            
            return True, state
        else:
            print("Already visited this one!")
            return False, curr_state
    
    else:
        print("Cannot move in this direction ")
        return False, curr_state

rec=0
def bfs (state):
    global rec
    rec+=1
    print("recursion count: ",rec)
    print("recursive call here with state:")
    print(state.state)
    open = False
    if (state.state==goal_state).all():
        print("REACHED GOAL!\n",state.state)
        return
    
    else:
        # Try and move left
        retval,new_state = move_state(state , 'l')
        if retval:
            visited_states.append(new_state)
            open_nodes.append(new_state)
            open = True
            print()

        # try and move up
        retval,new_state = move_state(state , 'u')
        if retval:
            visited_states.append(new_state)
            open_nodes.append(new_state)
            open = True

        # try and move right
        retval,new_state = move_state(state , 'r')
        if retval:
            visited_states.append(new_state)
            open_nodes.append(new_state)
            open = True
            

        # try and move up
        retval,new_state = move_state(state , 'd')
        if retval:
            visited_states.append(new_state)
            open_nodes.append(new_state)
            open = True

        if(not open):
            open_nodes.pop(0)
        # print(len(open_nodes))
        bfs(open_nodes[0])



# Format of states stored: {node_index: n(int), parent_index: p(int), node_state: state(np.ndarray)}
visited_states= []
open_nodes = []
moveBindings={'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
node_count = 0 # count of nodes in visited, is used for indexing nodes
explore_order = ['l','u','r','d']
goal_state=np.array([[1,4,7],[2,5,8],[3,6,0]])

if __name__=="__main__":
    current_state = Node()
    current_state.parent = 0
    current_state.index = 0
    # current_state.state=np.array([[1,4,6],[2,3,0],[8,7,5]])
    # test case 1:
    # current_state.state=np.array([[1,4,7],[5,0,8],[2,3,6]])
    # test case 2:
    current_state.state=np.array([[4,7,0],[1,2,8],[3,5,6]])


    
    visited_states.append(current_state)
    open_nodes.append(current_state)

    # print("initial state:\n",current_state.state)
    # retval,current_state=move_state(current_state,'l')
    
    # print("before second move:\n",current_state.state)
    # retval,current_state=move_state(current_state,'r')

    # print("before third move:\n",current_state.state)
    # retval,current_state=move_state(current_state,'u')

    # print("before fourth move:\n",current_state.state)
    # retval,current_state=move_state(current_state,'r')

    # print("before fifth move:\n",current_state.state)
    # retval,current_state=move_state(current_state,'d')
    
    # print("before sixth move:\n",current_state.state)
    bfs(current_state)

