from packages.utils import get_emails
from fake_useragent import UserAgent
ua = UserAgent()

ems = get_emails('https://en.wikipedia.org/wiki/Email', ua.random)
print(ems)