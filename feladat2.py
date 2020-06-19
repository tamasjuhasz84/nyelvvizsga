def f2():

    import sqlite3

    conn = sqlite3.Connection('nyelvvizsga.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM sikeres''')
    nyelvek=c.fetchall()
    szótár = {}
    for sor in nyelvek:
        osszes=sum(sor[1:])
        szótár.update({sor[0]:osszes})


    c.execute('''SELECT * FROM sikertelen''')
    nyelvek=c.fetchall()
    for sor in nyelvek:
        osszes=sum(sor[1:])
        szótár[sor[0]] +=osszes

    vödör=sorted(szótár.items(), key=lambda x:x[1], reverse=True)
    return(vödör[0][0],vödör[1][0],vödör[2][0])
