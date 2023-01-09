
import requests
from bs4 import BeautifulSoup


def crawling(soup):
  result = []
  tbody = soup.find('tbody')
  for p in tbody.find_all('p', class_ = 'title'):
    result.append(p.get_text().replace('\n', ''))
  return result

def main():
  # 코드 작성후 , crawling 함수에 객체 전살(soup)]
  custom_header ={
  'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
  }

  url = 'https://music.bugs.co.kr/chart/'
  req = requests.get(url, headers = custom_header)
  # soup 객체
  soup = BeautifulSoup(req.text, "html.parser")
  result = crawling(soup)
  print(result)
  

if __name__ == "__main__":
  main()