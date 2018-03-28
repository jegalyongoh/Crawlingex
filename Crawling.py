from urllib.request import urlopen              # url을 열기위해 urlopen을 import 한다
from bs4 import BeautifulSoup                   # 크롤링을하기위해 BeautifulSoup를 한다
import pymysql                                  # 이 예제는 크롤링한 내용을 DB에 담는 예제이므로 pymysql도 import 한다

conn = pymysql.connect(host='127.0.0.1', port=3307, user='root', passwd='a1234', db='bucketlist')   # DB 접속
cur = conn.cursor()


url = "https://www.rottentomatoes.com//"    # 크롤링하고싶은 페이지 url 입력
html = urlopen(url)
source = html.read()                            # 소스를 읽는다
html.close()                                    # 모두 진행한 후 close 해준다
index = 0

soup = BeautifulSoup(source, "html5lib")
table = soup.find(id="Top-Box-Office")
movies = table.find_all(class_="middle_col")
grade = table.find_all(class_="tMeterScore")
print(movies)
""" for movie in movies:
    title = movie.get_text()
    title.strip()
    link = movie.a.get('href')
    url = 'https://www.rottentomatoes.com' + link
    gra = grade[index].get_text()
    query = "INSERT soup VALUES('%s', '%s', '%s')" % (title, url, gra)
    cur.execute(query)
    conn.commit()
    print("DB 입력 완료 title = %s , url = %s ,grade = %s " % (title, url, gra))
    index += 1 """
