import sys
from operator import itemgetter

distances = []
estimateVal = 0.0
k = 5

for line in sys.stdin:
    line = line.strip()
    elements = line.split()
    distances.append(elements)

distances = sorted(distances)

for i in range(k):
    try:
        estimateVal += float(distances[i][1])
    except ValueError:
        continue

print estimateVal/k
