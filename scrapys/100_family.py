import requests
from lxml import etree
import re
import threading

from my_mysql import create_table, insert_keys, insert_data


def get_page(address):
	url = "http:"+address
	headers =  {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		text = response.content.decode('utf-8')
		return text
	return None

def get_one_parse(html):
    etree_html = etree.HTML(html)
    name_address = etree_html.xpath('//a[@class="btn btn2"]/@href')
    adress = etree_html.xpath('//a[@class="btn btn2"]')
    data_value = ''
    for adr in adress:
        message = adr.xpath('./text()')[0]
        title = adr.xpath('./@title')[0]
        number = re.findall(r'\d+',title)[0]
        family_name = str(message).replace('姓名字大全','')
        if data_value:
            data_value += ',("%s",%s)' % (family_name,number)
        else:
            data_value +='("%s",%s)' % (family_name,number)
    # create_table('families')
    # insert_keys('families','family_name','varchar(32)','unique')
    # insert_keys('families','number','varchar(32)')
    # insert_data('families',['family_name','number'],data_value)
    return name_address

def get_two_parse(html,html_address):
    etree_html = etree.HTML(html)
    try:
        a_address = etree_html.xpath('//a[@class="btn btn-link"]')
        value = ''
        for a_adr in a_address:
            try:
                name = a_adr.xpath('./text()')[0]
                html_adr = a_adr.xpath('.//@href')[0]
                html3_adr = '//' + html_address+str(html_adr)
                html3 = get_page(str(html3_adr))
                message = get_three_parse(html3)
                # create_table('name_message')
                # insert_keys('name_message','name','varchar(32)','unique')
                # insert_keys('name_message','family_name','varchar(16)')
                # insert_keys('name_message','number','varchar(16)')
                # insert_keys('name_message','girl_rate','varchar(16)')
                # insert_keys('name_message','body_rate','varchar(16)')
                # insert_keys('name_message','name_refer','varchar(1024)')
                # insert_keys('name_message','five','varchar(32)')
                # insert_keys('name_message','three','varchar(32)')
                insert_data('name_message',['name', 'family_name', 'number', 'girl_rate', 'body_rate', 'name_refer', 'five,three'],message)
            except:
                continue
        return value
    except:
        return


def get_three_parse(html):
    etree_html = etree.HTML(html)
    left = etree_html.xpath('//div[@id="head_"]//div[@class="navbar-header"]/a/div/text()')[0]
    name_div = etree_html.xpath('//div[@class="panel-heading"]/h3/text()')[0]
    name = str(name_div).split('"')[1]
    number_label = etree_html.xpath('//div[@class="navbar-brand"]/text()')[0]
    number = re.findall('\d+',number_label)[0]
    family_name = str(left).replace('姓之家','')[0]
    rate1 = etree_html.xpath('//div[@class="progress-bar progress-bar-warning"]/@style')[0]
    rate2 = etree_html.xpath('//div[@class="progress-bar"]/@style')[0]
    girl_rate =str(rate1).split(':')[-1].split(';')[0]
    body_rate =str(rate2).split(':')[-1].split(';')[0]
    name_refer = etree_html.xpath('//div[@class="panel-body"]/strong/text()')[0]
    math = etree_html.xpath('//div[@class="col-xs-6"]/blockquote/text()')
    five = math[0]
    three = math[1]
    value = '("%s","%s","%s","%s","%s","%s","%s","%s")' % (name,family_name,number,girl_rate,body_rate,name_refer,five,three)
    return value

def url_spilt(urls):
    url_list = []
    url_list_1 =[]
    for url in urls:
        url_list_1.append(url)
        if len(url_list_1)==15:
            url_list.append(url_list_1)
            url_list_1 = []
    return url_list

def thread_url(urls):
    for name_ads in urls:
        addr1 = str(name_ads)
        for i in range(1,11):
            addr2 = addr1.replace('.html','_%d.html' % i)
            addr3 = addr1.split('/')[-2]
            html2 = get_page(addr2)
            get_two_parse(html2,addr3)



def to_start(urls):
    threads = []
    for url_list in urls:
        t=threading.Thread(target=thread_url,args=(url_list,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


def main():
    html1 = get_page('//www.resgain.net/xmdq.html')
    name_adss = get_one_parse(html1)
    url_list = url_spilt(name_adss)
    to_start(url_list)


if __name__ == '__main__':
    main()