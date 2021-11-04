import time

Inaltime = int(input("Inaltime: "))
Greutate = float(input("Greutate: "))
Inaltime = Inaltime/100
BMI = Greutate/(Inaltime*Inaltime)
XX = str(BMI)

print("Indexul tau este: ", XX[:4])
time.sleep(.4)
print("     ---")
time.sleep(0.6)
if BMI <= 16:
    print('\033[31m' + "Risc major de boală")
elif BMI <= 18.5:
    print('\033[93m' + "Risc minor de boală")
elif BMI <= 25:
    print('\033[32m' + "Sănătos")
elif BMI <= 30:
    print('\033[93m' + "Supraponderal")
else:
    print('\033[31m' + "Obezitate")
