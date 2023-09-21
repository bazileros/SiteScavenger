import os
import requests
from bs4 import BeautifulSoup
import wget


class WebsiteDownloader:
    """
    A class for downloading an entire website for offline viewing.

    Args:
        url (str): The URL of the website to download.
        folder (str): The target folder where the website will be saved.

    Methods:
        create_target_folder: Create the target folder for saving the website.
        download_website: Download the entire website, including linked pages and resources.
        download_page: Download an HTML page and its associated resources.
        save_html_content: Save the HTML content of a page to a file.
        download_resource: Download a resource (e.g., image, stylesheet, script) and save it.
    """

    def __init__(self, url, folder):
        self.url = url
        self.folder = folder

    def create_target_folder(self):
        """
        Create the target folder for saving the website.

        Returns:
            str: The full path to the target folder.
        """
        folder_path = os.path.join(os.getcwd(), self.folder)
        os.makedirs(folder_path, exist_ok=True)
        return folder_path

    def download_website(self):
        """
        Download the entire website, including linked pages and resources.
        """
        folder_path = self.create_target_folder()
        self.download_page(self.url, folder_path)

    def download_page(self, url, folder):
        """
        Download an HTML page and its associated resources.

        Args:
            url (str): The URL of the page to download.
            folder (str): The target folder where the page will be saved.
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.save_html_content(soup, folder)

        for resource in soup.find_all(['img', 'link', 'script']):
            resource_url = resource.get('src') or resource.get('href')
            if resource_url:
                self.download_resource(resource_url, folder)

    def save_html_content(self, soup, folder):
        """
        Save the HTML content of a page to a file.

        Args:
            soup (BeautifulSoup): The parsed HTML content of the page.
            folder (str): The target folder where the HTML file will be saved.
        """
        with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as html_file:
            html_file.write(soup.prettify())

    def download_resource(self, url, folder):
        """
        Download a resource (e.g., image, stylesheet, script) and save it.

        Args:
            url (str): The URL of the resource to download.
            folder (str): The target folder where the resource will be saved.
        """
        try:
            wget.download(url, out=folder)
        except Exception as e:
            print(f"Failed to download {url}: {str(e)}")


if __name__ == '__main__':
    website_url = input("Enter URL: ")
    output_folder = input("Enter target folder: ")

    downloader = WebsiteDownloader(website_url, output_folder)
    downloader.download_website()
