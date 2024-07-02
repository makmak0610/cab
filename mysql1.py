import tkinter as tk
from tkinter import ttk
import pymysql

# Establish a connection to the MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='saloni',
    database='converter'
)

cursor = conn.cursor()

# Function to fetch data from the database and populate the Treeview
def load_data():
    # Clear existing data in the Treeview
    tree.delete(*tree.get_children())

    # Fetch data from the table
    cursor.execute("SELECT * FROM data2")
    rows = cursor.fetchall()

    # Populate the Treeview
    for row in rows:
        tree.insert('', 'end', values=row)

# Create the main window
root = tk.Tk()
root.title('PyMySQL Database Table Viewer')

# Create a Treeview widget
tree = ttk.Treeview(root, columns=('Id', 'Username', 'From_currency' ,'To_currency','Amount', 'Convert amount'), show='headings')
tree.heading('Id', text='Id')
tree.heading('Username', text='Username')
tree.heading('From_currency', text='From_currency')
tree.heading('To_currency', text='To_currency')
tree.heading('Amount', text='Amount')
tree.heading('Convert amount', text='Convert amount')


tree.pack()

# Load data into the Treeview
load_data()

# Button to refresh data
refresh_button = tk.Button(root, text='Refresh Data', command=load_data)
refresh_button.pack()

def w1():
    root.destroy()
    import adminwelcome

refresh_button = tk.Button(root, text='Back', command=w1)
refresh_button.pack()
# Run the main loop
root.mainloop()

# Close the cursor and database connection
cursor.close()
conn.close()
