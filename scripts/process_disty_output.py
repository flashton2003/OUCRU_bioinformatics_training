import fileinput

lines = []

for line in fileinput.input():
	lines.append(line.strip())

lines = lines[1:]
lines = [x.split()[1:] for x in lines]

i = 1
all_pwd = []

for x in lines:
	all_pwd.extend(x[i:])
	i += 1

for x in all_pwd:
	print x(base)
