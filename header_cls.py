import random



headers1 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "aliyungf_tc=AQAAAFHKAV7aNggA6pngepu311FCnbir; acw_tc=AQAAAOiiTyuLWQgA6pngeizqWBJzfZ4d; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1531976071,1531979926,1531993021,1531997906; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1531997906",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}


headers2 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "aliyungf_tc=AQAAAFHKAV7aNggA6pngepu311FCnbir; acw_tc=AQAAAOiiTyuLWQgA6pngeizqWBJzfZ4d; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1531993021,1531997906,1531997916,1531997996; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1531998267",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers3 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "aliyungf_tc=AQAAAFHKAV7aNggA6pngepu311FCnbir; acw_tc=AQAAAOiiTyuLWQgA6pngeizqWBJzfZ4d; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1531993021,1531997906,1531997916,1531997996; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1531998305",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers4 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "aliyungf_tc=AQAAAFHKAV7aNggA6pngepu311FCnbir; acw_tc=AQAAAOiiTyuLWQgA6pngeizqWBJzfZ4d; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1531993021,1531997906,1531997916,1531997996; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1531998313",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers5 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "aliyungf_tc=AQAAAFHKAV7aNggA6pngepu311FCnbir; acw_tc=AQAAAOiiTyuLWQgA6pngeizqWBJzfZ4d; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1531997906,1531997916,1531997996,1531998355; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1531998397",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers6 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "aliyungf_tc=AQAAAFHKAV7aNggA6pngepu311FCnbir; acw_tc=AQAAAOiiTyuLWQgA6pngeizqWBJzfZ4d; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1531997996,1531998355,1532048005,1532048071; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1532048071",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers7 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "aliyungf_tc=AQAAAFHKAV7aNggA6pngepu311FCnbir; acw_tc=AQAAAOiiTyuLWQgA6pngeizqWBJzfZ4d; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1531998355,1532048005,1532048071,1532051347; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1532051347",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers8 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "aliyungf_tc=AQAAAFHKAV7aNggA6pngepu311FCnbir; acw_tc=AQAAAOiiTyuLWQgA6pngeizqWBJzfZ4d; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1532048005,1532048071,1532051347,1532051397; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1532051397",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers9 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "aliyungf_tc=AQAAAFHKAV7aNggA6pngepu311FCnbir; acw_tc=AQAAAOiiTyuLWQgA6pngeizqWBJzfZ4d; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1532048071,1532051347,1532051397,1532051439; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1532051474",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers10 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "aliyungf_tc=AQAAAFHKAV7aNggA6pngepu311FCnbir; acw_tc=AQAAAOiiTyuLWQgA6pngeizqWBJzfZ4d; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1532048071,1532051347,1532051397,1532051439; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1532051514",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}


header_list = [headers1,headers2,headers3,headers4,headers5,headers6,headers7,headers8,headers9,headers10]

def get_headers():
    headers = random.choice(header_list)
    # print (headers)
    return headers

# get_headers()