import requests as rq
import shutil
import ctypes

def down_pic(url, path):
	#path='new_file.jpg'
	if "imgur" in url:
		url+=".jpg"
	r = rq.get(url, stream=True)
	if r.status_code == 200:
	    with open(path, 'wb') as f:
	        r.raw.decode_content = True
	        shutil.copyfileobj(r.raw, f) 

def set_wallpaper(path):
	SPI_SETDESKWALLPAPER=20
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER,0,path,0)


down_pic('https://imgur.com/1EtMzkQ', 'imgur_pic.jpg')