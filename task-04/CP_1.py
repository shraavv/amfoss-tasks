def check_winner(g):
    for i in range(3):
        if g[i][0] == g[i][1] == g[i][2] and g[i][0] != '.':
            return g[i][0]
        if g[0][i] == g[1][i] == g[2][i] and g[0][i] != '.':
            return g[0][i]

    if g[0][0] == g[1][1] == g[2][2] and g[0][0] != '.':
        return g[0][0]
    if g[0][2] == g[1][1] == g[2][0] and g[0][2] != '.':
        return g[0][2]
    return "DRAW"

t = int(input())
for _ in range(t):
    g = [input() for _ in range(3)]
    winner = check_winner(g)
    print(winner)