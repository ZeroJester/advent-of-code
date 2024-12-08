from collections import defaultdict

input = """...O.....0...............................p..k.....
O.........o....w..T.........................p.....
..................w..........oM...................
.............................................Y....
o.............T...........................z.....pk
.....................................z..Y....t.F..
...........T..........................F.......Y...
...................A............z...k..M..........
....O.........j....w.....................M........
..........w....T..................M..k............
.............5.............................F.....t
......................A.............F....E........
.....................S.........A..................
.P................................................
........................A...E.............x...t...
............j.........................t.........x.
.......................j.........................x
....................................E........c....
.............P.......E............................
...............j..5...............q...............
..............P..............................Qc...
..........C..........s................c........x..
.............C...r................................
.....C......V..........q...................Q......
...........yX.........q...................Q.......
.....X....................e.............m.........
.2.................e..7....m.......c..............
......i..........e...K..............f....U...WQ...
...X....................e....................V...Y
...............5..X.....0.........................
..C..i......5..3...sK......J.........f..B.........
2............3.............0I...a.........BNb.....
.........................K............m...........
.r........3...............s....7...m.v...f.......b
........3........7.....Iy..........q...b.N........
.....R.1.......................n.....a.B.......VN.
......R.........9...................a...W.........
..........7.6................S....................
..............r.......s...0........nb....W..f..B..
...2...........I......K...........................
..............................u...n............U..
............r......y.............O............W...
.......R..........v..u................N...V.......
..........R.8..4.9..y........u....................
...8...............v................J.............
.....8..............4.........Z.........n.....J.U.
...........4i....................Z..S.............
..............9...........1.u.S................J..
8...6....9..4......a........Z.1...................
....................v..i.............Z............"""


lines = input.splitlines()
grid = [list(line) for line in lines]

char_dict = defaultdict(list)
maxy = len(grid)
maxx = len(grid[0])

for y in range(maxy):
    for x in range(maxx):
        char = grid[y][x]
        if char != ".":
            char_dict[char].append((y, x))

total = 0
for key in char_dict:
    for pair1 in char_dict[key]:
        for pair2 in char_dict[key]:
            if pair1 != pair2:
                y_diff = pair2[0] - pair1[0]
                x_diff = pair2[1] - pair1[1]

                new_y_cord = pair1[0] - y_diff
                new_x_cord = pair1[1] - x_diff

                if maxy > new_y_cord > -1 and new_x_cord < maxx and new_x_cord > -1:
                    if grid[new_y_cord][new_x_cord]!="#":
                        grid[new_y_cord][new_x_cord] = "#"
                        total+=1

print("Total: ", total)

for row in grid:
    print(row)