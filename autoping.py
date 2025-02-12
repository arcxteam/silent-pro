import requests
import time
import threading

position_url = "https://ceremony-backend.silentprotocol.org/ceremony/position"
ping_url = "https://ceremony-backend.silentprotocol.org/ceremony/ping"
token_file = "tokens.txt"

def load_tokens():
    try:
        with open(token_file, "r") as file:
            tokens = [line.strip() for line in file if line.strip()]
            print(f"{len(tokens)} tokens loaded.")
            return tokens
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return []

def get_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

def get_position(token):
    try:
        response = requests.get(position_url, headers=get_headers(token))
        if response.status_code == 200:
            data = response.json()
            print(f"[Token {token[:6]}...] Position: Behind {data['behind']}, Time Remaining: {data['timeRemaining']}")
            return data
        print(f"[Token {token[:6]}...] Failed to fetch position. Status: {response.status_code}")
    except Exception as e:
        print(f"[Token {token[:6]}...] Error fetching position: {e}")

def ping_server(token):
    try:
        response = requests.get(ping_url, headers=get_headers(token))
        if response.status_code == 200:
            data = response.json()
            print(f"[Token {token[:6]}...] Ping Status: {data}")
            return data
        print(f"[Token {token[:6]}...] Failed to ping. Status: {response.status_code}")
    except Exception as e:
        print(f"[Token {token[:6]}...] Error pinging: {e}")

def run_automation(token):
    while True:
        get_position(token)
        ping_server(token)
        time.sleep(10)

def main():
    tokens = load_tokens()
    if not tokens:
        print("No tokens available. Exiting.")
        return
    
    threads = []
    for token in tokens:
        thread = threading.Thread(target=run_automation, args=(token,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
