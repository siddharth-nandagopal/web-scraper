# web-scraper
a simple web scraper in Python & parallelize it with Ray to speed up

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
    INFO worker.py:1786 -- Started a local Ray instance.
    number of links scraped from base https://docs.ray.io/en/latest/index.html till depth 2: 288
    python3 main.py  4.80s user 2.83s system 10% cpu 1:14.73 total
    ```

    ```
    begin web-scraper...
    INFO worker.py:1786 -- Started a local Ray instance.
    web-scraper parallely run on 6 links
    339
    339
    339
    200
    200
    200
    python3 main.py  4.00s user 2.22s system 10% cpu 58.924 total
    ```