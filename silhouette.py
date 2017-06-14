import math

def euclidean(first, second):

        sum = 0

        for i in range(len(first)):

                sum += (first[i] - second[i]) * (first[i] - second[i])

        sum = math.sqrt(sum)

        return sum


def silhouette(first, second):

	first_total = 0
	div_first = 0
	second_total = 0
	div_second = 0

	for item in first:

		for compare in first:

			if item != compare:

				first_total += euclidean(item, compare)
				div_first += 1

		for compare in second:

			second_total += euclidean(item, compare)
			div_second += 1

	first_total = first_total / div_first
	second_total = second_total / div_second

	return (second_total - first_total) / max(first_total, second_total)
