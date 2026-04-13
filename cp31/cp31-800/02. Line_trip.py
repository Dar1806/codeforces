for x in range(int(input())):
	last_nbr = int(input().split(" ")[1])
	n = list(map(int, input().split(" ")))
	liters = n[0]
	for nlist in range(1, len(n)):
		temp = n[nlist] - n[nlist - 1]
		if temp > liters:
			liters = temp
	nlist = len(n) - 1
	if (liters < (last_nbr - n[nlist]) * 2):
		liters = (last_nbr - n[nlist]) * 2
	print(liters)