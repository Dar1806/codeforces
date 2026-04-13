for _ in range(int(input())):
	arr = list(map(int, input().split(" ")))
	a = arr[0]
	b = arr[1]
	c = arr[2]
	if (c % 2 == 1):
		if (a < b):
			print("Second")
		else:
			print("First")
	else:
		print("Second")