1. DOWNLOAD THE PROJECT FILE
2. EXTRACT THE CONTENT SOME WHERE IN YOUR PC
3. OPEN THE PROJECT FOLDER
4. OPEN THE FOLDER NAMED 'dist'
5. EXECUTE THE main.exe

IF IT DOES NOT WORK YOU ARE GOING TO HAVE TO PASTE THE LINE BELOW AND PASTE IT IN YOUR TERMINAL

pip install customtkinter tkinter selenium python-dotenv pyautogui pandas


![buh](https://github.com/FlamingoLindo/MOVIE_GUI/assets/101421364/ac28ee4d-4ab2-4706-9bb7-18459fddaa57)

pyinstaller --onefile --add-data "Icons;Icons" --add-data "Pages;Pages" --add-data "Scripts;Scripts" --add-data ".env;." --add-data "chromedriver.exe;." --icon="C:\\Users\\josef\\Desktop\\MOVIE_GUI\\Icons\\movie.ico" --noconsole main.py



