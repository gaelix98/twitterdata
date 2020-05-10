import pandas
import matplotlib.pyplot as plt
import numpy
import json

##ultimo=Timestamp('2020-03-10 14:45:40+0000')
##primo= Mon Mar 09 11:25:56 +0000 2020

verifica=10000

iteratore = pandas.read_json("C:/Users/Utente/PycharmProjects/tesiTwitter/twitter_dataset_0.json", lines=True, chunksize=10000)

#dict delle ore del giorno, l'ora del tweet è la chiave del dict, se ci sono tot tweet in un'ora verranno contati in quell'ora.
dic={"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0,"21":0,"22":0,"23":0,"0":0, "1":0, "2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0, "9":0,"10":0}
lista=[]
for x in iteratore:

    z = x["created_at"].to_dict()

    print(z.values())
    lista=lista+list(z.values())


for item in lista:

    if item!=item:
        print("bingo")
        continue
    print(item.hour)
    dic[str(item.hour)] = dic.get(str(item.hour)) + 1


print(len(lista))
print(dic)







