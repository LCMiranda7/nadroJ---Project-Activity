import requests

def get_ip():
    # Fetch public IPv4 address
    response = requests.get('https://api.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_address = get_ip()
    try:
        # Fetch location data from ipinfo.io
        response = requests.get(f'https://ipinfo.io/{ip_address}/json').json()
        location_data = {
            "IPv4 Address": ip_address,
            "City": response.get("city", "Unknown"),
            "Region": response.get("region", "Unknown"),
            "Country": response.get("country", "Unknown"),
            "Organization": response.get("org", "Unknown"),
        }
    except requests.exceptions.RequestException:
        location_data = {
            "IPv4 Address": ip_address,
            "City": "Error fetching location",
            "Region": "Error fetching location",
            "Country": "Error fetching location",
            "Organization": "Error fetching location",
        }
    return location_data

print("The user's IPv4 address and current location is as follows:")
print(get_location())
