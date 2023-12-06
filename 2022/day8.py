#height of trees
from utils import getData
import numpy as np
from itertools import takewhile

if __name__ == "__main__":
    data = []
    allTrees = getData("day8.txt")
    for line in allTrees:
        data.append(list(line)[:-1])

    
    data = np.array(data)
    

    #get all the directions for each cell and compare
    visible = len(data[:, 0]) * 2 + len(data[0, :]) * 2 - 4
    scenicScore = []
    # print(data)
    # print(data[1, :1])
    # print(data[1, 1+1:])
    # print(data[:1, 1])
    # print(data[1+1:, 1])
    #row
    for i in range(1, len(data[:, 0])-1):
        #column
        for j in range(1, len(data[0, :])-1):
            #print(i, j)
            current = data[i, j]
            left = data[i, :j]
            right = data[i, j+1:]
            top = data[:i, j]
            bottom = data[i+1:, j]

            scenicLeft = []
            scenicRight = []
            scenicTop = []
            scenicBottom = []

            #scenic left
            for k in left:
                if k <= current:
                    scenicLeft.append(k)
                elif k > current:
                    scenicLeft.append(k)
                    break

            #scenic right
            for k in right:
                if k <= current:
                    scenicRight.append(k)
                elif k > current:
                    scenicRight.append(k)
                    break
            
            #scenic top
            for k in top:
                if k <= current:
                    scenicTop.append(k)
                elif k > current:
                    scenicTop.append(k)
                    break
            
            #scenic left
            for k in bottom:
                if k <= current:
                    scenicBottom.append(k)
                elif k > current:
                    scenicBottom.append(k)
                    break

            
            scenic = len(scenicTop) * len(scenicBottom) * len(scenicRight) * len(scenicLeft)
            scenicScore.append(scenic)

            #checking if any tree is bigger than the current in any direction
            if max(left) < current or max(right) < current or max(top) < current or max(bottom) < current:
                visible += 1
    
    print(visible)
    print(max(scenicScore))
            

    