import customtkinter as ctk

ctk.set_default_color_theme('blue')
ctk.set_appearance_mode('System')

app = ctk.CTk() # Create the main window

app.title('ORM Generator')
app.geometry('800x600')
app.register('home', 'Home')

# Title
label = ctk.CTkLabel(app, text="Générateur ORM personnalisé", font=("Arial", 18))
label.pack(pady=20)

# Dropdown SQL
options = ['MySQL', 'PostgreSQL', 'SQLite', 'Oracle']
dropDownSql = ctk.CTkOptionMenu(app, values=options)
dropDownSql.pack(pady=10)

app.mainloop()