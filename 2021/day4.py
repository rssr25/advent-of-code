#bingo
import numpy as np


def Bingo(draws, cards):
    pass



if __name__ == "__main__":
    with open("day4.txt", 'r') as data:

        lines = data.readlines()
        numbers = lines[0].split(",")
        print(lines)

        lines = [value for value in  lines if value != "\n"][1:]
        print(lines)
        cards = []
        
        for i in range(0, len(lines), 5):
            card = [lines[i][:-1].split(" "), 
                    lines[i+1][:-1].split(" "),
                    lines[i+2][:-1].split(" "),
                    lines[i+3][:-1].split(" "),
                    lines[i+4][:-1].split(" ")]

            cards.append(card)
        
        #filter empties
        for card in cards:
            for i in range(0, 5):
                row = [k for k in card[i] if k != '']
                card[i] = row

        cards = np.array(cards)


    Bingo(numbers, cards)