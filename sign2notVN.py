import urllib2

web = urllib2.urlopen('http://daynhauhoc.com/raw/7089')
tep=open("amigo.txt","w")
tep.write(web.read())
tep.close


tep=open("amigo.txt","r")
print (tep.read())

#Ham chuyen tu co dau sang khong dau UTF-8
#Date first code: 2015/5/11
#Tac gia: Thanh Pham - @thanhmssl10 - DNH
#Dau vao la cac ki tu UTF-8, dau ra se la ki tu khong dau de hien thi tren cmd cua windows


def sign2notVN
