for _ in range(int(input())):
	lena = int(input())
	a = list(map(int, input().split(" ")))
	a.sort()
	if a[0] == a[-1]:
		print("-1")
	else:
		b = []
		c = []
		max = a[-1]
		for i in range(len(a)):
			if a[i] == max:
				c.append(a[i])
			else:
				b.append(a[i])
		print(len(b), len(c))
		print(" ".join(map(str, b)))
		print(" ".join(map(str, c)))