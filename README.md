![image](https://github.com/user-attachments/assets/2c8a9642-2a01-4672-a13d-73df77f2fbfb)


# 🧾 Korean Lotto Results Scraper

This is a simple Python script that scrapes the latest winning numbers from the official Korean Lotto website (https://www.dhlottery.co.kr).

## 📌 Description

The script fetches the most recent round number and retrieves winning numbers for the last 50 draws. It uses `requests` and `BeautifulSoup` for web scraping.

## 🔧 Features

- Automatically gets the latest draw number
- Scrapes main winning numbers (excluding bonus number)
- Loops through the last 50 draw rounds
- Clean and beginner-friendly code

## 🛠️ Built With

- Python 3
- `requests`
- `beautifulsoup4`

## ▶️ How to Run

1. Install dependencies (if not already installed):
   ```bash
   pip install requests beautifulsoup4
2. Run the script:
   python lotto_scraper.py
3. You'll see the winning numbers for the last 50 draws printed in the console.

## 📄 Notes
- Bonus number and draw date are already parsed in the code but currently commented out. You can easily enable them if needed.
- You can modify the range in the loop to get more or fewer results.
