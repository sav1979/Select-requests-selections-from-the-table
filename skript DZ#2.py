# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 13:58:44 2022

@author: sklad_2
"""

import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:admin@locaihost:5432/схема ДЗ №3.drawio')
engine

connection = engine.connect()

connection.execute("""import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:admin@locaihost:5432/схема ДЗ №3.drawio')
engine

connection.execute("""SELECT album_name, year_of_release FROM List_albums
                   WHERE year_of_release >= 2018;
        """)
        
connection.execute("""SELECT title_track, time FROM List_tracks  
                   WHERE time ORDER BY time ASC
                   LIMIT 1;
        """)
        
connection.execute("""SELECT title_track, time FROM List_tracks 
                   WHERE time >= 3,5;
        """)
        
connection.execute("""SELECT name_collection FROM name_collection and 
                   SELECT year_of_release FROM List_albums     
                  WHERE year_of_release ('2018', '2019', '2020');
        """)
        
connection.execute("""SELECT nickname FROM cataloge_executors    
                   WHERE nickname not LIKE '%% %%'
        """)
        
connection.execute("""SELECT title_track FROM List_tracks    
                   WHERE title_track '%% мой/my %%'
        """)