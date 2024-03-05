# Using: https://github.com/celebi-pkg/flight-analysis 
# Keep the dates in format YYYY-mm-dd
from google_flight_analysis.scrape import *
from pathlib import Path  # for filepaths
import pandas as pd
from IPython.display import display

# pd.set_option('display.max_rows', 1000)
# pd.set_option('display.max_columns', 1000)
# pd.set_option('display.width', 1000)

result = Scrape('ATL', 'MYR', '2024-03-22', '2024-03-24')  # obtain our scrape object, represents out query
ScrapeObjects(result)  # runs selenium through ChromeDriver, modifies results in-place
result.data.to_html('Test_Data.html')  # saves the data to a html file
'''
with pd.option_context('display.max_rows', 3, 'display.max_columns', None):
    display(result.data)
print("\nProgram Done.")
'''
