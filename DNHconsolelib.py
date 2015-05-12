#Date first code: 2015/5/11
#Thanh Pham - @thanhmssl10 - DNH
#DNHconsole module - Truy cap Daynhauhoc.com qua giao dien console

domain='http://daynhauhoc.com'
GioiHanDong=999
#Thoi gian thuc hien nhung cau lenh lay du lieu kha lau nen phai co WaitString
WaitString="\nCho chut nhe :D ......"
#Cac mang chua Ten topic va link raw
LinkTrangHome=[]
TenBaiVietGlobal=[]
for i in range(0,50):       
        LinkTrangHome.append("")
        TenBaiVietGlobal.append("")


def help():
    print """

    #Gioi thieu chung cac chuc nang cua DNHconsole

     """
#1.Lay du lieu cua cac topic nhu: Ten topic, link thuong dung, so comment, user tham gia thao luan, so view, thoi gian active lan cuoi,...
#Ham ho tro viec boc tach du lieu                   
def LayChuoi(DayGoc,DayDinhVi,KiTuKetThuc):

    ViTriCuaDayDinhVi=DayGoc.find(DayDinhVi)
    ViTriCuaKiTuKetThuc=0
    if ViTriCuaDayDinhVi>0:
        ViTriCuaKiTuKetThuc=DayGoc.find(KiTuKetThuc,(ViTriCuaDayDinhVi+len(DayDinhVi)))

    DayOutput=""
    if ViTriCuaKiTuKetThuc>0:
        DayOutput=DayGoc[(ViTriCuaDayDinhVi+len(DayDinhVi)):ViTriCuaKiTuKetThuc]


    if DayOutput != "":
        return DayOutput
    else:
        return -1
#Ham chuyen doi link thuong dung sang link raw de dang dang lay noi dung topic
def linktoraw(link):
    ViTriCuaKiTuBatDau=link.find("/",len(domain)+5)

    DemSoKiTuCanCat=0
    for i in range(0,200):
        try:
            if link[ViTriCuaKiTuBatDau:][i].isdigit:
                DemSoKiTuCanCat+=1
            else:
                break
        except:
            break
            pass
        
        
    linkRaw=link[ViTriCuaKiTuBatDau+1:ViTriCuaKiTuBatDau+DemSoKiTuCanCat]
    return domain+"/raw/" + str(linkRaw) 
#Ham cho du lieu goc tu mot link bat ki
def sourcetext(link):
    print WaitString

    #Luu du lieu web vao mot phai temp
    import urllib2
    web = urllib2.urlopen(link)
    tep=open('tempDNHpage.txt',"w")
    tep.write(web.read())
    tep.close()
   
    #Chuyen doi chu co dau thanh khong dau de cmd hien thi de dang
    import unicodedata
    input = open('tempDNHpage.txt').read().decode('UTF-8')
    output = unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')

    #Ghi lai du lieu da chuyen doi vao file temp
    tep=open('tempDNHpage.txt',"w")
    tep.write(output)
    tep.close()
    return output
#2.Show du lieu: In Danh sach Topic, In Topic, OIn Commment, ... 

def see(ID):
    if LinkTrangHome[ID]=="":
        home()
    print WaitString
    import urllib2
    web = urllib2.urlopen(LinkTrangHome[ID])
    tep=open('tempDNHpage.txt',"w")
    tep.write(web.read())
    tep.close()
   
    import unicodedata
    input = open('tempDNHpage.txt').read().decode('UTF-8')
    output = unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')

    tep=open('tempDNHpage.txt',"w")
    tep.write(output)
    tep.close()
    tep=open('tempDNHpage.txt',"r")
    
    print "\n\n\n"
    print "===================================================="
    print "===================================================="
    print "===================================================="
    print "\n\n\n"
    print "  "+"["+str(ID)+"]:"+TenBaiVietGlobal[ID]
    print "\n"
    for i in range(0,GioiHanDong):
        textline=tep.readline()
        if textline!="":
            print textline
            raw_input()
    print "\n\n\n"
    print "====================================================" 
    print "===================================================="
    print "====================================================" 
    print "\n\n\n"
    tep.close()
def showall(link):
    print "\n\n\n"
    print "===================================================="
    print "===================================================="
    print "===================================================="
    print "\n\n\n"
    print "\n"
    print sourcetext(link)
    print "\n\n\n"
    print "====================================================" 
    print "===================================================="
    print "====================================================" 
    print "\n\n\n"
def seecomment(ID,STT):
    if str(LinkTrangHome[int(ID)])=='':
        print "Link Trang Home bi trong"
        home()
    link=LinkTrangHome[int(ID)]+"/"+str(STT)
    

    print WaitString
    
    import urllib2
    web = urllib2.urlopen(link)
    tep=open('tempDNHpage.txt',"w")
    tep.write(web.read())
    tep.close()
   
    import unicodedata
    input = open('tempDNHpage.txt').read().decode('UTF-8')
    output = unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')

    tep=open('tempDNHpage.txt',"w")
    tep.write(output)
    tep.close()
 
    tep=open('tempDNHpage.txt',"r")
    
    print "\n\n\n"
    print "===================================================="
    print "===================================================="
    print "===================================================="
    print "\n\n\n"
    print "  Comment["+str(STT)+"]:"+"["+str(ID)+"]"+":"+TenBaiVietGlobal[int(ID)]
    print "\n"
    for i in range(0,GioiHanDong):
        textline=tep.readline()
        if textline!="":
            print textline
            raw_input()
    print "\n\n\n"
    print "====================================================" 
    print "===================================================="
    print "====================================================" 
    print "\n\n\n"
    tep.close()
def home():
    TempHome=open('tempHome.txt','w')
    TempHome.write(sourcetext(domain))
    TempHome.close()
    
    TempHome=open('tempHome.txt','r')
    lineData=[]
    for i in range(0,GioiHanDong+1):
        lineData.append(TempHome.readline())



    
    STTTopic=0
    for i in range(0,GioiHanDong):
        TenBaiViet=LayChuoi(lineData[i],"<span itemprop='name'>","<")
        if (TenBaiViet!=-1) and (STTTopic < 20):
            STTTopic = STTTopic+1
            if STTTopic <10:
                print "\n[0"+str(STTTopic)+"]: "+ str(TenBaiViet)
                
            else:
                print "\n["+str(STTTopic)+"]: "+ str(TenBaiViet)
            TenBaiVietGlobal[STTTopic]=TenBaiViet

    STTLink=0
    for i in range(0,GioiHanDong):
        LinkBaiViet=LayChuoi(lineData[i],"<meta itemprop='url' content='","'")
        if (LinkBaiViet!=-1) and (STTLink < 20):
            STTLink= STTLink+1
            LinkTrangHome[STTLink]=linktoraw(LinkBaiViet)


