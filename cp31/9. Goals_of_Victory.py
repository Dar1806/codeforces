for _ in range(int(input())):
	n_team = int(input())
	score_team = list(map(int, input().split(" ")))
	count = 0
	score = 0
	while count < len(score_team):
		score += score_team[count]
		count += 1
	last_team = -score
	print(last_team)