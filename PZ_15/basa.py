import sqlite3 as sq
from data import info_lek, info_nal, info_punkt

with sq.connect("apteka.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS lekarstva(
    id_prep INTEGER PRIMARY KEY AUTOINCREMENT,
    name_prep VARCHAR(30),
    primenenie VARCHAR(70),
    country VARCHAR(20),
    price DECIMAL
    )""")

with sq.connect("apteka.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS nalichie(
    id_prep INTEGER,
    quantity DECIMAL,
    date_isp DATE,
    FOREIGN KEY (id_prep) REFERENCES lekarstva(id_prep) ON DELETE CASCADE ON UPDATE CASCADE
    )""")
    
with sq.connect("apteka.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS apt_punkt(
    no_punkta INTEGER PRIMARY KEY AUTOINCREMENT,
    address_punkta VARCHAR(60),
    name_prep VARCHAR(30),
    applications DECIMAL,
    application_date DATE,
    order_price DECIMAL,
    FOREIGN KEY (name_prep) REFERENCES lekarstva(name_prep) ON DELETE CASCADE ON UPDATE CASCADE
    )""")
    
with sq.connect("apteka.db") as con:
    cur = con.cursor() 
    cur.executemany("INSERT INTO lekarstva VALUES (?,?,?,?,?)", info_lek)
     
with sq.connect("apteka.db") as con:
    cur = con.cursor() 
    cur.executemany("INSERT INTO nalichie VALUES (?,?,?)", info_nal)

with sq.connect("apteka.db") as con:
    cur = con.cursor() 
    cur.executemany("INSERT INTO apt_punkt VALUES (?,?,?,?,?,?)", info_punkt)


# SELECT (8/8)
    
# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("SELECT * FROM nalichie WHERE quantity < 10")
#     result1 = cur.fetchall()
# print(result1)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("SELECT * FROM lekarstva WHERE country = 'Россия'")
#     result2 = cur.fetchall()
# print(result2)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("SELECT * FROM lekarstva WHERE price < 1000 ORDER BY name_prep")
#     result3 = cur.fetchall()
# print(result3)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("SELECT * FROM nalichie WHERE date_isp > '2020-12-01'")
#     result4 = cur.fetchall()
# print(result4)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("SELECT * FROM lekarstva WHERE price < 1000 ")
#    result5 = cur.fetchall()
# print(result5)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("SELECT * FROM lekarstva WHERE id_prep IN (SELECT id_prep FROM nalichie WHERE quantity < 200 )")
#    result7 = cur.fetchall()
# print(result7)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("SELECT * FROM apt_punkt WHERE no_punkta IN (SELECT id_prep FROM nalichie WHERE date_isp > '2021-09-30' )")
#    result8 = cur.fetchall()
# print(result8) 

# UPDATE (13/13)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("UPDATE nalichie SET date_isp = '2023-10-11' WHERE id_prep = 4")
#    result1 = cur.fetchall()
# print(result1)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("UPDATE lekarstva SET price = price + price*0.20  WHERE name_prep = 'метформин' ")
#     result2 = cur.fetchall()
# print(result2)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("UPDATE nalichie SET quantity = 100 WHERE id_prep = 5")
#     result3 = cur.fetchall()
# print(result3)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("UPDATE lekarstva SET price = price + price*0.20 ")
#     result4 = cur.fetchall()
# print(result4)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("UPDATE nalichie SET quantity = quantity - ( RANDOM( ) + quantity ) WHERE id_prep = 5")
#    result22 = cur.fetchall()
# print(result22)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("UPDATE nalichie SET quantity = quantity + ( RANDOM( ) + quantity ) WHERE id_prep = 6")
#    result32 = cur.fetchall()
# print(result32)

#    cur.execute ("UPDATE lekarstva SET price = 1000 ")
#    result42 = cur.fetchall()
# print(result42)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("UPDATE nalichie SET date_isp = '2021-09-30' ")
#    result5 = cur.fetchall()
# print(result5)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("UPDATE lekarstva SET name_prep = 'Аскорутин', primenenie = 'для профилактики', country = 'Россия', price = 20 WHERE id_prep = 9 ")
#    result6 = cur.fetchall()
# print(result6)

# В 7 задании нужно сделать тоже самое.(Преподаватель сказал просто изменять информацию,которую просят в первой части задания.)
# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("UPDATE lekarstva SET name_prep = 'hdjgdkl', primenenie = 'для профилактики', country = 'Франция', price = 800 WHERE id_prep = 9 ")
#    result7 = cur.fetchall()
# print(result7)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("UPDATE lekarstva SET price = 20 WHERE id_prep = 9 ")
#    result8 = cur.fetchall()
# print(result8)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("UPDATE lekarstva SET name_prep = 'мяу', primenenie = 'для профилактики', country = 'Германия', price = 8999 WHERE id_prep = 3 ")
#    result9 = cur.fetchall()
# print(result9)

# В 10 задании нужно сделать, по сути, тоже самое.
# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("UPDATE lekarstva SET name_prep = 'kakoeto lekarstvo', primenenie = 'для профилактики', country = 'Ямайка', price = 1000 WHERE id_prep = 4 ")
#    result10 = cur.fetchall()
# print(result10)

# DELETE (15/15)

#with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("DELETE FROM nalichie WHERE date_isp > '2021-09-30' ")
#    result1 = cur.fetchall()
#print(result1)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("DELETE FROM lekarstva WHERE country = 'США' and price < 75*10 ")
#     result2 = cur.fetchall()
# print(result2)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("DELETE FROM apt_punkt WHERE order_price > 75*50 ")
#     result3 = cur.fetchall()
# print(result3)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("DELETE FROM nalichie WHERE quantity = 0 ")
#     result4 = cur.fetchall()
# print(result4)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("DELETE FROM lekarstva WHERE country = 'Россия' ")
#     result5 = cur.fetchall()
# print(result5)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("DELETE FROM apt_punkt WHERE applications > 10 ")
#     result6 = cur.fetchall()
# print(result6)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("DELETE FROM nalichie WHERE date_isp > '2021-10-01' ")
#     result7 = cur.fetchall()
# print(result7)    

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("DELETE FROM lekarstva WHERE price > 75*100 ")
#     result8 = cur.fetchall()
# print(result8)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("DELETE FROM apt_punkt WHERE name_prep IN (SELECT name_prep FROM lekarstva WHERE country = 'Германия')")
#     result9 = cur.fetchall()
# print(result9)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("DELETE FROM lekarstva WHERE name_prep LIKE 'а%' ")
#     result10 = cur.fetchall()
# print(result10)

# with sq.connect("apteka.db") as con:
#     cur = con.cursor()
#     cur.execute ("DELETE FROM lekarstva WHERE country = 'США' AND price > 50*75 ")
#     result12 = cur.fetchall()
# print(result12)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("DELETE FROM apt_punkt WHERE name_prep IN (SELECT name_prep FROM lekarstva WHERE country = 'Россия')")
#    result13 = cur.fetchall()
# print(result13)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("DELETE FROM apt_punkt WHERE no_punkta IN (SELECT id_prep FROM nalichie WHERE quantity = 0)")
#    result14 = cur.fetchall()
# print(result14)

# with sq.connect("apteka.db") as con:
#    cur = con.cursor()
#    cur.execute ("DELETE FROM apt_punkt WHERE no_punkta IN (SELECT id_prep FROM nalichie WHERE quantity = 0)")
#    result15 = cur.fetchall()
# print(result15)

