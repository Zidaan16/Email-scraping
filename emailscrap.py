import re, os, time, requests

os.system("cls")
merah = '\033[1;31m'
normal = '\033[0m'
# Useragent
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
# Banner
print("\033[31m      ________ ____ ____ __ ______ __________")
print("\033[31m     / __/ __// __// __// // / / // __/_  __/")
print(merah+"    / _// _ \/ _ \/ _ \/ _  /_  _/\ \  / /   ")
print(merah+"   /___/\___/\___/\___/_//_/ /_//___/ /_/  ")
print(" --------------------------------------------")
print("  Tools by: XDizzy25\n"+normal)
url = input("url> ")
print("\n")
# Main
r = requests.get(url, headers=user_agent)
regex = list(set(re.findall("([a-zA-Z0-9_.+-]+@+[a-zA-Z0-9._+-]+.[a-zA-Z0-9+]+)", r.text)))
for i in regex:
	print(i)
