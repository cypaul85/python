from crawler import crawl

url="https://www.instagram.com/"
pageContent = crawl(url)

print(pageContent)