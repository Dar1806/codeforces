for _ in range(int(input())):
	len_list = int(input())
	number_list = list(map(int, input().split(" ")))
	odd = 0
	for i in range(len_list):
		if number_list[i] % 2 == 1:
			odd += 1
	if odd %2 == 1:
		print("NO")
	else:
		print("YES")

