

import pymysql




#存入数据库
def save_content(*args):
    conn = pymysql.connect(host='47.97.111.88', user='dengtacj', password='dengtacj2015', db='db_dengta_info')
    cur = conn.cursor()
    sql = 'insert into t_news(info_id,title,content,channel,status,publish_time,create_time,ipublish) values(%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(sql, (args))
    conn.commit()
    cur.close()
    conn.close()


#删除第三方平台故意的不完整数据,与第三方平台数据更新保持一致
def delete_news(info_id):
    conn = pymysql.connect(host='47.97.111.88', user='dengtacj', password='dengtacj2015', db='db_dengta_info')
    cur = conn.cursor()
    sql = 'delete from t_news where info_id = {}'.format(info_id)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()



#从数据库中选出最大的时间戳，新爬取新闻的时间戳大于已存在的最大时间戳，进行下一步
def get_max_timestamp(channel):
    conn = pymysql.connect(host='47.97.111.88', user='dengtacj', password='dengtacj2015', db='db_dengta_info')
    cur = conn.cursor()
    sql = 'select max(ipublish) from t_news where channel={}'.format(channel)
    cur.execute(sql)
    max_publish_timestamp = cur.fetchall()[0][0]
    if max_publish_timestamp != None:                     #判断首次选取，数据库为空，时间戳返回None的情况
        max_publish_timestamp = max_publish_timestamp
    else:
        max_publish_timestamp = 0
    return max_publish_timestamp
