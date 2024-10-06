# web-scraper
a simple web scraper in Python

## steps to run
1. install dependencies
    ```
    asdf install

    poetry install
    ```
2. execute web-scraper
    ```
    python3 main.py
    ```
    sample output:
    ```
    begin web-scraper...
    number of links scraped from base https://docs.ray.io/en/latest/index.html till depth 2: 288
    ```
    (OR)
    ```
    time python3 main.py
    ```
    sample output:
    ```
    begin web-scraper...
    number of links scraped from base https://docs.ray.io/en/latest/index.html till depth 2: 288
    python3 main.py  11.48s user 0.24s system 25% cpu 46.391 total
    ```