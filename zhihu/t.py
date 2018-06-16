# -*- coding: utf-8 -*-
import requests
import json
targetUrl = "http://test.abuyun.com"

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "H925Y48JZ8LP432D"
proxyPass = "0D5A93B602C2648D"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
  "host" : proxyHost,
  "port" : proxyPort,
  "user" : proxyUser,
  "pass" : proxyPass,
}

proxies = {
    "http"  : proxyMeta,
    "https" : proxyMeta,
}


headers = {
    'cookie': 'd_c0="AEACagcEdguPTuI-xvKbwbrymWD3Qz_hjTg=|1489678463"; _zap=c59a21e5-6ba7-454b-b55d-f49d4bb2514d; q_c1=f3a6b725fa0740809d3fbfa7b27a0a82|1504404590000|1489678461000; __DAYU_PP=VnRZaAbVjF2Y72i2Ibze2f45defbc60a; q_c1=f3a6b725fa0740809d3fbfa7b27a0a82|1526799064000|1489678461000; __utma=51854390.1250038235.1508418197.1512663574.1528548346.6; __utmz=51854390.1528548346.6.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|2=registration_date=20161215=1^3=entry_date=20170316=1; l_cap_id="NjZiYzIyMDA1MzFlNDI4Njk4ZDNhYTgyNjFlZmY4YmY=|1528736024|ca59c95a14550a036cb6d16979782ddfe70b2095"; r_cap_id="ZmFkOWVjYzYxYzIxNDA5NjgwMjFhMjRjZmY5MDY0ZGE=|1528736024|9fe5223a18d6d39e9d2b4e23ffd67dc89dff8573"; cap_id="NDVhM2FhM2ZhMzc3NDQ3OWI2MGM4ZTU4Y2E4ZjM5YTA=|1528736024|ce6a9fe8bc8f0516672050d194a103a5943a40be"; capsion_ticket="2|1:0|10:1528968544|14:capsion_ticket|44:M2JhMGZkNmZjNjg1NDNkNGE5ZDJlY2E4MTBjZGEyNzE=|228e7d312d7804e3c484938c2fc933184409537529335edb42c26fe25f536c13"; z_c0="2|1:0|10:1528968559|4:z_c0|92:Mi4xLTNEUUF3QUFBQUFBUUFKcUJ3UjJDeVlBQUFCZ0FsVk5iNE1QWEFBMWtLQVhBZG5JZnhnN1pZQkhHQnVPdEI0Ql9n|39067d8e9929bf2916181cd6a45a34316707ed06baa3a7cb4f385d11ede689bf"; _xsrf=788330fe-e55e-42ee-941f-06082b233b34; tgw_l7_route=7139e401481ef2f46ce98b22af4f4bed',
    # 'accept-encoding': 'gzip, deflate, br',
    'x-requested-with': 'Fetch',
    'accept-language': 'zh-CN,zh;q=0.9',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    # 'referer': 'https://www.zhihu.com/question/50101909',
    'authority': 'www.zhihu.com',
    'x-udid': 'AEACagcEdguPTuI-xvKbwbrymWD3Qz_hjTg=',
}

params = (
    ('sort_by', 'default'),
    # ('include', 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=best_answerer)].topics'),
    ('limit', '5'),
    ('offset', '15'),
)

response = requests.get('https://www.zhihu.com/api/v4/questions/27330476/answers?sort_by=default&limit=20&offset=20', headers=headers, params=params, proxies=proxies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.zhihu.com/api/v4/questions/50101909/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=5&offset=15', headers=headers)

bash_url = 'https://www.zhihu.com/question/27330476/answer/'
pre_results = json.loads(response.text)
url = pre_results['paging']['next']
# print(url)
# results = pre_results['data']
# for result in results:
#     comments = result['comment_count']
#     try:#可能没赞
#         likes = result['voteup_count']
#     except KeyError:
#         likes = 0
#     author = result['author']['name']
#     answer_id = result['id']
#     answer_url = bash_url + str(answer_id)
    # print(comments)
    # print(likes)
    # print(author)
    # print(answer_url)
res= requests.get(url, headers=headers, params=params, proxies=proxies)

