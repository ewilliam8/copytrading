import data
import json
from pprint import pprint
from ParseClass import Parse



parse = Parse()
# парсинг открытых позиций
with open("cache/mt_opened.json", "w+") as file:
    opened = parse.get(data.bybit_opened)
    file.write(opened)
    opened = json.loads(opened)["result"]["data"]

# проверка ставок бота
with open("cache/bot_orders.json", "r+") as file:
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
            # ОТКРЫВАЕМ ПОЗИЦИЮ
            print(f"{i} CREATE ORDER {mt_order}")
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
            # ЗАКРЫВАЕМ ПОЗИЦИЮ
            print(f"{i} DELETE ORDER {mt_order}")
            i += 1

        




