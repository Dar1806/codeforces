int(input())
arr = list(map(int, input().split(" ")))
for i in range(len(arr)):
	arr[i] = abs(arr[i])
arr.sort()
print(arr[0])