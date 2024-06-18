from customtkinter import *
import Pages.menu_window as menu_window

def hide_all():
    if menu_window:
        menu_window_instance = menu_window.Menu_window(win) 
        menu_window_instance.hide()  
    
def show_menu():
    hide_all()
    menu_window_instance = menu_window.Menu_window(win) 
    menu_window_instance.show()  
    
win = CTk()
win.geometry('550x200')

menu_window.setup_window(win)

show_menu()

win.mainloop()
