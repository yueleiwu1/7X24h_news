


import requests
import json
import time
from save_to_sql import save_content,get_max_timestamp,delete_news
from logger_error import logError
from rule import Rule,clean_href,clean_xgb,judge_title_length
from header_xgb import get_headers





def get_xgb():
    url = 'https://api.xuangubao.cn/api/messages/live?limit=20'
    headers = get_headers()
    response = requests.get(url,headers = headers,verify = False)
    jsonobj = json.loads(response.text)['Messages']
    max_timestamp = int(get_max_timestamp(0))
    # print 'max_timestamp:',max_timestamp
    for item in jsonobj:
        if int(item['CreatedAt']*1000) > max_timestamp:
            title = item['Title'].strip()
            content = item['Summary']
            content = clean_href(content)
            publish_timestamp = item['CreatedAt']
            publish_datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(publish_timestamp))
            create_datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            # print 'create_datetime:',create_datetime
            source  = 0 #'0:选股宝； 1：财联社'
            info_id = str(source)+item['Id']
            # print info_id
            delete_news(info_id)
            # publish_timestamp = int(time.time() * 1000)
            # time.sleep(1)
            simility_list = Rule(title)
            try:
                if simility_list[-1]>=0.35:
                    print("high simility:",source)
                    pass
                else:
                    # alike = 2
                    status = 1
                    title, content = clean_xgb(title, content)
                    title, content = judge_title_length(title, content)
                    total = list(title + content)
                    if len(total) != 0:
                        save_content(info_id, title, content, source, status,publish_datetime,create_datetime,int(publish_timestamp*1000))
                        print("save successfully:",source)
                    else:
                        pass
            except Exception as e:
                logError(str(e) + '-----------------' + info_id + '------------------' + title)

        else:
            print ('bubaocun')
            break


#
# def run_xgb():
#     while True:
#         get_xgb(url)
#         time.sleep(180)
# run_xgb()


"""航运板块午后异动，龙头中远海特直线封板，龙二中远海能大涨4%，中远海发、宁波海运、中远海控纷纷跟涨"""

"""​航运股午后全线爆发，中远海特(sh600428)直线封涨停，宁波海运(sh600798)、中远海能(sh600026)、连云港(sh601008)、南京港(sz002040)等多只个股上涨。​航运股午后全线爆发，中远海特(sh600428)直线封涨停，宁波海运(sh600798)、中远海能(sh600026)、连云港(sh601008)、南京港(sz002040)等多只个股上涨。"""