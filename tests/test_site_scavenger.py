import os
import shutil
from site_scavenger import WebsiteDownloader


def test_website_downloader():
    # Create a temporary directory for testing
    test_folder = "test_download"
    downloader = WebsiteDownloader("https://example.com", test_folder)

    # Run the download_website method
    downloader.download_website()

    # Check if the index.html file was created
    assert os.path.isfile(os.path.join(test_folder, "index.html"))

    # Clean up the temporary directory
    shutil.rmtree(test_folder)


if __name__ == "__main__":
    test_website_downloader()
