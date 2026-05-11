for _ in range(int(input())):
	arr = list(map(int, input().split(" ")))
	n = arr[0]
	k = arr[1]
	x = arr[2]
	if (x != 1):
		print("YES")
		print(n)
		print(" ".join(["1"] * n))
	elif (k == 1 and x == 1):
		print("NO")
	elif(k <= 2 and n % 2 == 1):
		print("NO")
	else:
		if (n % 2 == 0):
			print("YES")
			print(n // 2)
			print(" ".join(["2"] * (n // 2)))
		else:
			print("YES")
			print(((n - 3) // 2) + 1)
			n = n - 3
			print("3", end=" ")
			print(" ".join(["2"] * (n // 2)))


