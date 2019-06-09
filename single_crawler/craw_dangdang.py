from selenium import webdriver
import csv


base_url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-'
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)

csv_file = open("book_data.csv","w",newline='')
writer = csv.writer(csv_file)
writer.writerow(['书名', '作者', '价格', '图片链接', '描述'])

# while url != 'javascript:void(0)':
for i in range(1, 26):
    url = base_url + str(i)
    driver.get(url)
    print(driver.title)
    data = driver.find_element_by_css_selector(".bang_list.clearfix.bang_list_mode").find_elements_by_tag_name("li")
    print(len(data))
    for li in data:
        try:
            picture_url = li.find_element_by_class_name("pic").find_element_by_tag_name("img").get_attribute("src")
            book_name = li.find_element_by_class_name("name").find_element_by_tag_name("a").text
            author = li.find_elements_by_class_name("publisher_info")[0].find_elements_by_tag_name("a")[0].text
            price = li.find_element_by_class_name("price").find_elements_by_tag_name("span")[0].text[1:]
            print(picture_url)
            print(book_name)
            print(author)
            print(price)
            writer.writerow([book_name, author, price, picture_url, book_name])
        except IndexError:
            continue
        else:
            continue

csv_file.close()
# print(data)
