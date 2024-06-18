import customtkinter
from customtkinter import *
from Scripts import *

class AffiliateWindow:
    def __init__(self, master):
        self.master = master
        self.window = CTkToplevel(master)
        self.window.geometry("500x240")
        self.window.iconbitmap(".\\Icons\\movie.ico")
        self.window.title("Affiliate Window")

        self.go_back_btn = CTkButton(self.window, text="←", height=1, width=50, command=self.go_back,fg_color="#144870", hover_color="#08253b")
        self.go_back_btn.grid(row=0, column=0, padx=0, pady=0, sticky="w")
        
        # AFFILIATE BUTTONS
        self.create_account_aff_btn = customtkinter.CTkButton(self.window, text="Create Account", fg_color="#144870", hover_color="#08253b", command=self.btn_create_affiliate_account)
        self.create_account_aff_btn.grid(row=3, column=2, padx=3, pady=20, sticky="nsew")
        
        self.create_request_aff_btn = customtkinter.CTkButton(self.window, text="Create Account Requests", fg_color="#144870", hover_color="#08253b", command=self.btn_create_affiliate_request)
        self.create_request_aff_btn.grid(row=3, column=3, padx=3, pady=20, sticky="nsew")
        
    def go_back(self):
        self.window.destroy()  
        self.master.deiconify()  

# AFFILIATE BUTTONS
    def btn_create_affiliate_account(self):
        create_affiliate_account_func()
    
    def btn_create_affiliate_request(self):
        create_affiliate_request_func()
        
if __name__ == "__main__":
    root = CTk()  
    app = AffiliateWindow(root)
    root.mainloop()
