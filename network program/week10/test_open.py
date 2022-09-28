f = open('myswitches.txt')
x = list(f)
j = []
for i in x:
    j.append(i[0:-1])
print(j)

"""

for line in x:
    print(line)
    print("Configuring Switch " + (line))
"""