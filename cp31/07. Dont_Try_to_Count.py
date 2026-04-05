for _ in range(int(input())):
	arr = list(map(int, input().split(" ")))
	n = arr[0]
	m = arr[1]
	x_n = input()
	s_m = input()
	count = 0
	while s_m not in x_n and count <= 5:
		x_n *= 2
		count += 1
	if count > 5:
		print("-1")
	else:	
		print(count)