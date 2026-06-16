points = {}
gd = {}
matches = {}
for match in matches:
    team1, team2 = match[0], match[1]
    goals1, goals2 = map(int, match[2].split("-"))

    points.setdefault(team1, 0)
    points.setdefault(team2, 0)
    gd.setdefault(team1, 0)
    gd.setdefault(team2, 0)

    gd[team1] += goals1 - goals2
    gd[team2] += goals2 - goals1

    if goals1 > goals2:
        points[team1] += 3
    elif goals1 < goals2:
        points[team2] += 3
    else:
        points[team1] += 1
        points[team2] += 1

winner = max(points, key=lambda team: (points[team], gd[team]))
print(winner, points[winner])
