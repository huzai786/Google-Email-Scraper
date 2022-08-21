<b><i> Google Email Scraper </i></b>

#### A command line scraper that scrapes emails from the results return by google search
---

## Application Format
user will be prompted to enter following:
 *keyword: query to search for
  *to pass multiple keywords, seperate them with comma (,)
 *Url_Count: total number of url to scrape
 *keyword_delay: Delay between each keyword (if multiple keyword supplied)
 *request_delay: Delay between each request


## Output
All txt files are stored in /output with the corresponding keyword name as prefix.


## Set Up
1. In the Google-Email-Scraper root directory, clone the project using 
```
git clone https://github.com/huzai786/fix-script.git
```

2. Set up a virtual environment
```
python -m venv venv
```

3. Activate the virtual environment
- Windows: `env\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

4. Install required packages
```
pip install -r requirements.txt
```

## TO RUN:
```
$ py main.py 
