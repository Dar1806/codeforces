for _ in range(int(input())):
	arr = list(map(int, input().split(" ")))
	n = arr[0]
	k = arr[1]
	list_n = list(map(int, input().split(" ")))
	if k in list_n:
		print("YES")
	else:
		print("NO")