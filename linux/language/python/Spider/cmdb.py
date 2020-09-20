# -*- coding:utf-8 -*-
#作用：批量获取域名
import requests
from lxml import etree

message = """nginx version: nginx/1.10.3
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC)
built with OpenSSL 1.0.2k-fips  26 Jan 2017
TLS SNI support enabled
configure arguments: --prefix=/opt/apps/nginx --with-http_stub_status_module --with-http_ssl_module --with-http_geoip_module --with-http_gzip_static_module --with-ipv6 --with-http_realip_module --add-module=/opt/src/upload/module/ip2location-nginx-master/ --user=swadmin --group=swadmin
"""
with open("domain.txt","a")as f:
    f.write("\n"+message+"\n")

url = "https://cmdb.yibofafa666.com:2370"
# imput_lingpaima = "kfcp aaaa wcp 8hcp mtc dongf hbgj hgmkt 80cp hbet amyl gwns ambl hg ambjl lfcp bwin cmgm njs fcgj aapj cxpj wnsa phg jdgj aws amyh vwns xhtd ammgm hgxj cjs fpj abet blb ylg zyl fxpj ajs ahg xcp kxpj uwns amdb fwns jsdb cszx gyh btyc xwns rxpj djyl hggj jsda qpj thcp cpj byh asmh lqcp chg wnse wpyl dhg beta hgyl fjs yldc ahy ylca wnsd fhcp eecp ejs hgwb 5ycp hgwa 1hcp hjs jdaa b8cp tycp 6ajs axh dmgm khg csmh pjylc jhg hgyh hj jpj 1bet 1acp pjjt yhylc 1gfc ihg ddcp aodc ljs bxh 1hgc hyh cp36 1pjh blhyl nwns qwns epj hq ctyc atyc hccc jlgj betdc qmcp xsj ywns kjs 1mgm pjgb gjs sjcp 1xpj bjs xpjj wnsh amhg ahq jsgb yxlm 2xpj tjs hgwd 2ayh jsxs 1zdj fbet spj xmcp 68gj hgam 58cp fccp 1fhc 5wns 118c ttcp 6xpj jxcp 3ayh 6wns 5hcp 7wns 365c 7xpj dycp 302c 1blr 5ayh cptt xsyl jscp 686c 168c hgwe gjcp 8wns xycp fsmh diyc ylhg 1apj gsmh wnsg cpjs wxgj shgj ftcp yund 2apj alpk dinf 2ajs 5apj hgwf ycai 7apj 3apj hggb hgwg wjcp 6ayh 5ajs btai 588c 7ajs 3651 66cp 1cpj 9wns dadj 1cws 2mgm 2tcp 1tcp 3mgm bsgj 2cpj 5cpj 6gcp 2hgc 8ayh 7cpj 3hgc xfcp 8cpj 9cpj tccp 5822 dfsy yhcp 9ayh xiny dafa 1gbt 3dpj amcp 5dpj caik 3blr ydcp 3cws yqcp ftyc 5cws amxj 1ayl qhyc 6hgc 6dpj 3cjs 9hgc 8hgc 1cyh 5cjs 1hgd 7hgc 1hcw jfhc 7dpj 7cjs 5mgm 9cjs 2hgd 1ylg 6cws 7cws 3fhc 1fpj d9cp 2fpj ycgj 1djs 2cyh 6mgm hg71 fxcp ysbo 1chq 1aam 89yl 7mgm 5cyh 3fpj zscp hg57 2djs 3cyh 9cws rycp xllc ywcp 5djs 8mgm jnhc gtyc 5hgd 1jyl 2dws 5dws wtcp 3ayl jycp 8cyh 36cp 16cp youd 1jbb 6dws 2yud 8fpj tyic 9fpj sdyl 5ayl 9cyh 3yud 7hgd sfcp yinh thao lubo 7djs yinc 8djs 8dws 9dws 1gpj 5fhc agcp ccgj 13cp fycp jbao 5812 1fws 6ayl fgcp 3tcp 2gpj 2fws qmin fhgj 888c gcai 6fws 3fws 5gpj 6cai hylc 7fws jtyc 6tyl 8hgd 1tcc 9hgd 6gpj whyl 8fws 1317 ltyc 1816 cp59 1lfc 1519 wyyl 5000 7270 5937 cp39 mtyc jzgj 8637 1299 cai7 flic 1gws 1axj 7gpj bmgj 3dyh jiny 9mgm 9ayl 1hpj betb 8gpj tmcp 2hpj 6blr jixc cqcp wjsi 9djs lcgj 1byl ptyc qtyc fhyl 778c 8gws hwgj lhgj 2ejs s8yl 1dhc 9gws 1hws 2csj fgui cai8 8fhc 2hws 3hge 7hpj fclm bxin 8hpj 1wzw 3hws 5hws wsgj styc 5hge 6hws 9hpj ybcp 3ejs 1jpj yzgj 1xyc 6022 2jpj 7ejs utyc hwcp 6ejs whgj zmgm 5jpj 1jlc 99gj guib msmh abgj qtcp 8ejs huih njcp vtyc 1yfc zgfl 8hws 2chq 6jpj lejc jryl wygj 6134 2jws kaib wmcp 7jpj 8hge 7bet 1wmc 9ejs 8jpj 23cp bfhc 3csj 2fjs c8cp 2dfy 1flc 9jpj hccp 2flc 6byl 9hge wanb ymgm hxxs chcp bets lcai bsyl ztyc 1zyc wscp 518c 1tyc gczx dinc cfhc 1alc zgfc 6jws dasx 2hgf okgj bwzz 1kpj dxcp jxgj bfyl 7jws dxyl jiuj ysgj cwan 2eyh 2kpj wbai"
imput_lingpaima = "kfcp wcp 8hcp hbgj hbet amyl gwns ambl hg ambjl lfcp bwin cmgm njs fcgj aapj zyl cxpj phg jdgj aws amyh vwns xhtd ammgm hgxj cjs fpj blb abet ylg fxpj ajs ahg xcp kxpj uwns fwns jsdb cszx btyc xwns rxpj djyl hggj jsda qpj thcp cpj asmh lqcp chg wnse wpyl dhg beta hgyl fjs yldc ahy ylca wnsd fhcp eecp ejs hgwb 5ycp hgwa 1hcp hjs jdaa b8cp tycp 6ajs axh dmgm khg csmh pjylc jhg hgyh hj 1bet pjjt yhylc 1gfc ddcp aodc ljs bxh 1hgc hyh cp36 1pjh blhyl nwns qwns epj ctyc atyc betdc qmcp xsj ywns kjs 1mgm pjgb gjs sjcp 1xpj bjs wnsh amhg ahq jsgb yxlm 2xpj tjs hgwd 2ayh jsxs 1zdj fbet spj xmcp 68gj hgam 58cp 1fhc 5wns 118c ttcp 6xpj jxcp 3ayh 6wns 7wns 7xpj dycp 1blr cptt xsyl jscp 686c 168c hgwe gjcp 8wns diyc ylhg 1apj gsmh wnsg ftcp 2apj yund alpk dinf 2ajs 5apj hgwf ycai 7apj 3apj hggb hgwg 6ayh 5ajs 588c 7ajs 3651 66cp 1cpj 9wns dadj 2mgm 2tcp 1tcp 3mgm bsgj 2cpj 5cpj 6gcp 2hgc 7cpj 3hgc xfcp 8cpj 9cpj tccp dfsy xiny 9ayh dafa 1gbt 3dpj 5dpj caik 3blr ydcp 3cws yqcp 5cws amxj 1ayl 6hgc 6dpj 3cjs 9hgc 8hgc 1cyh 5cjs 7hgc 1hcw jfhc 7dpj 5mgm 9cjs 2hgd 1ylg 6cws 7cws 3fhc 1fpj 2fpj ycgj 1djs 2cyh 6mgm hg71 1aam 89yl 7mgm 5cyh 3fpj zscp hg57 2djs 3cyh rycp xllc ywcp 5djs 8mgm jnhc gtyc 2dws 5dws wtcp 3ayl jycp 8cyh 36cp 16cp youd 1jbb 6dws 2yud 8fpj 9fpj 5ayl 9cyh 3yud thao yinh 7djs 8dws 9dws 1gpj 5fhc ccgj 13cp fycp jbao 5812 1fws fgcp 3tcp 2gpj 2fws qmin fhgj 888c gcai 6fws 3fws 5gpj 6cai hylc 7fws 6tyl 8hgd 1tcc 9hgd 6gpj whyl 8fws 1317 ltyc 1816 cp59 1lfc 1519 wyyl 5000 7270 5937 cp39 mtyc jzgj 8637 1299 cai7 flic 1gws 1axj 7gpj 3dyh jiny 9mgm 9ayl 1hpj betb tmcp 2hpj 6blr jixc cqcp wjsi 9djs lcgj 1byl ptyc qtyc 778c 8gws lhgj 2ejs 1hws 2csj cai8 8fhc 2hws 3hge fclm 8hpj 3hws styc 5hge 6hws 9hpj 1jpj yzgj 1xyc 2jpj 7ejs utyc 6ejs whgj zmgm 5jpj 1jlc 99gj guib msmh abgj huih vtyc 1yfc 8hws 6jpj lejc jryl 6134 2jws kaib 8hge 7bet 1wmc 9ejs 8jpj 23cp bfhc 2fjs c8cp 2dfy 9jpj hccp 2flc 6byl wanb ymgm hxxs chcp bets lcai bsyl ztyc 1zyc wscp 518c 1tyc gczx dinc 1alc 6jws dasx 2hgf okgj bwzz 1kpj dxcp jxgj bfyl 7jws dxyl jiuj ysgj cwan 2eyh 2kpj wbai rhcp aicp wanx kyyl 500c zcyl 1ahy 9bet 7hgf 8bet 5fjs 3eyh 3kpj 8hgf 5eyh 5cai 5hgf 6fjs 8jws 3hgf tyxj 6hgf 9hgf kkgj 5bai 2dfc wdyl jjyl xhgj"
input_lingpaima_list = imput_lingpaima.split(" ")
# print(input_lingpaima_list)

session = requests.session()

session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Referer': 'https://cmdb.yibofafa666.com:2370/'
}

response_index = session.get(url)

# with open("cmdb.html", "wb") as f:
#     f.write(response.content)

html_index = etree.HTML(response_index.content.decode())

csrf_token = html_index.xpath('//*[@id="login-page"]/div/form/input/@value')[0]

# print(csrf_token)

form_login_data = {
    "csrfmiddlewaretoken": csrf_token,
    "uname": "德邦",
    "password": "TGwork638533.",
    "email": ""
}

response_login = session.post('https://cmdb.yibofafa666.com:2370', data=form_login_data)
# with open("cmdb.html","wb")as f:
#     f.write(response_login.content)
# print(response_login.content.decode())

html_login = etree.HTML(response_login.content.decode())

domain_url = url + html_login.xpath('//*[@id="nav-accordion"]/li[4]/a/@href')[0]

html_domain = session.get(domain_url)

# print(html_domain .status_code)
# print(html_domain .url)

# with open("cmdb.html", "wb") as f:
#     f.write(response_domain.content)

for alone_lingpaima in input_lingpaima_list:
    form_query_data = {
        "csrfmiddlewaretoken": csrf_token,
        "token": alone_lingpaima,
        "domain_kind": "all",
        "status": "全部"
    }

    response_query = session.post(html_domain .url, data=form_query_data)

    html_query = etree.HTML(response_query.content.decode())

    # print(response_query.status_code)
    # print(response_query.url)

    # with open("cmdb.html", "wb") as f:
    #     f.write(response_query.content)

    error_list = []

    try:
        output_lingpaima = html_query.xpath('//div[@id="div5"]//tr/td[3]/text()')[0].replace("\n", "").replace(" ", "")
    except:
        # print("没有%s这个令牌码" % alone_lingpaima)
        error_list.append(alone_lingpaima)
    # print(type(output_lingpaima))
    # print(output_lingpaima)
    domain_name_list = html_query.xpath('//div[@id="div5"]//tr/td[4]')
    # print(type(domain_name_list))
    # print(domain_name_list)
    domain_list = html_query.xpath('//div[@id="div5"]//tr/td[6]')
    # text = domain_name_list[1].xpath('./text()')[0]
    #
    # print(text)

    num = len(domain_name_list)
    # print(num)
    domain_finish_list = []
    for i in range(0, num):
        # print(i)
        temp = {}
        temp['domain_name'] = output_lingpaima + domain_name_list[i].xpath('./text()')[0].replace("\n", "").replace(" ",
                                                                                                                    "")
        temp['domain'] = domain_list[i].xpath('./text()')[0].replace("\n", "").replace(" ", "")
        domain_finish_list.append(temp)
    j = 0
    for i in domain_finish_list:
        if j == 5:
            # print(j)
            # print()
            print(str(i))
            with open('domain.txt','a') as f:
                f.write(str(i)+"\n"+"\n")
            j = 0
        else:
            # print(j)
            j = j + 1
            print(str(i))
            with open('domain.txt','a') as f:
                f.write(str(i)+"\n")

print()
print("以下令牌码cmdb不存在")
for i in error_list:
    print(i)

