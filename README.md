# Web Scraping OLX with Python
This project is a simple web scraping application that extracts real estate offer data from the OLX website using Python. 
The extracted data is then stored in a SQLite database.
## Usage
To run the script, navigate to the project directory and execute the following command in your terminal:
### python project.py setup
This command sets up the SQLite database where the data will be stored.

To parse the OLX website, execute the following command:
### python project.py

This command will scrape data from the first 25 pages of the real estate offers in Malopolskie region. 
The extracted data will be stored in the SQLite database.

## Libraries
The following libraries were used in this project:

-BeautifulSoup - for parsing HTML

-Requests - for making HTTP requests

-SQLite - for creating and interacting with the SQLite database

## Functionality
The script extracts the following data from each offer:

Title
Price
Location
The parse_price function formats the price to a float value. The script then inserts the data into the SQLite database.

Optionally, the script can also print offers with a price less than 150,000 PLN located in Krakow.

## Future Improvements
This project is a simple implementation of web scraping using Python. Improvements that can be made in the future include:

Adding error handling for different scenarios
Extracting more data from each offer (e.g., description, number of rooms)
Providing more options for filtering and sorting the extracted data


### Project is no longer supported, so there is no guarantee that it is working on a current version of OLX
