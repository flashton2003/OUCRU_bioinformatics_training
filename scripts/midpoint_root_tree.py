from ete3 import Tree
import fileinput

lines = []

for line in fileinput.input():
	lines.append(line.strip())


tree = Tree(lines[0])

R = tree.get_midpoint_outgroup()
tree.set_outgroup(R)

print tree.write()
