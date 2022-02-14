# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:34:39 2022

@author: sklad_2
"""

import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:admin@locaihost:5432/схема ДЗ №3.drawio')
engine

connection = engine.connect()

connection.execute("""INSERT INTO cataloge_executors
        VALUES(1 2 3 4 5 6 7 8,
               Хабиб Batrai Ханна & Миша Марвин Клава Кока Сергей Завьялов Мот Роберт Катчиев Гербер,
               1 2 3 4 5);
        """)

connection.execute("""INSERT INTO List_albums
        VALUES(1 2 3 4 5 6 7 8, 
               1 2 3 4 5 6 7 8,
               Разрывная Самба Французский поцелуй ЛА ЛА ЛА Джентльмен Remote Разошлись Карьера,
               2010 2020 2018 2017 2018);
        """)
        
connection.execute("""INSERT INTO List_tracks
        VALUES(1 2 3 4 5 6 7 8, 
               1 2 3 4 5 6 7 8 9 10 11 12 13 14 15,
               НЕЖНОСТЬ  КУКУШКА  СЛАВЬСЯ  ВЕЧНАЯ ВЕСНА ВРЕМЯ КОЛОКОЛЬЧИКОВ  ВЕСНА  ВСЕ КАК У ЛЮДЕЙ  
               БАЛЛАДА ОБ УХОДЕ В РАЙ  РОДНАЯ  КОНЬ  КВАДРАТЫ  НАТАЛИ  ТЕАТР ТЕНЕЙ  СЕРЫЙ ГОЛУБЬ  КОСОВО ПОЛЕ,
               2,56 3,12, 3,42 3,58, 4,04 3,23 2,47 3,17 4,29 3,41 3,26 4,58 2,49 3,27 2,52);
        """)
        
connection.execute("""INSERT INTO List_of_genres 
        VALUES(1 2 3 4 5,
               Блюз Джаз Шансон Рок Поп );
        """)
        
connection.execute("""INSERT INTO List_repertoire
        VALUES(1 2 3 4 5 , 
               1 2 3 4 5 6 7 8,
               1 2 3 4 5 6 7 8,
               1 2 3 4 5 6 7 8 9 10 11 12 13 14 15);
        """)        
        
connection.execute("""INSERT INTO name_collection
        VALUES(1 2 3 4 5 6 7 8, 
               name 1 name 2 name 3 name 4 name 5 name 6 name 7 name 8,
               1 2 3 4 5 6 7 8 9 10 11 12 13 14 15,
               1 2 3 4 5 6 7 8);
        """)