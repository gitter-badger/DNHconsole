import DNHconsolelib
#Gioi Han Tham So Truyen Trang Home
mang1den20=[]
for  i in range(1,20):
	mang1den20.append(str(i))
GioiHanThamSoTruyenTrangHome=['i','l','c','h','x']+mang1den20
#Gioi Han Tham So Truyen Trang Comment Khi Chon Trang
GioiHanThamSoTruyenTrangComment1=['b']+mang1den20
#Gioi Han Tham So Truyen Trang Comment Khi Chon STT Comment
mang1den10=[]
for  i in range(1,10):
	mang1den10.append(str(i))
GioiHanThamSoTruyenTrangComment2=['f','l','b']+mang1den10


DNHconsolelib.help()
commander=raw_input('\nEnter de ve trang chu!')
DNHconsolelib.home()
commander=''
while commander!='x':
	print """
	Go i de xem lai trang gioi thieu
	Go l de mo trang moi nhat
	Go cac so trong khoang 1-20 de xem cach trang tuong ung
	Go c de xem comment
	Go h de ve trang chu
	Go x de thoat
	"""
	commander=str(raw_input('\nBan muon lam gi tiep theo? : '))
	#DUNG TRY de bo loi, khi DEBUG phai thay pass bang raise
	try:
		if commander in GioiHanThamSoTruyenTrangHome:
			if commander =='h':
				DNHconsolelib.home()
			elif commander =='i':
				DNHconsolelib.help()
			elif commander =='l':
				DNHconsolelib.home()
				DNHconsolelib.see(4)
			elif commander=='x':
				break
			elif commander=='c':
				idTopicComment=''
				while idTopicComment!='b' :
					idTopicComment=str(raw_input("\n   Go cac so trong khoang 1-20 tuong ung voi topic ban muon xem comment:\n   \
Go b de quay lai\n"))
					if idTopicComment in GioiHanThamSoTruyenTrangComment1:
						if idTopicComment=='b':
							break
						elif int(idTopicComment)>=1 and int(idTopicComment)<=20:
							cmdComment=''
							while cmdComment!='b':
								print """

	Go f de xem comment dau tien
	Go l de xem comment cuoi cung
	Go so thu tu comment ma ban muon xem
	Go b de quay lai
	"""
								cmdComment=str(raw_input('\nBan muon xem comment nao? : '))
								if cmdComment in GioiHanThamSoTruyenTrangComment2:
									if cmdComment=='b':
										break
		  					     	#eblif cmdComment =='l':
										#DNHconsolelib.seecomment(idTopicComment,MaxNumComment[idTopicComment])
									elif cmdComment =='f':
										DNHconsolelib.seecomment(idTopicComment,2)
									elif int(cmdComment)>=1 and int(cmdComment)<=10:
										DNHconsolelib.seecomment(int(idTopicComment),cmdComment)

						
			elif int(commander)>=1 and int(commander)<=20:
				DNHconsolelib.see(int(commander))


	except Exception, e:
		raise


	