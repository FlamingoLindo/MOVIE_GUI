from customtkinter import *
from Pages.MOVIE.company_window import CompanyWindow
from Pages.MOVIE.student_window import StudentWindow
from Pages.MOVIE.professor_window import ProfessorWindow
from Pages.MOVIE.affiliate_window import AffiliateWindow

class Menu_window:
    def __init__(self, master):
        self.master = master
        self.master.title("Menu")
        self.master.iconbitmap(".\\Icons\\aaaaa.ico")
        self.label = CTkLabel(master, text="Choose the project", font=("Arial", 20, "bold"))
        
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

    def hide(self):
        self.label.grid_forget()
        self.company_btn.grid_forget()
        self.student_btn.grid_forget()
        self.professor_btn.grid_forget()
        self.affiliate_btn.grid_forget()

    def open_company_page(self):
        self.master.withdraw()  # Hide the main window
        CompanyWindow(self.master)  # Create and display the GeneralWindow instance

    def open_student_page(self):
        self.master.withdraw()
        StudentWindow(self.master)
        
    def open_professor_page(self):
        self.master.withdraw()
        ProfessorWindow(self.master)
        
    def open_affiliate_page(self):
        self.master.withdraw()
        AffiliateWindow(self.master)

def setup_window(master):
    menu_window = Menu_window(master)
    menu_window.show()

if __name__ == "__main__":
    root = CTk()
    setup_window(root)
    root.mainloop()
