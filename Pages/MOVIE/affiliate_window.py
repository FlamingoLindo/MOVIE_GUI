import customtkinter
from customtkinter import *
from Scripts import *

class AffiliateWindow:
    def __init__(self, master, on_close_callback):
        self.master = master
        self.on_close_callback = on_close_callback
        self.window = CTkToplevel(master)
        self.window.geometry("500x240")
        self.window.title("Affiliate Window")

        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        icon_path = os.path.join(base_path, "Icons", "movie.ico")
        self.master.iconbitmap(icon_path)

        # AFFILIATE BUTTONS
        self.create_account_aff_btn = customtkinter.CTkButton(self.window, text="Create Account", fg_color="#144870", hover_color="#08253b", command=self.btn_create_affiliate_account)
        self.create_account_aff_btn.grid(row=0, column=2, padx=3, pady=20, sticky="nsew")

        self.create_request_aff_btn = customtkinter.CTkButton(self.window, text="Create Account Requests", fg_color="#144870", hover_color="#08253b", command=self.btn_create_affiliate_request)
        self.create_request_aff_btn.grid(row=0, column=3, padx=3, pady=20, sticky="nsew")

        # Override the close button
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def btn_create_affiliate_account(self):
        create_affiliate_account_func()

    def btn_create_affiliate_request(self):
        create_affiliate_request_func()

    def on_close(self):
        self.on_close_callback()
        self.window.destroy()

if __name__ == "__main__":
    root = CTk()
    app = AffiliateWindow()
    root.mainloop()

