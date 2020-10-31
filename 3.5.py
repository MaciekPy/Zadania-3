# Napisać program rysujący "miarkę" o zadanej długości.
# Należy prawidłowo obsłużyć liczby składające się z kilku cyfr 
# (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
# Należy zbudować pełny string, a potem go wypisać.

length = input("Podaj długośc linijki : ")
linijka = []
for i in range(int(length)):
	linijka.append("|")
	for j in range(4):
		linijka.append(".")

linijka.append("|")	
linijka.append("\n")

for i in range(int(length)+1):
	
	linijka.append(str(i))
	x = 4
	if i > 8:
		x = 3
	for j in range(x):	
		linijka.append(" ")
		
	

str1 = "".join(linijka)
print(str1)