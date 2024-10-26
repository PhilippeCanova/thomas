trouvees = 20
magiques = 70
volees = 3

pieces = trouvees
perte = 0

vacances = [1, 5, 8, 16, 17]
for semaine in range(1, 53):
    pieces = pieces + magiques - volees
    
    if semaine not in vacances:
        perte = perte + volees

    print("Semaine %s = %s pièces et combien de volées ? %s" % (semaine, pieces, perte))
