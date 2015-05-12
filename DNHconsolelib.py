#Date first code: 2015/5/11
#Thanh Pham - @thanhmssl10 - DNH
#DNHconsole module - Truy cap Daynhauhoc.com qua giao dien console

domain='http://daynhauhoc.com'
GioiHanDong=999
#Mang chua du lieu cua cac Topic
TenTopicHome=[]
SoTopic=0
#Manrg chua ID topic o trang home
IDTopicHomeRaw=[]
#Mang chua link topic da convert sang link raw
LinkTopicHomeRaw=[]
#Mang chua CategoryID cua topic, amg nay di cung mang CategoryTextofID

CategoryTextofID

#Trash
lineData=[]
TenBaiVietGlobal=[]
LinkTrangHome=[]
for i in range(0,50):       
        LinkTrangHome.append("")
        TenBaiVietGlobal.append("")

#In nhung dong dau tien ma user nhin thay
def help():
    print """

    #Gioi thieu chung cac chuc nang cua DNHconsole """
# 1.Lay du lieu cua cac topic nhu: Ten topic, link thuong dung, so comment, user tham gia thao luan, so view, thoi gian active lan cuoi,...
# ===============================================================
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
        return "nothing"
#Ham lay ID cua topic, ho tro cho ham linktoraw
def LayIDtopic(link):
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
    ID=link[ViTriCuaKiTuBatDau+1:ViTriCuaKiTuBatDau+DemSoKiTuCanCat]
    return ID
#Ham chuyen doi link thuong dung sang link raw de dang dang lay noi dung topic
def linktoraw(link):
    return domain+"/raw/" + str(LayIDtopic) 
#Ham cho du lieu goc tu mot link bat ki
def sourcetext(link):
    #Thoi gian thuc hien nhung cau lenh lay du lieu kha lau nen phai co WaitString
    WaitString="\nCho chut nhe :D ......"
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

#Cap nhat mot so thong tin cua cac topic
def updateDataHome():
    #Dung sourcetext de lay du lieu tu trang chu
    ##Tach dong tu du lieu cua sourcetext dua vao mang
    PhoiDulieuTrangHomeDaTachDong=sourcetext(domain).splitlines()
    #Trich xuat du lieu cua moi topic, gan ID cho moi topic
    ##Duyet tung dong cua Phoi Du Lieu
    for i in range(0,PhoiDulieuTrangHomeDaTachDong.__len__()):
    ##Trich xuat Ten topic
    ###Dung ham lay chuoi de tach du lieu theo tung dong
        if LayChuoi(PhoiDulieuTrangHomeDaTachDong[i],"<span itemprop='name'>","<") !="nothing":
            TenTopicHome.append(LayChuoi(PhoiDulieuTrangHomeDaTachDong[i],"<span itemprop='name'>","<"))
        #Trich xuat so topic
        if (i==PhoiDulieuTrangHomeDaTachDong.__len__()-1):
            SoTopic=TenTopicHome.__len__()
        #Trich xuat ID topic
        if LayChuoi(PhoiDulieuTrangHomeDaTachDong[i],"<meta itemprop='url' content='","'") !="nothing":
            IDTopicHomeRaw.append(LayIDtopic(LayChuoi(PhoiDulieuTrangHomeDaTachDong[i],"<meta itemprop='url' content='","'")))       
        #Trich xuat link raw topic
        if LayChuoi(PhoiDulieuTrangHomeDaTachDong[i],"<meta itemprop='url' content='","'") !="nothing":
            LinkTopicHomeRaw.append(linktoraw(LayChuoi(PhoiDulieuTrangHomeDaTachDong[i],"<meta itemprop='url' content='","'")))
        ##Trich xuat Category

        ##Trich xuat Users(user tham gia thao luan topic do)
        ##Trich xuat Replies (So comment)
        ##Trich xuat Views(So luot View)
        ##Trich xuat Link toptic (sau do tach ra Link raw)
    for i in range(0,PhoiDulieuTrangHomeDaTachDong.__len__()):
        if IDTopicHomeRaw[0] in PhoiDulieuTrangHomeDaTachDong[i]:
            if "category_id" in PhoiDulieuTrangHomeDaTachDong[i][PhoiDulieuTrangHomeDaTachDong[i].find(IDTopicHomeRaw[0]):]:
                print PhoiDulieuTrangHomeDaTachDong[i][PhoiDulieuTrangHomeDaTachDong[i].find("category_id")+len("category_id")+2:PhoiDulieuTrangHomeDaTachDong[i].find("category_id")+len("category_id")+3]
    

    #luu vao tempHome.txt
    # fileTempHome=open('tempHome.txt','w')
    # fileTempHome.write(sourcetext(domain))
    # fileTempHome.close()
    #Load tung dong du lieu tu temp.txt ra de xu li theo tung dong
    return IDTopicHomeRaw[0]

#Cap nhat toan bo du lieu cua cac topic, danh cho ket noi tot
def updateFullDataHome():
    PhoiDuLieuHomeChuaTachDong=sourcetext(domain)

#2.Show du lieu: In Danh sach Topic, In Topic, In Commment, ... 
# ===============================================================
#Ham show ra danh sach topic moi nhat tren trang chu 
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
#Ham show ra noi dung topic, an enter de chuyen
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
#Ham show ra TAT CA noi dung topic
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
#Ham show ra noi dung comment thu STT cua topic co ma so la ID
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
