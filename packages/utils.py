import os
import re
import sys
import requests
from fake_useragent import UserAgent
from googlesearch import search
from typing import Generator


def store_urls(search_term: str, total_urls: int) -> str:
    """Store the urls from google search results"""
    
    file_name = re.sub("\s", "_", search_term)
    fpath = os.path.join(os.getcwd(), "files", f"{file_name}_urls.txt")
    print("getting urls....")
    
    try:
        urls = search(f"{search_term}", num_results=total_urls)
        with open(fpath, "w", encoding='utf-8') as fn:
            for url in urls:
                fn.write(url)
                fn.write("\n")
            print(f"{file_name}_url.txt created!")
            return fpath

    except Exception as e:
        print(e)



def extract_emails(html_text: str) -> list:
    """Regex to extract email from html text"""
    
    pattern = r'[\w.+-]+@[\w-]+\.[\w.-]+'
    matches = re.findall(pattern, html_text)
    return matches



def get_emails(url: str, user_agent: UserAgent) -> list:
    """Download html content from the url and scrapes and returns emails from it"""

    headers = {"User-Agent":f"{user_agent}"}
    emails = []
    try:
        res = requests.get(url, headers=headers, timeout=5)
        if res.status_code == 200:
            html_text = str(res.text)
            emails = extract_emails(html_text)
            return emails, 'Successful'
        
        else:
            return [], 'Unsuccessful'
        
    except KeyboardInterrupt:
        sys.exit()
    
    except ConnectionResetError as e:
        return [], f'Unsuccessful Error: {e}'
    
    except requests.ReadTimeout as e:
        return [], f'Unsuccessful Error: {e}'
    
    except requests.RequestException as e:
        return [], f'Unsuccessful Error: {e}'
    
    except Exception as e:
        return [], f'Unsuccessful Error: {e}'



def take_input():
    """ Take input from user """
    
    print("Enter the search term (comma separated if more than one values): ")
    search = input("> ")
    search_list = search.split(",")
    search_list = [s.strip() for s in search_list]
    delay = 1
    if len(search_list) > 1:
        print('Delay between each keyword search (seconds): ')
        delay = int(input('> '))
    while True:
        try:
            count = int(input("Enter the total number of urls to scrape: "))
            break
        except ValueError:
            print("Please enter a number")
            continue
    return search_list, count, delay




def emails_to_file(search_term: str, emails: list) -> None:
    """Create an absolute file path from the search term and dump emails into it"""
    
    file_name = re.sub("\s", "_", search_term)
    output_file_path = os.path.join(os.getcwd(), "output", f"{file_name}_emails.txt")

    with open(output_file_path, "w", encoding="utf-8") as file_write:
        for email in emails:
            file_write.write(email)
            file_write.write("\n")
    print(f"{file_name}_emails.txt Created!")
