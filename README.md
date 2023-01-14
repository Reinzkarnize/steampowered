# steampowered
This package utilizes a web scraping method to collect data from the steam powered website, and converts it into various formats such as JSON, CSV and Excel files.

## HOW IT WORK?
This package will scrape the game details from [steam store](https://store.steampowered.com/) using requests and save the results in multiple formats using pandas. Here is what the package will do:

1. Use requests to scrape product detail from the given game search.
2. Use pandas to create a DataFrame with the scraped data.
3. Save the DataFrame as JSON, CSV, and Excel files.
4. The output files will be saved in the current working directory.

## HOW TO USE
To use this package, follow these steps:

1. Open a terminal window.
2. Type py main.py and press Enter.
3. When prompted, enter the games that you want to scrape.
4. The script will automatically scrape data from the given URL and produce the output in a folder called "result".

## Author
Fauzi Kurniawan