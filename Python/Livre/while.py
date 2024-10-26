marche = 0
fatigue = False
meteo = True

while marche < 10000 and fatigue == False and meteo == True:
    marche = marche + 1 
    if marche == 9997:
        continue
    print("Caca %s " % marche)


for i in range(0, 10):
    if i == 5:
        continue
    print(i)

    if i == 7:
        break