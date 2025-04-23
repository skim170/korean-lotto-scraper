import requests
from bs4 import BeautifulSoup

def getLastNo():
    req = requests.get('https://www.dhlottery.co.kr/gameResult.do?method=byWin')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    # 회차 크롤링
    no = soup.select('div.win_result > h4 > strong')

    # 최신 회차 번호를 가져온다
    return no[0].text

def crawlingLotto(nums):
    # 로또 이번주 당첨 번호 사이트 주소
    req = requests.get('https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=' + str(nums))
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # 회차 크롤링
    no = soup.select('div.win_result > h4 > strong')
    # 추첨일
    date = soup.select('div.win_result > p')
    # 당첨 번호
    nums_win = soup.select('div.num.win > p > span')
    # 보너스 번호
    nums_bonus = soup.select('div.num.bonus > p > span')

    # 당첨번호를 리스트로 정리
    I = []
    for t in nums_win:
        I.append(t.text)
    
    # 나머지 데이터를 추가
    # I += [nums_bonus[0].text, no[0].text, date[0].text]

    # 정리된 리스트 반환
    return I

if __name__ == "__main__":
    lastno = int(getLastNo()[:-1])

    for i in range(lastno, lastno - 50, -1):
        nums = crawlingLotto(i)
        print(nums)
