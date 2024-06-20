import sys
import os
from customtkinter import *
from Pages.MOVIE.company_window import CompanyWindow
from Pages.MOVIE.student_window import StudentWindow
from Pages.MOVIE.professor_window import ProfessorWindow
from Pages.MOVIE.affiliate_window import AffiliateWindow

class Menu_window:
    def __init__(self, master):
        self.master = master
        self.master.title("Menu")
        # Load the icon
        # Get the base path for PyInstaller bundled app
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        icon_path = os.path.join(base_path, "Icons", "movie.ico")
        self.master.iconbitmap(icon_path)
        self.label = CTkLabel(master, text="Choose the platform", font=("Arial", 20, "bold"))

        self.company_btn = CTkButton(master, text="COMPANY", command=self.open_company_page)
        self.student_btn = CTkButton(master, text="STUDENT", command=self.open_student_page)
        self.professor_btn = CTkButton(master, text="PROFESSOR", command=self.open_professor_page)
        self.affiliate_btn = CTkButton(master, text="AFFILIATE", command=self.open_affiliate_page)

    def show(self):
        self.label.grid(row=0, column=1, padx=3, pady=3, sticky="nsew")
        self.company_btn.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.student_btn.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")
        self.professor_btn.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.affiliate_btn.grid(row=2, column=2, padx=20, pady=20, sticky="nsew")

    def open_company_page(self):
        self.open_new_window(CompanyWindow)

    def open_student_page(self):
        self.open_new_window(StudentWindow)

    def open_professor_page(self):
        self.open_new_window(ProfessorWindow)

    def open_affiliate_page(self):
        self.open_new_window(AffiliateWindow)

    def open_new_window(self, window_class):
        self.master.withdraw()
        new_window = window_class(self.master, self.on_new_window_close)
        new_window.window.protocol("WM_DELETE_WINDOW", new_window.on_close)

    def on_new_window_close(self):
        self.master.deiconify()

def setup_window(master):
    menu_window = Menu_window(master)
    menu_window.show()

if __name__ == "__main__":
    root = CTk()
    setup_window(root)
    root.mainloop()
