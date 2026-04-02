from connect import conn, cur


def add_contact(name, phone):
    cur.execute("CALL public.upsert_contact(%s::text, %s::text)", (name, phone))
    conn.commit()

def print_rows(rows):
    if not rows:
        print("No contacts found")
        return

    for i, (name, phone) in enumerate(rows, start=1):
        print(f"{i}. Name: {name} | Phone: {phone}")



def show():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    if not rows:
        print("No contacts found")
        return
    for i, (name, phone) in enumerate(rows, start=1):
        print(f"{i}. Name: {name} | Phone: {phone}")


def insert_many():
    names=[]
    phones=[]
    count=int(input("How many contacts:"))

    for i in range(count):
        name = input(f"Enter name {i+1}: ")
        phone = input(f"Enter phone {i+1}: ")

        names.append(name)
        phones.append(phone)

    cur.execute("CALL insert_m(%s, %s)", (names, phones))
    conn.commit()

    print("Done")


def update_phone(name, new_phone):
    cur.execute("CALL public.upsert_contact(%s::text, %s::text)", (name, new_phone))
    conn.commit()

def update_name(old_name, new_name):
    cur.execute("UPDATE contacts SET name=%s WHERE name=%s", (new_name,old_name))
    conn.commit()

def search_name(name):
    cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (name,))
    rows = cur.fetchall()
    print_rows(rows)

def search_phone(phone):
    cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (phone,))
    rows = cur.fetchall()

    print_rows(rows)
def delete_contact(value):
    cur.execute("CALL public.delete_contact(%s::text)", (value,))
    conn.commit()



while True:
    print("\n1)Add 2)Show 3)Update phone number 4)Update name 5)Delete 6)Search by name 7)Search by phone 8)Insert many contacts 10)Exit")
    n=input("Choose:")

    if n=="1":
        name=input("Name: ")
        phone=input("Phone number: ")
        add_contact(name, phone)
        print("Done")
    elif n=="2":
        show()

    elif n=="3":
        name=input("Name: ")
        new_phon=input("New phone number: ")
        update_phone(name, new_phon)
        print("Done")
    elif n=="4":
        name=input("Name: ")
        new_nam=input("New name: ")
        update_name(name, new_nam)
        print("Done")
    elif n=="5":
        value=input("Enter name or phone: ")
        delete_contact(value)
        print("Done")
    elif n=="6":
        name=input("Enter name to search: ")
        search_name(name)
    elif n=="7":
        phone=input("Enter phone to search: ")
        search_phone(phone)
    elif n=="8":
        insert_many()
    elif n=="10":
        break