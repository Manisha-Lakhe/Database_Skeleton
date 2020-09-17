import sqlite3

db = sqlite3.connect('lybrary.sqlite')

def add():
    record = 0
    db.execute("CREATE TABLE IF NOT EXISTS lybrary(name TEXT, price INTEGER)")
    print("Enter the details: \n")
    nameip = input("Name of the book :")
    priceip = input("Price of the book :")
    db.execute("INSERT INTO lybrary values('{}', {})".format(nameip,priceip))
    record = record+1


def update():
      up_book = input("Enter the name of the book to be updated : ")
      new_book = input("Enter the new name of the book : ")
      new_price = input("Enter the price of the book : ")
      db.execute("UPDATE lybrary SET name = '{0}',price = {1} WHERE name = '{2}'".format(new_book, new_price,up_book))


def delete():
      del_book = input("Enter the name of the book to be deleted : ")
      db.execute("DELETE FROM lybrary WHERE name = '{}'".format(del_book))
def display():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM lybrary')
    for row in cursor:
        print(row)

def errorHandler():
    print("Error Occured! Plz try again!")

print('~' *80)
print('~'*36 + "LYBRARY" + '~'*37)
print('~'*35 + "MANAGEMENT" + '~'*35)
print('~' *80)

while True:
      print('MENU:\n'
            '1.ADD\n'
            '2.UPDATE\n'
            '3.DELETE\n'
            '4.DATABASE\n'
            '5.EXIT')

      choice = int(input("Enter Your Choice: "))
      operations = {
        1: add,
        2: update,
        3: delete,
        4: display,
        5: exit
      }
      operations.get(choice, errorHandler)()
