from lib import sashin
import sys, os
from threading import Thread


blue = "\033[34;1m"
default = "\033[0m"
orange = "\033[33;1m"
cyan = "\033[32;1m"
red = "\033[31;1m"
bold = "\033[1m"
cyan_blink = "\033[32;5m"
blink = "\033[5m"
enc_type = ''
enc_type_= ['tama7','tama127']


def banner():
	__banner = """
	[ """+cyan+"""Sashin Kakushi ( Hide files into image )"""+default+"""\t\t]
	[ """+blue+"""Author  """+default+""" : Rizal ( zal-byte )\t\t\t\t]
	[ """+blue+"""Github  """+default+""" : https://github.com/zal-byte/SashinKakushi\t]   
	[ """+orange+"""Note  """+default+"""   : Only Support .JPG, .PNG extension.\t\t]
	[ """+cyan+"""EncType  """+default+""": """+enc_type_[int(enc_type) - 1]+"""\t\t\t\t\t]
	"""
	return __banner

def help():
	__v = """
	"""+blue+"""========== Menu =========="""+default+"""
	"""+cyan+"""set_imgpath\t\t\t"""+default+""": Set image path
	"""+cyan+"""set_filepath\t\t\t"""+default+""": Set file path want to hide
	"""+cyan+"""set_bytesize\t\t\t"""+default+""": Set byte size ( More larger more lag if your device is low spec )
	"""+orange+"""\t\t\t\t[ Default byte size ( 10 ) bytes ]
	"""+cyan+"""save\t\t\t\t"""+default+""": Hide the file into image
	"""+blue+"""========== Mode =========="""+default+"""
	"""+cyan+"""extract\t\t\t\t"""+default+""": Set to extract mode
	"""+cyan+"""restore\t\t\t\t"""+default+""": Set to restore mode
	"""+blue+"""========== Program ======="""+default+"""
	"""+red+"""exit\t\t\t\t"""+default+""": Exit from this program
	"""
	print(__v)
def e_mode():
	__v = """
	"""+cyan+"""set_imgpath\t\t\t"""+default+""": Set image path
	"""+cyan+"""set_saveas\t\t\t"""+default+""": Set image save as
	"""+cyan+"""extract\t\t\t\t"""+default+""": Extract hidden files
	"""+blue+"""back\t\t\t\t"""+default+""": Back to hide mode
	"""
	print(__v)

def r_mode():
	__v = """
	"""+cyan+"""set_imgpath\t\t\t"""+default+""": Set image path
	"""+cyan+"""restore\t\t\t\t"""+default+""": Restore img files
	"""+blue+"""back\t\t\t\t"""+default+""": Back to hide mode
	"""
	print(__v)	

def preload():
	print( banner()) 

	_sashin = sashin.Sashin()
	_sashin.enc_type = enc_type
	pre = True
	pres = True
	while pre:
		cmd = input(bold+"hide_mode > "+default)
		cmd = cmd.split()
		if len(cmd) <= 1:
			if cmd[0].lower() == "help" or cmd[0].lower() == '?':
				help()
			elif cmd[0].lower() == "save":
				thread = Thread(target=_sashin.save())
				thread.start()
			elif cmd[0].lower() == "extract":
				_sashin.img_path = ""
				pres = True
				while pres:
					cm = input(bold+"extract_mode > "+default)
					cm = cm.split()
					if len(cm) > 1:
						if cm[0].lower() == "set_imgpath":
							_sashin.img_path = ""
							_sashin.set_ImgPath( cm[1] )
						elif cm[0].lower() == "set_saveas":
							_sashin.save_as = ""
							_sashin.set_SaveAs( cm[1] )
						else:
							print("[ * ] Insert img path")
					else:
						if cm[0].lower() == "help" or cm[0].lower() == '?':
							e_mode()						
						elif cm[0].lower() == "back":
							pres = False
						elif cm[0].lower() == "exit":
							exit()
						elif cm[0].lower() == "extract":
							if _sashin.save_as != "":
								_sashin.extract()
							else:
								print("[ ! ] Please set save as values")
						elif cm[0].lower() == "os(clear)":
							os.system('clear')
							print(banner())
						else:
							print("[ ? ] Unknown command, " +str(cm[0]))
			elif cmd[0].lower() == "restore":
				_sashin.img_path = ""
				pres = True
				while pres:
					cm = input(bold+"restore_mode > "+default)
					cm = cm.split()
					if len(cm) > 1:
						if cm[0].lower() == "set_imgpath":
							_sashin.img_path = ""
							_sashin.set_ImgPath( cm[1] )
						else:
							print("[ * ] Insert img path")
					else:
						if cm[0].lower() == "help" or cm[0].lower() == '?':
							r_mode()						
						elif cm[0].lower() == "back":
							pres = False
						elif cm[0].lower() == "exit":
							exit()
						elif cm[0].lower() == "restore":
							if _sashin.img_path != "":
								_sashin.restore()
							else:
								print("[ ! ] Please set img_path values")
						elif cm[0].lower() == "os(clear)":
							os.system('clear')
							print(banner())
						else:
							print("[ ? ] Unknown command, " +str(cm[0]))
			elif cmd[0].lower() == "exit":
				exit()
			elif cmd[0].lower() == "os(clear)":
				os.system('clear')
				print(banner())
			else:
				print("[ ? ] Unknown command, " +str(cmd[0]))
		else:
			if cmd[0].lower() == "set_imgpath":
				_sashin.img_path = ""
				_sashin.set_ImgPath( cmd[1] )
			elif cmd[0].lower() == "set_filepath":
				_sashin.file_path = ""
				_sashin.set_FilePath( cmd[1] )
			elif cmd[0].lower()== "set_bytesize":
				_sashin.byte_size = 10
				_sashin.set_byteSize(int(cmd[1]))

def msg( text ):
	print( text )
def exit():
	sys.exit()

if __name__ == "__main__":
	try:
		_bann = """
		[ Select encryption type ]
		[ 1 ] Tama7\t\t ]
		[ 2 ] Tama127\t\t ]
		[------------------------]
		"""
		print(_bann)
		c = str(input('select_> '))
		if c == '1':
			enc_type = '1'
		elif c=='2':
			enc_type = '2'
		else:
			print(red+'[ ! ] Select type of encryption first'+default)
		
		if c != '1':
			if c != '2':
				print(red + '[ ! ] Exiting...'+default)
			else:
				os.system('clear')
				preload()
		else:
			os.system('clear')
			preload()
	except KeyboardInterrupt:
		print(orange+"\n[ * ] Interrupted by CTRL + C"+default)
		
