import dotenv import load_dotenv
import os
import pandas as pd

# load dotenv
load_dotenv()


class FredDataCollector:
    def __init__(self):
        self.api_key = os.getenv("FRED_API_KEY")
        
    def get_economic_data(self, start_date: str, end_date: str = "Today") -> pd.Series:
        """
        Fetches Relevant information from FRED database,
        using the environment API Key. Uses Dates to get
        best information
        """
    
    def get_gdp_data(self, country: str, start_date: str, end_date: str = "Today"):
        """_summary_

        Args:
            country (str): Country/State for GDP Analysis
            start_date (str): Date to begin intended observations
            end_date (str): last date needed for necessary information.
            Defaults to today if not specified
        """
        pass

class AlphaVantageCollector:
    
    def __init__(self):
        self.api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    
class NewsCollector:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
    
    def collect(self):
        """
        Collects Sample News Data
        """