# Check and download input files for new problems
# Run this every morning/day
import datetime
import os
import requests

year = "2024"

current_day = datetime.date.today().day
days = range(1, current_day+1)

base_url = "https://adventofcode.com"

with open("session-cookie") as session_cookie_file:
    session_cookie = session_cookie_file.readline().strip()
    cookies = {
        "session": session_cookie
    }
    print(cookies)
    for day in days:
        remote_path = f"{base_url}/{year}/day/{day}/input"
        local_dir = f"{year}/day{day}"
        local_path = f"{local_dir}/input"
        if not os.path.exists(local_dir):
            os.mkdir(local_dir)
            print(f"Creating new directory {local_dir}")

        response = requests.get(remote_path, cookies=cookies, stream=True)
        print(response)
        # Check if the request was successful
        if response.status_code == 200:
            with open(local_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # Filter out keep-alive chunks
                        file.write(chunk)
            print(f"File downloaded successfully to {local_path}")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")


