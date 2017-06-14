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


s = silhouette(

[[0.49, 0.64, 0.34, 0.78, 0.21], 
[0.09, 0.55, 0.12, 0.78, 0.05], 
[0.255, 0.75, 0.35, 0.72, 0.25], 
[0.1, 0.42, 0.22, 0.72, 0.26], 
[0.72, 0.6, 0.45, 0.79, 0.45], 
[0.12, 0.28, 0.2, 0.78, 0.2], 
[0.285, 0.64, 0.18, 0.61, 0.45], 
[0.345, 0.299, 0.1, 0.64, 0.13], 
[0.315, 0.69, 0.28, 0.8, 0.7], 
[0.365, 0.68, 0.1, 0.63, 0.18], 
[0.62, 0.62, 0.24, 0.65, 0.25], 
[0.45, 0.65, 0.19, 0.99, 0.55], 
[0.06, 0.29, 0.35, 0.76, 0.25], 
[0.2, 0.52, 0.36, 0.84, 0.25]] 

,

[[0.9, 0.26, 0.19, 0.58, 0.79], 
[0.76, 0.258, 0.07, 0.83, 0.34], 
[0.48, 0.3, 0.15, 0.65, 0.77], 
[0.48, 0.12, 0.28, 0.7, 0.71], 
[0.08, 0.08, 0.08, 0.98, 0.24], 
[0.73, 0.2, 0.07, 0.72, 0.26], 
[0.91, 0.58, 0.26, 0.89, 0.88], 
[0.6, 0.31, 0.31, 0.87, 0.58], 
[0.64, 0.09, 0.33, 0.65, 0.5], 
[0.27, 0.1, 0.1, 0.7, 0.25], 
[0.99, 0.49, 0.07, 0.7, 0.69]]

)


print s
