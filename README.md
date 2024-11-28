---
# Rightmove Property Scraper

A web scraping project developed with [Scrapy](https://scrapy.org/) to extract property data from the Rightmove website. This project collects detailed information on properties for sale in London, including addresses, property types, bedrooms, transactions, and geographical coordinates.

---
## Table of Contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

---
## Description

This project uses Scrapy to scrape property data from the Rightmove website. It handles pagination, scraping up to the third page of results. The collected data is structured and can be used for real estate market analysis, price forecasting, or other property-related applications.

---
### Key Features:
- **Data Extraction**: Collects property data such as address, property type, number of bedrooms, transactions, and geolocation.
- **Pagination**: Handles pagination, automatically navigating to the next page to scrape more data (up to the third page).
- **JSON Parsing**: Uses JSON parsing for dynamically loaded data on the page.
- **Error Handling**: Logs parsing errors and pages without properties.

---
## Prerequisites

Before running the project, ensure that you have the following dependencies installed:

- Python 3.6 or higher
- Scrapy (version 2.5.0 or higher)

---
### Dependencies

You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```
---
## Installation

### 1. Clone the repository

Clone the project to your local machine using Git:

```bash
git clone https://github.com/marcellin-d/Rightmove-Property-Scraper.git
cd rightmove-scraper
```

### 2. Create a virtual environment (optional but recommended)

To manage dependencies, it is highly recommended to create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- On **Windows**:

```bash
venv\Scripts\activate
```

- On **macOS/Linux**:

```bash
source venv/bin/activate
```

### 3. Install dependencies

Install the required dependencies via pip:

```bash
pip install -r requirements.txt
```

### 4. Set up your Scrapy project

Ensure that your Scrapy project is set up correctly. The `scrapy.cfg` file and other necessary files should be present in the project directory.

## Usage

To run the spider and collect property data, use the following command:

```bash
scrapy crawl rightmoveSpider
```

This will start the scraping process and save the results in a CSV, JSON, or other formats depending on your configuration in `settings.py`.

---
### Parameters

- **Pages**: The spider collects data from the first to the third page of Rightmove search results.
- **Output Format**: By default, results are saved in JSON format.

You can modify these parameters as needed in the `settings.py` file.

---
## Project Structure

Here’s the basic structure of the Scrapy project:

```
rightmove-scraper/
├── rightmoveSpider.py            # Main spider to scrape data
├── scrapy.cfg                    # Scrapy project configuration
├── items.py                      # Item definitions
├── pipelines.py                  # Pipelines for data processing
├── settings.py                   # Scrapy settings configuration
├── requirements.txt              # List of dependencies
└── README.md                     # This README file
```
---
### File Details:

- **rightmoveSpider.py**: Contains the spider responsible for data extraction and pagination.
- **items.py**: Defines the fields for the extracted data (e.g., address, property type, etc.).
- **settings.py**: Contains the project configuration for Scrapy, including user-agent settings, pipelines, and other parameters.


___
## 📫 Contact

For questions or suggestions, feel free to reach out:  
- **Name**: Marcellin DJAMBO
- **Email**: djambomarcellin@gmail.com
- **LinkedIn**: [My LinkedIn Profile](https://www.linkedin.com/in/marcellindjambo)
