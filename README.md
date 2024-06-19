pip install customtkinter tkinter selenium python-dotenv pyautogui 

pyinstaller --onefile --add-data "Icons;Icons" --add-data "Pages;Pages" --add-data "Scripts;Scripts" --add-data ".env;." --add-data "chromedriver.exe;." --icon="C:\\Users\\josef\\Desktop\\MOVIE_GUI\\Icons\\movie.ico" --noconsole main.py
