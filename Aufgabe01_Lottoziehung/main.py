import numpy as np
import matplotlib.pyplot as plt

print("Lottozahlen: ")
anzahl_zahlen = 45
Lottozahlen = np.arange(1, anzahl_zahlen+1)

def lotto_ziehung(anzahl_ziehungen):
    index = anzahl_zahlen-1
    for x in range(anzahl_ziehungen):
        ziehung = np.random.randint(0, index, 1)
        Lottozahlen[ziehung], Lottozahlen[index] = Lottozahlen[index], Lottozahlen[ziehung]
        index -= 1


statistik_dict = {}

for i in range (anzahl_zahlen):
    statistik_dict[i+1] = 0


for i in range(10000):
    lotto_ziehung(6)
    gezogeneZahlen = Lottozahlen[-6:]
    #print(gezogeneZahlen)
    for zahl in gezogeneZahlen:
        statistik_dict[zahl] += 1

#Ausgabe mit Diagramm
x = list(statistik_dict.keys())
y = list(statistik_dict.values())

plt.bar(x, y)
plt.title("Häufigkeit der Lottozahlen")
plt.xlabel("gezogene Lottozahl")
plt.ylabel("Häufigkeit")
plt.show()