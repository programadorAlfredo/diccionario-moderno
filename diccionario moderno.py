word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
meme_dict = {"LOL" : "una respuesta a algo gracioso",
             "CRINGE" : "algo raro o embarazoso",
             "ROFL" : "una respuesta a una broma",
             "SHEESH" : "ligera desaprobación",
             "CREEPY" : "aterrador, siniestro",
             "AGGRO" : "ponerse agresivo/enojado"}
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("palabra no detectada")
