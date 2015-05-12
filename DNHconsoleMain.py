import DNHconsolelib
import os
#Gioi Han Tham So Truyen Trang Home
mang1den20=[]
for  i in range(1,20):
	mang1den20.append(str(i))
GioiHanThamSoTruyenTrangHome=['m','i','l','c','h','x']+mang1den20
#Gioi Han Tham So Truyen Trang Comment Khi Chon Trang
GioiHanThamSoTruyenTrangComment1=['b']+mang1den20
#Gioi Han Tham So Truyen Trang Comment Khi Chon STT Comment
mang1den10=[]
for  i in range(1,10):
	mang1den10.append(str(i))
GioiHanThamSoTruyenTrangComment2=['f','l','b','']+mang1den10


DNHconsolelib.help()
commander=raw_input('\nEnter de ve trang chu!')
DNHconsolelib.home()
commander=''
while commander!='x':
	print """
	Go m de doi mau chu(Chuc nang nay co the bi Antivirus Warning)
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
			if commander =='m':
				DNHconsolelib.home()
				os.system('color '+str(raw_input('Go 1 trong cac so 1-9 de chon mau, hoac tu a den f: ')))
				continue
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
							DaXem1Comment = False
							cmdComment=''
							while cmdComment!='b':
								if DaXem1Comment:
									print """
	\n\nEnter de xem comment TIEP THEO!!!!!
	Go f de xem comment dau tien
	Go l de xem comment cuoi cung
	Go so thu tu comment ma ban muon xem
	Go b de quay lai
	"""
									cmdCommentBefore=cmdComment
									cmdComment=str(raw_input('\nBan muon xem comment nao? : '))
									if cmdComment in GioiHanThamSoTruyenTrangComment2:
										if cmdComment=='b':
											break
										elif cmdComment=='' and str(cmdCommentBefore) in mang1den10 and cmdCommentBefore!='10':
											DNHconsolelib.seecomment(idTopicComment,cmdCommentBefore+1)
			  					     	#eblif cmdComment =='l':
											#DNHconsolelib.seecomment(idTopicComment,MaxNumComment[idTopicComment])
											#DaXem1Comment=True
										elif cmdComment =='f':
											cmdComment=2
											DNHconsolelib.seecomment(idTopicComment,cmdComment)
											DaXem1Comment=True
										elif int(cmdComment)>=1 and int(cmdComment)<=10:
											DNHconsolelib.seecomment(int(idTopicComment),cmdComment)
											DaXem1Comment=True									
								else:	
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
										elif cmdComment=='':
												continue
			  					     	#eblif cmdComment =='l':
											#DNHconsolelib.seecomment(idTopicComment,MaxNumComment[idTopicComment])
											#DaXem1Comment=True
										elif cmdComment =='f':
											cmdComment=2
											DNHconsolelib.seecomment(idTopicComment,cmdComment)
											DaXem1Comment=True
										elif int(cmdComment)>=1 and int(cmdComment)<=10:
											DNHconsolelib.seecomment(int(idTopicComment),cmdComment)
											DaXem1Comment=True
						
			elif int(commander)>=1 and int(commander)<=20:
				DNHconsolelib.see(int(commander))


	except Exception, e:
		raise


	