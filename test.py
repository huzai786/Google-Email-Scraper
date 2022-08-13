import requests
import sys
from requests_html import HTMLSession
from fake_useragent import UserAgent
from packages.utils import extract_emails
from humanfriendly import format_timespan
import pstats


ua = UserAgent()


session = HTMLSession()

# with open('files/copyright_email_urls.txt', 'r') as f: 
#     for u in f:
#         try:
#             res = session.get(u.strip())
#             res.html.render(sleep=1, scrolldown=0, wait=1, timeout=30)
#             print(res.status_code)            
#             emails = extract_emails(str(res.html.html))
#             print(emails)
#         except requests.RequestException as e:
#             print('error', u)
#             print(e)
        
# url = "https://www.analyticsinsight.net/why-do-developers-cherish-python-despite-its-biggest-downsides/"
# res = session.get(url)
# res.html.render(sleep=1, scrolldown=0, wait=1, timeout=30)
# print(res.status_code)
# # with open('data.html', 'w', encoding='utf-8') as f:
#     # f.write(str(res.text))
# emails = extract_emails(res.html.html)
# print(emails)

