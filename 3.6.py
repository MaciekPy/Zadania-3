# Napisać program rysujący prostokąt zbudowany z małych kratek.
# Należy zbudować pełny string, a potem go wypisać.


kwadrat = []
for k in range(3):
	for i in range(5):
		kwadrat.append("+")
		for j in range(3):
			kwadrat.append("-")
	kwadrat.append("+")
	kwadrat.append("\n")

	for i in range(5):
		kwadrat.append("|")
		for j in range(3):
			kwadrat.append(" ")
	kwadrat.append("|") 
	kwadrat.append("\n")
	
for i in range(5):
	kwadrat.append("+")
	for j in range(3):
		kwadrat.append("-")
kwadrat.append("+")
kwadrat.append("\n")
	
	
str1 = "".join(kwadrat)
print(str1)