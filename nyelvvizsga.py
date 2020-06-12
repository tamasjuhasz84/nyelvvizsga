import PySimpleGUI as sg
import sqlite3

#SQL
conn = sqlite3.Connection('nyelvvizsga.db')
c = conn.cursor()
c.execute('''
         CREATE TABLE IF NOT EXISTS sikeres (
                                       nyelv  TEXT
                                       2009   INTEGER
                                       2010   INTEGER
                                       2011   INTEGER
                                       2012   INTEGER
                                       2013   INTEGER
                                       2014   INTEGER
                                       2015   INTEGER
                                       2016   INTEGER
                                       2017   INTEGER
                                       2018   INTEGER
                                       )
         ''')
conn.commit()

c.execute('''
         CREATE TABLE IF NOT EXISTS sikertelen (
                                       nyelv  TEXT
                                       2009   INTEGER
                                       2010   INTEGER
                                       2011   INTEGER
                                       2012   INTEGER
                                       2013   INTEGER
                                       2014   INTEGER
                                       2015   INTEGER
                                       2016   INTEGER
                                       2017   INTEGER
                                       2018   INTEGER
                                       )
         ''')
conn.commit()

c.execute