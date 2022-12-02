from utils import getData

if __name__ == "__main__":

    fullData = getData("day2.txt")
    fullData = [i[:-1] for i in fullData]
    fullData = [i.split(" ") for i in fullData]
    print(fullData)
    
    draw_score = {"X":1, "Y":2, "Z":3}

    r = ['A', 'X']
    p = ['B', 'Y']
    s = ['C', 'Z']


    score = 0
    tie = 3
    win = 6
    lose = 0

    for i in range(0, len(fullData)):
        opponent = fullData[i][0]
        me = fullData[i][1]
        
        if (opponent == "A" and me == "X") or (opponent == "B" and me == "Y") or (opponent == "C" and me == "Z"):
            score = score + draw_score[me] + tie #this is a tie
        
        elif (opponent == "A" and me == "Y") or (opponent == "B" and me == "Z") or (opponent == "C" and me == "X"):
            score = score + draw_score[me] + win #this is a win
        
        else:
            score = score + draw_score[me] + lose
    
    print(score)


    #part2
    score = 0
    for i in range(0, len(fullData)):
        opp = fullData[i][0]
        whatToDo = fullData[i][1]
        me = None

        if whatToDo == "X":
            #we need to lose
            if opp == "A":
                me = "Z"
            
            elif opp == "B":
                me = "X"
            
            elif opp == "C":
                me = "Y"
            
            score = score + lose + draw_score[me]
            

                
        
        if whatToDo == "Y":
            #we need to have a tie
            if opp == "A":
                me = "X"
            
            elif opp == "B":
                me = "Y"
            
            elif opp == "C":
                me = "Z"
            
            score = score + tie + draw_score[me]

        if whatToDo == "Z":
            #we need to win

            if opp == "A":
                me = "Y"
            
            elif opp == "B":
                me = "Z"
            
            elif opp == "C":
                me = "X"
            
            score = score + win + draw_score[me]
    
    print(score)







        


