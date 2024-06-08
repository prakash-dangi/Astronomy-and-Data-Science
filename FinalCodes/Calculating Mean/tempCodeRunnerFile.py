with open("data.csv", "r") as csvfile:
    data = [line.strip().split(",") for line in csvfile]

print(data)