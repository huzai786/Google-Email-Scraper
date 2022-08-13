import sys
import time
import cProfile

try:
    from requests_html import HTMLSession
    from fake_useragent import UserAgent
    from humanfriendly import format_timespan
    from packages.utils import (
        emails_to_file,
        take_input,
        get_emails,
        store_urls
    )


except ModuleNotFoundError as e:
    print(e)
    print("Please install dependencies from requirements.txt")





def main():
    searches_items, count = take_input()
    print(f"Found {len(searches_items)} search terms!, {searches_items}")
    ua = UserAgent()
    session = HTMLSession()
    for s in searches_items:
        unique_emails = []
        file_name = store_urls(s, count)
        with open(file_name, "r", encoding="utf-8") as url_file:
            for i, url in enumerate(url_file):
                url = url.strip()
                if not url.endswith('.pdf'):
                    emails, msg = get_emails(url.strip(), ua.random, session)
                    print(f'url number {i + 1} Status: {msg}')
                    if emails:
                        for email in emails:
                            if email not in unique_emails:
                                if email.endswith((".com", ".net", ".org")):
                                    unique_emails.append(email)
                    else:
                        continue
        emails_to_file(s, unique_emails)




if __name__ == "__main__":
    print("Starting the script (ctrl+c to exit)")
    start_time = time.perf_counter()
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    except RuntimeError:
        sys.exit()
    except Exception:
        sys.exit()
    end_time = time.perf_counter()
    
    time_to_run = int((end_time - start_time))
    print(f"Elapse Time: {time_to_run} seconds")
    
