#Kérjen be a felh asználótól egy évet! Ellenőrizze, hogy a bekért év 2009 és 2017 között
#van! A program futása csak akkor folytatódjon, ha a felhasználó helyes értéket ad meg.
#(Feltételezheti, hogy a felhasználó számot ad meg.)

def f3():
#    print('Kérem adjon meg egy évet 2009 és 2017 között.')
    a='kezdő'
    év=1
    while a!= év:
        a = int(input())
        if 2008< a <2018:
            év = a
        else:
            print('Helytelen év. Kérem adjon meg egy évet 2009 és 2017 között.')
    return év

if __name__ == "__main__":
    print(f3())