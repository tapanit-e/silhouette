# silhouette index with Python

Plain Python implementation of [silhouette index](https://en.wikipedia.org/wiki/Silhouette_(clustering)).

Takes clustered matrix presentation as an input value and calculates the lowest silhouette index between the datums.

```python
s = lowest_silhouette([[[1, 2, 3], [2, 2, 2]], [[100, 100, 100], [104, 101, 100]]])
print s
# 0.97591722927
```
