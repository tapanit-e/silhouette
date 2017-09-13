import math

def euclidean(first, second):
	assert len(first) == len(second), 'Vector lengths do not match.'
        sum = 0
        for i in range(len(first)):
                sum += (first[i] - second[i]) * (first[i] - second[i])
        return math.sqrt(sum)

def silhouette(first, second):
	first_total = 0
	div_first = 0
	second_total = 0
	div_second = 0
	for item in first:
		for compare in first:
			if item is not compare:
				first_total += euclidean(item, compare)
				div_first += 1
		for compare in second:
			second_total += euclidean(item, compare)
			div_second += 1
	assert div_first != 0 and div_second != 0, '0 as divisor.'
	first_total = first_total / div_first
	second_total = second_total / div_second
	return (second_total - first_total) / max(first_total, second_total)

def lowest_silhouette(mat):
	lowest = None
	for item in mat:
		for compare in mat:
			if item is not compare and len(item) > 1 and len(compare) > 1:
				sil = silhouette(item, compare)
				if lowest == None or sil < lowest:
					lowest = sil
	return lowest
