from Functions.libs import *

def check_file_age(filename):
    if not os.path.exists(filename):
        return True
    else:
        file_date_str = filename.split('_')[-1].split('.')[0]
        file_date = datetime.strptime(file_date_str, "%Y-%m-%d")
        return (datetime.now() - file_date).days > 365