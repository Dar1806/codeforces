for _ in range(int(input())):
		lenb = int(input())
		b = list(map(int, input().split(" ")))
		a = [b[0]]
		for i in range(1, len(b)):
			if b[i - 1] > b[i]:
				a.append(b[i])
			a.append(b[i])
		print(len(a))
		print(" ".join(map(str, a)))