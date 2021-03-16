from voice import Voice

carti = Voice('./carti')
bowie = Voice('./bowie')
carti.set_peer(bowie)
bowie.set_peer(carti)

for x in range(10):
    carti.talk()
    bowie.talk()