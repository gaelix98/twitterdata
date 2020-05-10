import pandas
import matplotlib.pyplot as plt
import numpy
import json

iteratore = pandas.read_json("C:/Users/Utente/PycharmProjects/tesiTwitter/twitter_dataset_0.json", lines=True,
                             chunksize=10000)
dizionario = {}
# 479952
inizio = 0

# 228
fine = 10000
for x in iteratore:
    for i in range(inizio, fine):
        z = x["entities"].to_dict()
        if i == 156672 or i == 156728:  ##156671  e 156727 si rompe tutto
            continue
        if i == 479952:
            break
        hashtaggo = (z[i]["hashtags"])
        lunghezza = len(hashtaggo)
        if lunghezza != 0:
            for t in range(lunghezza):
                print(i)
                testo=hashtaggo.__getitem__(t)["text"]
                if dizionario.get((testo), "x") == ("x"):
                    dizionario[testo] = 1
                else:
                    dizionario[testo] = dizionario.get(testo) + 1

    inizio = fine
    fine += 10000

print(dizionario)

