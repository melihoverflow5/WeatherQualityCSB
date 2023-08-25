# Weather Quality Data Fetcher From CSB

[![PyPI version](https://badge.fury.io/py/WeatherQualityCSB.svg)](https://pypi.org/project/WeatherQualityCSB/0.1/)

This utility is designed to fetch weather quality data from the CSB website and save it as an Excel file.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Attributes](#attributes)
- [Methods](#methods)
- [Credits](#credits)

## Prerequisites

Ensure you have the following libraries installed:
- pytest
- os
- sys
- time
- json
- logging
- tqdm
- selenium
- custom module \`validations\` (containing \`validate_locations\`, \`validate_date\`, and \`validate_params\`)

You should also have ChromeDriver installed and available in your PATH to use with the Selenium WebDriver.

## Usage

To use the \`WeatherQuality\` class, simply initialize it with the desired parameters and then call the \`run\` method:

\```python
locations = {"Ankara": ["Etimesgut", "Sincan"]}
dates = ("DD-MM-YYYY HH:MM", "DD-MM-YYYY HH:MM")
params = ["Parameter1", "Parameter2"]

weather_quality_fetcher = WeatherQuality(locations=locations, dates=dates, params=params, logs=True)
weather_quality_fetcher.run()
\```

## Attributes

- \`locations\`: Dictionary where the keys are city names, and the values are lists of district names.
- \`dates\`: Tuple containing the start and end dates in the format \`(start_date, end_date)\`.
- \`params\`: (Optional) List of parameters to select when fetching data.
- \`headless\`: (Optional) Determines if the browser runs in headless mode (i.e., no GUI).
- \`download_path\`: (Optional) Path to the directory where the Excel file will be downloaded.
- \`logs\`: (Optional) Determines if progress logs should be printed to the console.
### You can look for parameters from [CSB's site](https://sim.csb.gov.tr/STN/STN_Report/StationDataDownloadNew).

## Methods

- \`__init__\`: Initializes the \`WeatherQuality\` instance.
- \`run\`: Initiates the process to fetch weather quality data from the CSB website and download it as an Excel file.
- Private methods for various tasks (e.g., selecting cities, selecting districts, etc.)

## Credits

Developed by [Melih Taşkın] as a utility to simplify and automate the process of fetching weather quality data.
