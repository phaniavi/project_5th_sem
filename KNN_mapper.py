import sys
import math

query = [sys.argv[1], sys.argv[2]]

for line in sys.stdin:
    avg = 0.0
    line = line.strip()
    features = line.split()
    for i in range(len(features)-1):
        if features[i]!='':
            avg += (float(features[i]) - float(query[i]))**2
    dist = math.sqrt(avg)
    print dist,features[-1]
