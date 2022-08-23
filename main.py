"""main.py scrapes emails from google search results"""
import sys
import time

try:
    from fake_useragent import UserAgent
    from datetime import timedelta
    from packages.utils import emails_to_file, take_input, get_emails, store_urls


except ModuleNotFoundError as e:
    print(e)
    print("Please install dependencies from requirements.txt")


def main():
    searches_items, count, delay, req_delay = take_input()
    print(f"Found {len(searches_items)} search terms!, {searches_items}")
    ua = UserAgent()
    for i, s in enumerate(searches_items):
        unique_emails = []
        if i != 0:
            time.sleep(delay)
        file_name = store_urls(s, count)
        with open(file_name, "r", encoding="utf-8") as url_file:
            for i, url in enumerate(url_file):
                url = url.strip()
                if not url.endswith(".pdf"):
                    time.sleep(req_delay)
                    print(f'{req_delay}s break')
                    emails, msg = get_emails(url.strip(), ua.random)
                    if msg == "break":
                        emails_to_file(s, unique_emails)
                        sys.exit()

                    print(f"url number {i + 1} Status: {msg}")
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
    time_string = "{:0>8}".format(str(timedelta(seconds=time_to_run)))
    print(f"Elapse Time: {time_string} seconds")
