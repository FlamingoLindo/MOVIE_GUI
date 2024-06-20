import os

# Get the absolute path of the Python script
def get_python_location():
    return os.path.dirname(os.path.abspath(__file__))

# Load the chromedriver.exe file
def load_chromedriver():
    local = get_python_location()
    chromedriver_path = os.path.join(local, "chromedriver.exe")
    chromedriver_path = chromedriver_path.replace('\\', '/')
    if os.path.isfile(chromedriver_path):
        return chromedriver_path
    else:
        raise FileNotFoundError(f"chromedriver.exe not found at {chromedriver_path}")


# Load the affiliates file
def load_aff_xlsx():
    local = get_python_location()
    aff_xlsx = os.path.join(local, "import_affiliates.xlsx")
    aff_xlsx = aff_xlsx.replace('\\', '/')
    if os.path.isfile(aff_xlsx):
        return aff_xlsx
    else:
        raise FileNotFoundError(f"Excel not found at {aff_xlsx}")
        
# Load the students file
def load_stu_xlsx():
    local = get_python_location()
    stu_xlsx = os.path.join(local, "import_students.xlsx")
    stu_xlsx = stu_xlsx.replace('\\', '/')
    if os.path.isfile(stu_xlsx):
        return stu_xlsx
    else:
        raise FileNotFoundError(f"Excel not found at {stu_xlsx}")
        
# Load the professors file
def load_pro_xlsx():
    local = get_python_location()
    pro_xlsx = os.path.join(local, "import_teachers.xlsx")
    pro_xlsx = pro_xlsx.replace('\\', '/')
    if os.path.isfile(pro_xlsx):
        return pro_xlsx
    else:
        raise FileNotFoundError(f"Excel not found at {pro_xlsx}")


"""def test_load_chromedriver():
    try:
        path = load_aff_xlsx()
        print(f"Chromedriver found at: {path}")
    except FileNotFoundError as e:
        print(e)

# Run the test function
test_load_chromedriver()"""