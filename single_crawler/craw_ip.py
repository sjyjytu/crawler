from selenium import webdriver


def get_ip(page):
    base_url = "http://www.xiladaili.com/gaoni/"
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    ips = []
    for i in range(1, page+1):
        url = base_url + "%d/" % i
        driver.get(url)
        trs = driver.find_elements_by_tag_name("tr")
        for tr in trs:
            try:
                tds = tr.find_elements_by_tag_name("td")
                ip = tds[0].text
                ips.append(ip)
            except IndexError:
                continue
            else:
                continue
    return ips


def get_ip2(page):
    base_url = "https://www.kuaidaili.com/free/inha/"
    # base_url = "http://www.xiladaili.com/"
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    ips = []

    for i in range(1, page):
        url = base_url + "%d/" % i
        driver.get(url)
        # print(driver.title)
        trs = driver.find_elements_by_tag_name("tr")
        # print(len(trs))
        for tr in trs:
            try:
                tds = tr.find_elements_by_tag_name("td")
                ip = tds[0].text
                port = tds[1].text
                ips.append(ip+":"+port)
            except IndexError:
                continue
            else:
                continue
    return ips


