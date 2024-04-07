import sys
input = sys.stdin.readline

game = 0
while 1:
    game += 1
    R, C = map(int, input().split())
    
    if R == 0 and C == 0:
        break
    sokoban = [list(input().rstrip()) for _ in range(R)]

    cx, cy = 0, 0

    box_state, box_target = 0, 0
    targets = []
    for a in range(R):
        for b in range(C):
            if sokoban[a][b] == 'w':
                cx, cy = a, b
            elif sokoban[a][b] == 'W':
                targets.append((a, b))
                cx, cy = a, b
                box_target += 1
            elif sokoban[a][b] == 'B':
                targets.append((a, b))
                box_state += 1
                box_target += 1    
            elif sokoban[a][b] == '+':
                targets.append((a, b))
                box_target += 1
                sokoban[a][b] = '.'


    keys = list(input().rstrip())

    direction = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    for key in keys:
        add_x, add_y = direction[key]
        ncx, ncy = cx+add_x, cy+add_y
        
        if sokoban[ncx][ncy] == '.':
            sokoban[cx][cy] = '.'
            sokoban[ncx][ncy] = 'w'
            cx, cy = ncx, ncy
            
        elif sokoban[ncx][ncy].lower() == 'b':
            if sokoban[ncx+add_x][ncy+add_y] == '.':
                sokoban[cx][cy] = '.'
                sokoban[ncx][ncy] = 'w'
                sokoban[ncx+add_x][ncy+add_y] = 'b'
                cx, cy = ncx, ncy
                if (ncx, ncy) in targets:
                    box_state -= 1
                if (ncx+add_x, ncy+add_y) in targets:
                    box_state += 1
            else:
                pass
        

        elif sokoban[ncx][ncy] == '#':
            pass

        if box_state == box_target:
 
            for x, y in targets:
                sokoban[x][y] = 'B'
            print("Game "+str(game)+": complete")
            for soko in sokoban:
                print("".join(soko))  
            break

    else:
        for x, y in targets:
            if sokoban[x][y] == '.':
                sokoban[x][y] = '+'
            elif sokoban[x][y] == 'b':
                sokoban[x][y] = 'B'
            elif sokoban[x][y] == 'w':
                sokoban[x][y] = 'W'

        print("Game "+str(game)+": incomplete")
        for soko in sokoban:
            print("".join(soko))