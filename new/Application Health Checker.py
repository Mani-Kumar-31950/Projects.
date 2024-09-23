import requests

URL = 'http://youtube.com'
TIMEOUT = 5

def check_health(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        if response.status_code == 200:
            return "UP"
        else:
            return f"DOWN (HTTP Status: {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"DOWN (Error: {e})"

if __name__ == "__main__":
    status = check_health(URL)
    print(f"Application Status: {status}")
