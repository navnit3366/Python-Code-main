probs = []
for a in range(1, 10):
    for b in range(1, 10):
        if set([a, 15-a-b, b, 5+b-a, 5, 5+a-b, 10-b, a+b-5, 10-a]) == set(range(1, 10)):
            probs.append([a, 15-a-b, b,
                                  5+b-a, 5, 5+a-b,
                                  10-b, a+b-5, 10-a])

matrix = []
for _ in range(3):
    for each in list(map(int, input().split())):
        matrix.append(each)

minimumCost = 100
for p in probs:
    cost = 0
    for i in range(9):
        cost += abs(matrix[i] - p[i])
    if cost < minimumCost:
        minimumCost = cost
        
print(minimumCost)