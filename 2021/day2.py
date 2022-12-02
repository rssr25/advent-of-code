def task1(movement)->int:
    h_pos = 0
    depth = 0

    for command in movement:
        c = command.split()
        direction = c[0]
        value = int(c[1])

        if(direction == "forward"):
            h_pos += value
        
        if (direction == "down"):
            depth += value

        if (direction == "up"):
            depth -= value
    print(h_pos, depth)
    return h_pos * depth

def task2(movement) -> int:
    h_pos = 0
    depth = 0
    aim = 0

    for command in movement:
        c = command.split()
        direction = c[0]
        value = int(c[1])

        if(direction == "forward"):
            h_pos += value
            depth += value * aim

        
        if (direction == "down"):
            aim += value

        if (direction == "up"):
            aim -= value

    print(h_pos, depth)
    return h_pos * depth


if __name__ == "__main__":

    movement = []
    with open("day2.txt", 'r') as data:
        movement = data.readlines()
        movement = [i[:-1] for i in movement]
    
    test = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    print(task1(movement))
    print(task2(movement))
