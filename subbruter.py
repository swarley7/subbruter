import random
import sys

if len(sys.argv) != 3:
	print("Usage: {} filename domain".format(sys.argv[0]))
	sys.exit(1)

filename, domain = sys.argv[1:]
with open(filename) as f:
	subz = set(i for i in f.read().split("\n"))

for sub in subz:
	if random.random() >= 0.97:
		print("{}.{}".format(sub, domain))
