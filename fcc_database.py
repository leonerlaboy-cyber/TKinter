from tkinter import *
import sqlite3


def submit():

    # Create database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    # Insert into table
    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            }
    )

    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

def query():
    # Create database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    # Query the database
    c.execute('SELECT *, oid FROM addresses')
    records = c.fetchall() #other options include fetchone and fetchmany(*insert how mnay*)
    # print(records)

    # Loop through results
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

root = Tk()
root.geometry('400x400')

# Databases

# Create database or connect to one
conn = sqlite3.connect('address_book.db')

# create cursor
c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE addresses 
#           (
#           first_name text,
#           last_name text,
#           address text,
#           city text,
#           state text,
#           zipcode integer
#           )
# ''')

# Create Text Box Labels
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)

address_label = Label(root, text='address')
address_label.grid(row=2, column=0)

city_label = Label(root, text='city')
city_label.grid(row=3, column=0)

state_label = Label(root, text='state')
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text='zipcode')
zipcode_label.grid(row=5, column=0)

# Create text entry

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)


l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)


address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)


zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# Create submit button

submit_button = Button(root, text='Add record to database', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button

query_button = Button(root, text='Show Records', command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Commit changes
conn.commit()

# Close connection
conn.close()

mainloop()