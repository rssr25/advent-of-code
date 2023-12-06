from utils import getData
data = getData("input_2.txt")

"""
1. Get the game number which is before :
2. Get the games which are after ;
3. for each game get the number of green, red and blue balls
4. count the total green, red and blue balls for the current game
5. The total of red balls should be <= 12, green balls should be <= 13 and blue balls should be <= 14
6. based on number 5. get the number of games which are valid
"""

def getTotalValidGames(data):
    totalValidGames = 0
    sumIdsValidGames = 0
    for i in range(len(data)):
        game = data[i]
        gameAndDraws = game.split(":")
        gameNumber = int(gameAndDraws[0].split(" ")[1])
        draws = gameAndDraws[1].split(";")

        blues = 0
        reds = 0
        greens = 0
        valid = True

        for draw in draws:
            balls = draw.split(",")
            for ball in balls:
                splittedBall = ball.split(" ")[1:]
                color = splittedBall[1]
                freq = int(splittedBall[0])
                if color == "green":
                    if freq > 13:
                        valid = False
                elif color == "red":
                    if freq > 12:
                        valid = False
                elif color == "blue":
                    if freq > 14:
                        valid = False

        if valid:
            totalValidGames += 1
            sumIdsValidGames += gameNumber
        
    return totalValidGames, sumIdsValidGames
                

def getPowerOfGames(data):
    sumPower = []

    for i in range(len(data)):
        game = data[i]
        gameAndDraws = game.split(":")
        gameNumber = int(gameAndDraws[0].split(" ")[1])
        draws = gameAndDraws[1].split(";")

        blues = []
        reds = []
        greens = []

        for draw in draws:
            balls = draw.split(",")
            for ball in balls:
                splittedBall = ball.split(" ")[1:]
                color = splittedBall[1]
                freq = int(splittedBall[0])

                if color == "green":
                    greens.append(freq)
                elif color == "red":
                    reds.append(freq)
                elif color == "blue":
                    blues.append(freq)
        
        maxblues = max(blues)
        maxreds = max(reds)
        maxgreens = max(greens)
        sumPower.append(maxblues * maxreds * maxgreens)
    
    return sum(sumPower)



validGames, sumIdsValidGames = getTotalValidGames(data)
print(validGames, sumIdsValidGames)
print(getPowerOfGames(data))