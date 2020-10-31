# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą
# x (typ float) i wypisujący parę x i trzecią potęgę x.
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
# Jeżeli użytkownik wpisze napis zamiast liczby,
# to program ma wypisać komunikat o błędzie i kontynuować pracę.
value = 0
t = True
while t:

	value = input("Podaj liczbe x ( jeżeli chcesz zatrzymać program wpisz \"stop\") : ")
	
	if value.isnumeric():
		print("x = " + str(value) + "\nx^3 = " +  str(int(value) ** 3))
	elif value == "stop":
		t = False
	elif value.isnumeric() == False:
		print("Błąd! Podana wartość nie jest liczbą")
	
		
		