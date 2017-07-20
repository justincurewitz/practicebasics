import ctypes

def set_wallpaper:
	SPI_SETDESKWALLPAPER=20
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER,0,"C:\\Users\\Justin\\Documents\\programs\\practicebasics\\python\\reddit_auto_background\\new_bg.jpg",0)