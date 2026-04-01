for _ in range(int(input())):
	arr = []
	target_score = []
	score = 0
	for i in range(10):
		arr.append(input())
	xscore = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
	yscore = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
	for colums in range(10):
		rows = 0
		for rows in range(10):
			if arr[colums][rows] == 'X':
				if xscore[rows] > yscore[colums]:
					score += yscore[colums]
				else:
					score += xscore[rows]
	print(score)