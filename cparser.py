#!usr/bin/python3
#!usr/bin/python

import argparse
import os, sys, platform
import requests as rq
import json as js
import time
import crysisconfig as cfg
import text
import debug as _debug

def ogrn_list(olist,debug): # olist - Путь до файла, debug - режим отладки
    with open("api.txt", 'r') as r_api:
        apiKey = r_api.read()
    try:
        print(text.banner_colored)
        ogrn_file = open(olist,"r") 
        ogrn_file.readline() 
        lines = [line.strip() for line in ogrn_file] # Убираем \n в строках
        if debug == True: # Если включен режим отладки, выводит в терминал значение lines
            _debug.debug()
            print(lines)
        for i in lines:
            result = rq.get(url=f"https://api.checko.ru/v2/company?key={apiKey}&ogrn={i}").json()
            with open(f"{i}",'w', encoding="utf-8") as json_file:
                js.dump(result,json_file,ensure_ascii=False,indent=2)
            print(f"[Успешно] Данные записаны в файл {i}_ogrn_result.json")
            time.sleep(2)
        ogrn_file.close()
    except rq.exceptions.ConnectionError:
        print("[Ошибка] Не удалось получить запрос \n Проверьте подключение и попробуйте снова")

def write_api(): # Записываем API-KEY в файл для дальнейшего использования. 
    api_key = str(input("Введите свой API-ключ с сайта checko.ru: \n"))
    with open("api.txt",'w') as apifile:
        apifile.write(str(api_key))
        apifile.close()
    print("[Предупреждение] API-ключ записан. \n [Предупреждение] Не удаляйте файл api.txt.")
    time.sleep(2)
    main()

def get_data_inn(inn):
    with open("api.txt", 'r') as r_api:
        apiKey = r_api.read()
    try:
        print(text.banner_colored)
        result = rq.get(url=f"https://api.checko.ru/v2/company?key={apiKey}&inn={inn}").json()
        with open(f"{inn}_inn_result.json", 'w', encoding='utf-8') as json_file: # Записываем данные в json файл
            js.dump(result,json_file, ensure_ascii=False, indent=2) # Записываем данные в json файл
        print(f"[Успешно] Данные записаны в файл INN:{inn}_result.json")
    except rq.exceptions.ConnectionError:
        print("[Ошибка] Не удалось получить запрос \n Проверьте подключение и попробуйте снова")
        error_choise = input("[Ошибка] Попробовать снова? [y] или [n]")
        if error_choise == "y" or "Y":
            time.sleep(1)
            main()
        else: os.exit(0)

def get_data_ogrn(ogrn):
    with open("api.txt", 'r') as r_api:
        apiKey = r_api.read()
    try:
        print(text.banner_colored)
        result = rq.get(url=f"https://api.checko.ru/v2/company?key={apiKey}&ogrn={ogrn}").json()
        with open(f"{ogrn}_ogrn_result.json", 'w', encoding='utf-8') as json_file: # Записываем данные в json файл
            js.dump(result,json_file, ensure_ascii=False, indent=2) # Записываем данные в json файл
        print(f"[Успешно] Данные записаны в файл {ogrn}_result.json")
    except rq.exceptions.ConnectionError:
        print("[Ошибка] Не удалось получить запрос \n Проверьте подключение и попробуйте снова")
        error_choise = input("[Ошибка] Попробовать снова? [y] или [n]")
        if error_choise == "y" or "Y":
            time.sleep(1)
            main()
        else: os.exit(0)

def main ():
    try:
        if os.path.isfile("api.txt") == True: # Проверяем, существует ли файл с API в директории скрипта.
            os.system("cls||clear")

            parser = argparse.ArgumentParser(description="Парсер Юриридческих лиц и ИП")
    
            parser.add_argument("--ogrn","-o",action="store",dest="ogrn",help="Поиск по ОГРН")
            
            parser.add_argument("--olist",'-ol',dest="olist",help="Парсинг большого количества данных. Укажите путь к файлу .txt")

            parser.add_argument("--inn","-i",dest="inn",help="Поиск по ИНН")

            parser.add_argument("--name","-n",dest="name",help="Поиск по названию или имени")

            parser.add_argument("--version","-v",help="Отображает текущую версию скрипта",action="version", version=f"Текущая версия crysis: {cfg.version}")
            
            parser.add_argument("--apikey","-ak",action="store_true",help="Перезаписать API-ключ")

            parser.add_argument("--credits",'-cr',action="store_true",help="Информация об авторе")

            parser.add_argument("--debug","-db",action="store_true",dest="debug",help ="""Включить режим отладки. Если вы столкнулись с багами
                                включите режим отладки, сделайте скриншот и создайте тему на github, либо пришлите мне на prvtangl@gmail.com""")
    
            args = parser.parse_args()

            if args.debug == True: 
                _debug.debug()
                print(args)

            if args.ogrn != None: 
                get_data_ogrn(args.ogrn,args.debug)

            if args.olist != None:
                ogrn_list(args.olist,args.debug)

            if args.inn != None:
                get_data_inn(args.inn,args.debug)

            if args.credits == True:
                print(text.colored_credits)
                print(text.credits_text)

            if args.apikey == True:
                write_api(args.debug)

        else:
            print("[Предупреждение] API-ключ не записан.")
            time.sleep(2)
            print("[Предупреждение] API-ключ не записан.")
            time.sleep(2)
            os.system("cls||clear")
            write_api()
    except ConnectionError:
        print("!")
if __name__ == '__main__':
    main()

    
   