

import time
import requests
import json
from save_to_sql import save_content,get_max_timestamp,delete_news
from logger_error import logError
from rule import Rule,clean_href,clean_cls,judge_title_length
from header_cls import get_headers




def get_cailianshe():
    url = 'https://www.cailianpress.com/nodeapi/telegraphs?&refresh_type=1&rn=20'
    headers = get_headers()
    response = requests.get(url,headers = headers,verify = False)
    jsonobj = json.loads(response.text)['data']['roll_data']
    max_timestamp = int(get_max_timestamp(1))
    for item in jsonobj:
        if int(item['modified_time']*1000) > max_timestamp:
            title = item['title'].strip()
            content = item['content']
            content = clean_href(content)
            publish_timestamp = item['modified_time']
            publish_datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(publish_timestamp))
            create_datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            # print 'create_datetime:', create_datetime
            source = 1  # '0:选股宝； 1：财联社'
            info_id = str(source)+str(item['id'])
            # print info_id
            delete_news(info_id)
            # publish_timestamp = int(time.time() * 1000)
            # time.sleep(1)
            simility_list = Rule(title)
            try:
                if simility_list[-1] >= 0.35:
                    print ("high simility:",source)
                    pass

                else:
                    # alike = 2
                    status = 1
                    title, content = clean_cls(title, content)
                    title, content = judge_title_length(title, content)
                    total = list(title + content)
                    if len(total) != 0:
                        save_content(info_id, title, content, source,status, publish_datetime, create_datetime,int(publish_timestamp*1000))
                        print ("save successfully:",source)
                    else:
                        pass
            except Exception as e:
                logError(str(e)+'-----------------'+info_id+'------------------'+title)
        else:
            print ('bubaocun')
            break
#
# def run_cls():
#     while True:
#         get_cailianshe(url)
#         time.sleep(180)
