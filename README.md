Instrctions to run the Script:

1.) Install Python: If you haven't already installed Python on your system, download and install it from the official Python website:
 python.org. 
Follow the installation instructions for your operating system.

2.) Install Required Libraries: Open a terminal or command prompt, and install the required libraries using pip, Python's package manager. 
Run the following commands:

pip install requests
pip install pandas

3.) Download the Script: Download the script (Script.py) to your local machine. 
Save it in a directory where you can easily access it.

4.) Find the Restaurant ID: Visit the Swiggy website, navigate to the restaurant page for which you want to fetch the menu, and note down the restaurant ID from the URL.

5.) Run the Script: Open a terminal or command prompt and navigate to the directory where you saved the script (Script.py). Run the script using Python, providing the restaurant ID as a command-line argument. For example:

python Script.py <restaurant_id>
Replace <restaurant_id> with the actual restaurant ID you obtained in step 4.

6.) View Output: After running the script, it will attempt to fetch the menu data from Swiggy's API. If successful, it will print debug information and save the menu data to a CSV file named 'menu.csv' in the same directory. You can open this CSV file in any spreadsheet software to view the menu data.

7.) Troubleshooting: If you encounter any errors or issues while running the script, double-check the restaurant ID, ensure you have an active internet connection, and verify that you've installed the required libraries correctly.


A brief explanation of the script's functionality:--

1. Command-line Argument: The script expects a restaurant ID as a command-line argument. This ID is used to identify the restaurant for which we want to fetch the menu data.

2. API Request: The script constructs a URL for Swiggy's API endpoint using the provided restaurant ID. This URL includes various parameters such as the page type, latitude, longitude, and complete menu flag.

3. HTTP Request: The script makes an HTTP GET request to the constructed API endpoint using the requests library. If the request is successful (status code 200), it receives a JSON response containing menu data.

4. Data Extraction: The script extracts relevant details from the JSON response, such as category names, dish names, prices, and descriptions. It organizes this data into a structured format, such as a list of dictionaries.

5. DataFrame Creation: The script converts the extracted menu data into a pandas DataFrame, which provides a tabular representation of the data with rows and columns. Each row corresponds to a menu item, and columns represent different attributes of the menu items.

6. CSV Output: Finally, the script saves the DataFrame to a CSV file named menu.csv in the current directory. This CSV file contains the menu data in a structured and easily readable format, making it convenient for further analysis or usage.


General setup steps:--

1. Internet Connection: Ensure that your computer has an active internet connection since the script fetches data from Swiggy's API.

2. Python and Required Libraries: Make sure you have Python installed on your system along with the required libraries (requests and pandas). You can install these libraries using pip as described in the earlier instructions.

3. Restaurant ID: You need to know the restaurant ID for the specific restaurant whose menu you want to fetch. You can obtain this ID by visiting the Swiggy website, navigating to the restaurant's page, and noting down the ID from the URL.
