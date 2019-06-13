import requests
import bs4
import json
import pandas as pd

def crawl(keyword):

    url = "https://search.shopping.naver.com/search/all.nhn?query=에어컨&cat_id=&frm=NVSHATC"
    data = requests.get(url)
    print(data.status_code,url)

    return data.content

def get_productinfo(li):
    try:
        img = li.find("img")
        alt = img['alt']

        if li.find("span", {"class":"_price_reload"}):
            price = li.find("span", {"class":"_price_reload"})
        else:
            price = li.find("span", {"class":"num"})
        aTit = li.find("a",{"class":"tit"})
        href = aTit['href']
        title = aTit['title']
    except:
        pass
        return

    return{"name":alt, "title":title, "price":price.text.replace(",",""),"link":href}

def parser(pageContent):
    bs_obj = bs4.BeautifulSoup(pageContent, "html.parser")

    ul = bs_obj.find("ul",{"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})

    products = []
    for li in lis:
        product = get_productinfo(li)
        if product:
            products.append(product)
    
    return products


pageContent = crawl('에어컨')
goods = parser(pageContent)
 
# file = open("./products.json","w+")
# file.write(json.dumps(products))
# file.close()

with open("./products.json", "w+") as file:
    file.write(json.dumps(goods))

#with문
# with open("test.txt","r") as txt:
    # txt.read()
#기존 코드
# txt = open("test.txt","r")
# txt.read()
# txt.close()

# for good in goods:
    # print(good)
# print(goods)

df = pd.read_json("./products.json")
# print(df.count())

writer = pd.ExcelWriter("products.xlsx")
df.to_excel(writer, "sheet1")
writer.save()
