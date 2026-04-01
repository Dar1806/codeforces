from collections import Counter
     
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split(" ")))
	count = len(set(arr))
	if count == 1:
		print("YES")
	elif count >= 3:
		print("NO")
	else:
		occ = Counter(arr)
		tab_occ = list(occ.values())
		if n % 2 == 0:
			if tab_occ[0] - tab_occ[1] == 0:
				print("YES")
			else:
				print("NO")
		else:
			if abs(tab_occ[0] - tab_occ[1]) == 1:
				print("YES")
			else:
				print("NO")