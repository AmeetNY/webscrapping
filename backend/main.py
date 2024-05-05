import requests
from bs4 import BeautifulSoup

def scrape_article_titles(url):
    """
    Scrapes article titles from the given URL and prints them.
    
    Parameters:
    url (str): The URL of the webpage to scrape.
    """
    try:
        # Fetch the webpage data with SSL verification disabled
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Raise an exception for bad status codes
        webpage_content = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(webpage_content, 'html.parser')
        titles = soup.select("MAGGI")  # Modify this selector based on the website structure

        if titles:
            print(f"Found {len(titles)} article titles.")
            for index, title in enumerate(titles, start=1):
                print(f"{index}. {title.get_text()}")
        else:
            print("No article titles found.")

    except requests.exceptions.RequestException as e:
        # Handle any network-related or request exceptions
        print(f"Error fetching webpage: {e}")

def main():
    # Define the target URL to scrape
    #url = "https://news.ycombinator.com/"
    url = "https://www.mynestle.in"
    # Call the scraping function
    scrape_article_titles(url)

# Ensure the main function is called only if this script is run directly
if __name__ == "__main__":
    main()
