from voice import Voice

carti1 = Voice('./carti')
carti2 = Voice('./carti')
for x in range(2):
    carti1.talk()
    carti2.talk()