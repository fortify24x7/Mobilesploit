"""
							 Mobilesploit
	MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
	MMMMMMMMMMM                MMMMMMMMMM
	MMMN$                           vMMMM
	MMMNl  MMMMM             MMMMM  JMMMM
	MMMNl  MMMMMMMN       NMMMMMMM  JMMMM
	MMMNl  MMMMMMMMMNmmmNMMMMMMMMM  JMMMM
	MMMNI  MMMMMMMMMMMMMMMMMMMMMMM  jMMMM
	MMMNI  MMMMMMMMMMMMMMMMMMMMMMM  jMMMM
	MMMNI  MMMMM   MMMMMMM   MMMMM  jMMMM
	MMMNI  MMMMM   MMMMMMM   MMMMM  jMMMM
	MMMNI  MMMNM   MMMMMMM   MMMMM  jMMMM
	MMMNI  WMMMM   MMMMMMM   MMMMM  JMMMM
	MMMMR  ?MMNM             MMMMM  dMMMM
	MMMMNm `?MMM    MMnMM    MMMM` dMMMMM
	MMMMMMN  ?MM   MM"M"MM   MM?  NMMMMMN
	MMMMMMMMNe    MM"   "MM    JMMMMMNMMM
	MMMMMMMMMMNm,            eMMMMMNMMNMM
	MMMMNNMNMMMMMNx        MMMMMMNMMNMMNM
	MMMMMMMMNMMNMMMMm+..+MMNMMNMNMMNMMNMM

Disclaimers:
	Mobilesploit is NOT an official program and isn't a original idea! Mobilesploit is strictly based off of Metasploit by Rapid7! Mobilesploit is a non-profit program which is open source! Mobilesploit does not contain any code from Metasploit!
	
	Please support Metasploit's Official Release! (http://metasploit.com)
	Copyright (C) 2006-2017, Rapid7 LLC
	Metasploit EULA (Legal Reference):
		https://information.rapid7.com/terms

About:
	Coding: Python 2.7.11
	Developer: @Russian_Otter
	Requirements: Pythonista 3 for iOS
	(Or Console.py for PC)

Encoding:
	Indent/Tab: 2
	Encoding: UTF-8

API Script:
	Check "API.md" for how to set up your own exploits that Mobilesploit can read!

"""

import sys, console, time, os, requests

loc = ""
sets = {}
var = []

def fdir(name,start="./",get=False):
	null = []
	for root, dirs, files in os.walk(start):
		for file in files:
			if "" in file and "__" not in file and file.endswith(".py"):
				epath = (os.path.join(root, file.replace(".py","")))
				if get == True:
					if "/" in epath and name in epath:
						null.append(epath)
				elif "/" in epath and name in epath:
					return epath
	return null

def meta_logo():
	console.set_color(1,1,1)
	console.set_font("Menlo",10)
	print " - Please Support Metasploit's Official Release! -\n"
	run = "[*] Starting the Mobilesploit Framework Console..."
	runu = run.upper()
	for x in range(len(run)):
		s = "\r"+run[0:x]+runu[x]+run[x+1:]
		sys.stdout.write(s)
		sys.stdout.flush()
		time.sleep(0.08)
	time.sleep(1)
	console.clear()
	console.set_font("Menlo",11)
	console.set_color(0,0,1)
	sys.stdout.write("""
	MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
	MMMMMMMMMMM                MMMMMMMMMM
	MMMN$                           vMMMM
	MMMNl""")
	console.set_color(1,1,1)
	sys.stdout.write("  MMMMM             MMMMM")
	console.set_color(0,0,1)
	sys.stdout.write("  JMMMM\n\t")
	sys.stdout.write("MMMNl")
	console.set_color(1,1,1)
	sys.stdout.write("  MMMMMMMN       NMMMMMMM")
	console.set_color(0,0,1)
	sys.stdout.write("  JMMMM\n\t")
	sys.stdout.write("MMMNl")
	console.set_color(1,1,1)
	sys.stdout.write("  MMMMMMMMMNmmmNMMMMMMMMM")
	console.set_color(0,0,1)
	sys.stdout.write("  JMMMM\n\t")
	sys.stdout.write("MMMNI")
	console.set_color(1,1,1)
	sys.stdout.write("  MMMMMMMMMMMMMMMMMMMMMMM")
	console.set_color(0,0,1)
	sys.stdout.write("  jMMMM\n\t")
	sys.stdout.write("MMMNI")
	console.set_color(1,1,1)
	sys.stdout.write("  MMMMMMMMMMMMMMMMMMMMMMM")
	console.set_color(0,0,1)
	sys.stdout.write("  jMMMM\n\t")
	sys.stdout.write("MMMNI")
	console.set_color(1,1,1)
	sys.stdout.write("  MMMMM   MMMMMMM   MMMMM")
	console.set_color(0,0,1)
	sys.stdout.write("  jMMMM\n\t")
	sys.stdout.write("MMMNI")
	console.set_color(1,1,1)
	sys.stdout.write("  MMMMM   MMMMMMM   MMMMM")
	console.set_color(0,0,1)
	sys.stdout.write("  jMMMM\n\t")
	sys.stdout.write("MMMNI")
	console.set_color(1,1,1)
	sys.stdout.write("  MMMNM   MMMMMMM   MMMMM")
	console.set_color(0,0,1)
	sys.stdout.write("  jMMMM\n\t")
	sys.stdout.write("MMMNI")
	console.set_color(1,1,1)
	sys.stdout.write("  WMMMM   MMMMMMM   MMMMM")
	console.set_color(0,0,1)
	sys.stdout.write("  JMMMM\n\t")
	sys.stdout.write("MMMMR")
	console.set_color(1,1,1)
	sys.stdout.write("  ?MMNM             MMMMM")
	console.set_color(0,0,1)
	sys.stdout.write("  dMMMM\n\t")
	sys.stdout.write("MMMMNm")
	console.set_color(1,1,1)
	sys.stdout.write(" `?MMM    MMnMM    MMMM`")
	console.set_color(0,0,1)
	sys.stdout.write(" dMMMMM\n\t")
	sys.stdout.write("MMMMMMN")
	console.set_color(1,1,1)
	sys.stdout.write("  ?MM   MM\"M\"MM   MM?")
	console.set_color(0,0,1)
	sys.stdout.write("  NMMMMMN\n\t")
	sys.stdout.write("MMMMMMMMNe    ")
	console.set_color(1,1,1)
	sys.stdout.write("MM\"   \"MM    ")
	console.set_color(0,0,1)
	sys.stdout.write("JMMMMMNMMM\n\t")
	sys.stdout.write("MMMMMMMMMMNm,            eMMMMMNMMNMM\n\t")
	sys.stdout.write("MMMMNNMNMMMMMNx        MMMMMMNMMNMMNM\n\t")
	sys.stdout.write("MMMMMMMMNMMNMMMMm+..+MMNMMNMNMMNMMNMM\n\t")
	console.set_color(1,1,1)
	print "       https://metasploit.com"
	print

def unilogo():
	console.set_font("Menlo",11)
	console.set_color(0,0,1)
	sys.stdout.write(u"""\n\t\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n\t\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588               \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n\t\u2588\u2588\u2588\u2588\u2588                           \u2588\u2588\u2588\u2588\u2588\n\t\u2588\u2588\u2588\u2588\u2588""")
	console.set_color(1,1,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588             \u2588\u2588\u2588\u2588\u2588")
	console.set_color(0,0,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588")
	console.set_color(1,1,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588       \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588")
	console.set_color(0,0,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588")
	console.set_color(1,1,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588")
	console.set_color(0,0,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588")
	console.set_color(1,1,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588")
	console.set_color(0,0,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588")
	console.set_color(1,1,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588")
	console.set_color(0,0,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588")
	console.set_color(1,1,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588   \u2588\u2588\u2588\u2588\u2588\u2588\u2588   \u2588\u2588\u2588\u2588\u2588")
	console.set_color(0,0,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588")
	console.set_color(1,1,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588   \u2588\u2588\u2588\u2588\u2588\u2588\u2588   \u2588\u2588\u2588\u2588\u2588")
	console.set_color(0,0,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588")
	console.set_color(1,1,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588   \u2588\u2588\u2588\u2588\u2588\u2588\u2588   \u2588\u2588\u2588\u2588\u2588")
	console.set_color(0,0,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588")
	console.set_color(1,1,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588   \u2588\u2588\u2588\u2588\u2588\u2588\u2588   \u2588\u2588\u2588\u2588\u2588")
	console.set_color(0,0,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588")
	console.set_color(1,1,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588             \u2588\u2588\u2588\u2588\u2588")
	console.set_color(0,0,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588\u2588")
	console.set_color(1,1,1)
	sys.stdout.write(u" \u2588\u2588\u2588\u2588\u2588    \u2588\u2588 \u2588\u2588    \u2588\u2588\u2588\u2588\u2588")
	console.set_color(0,0,1)
	sys.stdout.write(u" \u2588\u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588\u2588\u2588")
	console.set_color(1,1,1)
	sys.stdout.write(u"  \u2588\u2588\u2588   \u2588\u2588\u2588\u2588\u2588\u2588\u2588   \u2588\u2588\u2588")
	console.set_color(0,0,1)
	sys.stdout.write(u"  \u2588\u2588\u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588    ")
	console.set_color(1,1,1)
	sys.stdout.write(u"\u2588\u2588  \u2588  \u2588\u2588    ")
	console.set_color(0,0,1)
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588             \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588         \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n\t")
	sys.stdout.write(u"\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n\t")
	console.set_color(1,1,1)
	print "       https://metasploit.com"
	print
	console.set_font("Menlo",8)
	print """
       =[ mobilesploit v1.5.4.82942-mobile                ]
+ -- --=[ %s exploits - %s auxiliary - 1 post              ]
+ -- --=[ %s payloads - 0 encoders - 0 nops                ]
+ -- --=[ Free Metasploit Pro trail: http://r-7.co/trymsp ]
	
	""" %(len(os.listdir("exploit"))-1, len(os.listdir("auxiliary"))-1, len(os.listdir("payload"))-1)
	console.set_font("Menlo",9.5)

meta_logo()

def auto_pay(name,size):
	au = "  "+name+" "*(19-len(name)) + str(size)
	print au

def show_payload():
	print "\nAvailable Payloads"
	print "==================\n"
	print "  Name               Size"
	print "  ----               ----"
	try:
		for _ in os.listdir("./payload"):
			if "." in _ and "__" not in _:
				payinfo = _, len(open("./payload/"+_).read())
				auto_pay(payinfo[0], payinfo[1])
	except:
		pass
	print

def show_auxiliary():
	print "\nAvailable Auxiliary"
	print "====================\n"
	print "  Name             Rank        Description"
	print "  ----             ----        -----------"
	try:
		for _ in os.listdir("./auxiliary"):
			a = "./auxiliary/"
			try:
				if ".py" in _ and "_" not in _:
					execfile(a+_,{"desc":"get-id","name":_})
			except:
				pass
	except:
		pass
	print 

def auto_cmd(cmd,description):
	stbl = "  " + cmd + " "*(7-len(cmd)+7) + description + " "*(11-len(description))
	print stbl

console.set_font("Menlo",8)
print """
       =[ mobilesploit v2.5.4.82942-mobile                ]
+ -- --=[ %s exploits - %s auxiliary - 1 post              ]
+ -- --=[ %s payloads - 0 encoders - 0 nops                ]
+ -- --=[ Free Metasploit Pro trail: http://r-7.co/trymsp ]

""" %(len(os.listdir("exploit"))-1, len(os.listdir("auxiliary"))-1, len(os.listdir("payload"))-1)
time.sleep(0.5)
console.set_font("Menlo",9.5)

try:
	udcode = requests.get("https://raw.githubusercontent.com/RussianOtter/Mobilesploit/master/update.ms").text
	exec udcode
	f = open("update.ms","w")
	f.write(udcode)
	f.close()
except Exception as e:
	print e
	pass

def meta_launch(app):
	try:
		name = app.split("/")
		name = name[1]
		sets.update({"desc":"proc"})
	except:
		pass
	try:
		execfile(app+".py",sets)
	except:
		pass
	try:
		sets.pop("desc")
	except:
		pass

def meta_help(data,loc):
	if data == "force update":
		if raw_input("Are you sure you want to reinstall packages [y/n]") == "y":
			f = open("update.ms","w")
			f.write(" ")
			f.close()
			udcode = requests.get("https://raw.githubusercontent.com/RussianOtter/Mobilesploit/master/update.ms").text
			exec udcode
			f = open("update.ms","w")
			f.write(udcode)
			f.close()
	if data == "show auxiliary" or data == "show aux":
		show_auxiliary()
	if data == "exploit":
		meta_launch(loc)
	if data == "show exploits":
		print "\nAvailable Exploits"
		print "==================\n"
		print "  Name             Rank        Description"
		print "  ----             ----        -----------"
		try:
			for _ in os.listdir("./"):
				try:
					if "." not in _:
						for a in fdir("",_,True):
							execfile(a+".py",{"desc":"get-id","name":_})
				except:
					pass
		except:
			pass
		print
	if data.startswith("info ") and len(data) > 5:
		try:
			for _ in os.listdir("./"):
				try:
					if "." not in _:
						execfile(fdir(data[5:],_)+".py",{"desc":"get-info","name":data[5:]})
				except:
					pass
		except:
			pass
	if data == "show options" and loc != "":
		sets.update({"desc":"get-opt"})
		try:
			execfile(loc+".py",sets)
		except:
			print "Exploit Unavailable"
			pass
		sets.pop("desc")
	elif data == "get options":
		for _ in var:
			print _
	if data == "show payloads" or data == "show payload":
		show_payload()
	if data.startswith("set "):
		if "set exploit/" in data or "set auxiliary/" in data or "set payload/" in data:
			data = data[4:].split("/")
		else:
			data = data[4:].split(" ")
		try:
			if str(data[0]) == "payload" and "." in str(data[1]):
				sets.update({data[0]:open("./payload/"+data[1]).read().replace("\n","").replace("\r","")})
			else:
				sets.update({data[0]:data[1]})
			tran = data[0]+" => "+data[1]
			var.append(tran)
			print tran
		except:
			pass
		
	if data == "help" or data == "?":
		time.sleep(0.4)
		print "\nCore Commands"
		print "==============\n"
		print "  Command       Description"
		print "  -------       -----------"
		auto_cmd("?","Help Menu")
		auto_cmd("help","Help Menu")
		auto_cmd("back","Move back from the current context")
		auto_cmd("exit","Exit the console")
		auto_cmd("get options","Display set variables")
		auto_cmd("info","Get values from variables")
		auto_cmd("use","Select Module by name")
		auto_cmd("show","<options|payloads|auxiliary|exploits>")
		auto_cmd("size","Changes font size")
		auto_cmd("clear","Resets screen activity")
		auto_cmd("banner","Show the Unicode Banner")
		auto_cmd("remove","Delete Variable")
		auto_cmd("force update","Forcefully Reinstall Packages")
		print

def cpoint(loc=""):
	loc = loc.replace("./","")
	while 1:
		console.write_link("msf","")
		if loc == "":
			sys.stdout.write(" ")
		else:
			loco = loc.split("/")
			sys.stdout.write(" %s(" %(loco[0]))
			console.set_color(1,0,0)
			sys.stdout.write("%s" %(loco[1]))
			console.set_color(1,1,1)
			sys.stdout.write(") ")
		try:
			data = raw_input("> ")
		except:
			print
			data = ""
			pass
		if data == "clear":
			console.clear()
		if data.startswith("use ") and len(data) > 4:
			data = data[4:]
			if data in sets:
				try:
					cpoint(fdir(sets[data]))
				except:
					pass
			else:
				try:
					cpoint(fdir(data))
				except:
					pass
		if data == "back":
			break
		if data == "exit": 
			exit()
		if data == "banner":
			unilogo()
		meta_help(data,loc)
		if data.startswith("size ") and len(data) > 4:
			data = data[4:]
			try:
				console.set_font("Menlo",int(data))
			except:
				pass
		if data == "size":
			console.set_font("Menlo",9.5)
		if data.startswith("remove ") and len(data) > 6:
			data = data[7:]
			try:
				if data in sets:
					t = data+" => "+sets.get(data)
					sets.pop(data)
					var.remove(t)
					print "Removed Values For \"%s\"" %data
			except Exception as e:
				print e
				pass

while 1:
	cpoint()
