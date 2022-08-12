from packages.utils import get_emails
from fake_useragent import UserAgent
import os
import re

# ua = UserAgent()

# ems = get_emails('https://en.wikipedia.org/wiki/Email', ua.random)
# print(ems)
file_name = 'python'
fpath = os.path.join(os.getcwd(), "files", f"{file_name}_urls.txt")
print(type(fpath))