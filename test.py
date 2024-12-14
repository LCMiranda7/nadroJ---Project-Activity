import requests
import speedtest
import platform
import psutil

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

def internet_speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        return {
            "Download Speed": f"{download_speed:.2f} Mbps",
            "Upload Speed": f"{upload_speed:.2f} Mbps",
            "Ping": f"{ping:.2f} ms"
        }
    except Exception as e:
        return {
            "Download Speed": "Error fetching speed",
            "Upload Speed": "Error fetching speed",
            "Ping": "Error fetching ping"
        }

def get_system_info():
    try:
        system_info = {
            "Operating System": platform.system(),
            "OS Version": platform.version(),
            "Processor": platform.processor(),
            "Architecture": platform.architecture()[0],
            "RAM Size": f"{psutil.virtual_memory().total / 1_073_741_824:.2f} GB"
        }
        return system_info
    except Exception as e:
        return {
            "Operating System": "Error fetching OS",
            "OS Version": "Error fetching version",
            "Processor": "Error fetching processor",
            "Architecture": "Error fetching architecture",
            "RAM Size": "Error fetching RAM size"
        }

# Main Execution
print("The user's IPv4 address and current location is as follows:")
print(get_location())

print("\nInternet Speed Test Results:")
print(internet_speed_test())

print("\nSystem Information:")
print(get_system_info())
