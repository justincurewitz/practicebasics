import requests as rq
import praw
import get_pic
import string
import time

def monitor_user(username):
	api_info=open('reddit_api_info.txt', 'r')
	client=api_info.readline().split(":")[1].replace("\n","")
	secret=api_info.readline().split(":")[1].replace("\n","")
	ua=api_info.readline().split(":")[1]
	reddit=praw.Reddit(client_id=client, client_secret=secret, user_agent=ua)
	user=reddit.redditor(username)
	comments=user.comments.new()
	bg="background"
	info=open('last_bg_info.txt', 'r')
	id=info.readline().split(":")[1].replace("\n","")
	name=info.readline().split(":")[1].replace("\n","")
	for comment in comments:
		if comment.fullname == id:
			break
		if comment.body == bg:
			sub=comment.submission
			new_name="bg_"+str(string.atoi(name.split("_")[1].split(".")[0])+1)+'.jpg'
			get_pic.down_pic(sub.url, new_name)
			new_file="id:"+comment.fullname+"\nfile_name:"+new_name
			path="C:\\Users\\Justin\\Documents\\programs\\practicebasics\\python\\reddit_auto_background\\"+new_name
			get_pic.set_wallpaper(path)
			info=open('last_bg_info.txt', 'w')
			info.write(new_file)
			print "New Background downloaded!"
			break

while(True):
	monitor_user('a_texan_')
	time.sleep(10)