
# coding: utf-8

# In[1]:


#本部分调研搜索界面的第2页
#调用requetss包请求网页源代码
import requests
from bs4 import BeautifulSoup
from bs4 import element
import csv
#本次抽样百分之一，26份样品，1个页面
#本次直接爬取了从0到144页面的所有相应信息，将信息保存在csv格式文件之中

#以下是csv转换区，提前做好csv表格准备
csv_file = open('BellWetherAll.csv','w',encoding="gbk",newline='')
writer = csv.writer(csv_file)
writer.writerow(["艺术家","热度"])#编辑表格中的标题

for i in range(0,1):
    print(i)#这里用来验证页数是否正常
    icount = i*24
    url = "https://www.deviantart.com/popular-all-time/?section=&global=1&q=Dawn+Bellwether&offset="+str(icount)
    response = requests.get(url)
    #print(response.content.decode('utf-8'))

    #将网页源代码保存到本地MyBambi.html文件中
    file_obj = open('MyBellWetherAll.html','w')
    file_obj.write(response.content.decode('utf-8'))
    file_obj.close()

    #从bs4引入数据提取工具BeautifulSoup
    from bs4 import BeautifulSoup
    file_obj = open('MyBellWetherAll.html','r')#以读方式打开MyBambi文件
    html = file_obj.read() #把文件的内容全部读出来并赋值给html变量
    file_obj.close()
    soup = BeautifulSoup(html,'html5lib')#html.parser,html5lib初始化BeautifulSoup，使用lxml有可能会有格式问题
    #print(soup)#输出BeautifulSoup转换后 的源代码内容

    #all_bambis = soup.find('div',class_="page-results results-page-thumb torpedo-container torpedo-container-xs")
    all_bambis = soup.find('div',class_="browse-content with-sidemenu") #先找到所有bambi作品所在的最大div
    #print(all_bambis) #输出该范围的所有内容

    #注意：csv转换区！
   # csv_file = open('BambiPageAll.csv','w',encoding="gbk",newline='')
   # writer = csv.writer(csv_file)

    #writer.writerow(["艺术家","热度"])#写入标题
    #csv转换块暂时结束
    
    #一下是在先前程序测试后排出标签异常页的更新
    
    #if(i!=27 and i!=39 and i!=66 and i!=97and i!=106 and i!=140):
    for each_bambi in all_bambis.find_all('span',class_="info"):
            all_a_tag = each_bambi.find_all('a')
            all_hot_tag = each_bambi.find_all('span',class_="faves icon-faves")
            bambi_artist = all_a_tag[1].text
            bambi_hot = all_hot_tag[0].text
            print('艺术家:{},热度:{}'.format(bambi_artist,bambi_hot))
            writer.writerow([bambi_artist,bambi_hot])

csv_file.close()
    #print("write_finished!")


# In[ ]:




