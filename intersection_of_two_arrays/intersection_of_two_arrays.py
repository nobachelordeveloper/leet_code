def get_intersection(a,b):
	a.sort()
	b.sort()

	result = []
	i = 0
	j = 0

	while i < len(a) and j < len(b):
		if a[i] == b[j]:
			result.append(a[i])
			i += 1
			j += 1
		elif a[i] > b[j]:
			j += 1
		else:
			i += 1
	return result
