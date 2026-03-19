for _ in range(int(input())):
	ncells = int(input())
	arr = list(input())
	x = 0
	actions = 0
	while x < ncells:
		if x + 2 < ncells and arr[x] == '.' and arr[x + 1] == '.'  and arr[x + 2] == '.':
			x += 2
			actions += 2
			break
		x += 1
	x = 0
	if actions == 0:
		while x < ncells:
			if x + 2 < ncells and arr[x] == '.' and arr[x + 1] == '.'  and arr[x + 2] == '.':
				x += 2
				actions += 2
				break
			else:
				if arr[x] == '.':
					actions += 1
			x += 1
	print(actions)