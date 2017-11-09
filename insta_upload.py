#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import sys
import os

bot_user = 'UserName'
bot_pwd = 'PassWord'

def bot_profile_art(cred):
	''' Caption and hashtags '''
	print "[+] Using profile: Art"
	caption = 'Artist: {}\n\n#art#artwork#artist'.format(cred)
	return caption

def bot_profile_nature(cred):
	''' Caption and hashtags '''
	print "[+] Using profile: Nature"
	caption = 'Photographer: {}\n\n#amazing#nature#landscape'.format(cred)
	return caption

def bot_download_image(url,image_file):
	''' Download image from HTTP/HTTPS server '''
	try:
		print "[+] Downloading image from: {}".format(url)
		image_data = requests.get(url).content
	except Exception as e:
		print "[-] Unable to download image from: {}".format(url)

	''' Write data to disk '''
	try:
		with open(image_file, 'wb') as handler:
			handler.write(image_data)
			handler.close()
	except Exception as e:
		print "[-] Unable to write image file to disk"
	
def bot_upload_image(caption,image_file):
	''' import '''
	from InstagramAPI import InstagramAPI

	''' Login to bot '''	
	try:
		print "[+] Logging in as: {}".format(bot_user)
		api = InstagramAPI(bot_user,bot_pwd)
		api.login()
	except Exception as e:
		print "[-] Unable login as: {}".format(bot_user)

	''' Upload image '''		
	try:
		print "[+] Uploading image"
		api.uploadPhoto(image_file,caption=caption)
		if api.LastResponse.text == '{"status": "ok"}':
			print "[+] Upload done\n"
		if api.LastResponse.text == '{"message": "Uploaded image isn\'t in an allowed aspect ratio", "status": "fail"}':
			print "[-] Uploaded image isn't in an allowed aspect ratio"
	except Exception as e:
		print "[-] Unable to upload image {}".format(image_file)

	''' Removes the image once uploaded '''
	if os.path.exists(image_file):
		os.remove(image_file)

def bot_help():
	os.system("cls" if os.name == "nt" else "clear")
	print '''
     ___o .--.
   /___| |OO|       _         _       ___                       
  /'   |_|  |_     |_|___ ___| |_ ___|  _|___ _____ ___ _ _ ___ 
       (_    _)    | |   |_ -|  _| .'|  _| .'|     | . | | |_ -|     
       | |   \     |_|_|_|___|_| |__,|_| |__,|_|_|_|___|___|___|
       | |__./      Tool for uploading images to instagram bots
  
 Usage:
    python bot_upload.py -d <url>
    python bot_upload.py -u -p art -c Unknown
    python bot_upload.py -u -p nature -c Unknown
	'''		
	
def main():
	''' Print banner and usage '''
	bot_help()
	
	
	''' Args '''
	try:
		if sys.argv[1] == "-d":
			bot_download_image(sys.argv[2],'image.jpg')
		if sys.argv[1] == "-u":
			if sys.argv[2] == "-p": 
				if sys.argv[3] == "art":
					if sys.argv[4] == "-c":
						#print "[+] >>> Caption: {}\n[+] >>> File: {}".format(bot_profile_art(sys.argv[5]),'image.jpg')
						bot_upload_image(bot_profile_art(sys.argv[5]),'image.jpg')
		if sys.argv[1] == "-u":
			if sys.argv[2] == "-p": 
				if sys.argv[3] == "nature":
					if sys.argv[4] == "-c":
						#print "[+] >>> Caption: {}\n[+] >>> File: {}".format(bot_profile_nature(sys.argv[5]),'image.jpg')
						bot_upload_image(bot_profile_nature(sys.argv[5]),'image.jpg')
	except Exception as e:
		pass

if __name__ == "__main__":
	main()
