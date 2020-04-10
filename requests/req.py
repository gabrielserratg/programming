import requests
import sys
import threading
import random
import re
import argparse

reqcount = int(input("requests counts: "))
usrname = input("NickName of BOts: ")

msge = input("Your msg: ")
discordurl1 = "https://discordapp.com/api/webhooks/698029933384958044/G8mwIYpoEfflrQQ71i8EG_IHmg2x7QpRnmmcxnKmBiBo4kp7dd67EzSfvv_OMJwz-JBr"
discordurl2 = "https://discordapp.com/api/webhooks/698030015035604994/62RUHH-pC0sIRau5tnMDwMHdzdDTsEq_D3gq1FYv8WwCY04gge2jswlo4nfPMvdRVEOV"
discordurl3 = "https://discordapp.com/api/webhooks/698030042969800727/imFk-nmCvuFjcC-AHiSEFjzIr_mX6vMPJefxL_VogIp2kFSq3i27kCUDoDAhH4y5OjGl"
discordurl4 = "https://discordapp.com/api/webhooks/698030086045171773/HJG7WWv-3WgDuOpQ7BK4ICSpVVaCGoOASkEKdiqfoeSsBpoEfTBdFjuyCG9LKFyk-Ahs"
discordurl5 = "https://discordapp.com/api/webhooks/698030112184074270/5L8ObvUCr70HoRm9-l0kfU1LUW9X9qLu9mTZJNFVynHyt84zkdauC9EuG1It97CQi9ut"
discordurl6 = "https://discordapp.com/api/webhooks/698030140738895912/0c1OY68F50oi0HXzuuRi8PQwPjEDeXOkNRBbNVJNLzp4Zk0YfPiyMFFsFPoSyRVGSK8G"
discordurl7 = "https://discordapp.com/api/webhooks/698030166152052817/kCwi2t1MGh86FDtoLZR9fMBW6WwQMF8GE646oaAU757yxAbW3qGWuqJ-xYKTsPbc4w3f"
discordurl8 = "https://discordapp.com/api/webhooks/698030196011565066/R12go1kpOrel87AtXgRW_YwWgrVLDS75zhs0ZCwYxHNBq3euknl300P2znFuTpAOEgzN"
discordurl9 = "https://discordapp.com/api/webhooks/698030223341387826/o9WopawKqEA74D4I4NbhiK-sF-DUzRLaUwDw-Q92KG4aUiCvD813WJexjkxQgcaJYW18"
discordurl10 = "https://discordapp.com/api/webhooks/698030252277891184/7jbFhbh3e9WwvoaMtV112DT1IbzRMPP0TX2nWru9JfOnwfObUVNon-lAk85CAGyUa9Qw"

payload = {"username": usrname, "content": msge}

#while (reqcount > 1):

    #reqcount = reqcount + 1
for r in range(reqcount):
    requests.post(discordurl1, data=payload)
    requests.post(discordurl2, data=payload)
    requests.post(discordurl3, data=payload)
    requests.post(discordurl4, data=payload)
    requests.post(discordurl5, data=payload)
    requests.post(discordurl6, data=payload)
    requests.post(discordurl7, data=payload)
    requests.post(discordurl8, data=payload)
    requests.post(discordurl9, data=payload)
    requests.post(discordurl10, data=payload)
    print("Messagem: " + msge + "Sending..")

    






#host = 'localhost'
#reqcount = input("requests counts: ")

#print ("DDos in " + host + ", Quantidade de request: " + reqcount)
