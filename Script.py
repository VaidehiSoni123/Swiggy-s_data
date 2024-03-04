import requests
import pandas as pd
import sys

def get_menu(restaurant_id):
    # API endpoint URL for fetching menu data
    api_url = f"https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=18.56&lng=73.95&restaurantId={restaurant_id}"
    print("API URL:", api_url)
    
    # Send a GET request to the API endpoint
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract relevant details from the response JSON
        menu_data = []
        for category in response.json()['data']['menu']['categories']:
            category_name = category['name']
            for item in category['items']:
                name = item['name']
                price = item['price']
                description = item.get('description', '')
                menu_data.append({'Category': category_name, 'Name': name, 'Price': price, 'Description': description})
        
        return menu_data
    else:
        print("Failed to fetch data. Status Code:", response.status_code)
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <restaurant_id>")
        sys.exit(1)

    restaurant_id = sys.argv[1]
    print(f"Fetching menu for restaurant ID: {restaurant_id}...")
    
    # Get menu data
    menu_data = get_menu(restaurant_id)
    
    if menu_data:
        print("Menu data fetched successfully:")
        for item in menu_data:
            print(item)
        
        # Convert data to DataFrame
        df = pd.DataFrame(menu_data)
        
        # Save DataFrame to CSV
        df.to_csv('menu.csv', index=False)
        print("Menu data saved to menu.csv")
    else:
        print("No menu data found.")

