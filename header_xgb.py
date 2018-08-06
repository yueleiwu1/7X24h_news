import random



headers1 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "_ga=GA1.2.122018160.1531100158; _gid=GA1.2.473326463.1531704124; Hm_lvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531133310,1531183045,1531183069,1531704124; Hm_lvt_7e18ea40d71ecda0eacae51be020d9be=1531133310,1531183045,1531183069,1531704124; Qs_lvt_219689=1531733627%2C1531801832%2C1531873826%2C1531904109%2C1531979476; mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; Qs_pv_219689=1951161664801352200%2C87826364560831680%2C1195706540176178700%2C2407886599207186400%2C862065934520723200; Hm_lpvt_7e18ea40d71ecda0eacae51be020d9be=1531993010; Hm_lpvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531993010",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}


headers2 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "_ga=GA1.2.122018160.1531100158; _gid=GA1.2.473326463.1531704124; Hm_lvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531133310,1531183045,1531183069,1531704124; Hm_lvt_7e18ea40d71ecda0eacae51be020d9be=1531133310,1531183045,1531183069,1531704124; Qs_lvt_219689=1531733627%2C1531801832%2C1531873826%2C1531904109%2C1531979476; mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; _gat=1; Hm_lpvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531996129; Qs_pv_219689=1195706540176178700%2C2407886599207186400%2C862065934520723200%2C2084998691132879000%2C3067055085451166700; Hm_lpvt_7e18ea40d71ecda0eacae51be020d9be=1531996129",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers3 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; _ga=GA1.2.122018160.1531100158; _gid=GA1.2.473326463.1531704124; Hm_lvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531133310,1531183045,1531183069,1531704124; Hm_lvt_7e18ea40d71ecda0eacae51be020d9be=1531133310,1531183045,1531183069,1531704124; Qs_lvt_219689=1531733627%2C1531801832%2C1531873826%2C1531904109%2C1531979476; mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; Hm_lpvt_7e18ea40d71ecda0eacae51be020d9be=1531996252; Hm_lpvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531996252; Qs_pv_219689=2084998691132879000%2C3067055085451166700%2C797501836526184600%2C1370312976610318000%2C1307918545768853000",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers4 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; _ga=GA1.2.122018160.1531100158; _gid=GA1.2.473326463.1531704124; Hm_lvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531133310,1531183045,1531183069,1531704124; Hm_lvt_7e18ea40d71ecda0eacae51be020d9be=1531133310,1531183045,1531183069,1531704124; Qs_lvt_219689=1531733627%2C1531801832%2C1531873826%2C1531904109%2C1531979476; mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; Hm_lpvt_7e18ea40d71ecda0eacae51be020d9be=1531996252; Hm_lpvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531996252; Qs_pv_219689=2084998691132879000%2C3067055085451166700%2C797501836526184600%2C1370312976610318000%2C1307918545768853000",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers5 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': "mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; _ga=GA1.2.122018160.1531100158; _gid=GA1.2.473326463.1531704124; Hm_lvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531133310,1531183045,1531183069,1531704124; Hm_lvt_7e18ea40d71ecda0eacae51be020d9be=1531133310,1531183045,1531183069,1531704124; Qs_lvt_219689=1531733627%2C1531801832%2C1531873826%2C1531904109%2C1531979476; mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; _gat=1; Qs_pv_219689=797501836526184600%2C1370312976610318000%2C1307918545768853000%2C140068736112312430%2C4038033350368955400; Hm_lpvt_7e18ea40d71ecda0eacae51be020d9be=1531996348; Hm_lpvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531996348",
        'if-none-match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers6 = {'Accept':'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Cookie':'mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3AngX3fFVy8%22%2C%22ctn%22%3A%22%22%7D; _ga=GA1.2.122018160.1531100158; _gid=GA1.2.2087156575.1531100158; Hm_lvt_7e18ea40d71ecda0eacae51be020d9be=1531100159; Qs_lvt_219689=1531100158; Hm_lvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531100159; mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3AngX3fFVy8%22%2C%22ctn%22%3A%22%22%7D; Qs_pv_219689=2148682982257111000%2C1139737266589904400%2C1241156384444976600%2C2643750268665005600%2C2344350946163581400; Hm_lpvt_7e18ea40d71ecda0eacae51be020d9be=1531102421; Hm_lpvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531102421',
        'If-None-Match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'Upgrade-Insecure-Requests':'1',
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
headers7 = {'Accept':'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Cookie':"_ga=GA1.2.122018160.1531100158; _gid=GA1.2.473326463.1531704124; Hm_lvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531133310,1531183045,1531183069,1531704124; Hm_lvt_7e18ea40d71ecda0eacae51be020d9be=1531133310,1531183045,1531183069,1531704124; mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; Hm_lpvt_7e18ea40d71ecda0eacae51be020d9be=1532048023; Hm_lpvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1532048023; Qs_lvt_219689=1531801832%2C1531873826%2C1531904109%2C1531979476%2C1532048022; Qs_pv_219689=1307918545768853000%2C140068736112312430%2C4038033350368955400%2C3042842787151826400%2C2645365273004313600",
        'If-None-Match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'Upgrade-Insecure-Requests':'1',
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers8 = {'Accept':'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Cookie':"mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; _ga=GA1.2.122018160.1531100158; _gid=GA1.2.473326463.1531704124; Hm_lvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531133310,1531183045,1531183069,1531704124; Hm_lvt_7e18ea40d71ecda0eacae51be020d9be=1531133310,1531183045,1531183069,1531704124; mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; Qs_lvt_219689=1531801832%2C1531873826%2C1531904109%2C1531979476%2C1532048022; _gat=1; Hm_lpvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1532050694; Qs_pv_219689=4038033350368955400%2C3042842787151826400%2C2645365273004313600%2C2705239051965439500%2C55668026727756910; Hm_lpvt_7e18ea40d71ecda0eacae51be020d9be=1532050695",
        'If-None-Match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'Upgrade-Insecure-Requests':'1',
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers9 = {'Accept':'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Cookie':"mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; _ga=GA1.2.122018160.1531100158; _gid=GA1.2.473326463.1531704124; Hm_lvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531133310,1531183045,1531183069,1531704124; Hm_lvt_7e18ea40d71ecda0eacae51be020d9be=1531133310,1531183045,1531183069,1531704124; mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; Qs_lvt_219689=1531801832%2C1531873826%2C1531904109%2C1531979476%2C1532048022; _gat=1; Qs_pv_219689=2645365273004313600%2C2705239051965439500%2C55668026727756910%2C2080270969376786700%2C4556457156400409600; Hm_lpvt_7e18ea40d71ecda0eacae51be020d9be=1532050766; Hm_lpvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1532050767",
        'If-None-Match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'Upgrade-Insecure-Requests':'1',
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

headers10 = {'Accept':'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Cookie':"_ga=GA1.2.122018160.1531100158; _gid=GA1.2.473326463.1531704124; Hm_lvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1531133310,1531183045,1531183069,1531704124; Hm_lvt_7e18ea40d71ecda0eacae51be020d9be=1531133310,1531183045,1531183069,1531704124; mediav=%7B%22eid%22%3A%22498649%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22rz%60a*Uc%3D93%3C)T'9Vs%5B%25O%22%2C%22ctn%22%3A%22%22%7D; Qs_lvt_219689=1531801832%2C1531873826%2C1531904109%2C1531979476%2C1532048022; _gat=1; Hm_lpvt_6e8f4dfa25ad4f956a55c8dd8d01fdec=1532050852; Hm_lpvt_7e18ea40d71ecda0eacae51be020d9be=1532050852; Qs_pv_219689=55668026727756910%2C2080270969376786700%2C4556457156400409600%2C1650168016080657000%2C2398534456100873000",
        'If-None-Match':'dkWkvRGQwa7e6D9/A4YwfQ==',
        'Upgrade-Insecure-Requests':'1',
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
header_list = [headers1,headers2,headers3,headers4,headers5]

def get_headers():
    headers = random.choice(header_list)
    # print (headers)
    return headers

# get_headers()