from tkinter import *
from tkinter import ttk, messagebox
import csv

from database import *

create_database()

root = Tk()
root.title("NayePankh Foundation")
root.geometry("1000x700")
root.configure(bg="#f4f6f8")

# ================= TITLE =================

title = Label(
    root,
    text="NayePankh Foundation Volunteer Management System",
    font=("Arial", 20, "bold"),
    bg="#f4f6f8",
    fg="#1f3b4d"
)
title.pack(pady=15)

# ================= FORM =================

form_frame = Frame(root, bg="#f4f6f8")
form_frame.pack()

Label(form_frame, text="Name", bg="#f4f6f8").grid(row=0, column=0, padx=10, pady=5)
name_entry = Entry(form_frame, width=25)
name_entry.grid(row=0, column=1)

Label(form_frame, text="Age", bg="#f4f6f8").grid(row=1, column=0, padx=10, pady=5)
age_entry = Entry(form_frame, width=25)
age_entry.grid(row=1, column=1)

Label(form_frame, text="City", bg="#f4f6f8").grid(row=2, column=0, padx=10, pady=5)
city_entry = Entry(form_frame, width=25)
city_entry.grid(row=2, column=1)

Label(form_frame, text="Phone", bg="#f4f6f8").grid(row=3, column=0, padx=10, pady=5)
phone_entry = Entry(form_frame, width=25)
phone_entry.grid(row=3, column=1)

# ================= FUNCTIONS =================

def clear_fields():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    city_entry.delete(0, END)
    phone_entry.delete(0, END)

def refresh_table(data=None):

    for row in tree.get_children():
        tree.delete(row)

    if data is None:
        data = get_all_volunteers()

    for record in data:
        tree.insert("", END, values=record)

    update_report()

def save_volunteer():

    name = name_entry.get()
    age = age_entry.get()
    city = city_entry.get()
    phone = phone_entry.get()

    if name.strip() == "":
        messagebox.showerror(
            "Error",
            "Name is required"
        )
        return

    if not age.isdigit():
        messagebox.showerror(
            "Error",
            "Age must be a number"
        )
        return

    if not phone.isdigit():
        messagebox.showerror(
            "Error",
            "Phone must contain only numbers"
        )
        return
    
    if volunteer_exists(phone):
        messagebox.showerror(
        "Duplicate Entry",
        "Volunteer with this phone number already exists"
    )
    return

    add_volunteer(name, age, city, phone)

    messagebox.showinfo(
        "Success",
        "Volunteer Added Successfully"
    )

    clear_fields()
    refresh_table()

def search_data():

    keyword = search_entry.get()

    if keyword == "":
        refresh_table()
        return

    data = search_volunteer(keyword)
    refresh_table(data)

def delete_selected():

    selected = tree.focus()

    if not selected:
        messagebox.showerror(
            "Error",
            "Please select a volunteer"
        )
        return

    values = tree.item(selected)["values"]
    volunteer_id = values[0]

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this volunteer?"
    )

    if not confirm:
        return

    delete_volunteer(volunteer_id)

    messagebox.showinfo(
        "Deleted",
        "Volunteer Deleted Successfully"
    )

    refresh_table()

    delete_volunteer(volunteer_id)

    messagebox.showinfo(
        "Deleted",
        "Volunteer Deleted Successfully"
    )

    refresh_table()

def update_report():

    total = total_volunteers()

    report_label.config(
        text=f"Total Volunteers: {total}"
    )

def export_csv():

    data = get_all_volunteers()

    with open(
        "volunteers_report.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Name", "Age", "City", "Phone"]
        )

        writer.writerows(data)

    messagebox.showinfo(
        "Success",
        "CSV Report Exported Successfully"
    )

# ================= BUTTONS =================

Button(
    form_frame,
    text="Add Volunteer",
    width=15,
    command=save_volunteer,
    bg="lightgreen"
).grid(row=4, column=0, pady=10)

Button(
    form_frame,
    text="Clear",
    width=15,
    command=clear_fields,
    bg="lightyellow"
).grid(row=4, column=1)

# ================= SEARCH =================

search_frame = Frame(root, bg="#f4f6f8")
search_frame.pack(pady=10)

Label(
    search_frame,
    text="Search Volunteer:",
    bg="#f4f6f8"
).pack(side=LEFT)

search_entry = Entry(search_frame, width=30)
search_entry.pack(side=LEFT, padx=5)

Button(
    search_frame,
    text="Search",
    command=search_data
).pack(side=LEFT)

Button(
    search_frame,
    text="Show All",
    command=lambda: refresh_table()
).pack(side=LEFT, padx=5)

# ================= TABLE =================

columns = (
    "ID",
    "Name",
    "Age",
    "City",
    "Phone"
)

# ================= TABLE =================

table_frame = Frame(root)
table_frame.pack(pady=15)

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical"
)

columns = (
    "ID",
    "Name",
    "Age",
    "City",
    "Phone"
)

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=15,
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=tree.yview)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180)

tree.pack(side=LEFT)
scrollbar.pack(side=RIGHT, fill=Y)

# ================= ACTION BUTTONS =================

Button(
    root,
    text="Delete Selected Volunteer",
    command=delete_selected,
    bg="#ff9999",
    width=25
).pack()

Button(
    root,
    text="Export CSV Report",
    command=export_csv,
    bg="#87CEEB",
    width=25
).pack(pady=5)

# ================= REPORT =================

report_label = Label(
    root,
    text="Total Volunteers: 0",
    font=("Arial", 14, "bold"),
    bg="#f4f6f8"
)

report_label.pack(pady=15)

# ================= FOOTER =================

footer = Label(
    root,
    text="Developed for NayePankh Foundation Internship Project",
    bg="#f4f6f8",
    fg="gray"
)

footer.pack(side=BOTTOM, pady=10)

refresh_table()

root.mainloop()