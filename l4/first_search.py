# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def moves(grid, current, open_list, closed_list):
    move_cost = current[0] + 1 
    
    closed_list.append([current[1],current[2]]) #closes out the location
    for move in delta:
        #check to see if move is out of bounds
        vert_move = current[1]+move[0]
        horiz_move = current[2]+move[1]  
        #print (vert_move, horiz_move, move, closed_list)
       
        #debugging print statements 
        # print "vert_move > 0" if vert_move > 0 else "off" 
        # print "vert_move < len(grid)" if  vert_move < len(grid) else "off"
        # print "horiz_move > 0 " if   horiz_move > 0 else "off"
        # print "horiz_move < len(grid[0]) " if  horiz_move < len(grid[0]) else "off" 
        # print "grid[vert_move][horiz_move] == 0" if grid[vert_move][horiz_move] == 0 else "off"
        # print "[vert_move,horiz_move] not in closed_list" if   [vert_move,horiz_move] not in closed_list else "off"


        if (vert_move >= 0 and #ensures its in vert bounds 
           vert_move < len(grid) and #ensures its in vert bounds 
           horiz_move >= 0 and #ensures its in horiz bounds 
           horiz_move < len(grid[0]) and #ensures its in horiz bounds 
           grid[vert_move][horiz_move] == 0 and #checks to see if it is a valid square
           [vert_move,horiz_move] not in closed_list): #checks to see if it has already been seen
            open_list.append([move_cost,current[1]+move[0], current[2]+move[1]]) #appends the next move

    return open_list,closed_list


class BreakIt(Exception): pass

def search(grid,init,goal,cost):
    path = []
    failstate = False
    closed_list = []
    open_list = [[0,init[0],init[1]]]
    init_range = -1
    lowest_i = -1
    current = []
    while 1:
        #selects the best move from the list

        for i in range(len(open_list)):
            
            #print "open list:", open_list[i]
            if open_list[i][0]<=init_range or init_range == -1: #checks to see that the range is not initial or looks for the smalles
                init_range = open_list[i][0]
                lowest_i = i
        current = open_list[lowest_i]
        #print "selected", current
        del open_list[lowest_i] #removes the command from the open list
        init_range = -1
        lowest_i = -1
        #generates the new open list and closed coords
        open_list, closed_list = moves(grid, current ,open_list, closed_list)
        #raw_input("Press Enter to continue...")
        #print "open list:", open_list, "\n closed list", closed_list
        #if there are no more moves...shits broken
        if open_list == []: 
            return "fail"
            #raise BreakIt #autograder does not accept
        for move in open_list:
            if move[1] == goal[0] and move[2] == goal[1]:
                path.append(move)
                #return path #this would be the full path
                return move

print search(grid,init,goal,cost)


#autograder does not accept

# try:
#     path = search(grid, init, goal, cost)
#     print path[-1]
# except BreakIt:
#     print "fail"