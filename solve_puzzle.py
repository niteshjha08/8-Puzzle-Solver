#!/usr/bin/python3
import numpy as np
import os

def print_state(state):
    print(state.T.ravel())

visited_states= []

# print(current_state[z])
def move_state(curr_state,direction):
    state=curr_state.copy()
    zero_pos=np.argwhere(state==0)
    zero_pos=zero_pos[0]
    shiftY, shiftX = moveBindings[direction]

    new_zero_pos = np.array([zero_pos[0]+shiftY,zero_pos[1]+shiftX])

    # Check if movement is possible
    if(new_zero_pos[0] >= 0 and new_zero_pos[0]<3 and new_zero_pos[1] >= 0 and new_zero_pos[1]<3):
        print("Swapping :",state[zero_pos[0],zero_pos[1]]," and ", state[new_zero_pos[0],new_zero_pos[1]])

        init_val=state[zero_pos[0],zero_pos[1]]
        swap_val=state[new_zero_pos[0],new_zero_pos[1]]
        state[zero_pos[0],zero_pos[1]] = swap_val
        state[new_zero_pos[0],new_zero_pos[1]] = init_val
        return True, state
    
    else:
        print("Cannot move in this direction")
        return False, state

my_list=[]
def check_visited(state):
    visited=False
    for temp in visited_states:
        if(state==temp).all():
            visited=True
    return visited

if __name__=="__main__":
    moveBindings={'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
    current_state=np.array([[1,4,6],[2,3,0],[8,7,5]])

    visited_states.append(current_state)
    # print(visited_states)
    retval,new_state=move_state(current_state,'l')
    print("initial state:\n",current_state)
    if(retval):
        if not check_visited(new_state):
            visited_states.append(new_state)
            current_state = new_state
    print("before second move:\n",current_state)

    retval,new_state=move_state(current_state,'r')
    if(retval):
        if not check_visited(new_state):
            visited_states.append(new_state)
            current_state = new_state
        else: print("visited this one already!")

    print("before third move:\n",current_state)
    
    retval,new_state=move_state(current_state,'u')
    if(retval):
        if not check_visited(new_state):
            visited_states.append(new_state)
            current_state = new_state
        else: print("visited this one already!")

    print("before fourth move:\n",current_state)
    retval,new_state=move_state(current_state,'r')
    if(retval):
        if not check_visited(new_state):
            visited_states.append(new_state)
            current_state = new_state
        else: print("visited this one already!")

    print("before fifth move:\n",current_state)
    retval,new_state=move_state(current_state,'d')
    if(retval):
        if not check_visited(new_state):
            visited_states.append(new_state)
            current_state = new_state
        else: print("visited this one already!")
    print("before sixth move:\n",current_state)