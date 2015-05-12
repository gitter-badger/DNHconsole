#Date first code: 2015/5/11
#Tac gia: Thanh Pham - @thanhmssl10 - DNH
#DNHconsole module - Truy cap Daynhauhoc.com qua giao dien console


#1.Lay thong tin cua cac topic nhu: Ten topic, link thuong dung, so comment, user tham gia thao luan, so view, thoi gian active lan cuoi,...
domain='http://daynhauhoc.com'
GioiHanDong=999
WaitString="\nCho chut nhe :D ......"

LinkTrangHome=[]
TenBaiVietGlobal=[]
for i in range(0,50):       
        LinkTrangHome.append("")
        TenBaiVietGlobal.append("")

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
def sourcetext(link):
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
    return output

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
def help():
    print """






    #Gioi thieu chung cac chuc nang cua DNHconsole

    Day la module truy cap dien dan Daynhauhoc.com qua giao dien dong lenh
    (console) duoc viet bang Python 2.7.9 do Thanh Pham - @thanhmssl10 dat
    nhung dong code dau tien vao ngay 11/5/2015.

    ##Moudule co cac ham chinh nhu sau:

    ###2 Ham User su dung nhieu nhat    
    home():Ham nay khong co tham so, dung de xem cac bai viet moi nhat
    --------------------------------------------------------------------
    see(ID):   Co 1 tham so truyen vao la so tu 1 den 20
    --------------------------------------------------------------------


    ###Cac ham mo rong    
    show():    Co 2 tham so truyen vao la Link cua trang can xem va ID cua no
    vidu:      show('http://daynhauhoc.com/raw/7127',1)

    Ham nay in ra tren man hinh noi dung cua trang web va chuyen dong khi an
    Enter
    --------------------------------------------------------------------


    showall():  Co 1 tham so truyen vao la Link cua trang can xem
    vidu:       show('http://daynhauhoc.com/raw/7127',1)
    ...
    Ham day se in toan bo noi dung cua trang web ra cung luc
    --------------------------------------------------------------------
    





    Enter de doc tiep...
    """
    raw_input()
    print """






    #Gioi thieu chung cac chuc nang cua DNHconsole

    Ngoai nhung ham do ra thi module con co mot ho ham khac de phuc vu cho
    viec trich xuat du lieu tu website.

    Cac ham do la nhung ham tim, cat chuoi, nhung ham de chuyen tu link thuong
    sang link raw








    
















    
    
    

    
    """
