

import pymysql
import re


#第一步：从数据库中取出已爬数据
def get_info():
    conn = pymysql.connect(host='47.97.111.88', user='dengtacj', password='dengtacj2015', db='db_dengta_info')
    cur = conn.cursor()
    sql = 'select title from t_news order by ipublish DESC;'
    cur.execute(sql)
    # conn.commit()
    fetches = cur.fetchmany(20)
    return fetches

#第二步：初步清洗，去掉内容中链接

def clean_href(content):
    pattern1 = re.compile(r'<a.*?>')
    pattern2 = re.compile(r'</a>')
    content1 = pattern1.sub(r'',content)
    content2 = pattern2.sub(r'',content1)
    return content2

#第三步：去重，根据字频判断相似度
def Rule(title):
    fetches = get_info()
    list_simility = []
    total = list(title)
    # print set(total)
    if len(fetches) == 0:
        list_simility = [0]
    else:
        for fetch in fetches:
            list1 = list(str(fetch[0]))
            inter = list(set(total).intersection(set(list1)))
            union = list(set(total).union(set(list1)))
            simility = float(len(inter)) / len(union)
            # print ('title simility:',simility)
            if simility > 0.35:
                print ('title:',simility)
                list_simility.append(simility)
                break
            else:
                list_simility.append(simility)
    return list_simility

#第四步：标题及内容清洗：去掉选股宝、财联社、快讯（标题是"快讯",该情况去除了）
#选股宝清洗
def clean_xgb(title,content):
    pattern1 = re.compile(r'选股宝讯，')
    pattern2 = re.compile(r'选股宝')
    pattern3 = re.compile(r'【快讯】')
    pattern4 = re.compile(r'快讯：')
    pattern5 = re.compile(r'快讯')
    title1 = pattern1.sub(r'',title)
    title2 = pattern2.sub(r'',title1)
    title3 = pattern3.sub(r'',title2)
    title4 = pattern4.sub(r'',title3)
    title5 = pattern5.sub(r'',title4)
    content1 = pattern1.sub(r'', content)
    content2 = pattern2.sub(r'', content1)
    content3 = pattern3.sub(r'', content2)
    content4 = pattern4.sub(r'',content3)
    content5 = pattern5.sub(r'',content4)
    return title5,content5

#财联社清洗
def clean_cls(title,content):
    pattern1 = re.compile(r'财联社.*?讯，')
    pattern2 = re.compile(r'财联社')
    pattern3 = re.compile(r'【快讯】')
    pattern4 = re.compile(r'快讯：')
    pattern5 = re.compile(r'快讯')
    title1 = pattern1.sub(r'',title)
    title2 = pattern2.sub(r'',title1)
    title3 = pattern3.sub(r'',title2)
    title4 = pattern4.sub(r'', title3)
    title5 = pattern5.sub(r'',title4)
    content1 = pattern1.sub(r'', content)
    content2 = pattern2.sub(r'', content1)
    content3 = pattern3.sub(r'', content2)
    content4 = pattern4.sub(r'', content3)
    content5 = pattern5.sub(r'',content4)
    # judge_title_length(title3, content3)
    return title5,content5

#第五步：判断标题长度是否大于等于6

def judge_title_length(title,content):
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    title1 = pattern.findall(title)
    title2 = ''
    for i in title1:
        title2 = title2+i
    if title == r'这是一条VIP，进入VIP话题订阅可解锁查看':
        title = r''
        content = r''
    elif len(title2) > 6 and len(content) !=0:
        title = title
        content = content
    elif len(title2) > 6 and len(content) == 0:
        title = title
        content = title
    elif len(title2) <= 6 and len(content) == 0:
        pass
    elif len(title2) <=6 and len(content) != 0:
        title = title + ' '+content
        content = title
    else:
        title = title + ' ' +content
        # title = title[:101]
        content = title
    return title,content


#第六步：保存至数据库
