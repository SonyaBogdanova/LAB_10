'LAB_10'
# -*- coding: utf-8 -*-

def p1_p2():
    import json
    with open("10_1.json", "r", encoding='utf-8') as file:
        inf = json.load(file)

    z = int(input("Введите количество продуктов: "))

    products = {"products":[]}
    for i in range(z):
        name = input("Название: ")
        price = int(input("Цена: "))
        weight = int(input("Вес: "))
        available = bool(input("В наличии (введите 0 или 1): "))
        products["products"].append({"name":name,"price":price,"weight":weight,"available":available})

    inf["products"].extend(products["products"])

    for i in inf["products"]:
        print('\t')
        print("Название:", i["name"])
        print("Цена: ", i["price"])
        print("Вес: ", i["weight"])
        if i["available"]:
            print("В наличии")
        else:
            print("Нет в наличии!")

def p3():
    dictionary = {}

    with open("en-ru.txt", "r") as file:
        for line in file:
            en_w = line.split("-")[0].strip()
            ru_w = line.split("-")[1].strip().split(',')

            for i in ru_w:
                i = i.strip()
                if i in dictionary.keys():
                    dictionary[i] = dictionary[i] + ", " + en_w
                else:
                    dictionary[i] = en_w

    with open("ru-en.txt", "w") as file:
        for i in sorted(dictionary.keys()):
            file.writelines(f"{i} - {dictionary[i]}\n")


p1_p2(), p3()
