"""A cricket tournament records match results in the following format:
Team1-Team2-Score1-Score2
Where Score1 is Team1's runs and Score2 is Team2's runs.
The team with higher runs wins. In case of a tie, both teams get 1 point.
A win gives 2 points, a loss gives 0 points.
Write a program that:
1. Reads N match results.
2. Computes the total points for each team.
3. Prints all teams in descending order of points.
4. For equal points, sort alphabetically.
Input Format:
Line 1: N
Next N lines: Team1-Team2-Score1-Score2
Output Format:
TeamName Points (one per line, sorted)
Sample Input:
4
India-Australia-320-280
England-India-250-310
Australia-England-180-200
India-Pakistan-290-290
Sample Output:
India 4
England 2
Australia 0
Pakistan 1
• Delimiter is '-' (hyphen) — not underscore or space • Ties: both teams get 1 point each • Sort: descending points, then
alphabetical for ties"""

n = int(input("Write the score: "))

points = {}
for _ in range(n):
    Team1, Team2, Score1, Score2 = input().split("-")

    Score1 = int(Score1)
    Score2 = int(Score2)

    # check if they are in the points or not, cause we have to compare there only the teams score and all
    if Team1 not in points:
        points[Team1] = 0
    if Team2 not in points:
        points[Team2] = 0

    if Score1>Score2:
        points[Team1] +=2
    elif Score2>Score1:
        points[Team2]+=2
    else:
        points[Team1]+=1
        points[Score2]+=1

result = sorted(points.items(), key=lambda x: (-x[1], x[0]))

for team, point in result:
    print(team, point)
