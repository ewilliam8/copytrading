import data
import json
from pprint import pprint
from ParseClass import Parse

opened = '{"retCode":"0","retMsg":"success","result":{"data":[{"symbol":"ETHUSDT","entryPrice":"1188.35","sizeX":"1000000","createdAtE3":"1657440821682","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657440821686"},{"symbol":"ETHUSDT","entryPrice":"1188.45","sizeX":"1000000","createdAtE3":"1657440805245","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657440805249"},{"symbol":"BTCUSDT","entryPrice":"21200.5","sizeX":"100000","createdAtE3":"1657426749741","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657426749745"},{"symbol":"BTCUSDT","entryPrice":"21200.5","sizeX":"100000","createdAtE3":"1657426741557","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657426741561"},{"symbol":"BTCUSDT","entryPrice":"21200","sizeX":"100000","createdAtE3":"1657426734517","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657426734523"},{"symbol":"BTCUSDT","entryPrice":"21254","sizeX":"100000","createdAtE3":"1657420191908","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657420191913"},{"symbol":"BTCUSDT","entryPrice":"21265.5","sizeX":"100000","createdAtE3":"1657420182896","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657420182900"},{"symbol":"BTCUSDT","entryPrice":"21435.5","sizeX":"100000","createdAtE3":"1657415796655","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657415796660"},{"symbol":"BTCUSDT","entryPrice":"21503.5","sizeX":"100000","createdAtE3":"1657413287635","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657413287639"},{"symbol":"BTCUSDT","entryPrice":"21507.5","sizeX":"100000","createdAtE3":"1657413274510","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657413274515"},{"symbol":"BTCUSDT","entryPrice":"21381","sizeX":"100000","createdAtE3":"1657367879849","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657367879853"},{"symbol":"BTCUSDT","entryPrice":"21366","sizeX":"100000","createdAtE3":"1657367869320","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657367869324"},{"symbol":"BTCUSDT","entryPrice":"21320","sizeX":"100000","createdAtE3":"1657367859012","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657367859016"},{"symbol":"BTCUSDT","entryPrice":"21632.5","sizeX":"100000","createdAtE3":"1657359483418","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657359483423"},{"symbol":"BTCUSDT","entryPrice":"21629.5","sizeX":"100000","createdAtE3":"1657359459462","side":"Buy","leverageE2":"500","isIsolated":true,"transactTimeE3":"1657359459466"}]}}'
BOTORDERPATH = "cache/bot_orders.json"

def change_bot_orders(type, order):
    # https://howtodoinjava.com/json/append-json-to-file/
    with open(BOTORDERPATH, "r") as file:
        listObj = json.load(file)

    # order = json.loads(order)
    if(type == "add"):
        listObj.append(order)

    with open(BOTORDERPATH, 'w') as json_file:
        json.dump(listObj, json_file, 
                            indent=4,  
                            separators=(',',': '))

parse = Parse()
# парсинг открытых позиций
with open("cache/mt_opened.json", "w+") as file:
    # opened = parse.get(data.bybit_opened)
    # file.write(opened)
    opened = json.loads(opened)["result"]["data"]

# проверка ставок бота
with open(BOTORDERPATH, "r+") as file:
    lines = file.read()
    if lines:
        lines = json.loads(lines)


# если добавлен новый ордер?
i = 1
if opened:
    for mt_order in opened:
        
        create_order = True
        if lines:
            for line in lines:
                if line == mt_order:
                    create_order = False
        if create_order:
            # ОТКРЫВАЕМ ПОЗИЦИЮ mt_order
            print(f"{i} CREATE ORDER {mt_order}")
            change_bot_orders("add", str(mt_order))
            i += 1

print("- -  - - - - - - -  - - - ")

# если ордер закрыт?
i = 1
if lines:
    for line in lines:

        delete_order = True
        if opened:
            for mt_order in opened:
                if line == mt_order:
                    delete_order = False

        if delete_order:
            # ЗАКРЫВАЕМ ПОЗИЦИЮ mt_order
            print(f"{i} CLOSE ORDER {mt_order}")
            i += 1

        




