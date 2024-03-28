# Keep the dates in format YYYY-mm-dd
from google_flight_analysis.scrape import *


def create_flight_table(start, destination, start_date, end_date):
    result = Scrape(start, destination, start_date, end_date)  # obtain our scrape object, represents out query
    ScrapeObjects(result)  # runs selenium through ChromeDriver, modifies results in-place
<<<<<<< HEAD
    result.data.to_html('python/templates/Test_Data.html')  # save the data to a html file
    
=======
    result.data.to_html('python/static/Test_Data.html')  # save the data to a html file
>>>>>>> a162e262ded52e2f23d93217690f6ca993643ba6


# only run for testing if this is main file
if __name__ == '__main__':
    # pd.set_option('display.max_rows', 1000)
    # pd.set_option('display.max_columns', 1000)
    # pd.set_option('display.width', 1000)
    # Scrape('ATL', 'MYR', '2024-04-22', '2024-04-24')
    create_flight_table('MYR', 'GSP', '2024-04-22', '2024-04-24')
    func = open('python/templates/Test_Data.html','a')
    func.write("<link rel='stylesheet' href='styles.css'>")
    func.close()
'''
with pd.option_context('display.max_rows', 3, 'display.max_columns', None):
    display(result.data)
print("\nProgram Done.")
'''
