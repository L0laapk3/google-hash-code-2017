file = open("me_at_the_zoo.in", "r")

eerstelijn = map(lambda x: int(x), file.readline().split(" "))

V = eerstelijn[0]
E = eerstelijn[1]
R = eerstelijn[2]
C = eerstelijn[3]
X = eerstelijn[4]


#videogroootettete
vg = map(lambda x: int(x), file.readline().split(" "))


#cache endpoint verbindings latency winst
CE = [] # array met (latencywinst, endpoint, cacheserver)

for i in range(E):
    lijn = map(lambda x: int(x), file.readline().split(" "))
    latency = lijn[0]
    for j in range(lijn[1]):
        sublijn = map(lambda x: int(x), file.readline().split(" "))
        CE.append((latency - sublijn[1], i, sublijn[0]))


CE.sort(key = lambda x: -x[0])


print(CE)
