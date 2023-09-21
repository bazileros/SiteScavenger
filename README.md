# Site Scavenger

Back in the "real" world, I put my Python skills to work and created Site Scavenger. It's a tool that lets you capture entire websites for offline viewing, no matter where you are. Whether you're stuck on a desert island, deep in the Amazon rainforest, or just on a slow internet connection, Site Scavenger has your back!

So, here it is, a little piece of my island adventure brought to life in the form of Site Scavenger. I hope it serves you well, whether you're stranded on an island or just looking for a convenient way to browse websites offline.





Site Scavenger is a Python script that allows you to download an entire website for offline viewing, including HTML pages and associated resources.

## Usage

1. Clone the repository:
   
   ```bash
   git clone https://github.com/bazileros/SiteScavenger.git
   cd SiteScavenger
   ```

2. Check if you have `venv` installed (Python 3.3 and higher include it by default). If not, install it:
   
   ```bash
   python3 -m venv --help
   ```
   
    If you see the `venv` help message, it's already installed. If not, you can install it using the following:
   
   ```bash
   # On macOS and Linux
   sudo apt-get install python3-venv
   
   # On Windows
   python -m pip install virtualenv
   ```
   
   Using a virtual environment helps isolate project dependencies and avoid conflicts with other Python projects.

3. Create and activate a virtual environment:
   
   ```bash
   # On macOS and Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. Install the required dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

5. Run the script:
   
   ```bash
   python3 site_scavenger.py
   ```

6. Follow the prompts to enter the website URL and target folder.

## Requirements

- Python 3.6+
- `requests`, `beautifulsoup4`, and `wget` libraries (see `requirements.txt`)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This Python script allows you to download an entire website for offline viewing, including HTML pages and associated resources.

## Usage

1. Clone the repository:
   
   ```bash
   git clone https://github.com/bazileros/SiteScavenger.git
   cd SiteScavenger
   ```

2. Install the required dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   
   ```bash
   python3 site_scavenger.py
   ```

4. Follow the prompts to enter the website URL and target folder.

## Requirements

- Python 3.6+
- `requests`, `beautifulsoup4`, and `wget` libraries (see `requirements.txt`)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
