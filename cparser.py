#!usr/bin/python

import argparse
import os, sys
import requests as rq
import json as js
import time
import cconfig as cfg
import text
import debug as _debug

def ogrn_list(olist,debug): # olist - Путь до файла, debug - режим отладки
    with open("api.txt", 'r') as r_api:
        apiKey = r_api.read()
    try:
        print(text.banner_colored)
        ogrn_file = open(olist,"r") 
        ogrn_file.readline() 
        lines = [line.replace("\n",'') for line in ogrn_file] # Убираем \n в строках
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
    try:
        api_key = str(input("Введите свой API-ключ с сайта checko.ru: \n"))
        with open("api.txt",'w') as apifile:
            apifile.write(str(api_key))
            apifile.close()
        print("[Успешно] API-ключ записан.")
        time.sleep(2)
        main()
    except PermissionError:
        print("[Ошибка] Недостаточно прав для совершения данного действия.")
        print("Возможно, антивирус блокирует выполнения скрипта.")
def get_name(debug,name,save,obj):
    with open("api.txt", "r") as r_api:
        apiKey = r_api.read()
    try:
        name_result = rq.get(url=f"https://api.checko.ru/v2/search?key={apiKey}&by=name&obj={obj}&query={name}")
        name_json = name_result.json()
        print(name_json)
    except rq.exceptions.ConnectionError:
        print("[Ошибка] Проверьте подключение к интернету.")

def get_data(debug,company,type,search,save,finances):
    with open("api.txt", 'r') as r_api:
        apiKey = r_api.read()
    try:
        if debug == True:   
            print("Search:" + search)
            print("Type:" + type)
            print("Company:" + company)
        result = rq.get(url=f"https://api.checko.ru/v2/{company}?key={apiKey}&{search}={type}")
        if finances == True:
            fin_result = rq.get(f"https://api.checko.ru/v2/finances?key={apiKey}&{search}={type}")
            fin_json = fin_result.json()

            fin_data = fin_json["bo.nalog.ru"]
            fin_link = fin_data["Отчет"]
            try:
                link_2019 = fin_link["2019"]
                print(f"Отчёт за 2019: {link_2019}")
            except KeyError:
                print("[Финансы] 2019 год - не найдено.")
                pass
            try:
                link_2020 = fin_link["2020"]
                print("Отчёт за 2020:" + link_2020)
            except KeyError:
                print("[Финансы] 2020 год - не найдено.")
                pass
            try:
                link_2021 = fin_link["2021"]
                print("Отчёт за 2021:" + link_2021)
            except KeyError:
                print("[Финансы] 2021 год - не найдено.")
                pass
            try:
                link_2022 = fin_link["2022"]
                print("Отчёт за 2022" + link_2022)
            except KeyError:
                print("[Финансы] 2022 год - не найдено.")
                pass
            try:
                link_2023 = fin_link["2023"]
                print("Отчёт за 2023" + link_2023)
            except KeyError:
                print("[Финансы] 2023 - не найдено")
                pass


# Formatting data 
        if company == "company":
            try:
                result_json = result.json()

                fData = result_json["data"]

                d_ogrn = fData["ОГРН"]
        
                d_inn = fData["ИНН"]

                d_fullname = fData["НаимПолн"]

                d_datareg = fData["ДатаРег"]

                d_status = fData["Статус"]["Наим"]
        
                d_region = fData["Регион"]["Наим"]

                d_adress_city = fData["ЮрАдрес"]["НасПункт"]
        
                d_adress_rf = fData["ЮрАдрес"]["АдресРФ"]

                d_okved_code = fData["ОКВЭД"]["Код"]

                d_okved_naim = fData["ОКВЭД"]["Наим"]

                d_boss = fData["Руковод"]

                for items in d_boss:
                    d_boss_name = items["ФИО"]

                    d_boss_inn = items["ИНН"]

                    d_boss_dol = items["ВидДолжн"]

                    d_boss_naim_dol = items["НаимДолжн"]

                d_meta = result_json["meta"]

                m_request = d_meta["today_request_count"]

                m_balance = d_meta["balance"]
            except KeyError:
                pass
            try:
                
                print(f"ИНФОРМАЦИЯ О {d_fullname} \n")
            
                print(f"ОГРН:{d_ogrn} \n" )
                
                print(f"ИНН: {d_inn} \n")

                print(f"Название организации: {d_fullname} \n")

                print(f"Статус: {d_status} \n")

                print(f"Регион: {d_region} \n")

                print(f"Город: {d_adress_city} \n")

                print(f"Адрес: {d_adress_rf}")

                print(f"ОКВЭД-код: {d_okved_code} \n")

                print(f"Вид деятельности: {d_okved_naim} \n")

                print(f"Руководитель: {d_boss_name} \n")

                print(f"ИНН Руковод.: {d_boss_inn} \n")

                print(f"Должность: {d_boss_dol} \n")

                print(f"Название должности: {d_boss_naim_dol} \n")

                print(f"[Система] Количество запросов сегодня: {m_request} из 100 \n Баланс: {m_balance}")

                filename = d_fullname.replace('"',"")
                if save == True:
                    with open(f"{filename}_result.json", 'w', encoding='utf-8') as json_file: # Записываем данные в json файл
                        js.dump(result_json,json_file, ensure_ascii=False, indent=2) # Записываем данные в json файл
                        print(f"[Успешно] Данные записаны в файл {filename}_result")
            except UnboundLocalError:
                if debug == True:
                    print(UnboundLocalError)
                print("[Ошибка] Не все данные были корректно отображены.")
                pass 

        if company == "entrepreneur":
            try:

                result_json = result.json()

                fData = result_json["data"]

                e_ogrnip = fData["ОГРНИП"]

                e_okpo = fData["ОКПО"]

                e_datareg = fData["ДатаРег"]

                e_name = fData["ФИО"]

                e_type = fData["Тип"]

                e_sex = fData["Пол"]

                e_region = fData["Регион"]

                e_region_code = e_region["Код"]

                e_region_name = e_region["Наим"]

                e_region_city = fData["НасПункт"]

                e_okved = fData["ОКВЭД"]

                e_okved_code = e_okved["Код"]

                e_okved_name = e_okved["Наим"]

                e_fns = fData["РегФНС"]

                e_fns_code = e_fns["КодОрг"]

                e_fns_naim = e_fns["НаимОрг"]
            except KeyError:
                pass
            

            try:
                print(f" Сведения о {e_name}: \n")
                print(f" -------------------------")
                print(f" ОГРНИП: {e_ogrnip} \n")
                print(f"ОКПО: {e_okpo} \n")
                print(f"Дата Регистрации: {e_datareg} \n")
                print(f"Тип ИП: {e_type} \n")
                print(f"Пол: {e_sex} \n")
                print(f"Код региона: {e_region_code} \n")
                print(f"Регион: {e_region_name} \n")
                print(f"Населённый пункт: {e_region_city} \n")
                print(f"Код ОКВЭД: {e_okved_code} \n")
                print(f"Наименование по ОКВЭД: {e_okved_name} \n")
                print(f"Код  ФНС: {e_fns_code} \n")
                print(f"Имя ФНС: {e_fns_naim} \n")
                print(f"------------------------")
            except UnboundLocalError:
                print(UnboundLocalError)
                print("[Ошибка] Не все данные были корректно отображены.")
                pass
    except rq.exceptions.ConnectionError:
        print("[Ошибка] Не удалось получить запрос \n Проверьте подключение и попробуйте снова")
        if debug == True:
            print(rq.exceptions.ConnectionError)
def main ():
    try:
        if os.path.isfile("api.txt") == True: # Проверяем, существует ли файл с API в директории скрипта.
            os.system("cls||clear")

            print(text.banner_colored)

            parser = argparse.ArgumentParser(description="Парсер Юриридческих лиц и ИП")
    
            parser.add_argument("--ogrn","-o",action="store",dest="ogrn",help="Поиск ЮР.ЛИЦ по ОГРН ")
            
            parser.add_argument("--olist",'-ol',dest="olist",help="Поиск ЮР.ЛИЦ по ОГРН из файла. ")

            parser.add_argument("--inn","-i",dest="inn",help="Поиск ЮР.ЛИЦ по ИНН" )

            parser.add_argument("--ilist","-il",dest="iList",help="Поиск ЮР.ЛИЦ по ИНН из файла")

            parser.add_argument("--individuals","-ind",dest='ind',help="Поиск индивидуальных предпринимателей по ОГРН")

            parser.add_argument("--finances","-fnc",action="store_true",dest="finances",help="Получить ссылку на фин.отчёты.")

            parser.add_argument("--name","-n",dest="name",help=""""Поиск по названию. \n
                                Дополнительные аргументы: --namehelp или -nhelp - помощь по поиску
                                -org Поиск компании -ent поиск ИП
                                --foundername или -fn для поиска по ФИО учредителя \n
                                --leadername или -ln для поиска ФИО руководителя \n 
                                --region или -rg указать код региона организации
                                --okved или -od указать код ОКВЭД
                                --active или -act в результатах поиска будут только активные организации
                                --limit или -lim ограничения результатов поиска на одну страницу, по умолчанию 100,
                                --page или -pg номер страницы.Если количество результатов поиска превышает значение limit \n 
                                результаты будут разбиты на несколько страниц и вы сможете использовать данный параметр для просмотра нужной страницы. """)
            
            parser.add_argument("--namehelp","-nhelp",action="store_true",dest="namehelp")
            
            parser.add_argument("-org",action="store_true",dest="n_org")

            parser.add_argument("-ent",action="store_true",dest="n_ent")

            parser.add_argument("--foundername","-fn",dest="foundername")

            parser.add_argument("--leadername","-ln",dest="leadername")

            parser.add_argument("--region","-rg",dest="region")

            parser.add_argument("--save","-s",action="store_true",dest="save",help="Сохранить полную информацию в JSON без форматирования")

            parser.add_argument("--version","-v",help="Отображает текущую версию скрипта",action="version", version=f"Текущая версия crysis: {cfg.version}")

            parser.add_argument("--config","-cfg",dest="argconfig",help="Настройки")
            
            parser.add_argument("--apikey","-ak",action="store_true",help="Перезаписать API-ключ")

            parser.add_argument("--debug","-db",action="store_true",dest="debug",help ="Включить режим отладки")
    
            args = parser.parse_args()

            if args.debug == True: 
                _debug.debug()
                print(args)

            if args.ogrn != None:
                type = args.ogrn
                save = args.save
                finances = args.finances
                search = "ogrn"
                company = "company"
                get_data(args.debug,company,type,search,save,finances)

            if args.olist != None:
                ogrn_list(args.olist,args.debug)

            if args.inn != None:
                type = args.inn
                save = args.save
                finances = args.finances
                search = "inn"
                company = "company"
                get_data(args.debug,company,type,search,save,finances)
            
            if args.ind != None:
                type = args.ind
                save = args.save
                finances = args.finances
                search = "ogrn"
                company = "entrepreneur"
                get_data(args.debug,company,type,search,save,finances)

            if args.apikey == True:
                write_api(args.debug)

            if args.namehelp == True:
                print("""
                      Для того чтобы использовать поиск по имени, нужно вводить дополнительные аргументы \n 
                      Например, для поиска по имени организаций: python cparser.py --name ООО Ладья -org \n
                      -org или -ent являются обязательными аргументами!
                      Подробнее в документации: https://github.com/webcartel-https/crysisparser/wiki/""")

            if args.name != None:
                name = args.name
                debug = args.debug
                save = args.save
                foundername = args.foundername
                leadername = args.leadername
                region = args.region
                if args.n_org == True:
                    obj = "org"
                if args.n_ent == True:
                    obj = "ent"
                get_name(debug,name,save,obj)
        else:
            print("[Предупреждение] API-ключ не записан.")
            time.sleep(2)
            os.system("cls||clear")
            write_api()
    except PermissionError:
        print("!")
if __name__ == '__main__':
    main()

    
   