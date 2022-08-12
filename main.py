import sys
import time

try:
    from fake_useragent import UserAgent
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
    print(f"URL count: {count}")
    ua = UserAgent()
    try:
        for s in searches_items:
            unique_emails = []
            file_name = store_urls(s, count)
            with open(file_name, "r", encoding="utf-8") as url_file:
                urls = url_file.readlines()
            for i, url in enumerate(urls):
                emails = get_emails(url, ua.random)
                print(f'Url#{i + 1} out of {len(urls)} finished!')
                if emails:
                    for email in emails:
                        if email not in unique_emails:
                            unique_emails.append(email)
            emails_to_file(s, unique_emails)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("Starting the script (ctrl+c to exit)")
    start_time = time.perf_counter()
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting!')
        sys.exit()
    end_time = time.perf_counter()
    print("Elapse Time: ", int(end_time - start_time), "seconds")
