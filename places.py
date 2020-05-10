import pandas
import matplotlib.pyplot as plt
import numpy
import json

iteratore = pandas.read_json("C:/Users/Utente/PycharmProjects/tesiTwitter/twitter_dataset_0.json", lines=True,
                             chunksize=10000)
dizionario = {}
#479952
inizio=0
fine=10000
for x in iteratore:
    for i in range(inizio, fine):
        z = x["user"].to_dict()
        if i==156672 or i==156728: ##156671  e 156727 si rompe tutto
            continue
        if i==479952:
            break
        if z[i]["location"]==z[i]["location"]: # roba di verifica sul valore, faccio prima il check se è un valore accettabile o no
                posto = (z[i]["location"])  # mi scoccio di scrivere z[i] ogni volta.
                if posto is not None:

                    print(i)
                    # SE è none, vuol dire no posto, quindi inutile, se posto è !=none, allora vedo se l'ho messo nel
                    # dizionario, se messo allora good, aumento, altrimenti metto chiave
                    if dizionario.get((posto), "x") == ("x"):
                        dizionario[posto] = 1
                    else:
                        dizionario[posto] = dizionario.get(posto) + 1
    inizio=fine
    fine+=10000

print(dizionario)
