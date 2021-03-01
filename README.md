# Privacy-Policy-WebCrawler
Privacy Policy WebCrawler

Python script that crawls and scrapes privacy policy for information.

The script scapes p, li, td, span, and a tags with associated key words from the specified URL and puts them into a list.
That list gets cleaned and checked for duplicate strings and then sent to google sheets in the corresponding column.

The script also counts the number of strings in each category's list and calculates a score based off the number of strings and then that score is sent to the Google Sheet
