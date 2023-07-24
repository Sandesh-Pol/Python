if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().split()))
	a = max(arr)
	for i in range(len(arr)):
		if a in arr:
			arr.remove(a)
print(max(arr))
