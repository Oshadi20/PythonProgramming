rows = 2
cols = 3

# store the state utility values
prevUtil = [[0 for x in range(cols)] for x in range(rows)]
updatedUtil = [[0 for x in range(cols)] for x in range(rows)]

# function to check boundaries
# to check go up, down, left, right
def checkForBoundaries(pos, row , col):
    if(pos == 0 and (row-1) >= 0):
        return True
    elif(pos == 1 and (row+1) < 2):
        return True
    elif(pos == 2 and (col-1) >= 0):
        return True
    elif(pos == 3 and (col+1) < 3):
        return True
    else:
        return False

# function to get final state utilities after the convergence
def get_state_utilities(epsilon, rewardArr):
    i = 0
    delta = -1
    
    accuracy = epsilon*(0.001/0.999)
    converge = False
    
    while(not converge):
        # if a state reward is 1, update updatedUtil by 1
        for row in range(rows):
            for col in range(cols):
                if(rewardArr[row][col] == 1):
                    updatedUtil[row][col] = 1
                    continue
                
                # up command is given
                if(checkForBoundaries(0,row,col)):
                    util = 0.9 * prevUtil[row-1][col]
                else:
                    util = 0.9 * prevUtil[row][col]
                # if go left
                if(checkForBoundaries(2, row,col)):
                    util += 0.05 * prevUtil[row][col-1]
                else:
                    util += 0.05 * prevUtil[row][col]
                # if go right
                if(checkForBoundaries(3,row,col)):
                    util += 0.05 * prevUtil[row][col+1]
                else:
                    util += 0.05 * prevUtil[row][col]
                currMax = util
                util = 0
                
                # left command is given
                if(checkForBoundaries(2, row, col)):
                    util = 0.9 * prevUtil[row][col-1]
                else:
                    util = 0.9 * prevUtil[row][col]
                # if go up
                if(checkForBoundaries(0, row, col)):
                    util += 0.05 * prevUtil[row-1][col]
                else:
                    util += 0.05 * prevUtil[row][col]
                # if go down
                if(checkForBoundaries(1, row, col)):
                    util += 0.05 * prevUtil[row+1][col]
                else:
                    util += 0.05 * prevUtil[row][col]
                if(util > currMax):
                    currMax = util
                util = 0
                
                # right command is given
                if(checkForBoundaries(3, row, col)):
                    util = 0.9 * prevUtil[row][col+1]
                else:
                    util = 0.9 * prevUtil[row][col]
                # if go up
                if(checkForBoundaries(0, row, col)):
                    util += 0.05 * prevUtil[row-1][col]
                else:
                    util += 0.05 * prevUtil[row][col]
                # if go down
                if(checkForBoundaries(1, row, col)):
                    util += 0.05 * prevUtil[row+1][col]
                else:
                    util += 0.05 * prevUtil[row][col] 
                if(util > currMax):
                    currMax = util
                util = 0
                
                 # down command is given
                if(checkForBoundaries(1, row, col)):
                    util = 0.9 * prevUtil[row+1][col]
                else:
                    util = 0.9 * prevUtil[row][col]
                # if go left
                if(checkForBoundaries(2, row, col)):
                    util += 0.05 * prevUtil[row][col-1]
                else:
                    util += 0.05 * prevUtil[row][col]
                # if go right
                if(checkForBoundaries(3, row, col)):
                    util += 0.05 * prevUtil[row][col+1]
                else:
                    util += 0.05 * prevUtil[row][col]
                if(util > currMax):
                    currMax = util

                # when nothing to be done
                if(prevUtil[row][col] > currMax):
                    currMax = prevUtil[row][col]

                # update new value to updatedUtil
                updatedUtil[row][col] = rewardArr[row][col] + 0.999 * currMax

                # if delta is lower, update it to new computed value
                computedDelta = abs(updatedUtil[row][col] - prevUtil[row][col])
                if(computedDelta > delta):
                    delta = computedDelta

        #increment the number of iterations            
        i += 1
        
        #exit the loop, when the required accuracy is reached
        if(delta <= accuracy):
            converge = True
        delta = 0
        
        for row in range(rows):
            for col in range(cols):
                prevUtil[row][col] = updatedUtil[row][col]
        
        #print the content in prevUtil up to 4 decimal places
        for row in range(rows):
            for col in range(cols):
                print("%.4f" % round(prevUtil[row][col], 4), end="\t")
            print()
        print("\n")
    return i




rewardArr = [[-0.1, -0.1, -0.05], 
             [-0.1, -0.1, 1]]

epsilon = 0.01

iterations = get_state_utilities(epsilon, rewardArr)
print("Number of iterations:",iterations)
