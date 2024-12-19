with open("input_day1.txt", "r") as f:
    data = f.read().splitlines()

splits = [i.split(" ") for i in data]
x = [int(i[0]) for i in splits]
y = [int(i[-1]) for i in splits]

x = sorted(x)
y = sorted(y)

difference = [abs(x[i] - y[i]) for i in range(len(x))]
print(sum(difference))

similarity = [x[i]*y.count(x[i]) for i in range(len(x))]
print(sum(similarity))
