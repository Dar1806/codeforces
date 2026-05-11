for _ in range(int(input())):
	len_array = int(input())
	number_list = list(map(int, input().split(" ")))
	gap = abs(number_list[0] - number_list[1])
	for i in range(len_array - 1):
		if number_list[i] > number_list[i + 1]:
			print("0")
			break
	else:
		for i in range(len_array - 1):
			if (abs(number_list[i] - number_list[i + 1]) < gap):
				gap = abs(number_list[i] - number_list[i + 1])
		print((gap // 2) + 1)