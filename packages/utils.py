import os
import re
import requests
from googlesearch import search
from typing import Generator


def store_urls(search_term: str, total_urls: int) -> str:
    try:
        file_name = re.sub("\s", "_", search_term)
        fpath = os.path.join(os.getcwd(), "files", f"{file_name}_urls.txt")
        with open(fpath, "w") as fn:
            urls = search(f"{search_term}", num_results=total_urls)
            print("getting urls....")
            for url in urls:
                fn.write(url)
                fn.write("\n")
        print(f"{fname} created!")
        return fpath

    except Exception as e:
        print(e)


def get_emails(url: str, user_agent):
    headers = {"User-Agent": f"{user_agent}"}
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            html_text = str(res.text)
            print(html_text)
            emails = re.findall(r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)", html_text)
            return emails
        else:
            pass
    except requests.RequestException as e:
        print(e)
        pass


def take_input():
    print("Enter the search term (comma separated if more than one values): ")
    search = input("> ")
    search_list = search.split(",")
    search_list = [s.strip() for s in search_list]
    while True:
        try:
            count = int(input("Enter the total number of urls to scrape: "))
            break
        except ValueError:
            print("Please enter a number")
            continue
    return search_list, count


def emails_to_file(search_term, emails):
    file_name = re.sub("\s", "_", search_term)
    output_file_path = os.path.join(os.getcwd(), "output", f"{file_name}_emails.txt")

    with open(output_path, "w", encoding="utf-8") as file_write:
        for email in emails:
            file_write(email)
            file_write("\n")
    print(f"{file_name}_emails.txt Created!")
