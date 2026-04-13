for _ in range(int(input())):
	n = int(input().split(" ")[1])
	arr = list(map(int, input().split(" ")))
	if (n >= 2):
		print("YES")
	elif (arr == sorted(arr)):
		print("YES")
	else :
		print("NO")
