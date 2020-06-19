import PySimpleGUI as sg
import sqlite3
from feladat2 import f2
from feladat3 import f3
from feladat4 import f4
from feladat5 import f5
from feladat6 import f6

#SQL
conn = sqlite3.Connection('nyelvvizsga.db')
c = conn.cursor()
c.execute('DROP TABLE sikeres')
c.execute('DROP TABLE sikertelen')
c.execute('''
         CREATE TABLE IF NOT EXISTS sikeres (
                                       nyelv  TEXT,
                                       '2009'   INTEGER,
                                       '2010'   INTEGER,
                                       '2011'   INTEGER,
                                       '2012'   INTEGER,
                                       '2013'   INTEGER,
                                       '2014'   INTEGER,
                                       '2015'   INTEGER,
                                       '2016'   INTEGER,
                                       '2017'   INTEGER,
                                       '2018'   INTEGER
                                       )
         ''')

conn.commit()

c.execute('''
         CREATE TABLE IF NOT EXISTS sikertelen (
                                       nyelv  TEXT,
                                       '2009'   INTEGER,
                                       '2010'   INTEGER,
                                       '2011'   INTEGER,
                                       '2012'   INTEGER,
                                       '2013'   INTEGER,
                                       '2014'   INTEGER,
                                       '2015'   INTEGER,
                                       '2016'   INTEGER,
                                       '2017'   INTEGER,
                                       '2018'   INTEGER
                                       )
         ''')
conn.commit()

with open('sikeres.csv', 'r', encoding='LATIN2') as sikeres:
    fejlec=sikeres.readline()
    for sor in sikeres:
        s=sor.strip().split(';')
        c.execute("INSERT INTO sikeres VALUES(?,?,?,?,?,?,?,?,?,?,?)", s)
    conn.commit()

with open('sikertelen.csv', 'r', encoding='LATIN2') as sikertelen:
    fejlec=sikertelen.readline()
    for sor in sikertelen:
        s=sor.strip().split(';')
        c.execute("INSERT INTO sikertelen VALUES(?,?,?,?,?,?,?,?,?,?,?)", s)
    conn.commit()
    
a,b,c = f2()
print(f'2. feladat: A legnépszerűbb nyelvek:')
print(f'     {a}')
print(f'     {b}')
print(f'     {c}')
print(f'3. feladat:')
print(f'     Vizsgálandó év: ', end='')
év=f3()
f4(év)
f5()
f6()
