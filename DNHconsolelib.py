# Date first code: 2015/5/11
# Thanh Pham - @thanhmssl10 - DNH
# DNHconsole module - Truy cap Daynhauhoc.com qua giao dien console

domain = 'http://daynhauhoc.com'
# Thoi gian thuc hien nhung cau lenh lay du lieu kha lau nen phai co WaitString
WaitString = "\nCho chut nhe :D ......"

GioiHanDong = 999
# Mang chua Ten cua cac Topic
TenTopicHome = []
# So Topic da lay duoc, thuong la 30 topic
SoTopic = 0
# So luong comment cua cac Topic
NumCommentTopicHome = []
# Manrg chua ID topic o trang home
IDTopicHomeRaw = []
# Mang chua link topic da convert sang link raw
LinkTopicHomeRaw = []
# Mang chua CategoryID cua topic, mamg nay di cung tu dien CategoryTextID
CategoryID = []
CategoryTextID = {'1': 'Uncategorized', '3': 'Meta', '5': 'Videos', '6': 'Fun',
                  '7': 'HackerNews', '9': 'Programming', '20': 'English', '29': 'Unix-Linux',
                  '34': 'Windows', '32': 'Share', '33': 'Computer', '31': 'Writes', '21': 'Jobs',
                  '23': 'Devchat'}


# In nhung dong dau tien ma user nhin thay
def help():
    print """

    #Gioi thieu chung cac chuc nang cua DNHconsole """
# 1.Lay du lieu cua cac topic nhu: Ten topic, link thuong dung,
# so comment, user tham gia thao luan, so view, thoi gian active
# lan cuoi,...
# ===============================================================
# Ham ho tro viec boc tach du lieu

def LayChuoi(DayGoc, DayDinhVi, KiTuKetThuc):

    ViTriCuaDayDinhVi = DayGoc.find(DayDinhVi)
    ViTriCuaKiTuKetThuc = 0
    if ViTriCuaDayDinhVi > 0:
        ViTriCuaKiTuKetThuc = DayGoc.find(
            KiTuKetThuc, (ViTriCuaDayDinhVi+len(DayDinhVi)))

    DayOutput = ""
    if ViTriCuaKiTuKetThuc > 0:
        DayOutput = DayGoc[
            (ViTriCuaDayDinhVi+len(DayDinhVi)):ViTriCuaKiTuKetThuc]

    if DayOutput != "":
        return DayOutput
    else:
        return "nothing"
# Ham lay ID cua topic, ho tro cho ham linktoraw


def LayIDtopic(link):
    ViTriCuaKiTuBatDau = link.find("/", len(domain)+5)
    DemSoKiTuCanCat = 0
    for i in range(0, 200):
        try:

            if link[ViTriCuaKiTuBatDau:][i].isdigit:
                DemSoKiTuCanCat += 1
            else:
                break
        except:
            break
            pass
    ID = link[ViTriCuaKiTuBatDau + 1:ViTriCuaKiTuBatDau + DemSoKiTuCanCat]
    return ID
# Ham chuyen doi link thuong dung sang link raw de dang dang lay noi dung topic


def linktoraw(link):
    return domain + "/raw/" + str(LayIDtopic(link))
# Ham cho du lieu goc tu mot link bat ki


def sourcetext(link):

    print WaitString

    # Luu du lieu web vao mot phai temp
    import urllib2
    web = urllib2.urlopen(link)
    tep = open('tempDNHpage.txt', "w")
    tep.write(web.read())
    tep.close()

    # Chuyen doi chu co dau thanh khong dau de cmd hien thi de dang
    import unicodedata
    input = open('tempDNHpage.txt').read().decode('UTF-8')
    output = unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')

    # Ghi lai du lieu da chuyen doi vao file temp
    tep = open('tempDNHpage.txt', "w")
    tep.write(output)
    tep.close()
    return output

# Cap nhat mot so thong tin cua cac topic


def updateDataHome():
    # Dung sourcetext de lay du lieu tu trang chu
    # Tach dong tu du lieu cua sourcetext dua vao mang
    PhoiDulieuTrangHomeDaTachDong = sourcetext(domain).splitlines()
    # Trich xuat du lieu cua moi topic, gan ID cho moi topic
    # Duyet tung dong cua Phoi Du Lieu
    for i in range(0, PhoiDulieuTrangHomeDaTachDong.__len__()):
        # Trich xuat Ten topic
        # Dung ham lay chuoi de tach du lieu theo tung dong
        if LayChuoi(PhoiDulieuTrangHomeDaTachDong[i], "<span itemprop='name'>", "<") != "nothing":
            TenTopicHome.append(LayChuoi(PhoiDulieuTrangHomeDaTachDong[i], "<span itemprop='name'>", "<"))
        # Trich xuat so topic
        if (i == PhoiDulieuTrangHomeDaTachDong.__len__() - 1):
            global SoTopic
            SoTopic = TenTopicHome.__len__()
        # Trich xuat ID topic
        if LayChuoi(PhoiDulieuTrangHomeDaTachDong[i], "<meta itemprop='url' content='", "'") != "nothing":
            IDTopicHomeRaw.append(LayIDtopic(LayChuoi(
                PhoiDulieuTrangHomeDaTachDong[i], "<meta itemprop='url' content='", "'")))
        # Trich xuat Link toptic (sau do tach ra Link raw)
        if LayChuoi(PhoiDulieuTrangHomeDaTachDong[i], "<meta itemprop='url' content='", "'") != "nothing":
            LinkTopicHomeRaw.append(linktoraw(LayChuoi(
                PhoiDulieuTrangHomeDaTachDong[i], "<meta itemprop='url' content='", "'")))
    # Duyet lai tung dong cua Phoi Du Lieu de trich xuat cac du lieu con lai
    for i in range(0, PhoiDulieuTrangHomeDaTachDong.__len__()):
        # Trich xuat Category
        for STT in range(0, SoTopic):
            # Tim kiem theo ID cua topic
            ChuoiDinhViChuaIDTopic = '"id":'+IDTopicHomeRaw[STT]+',"title"'
            if '"id":'+IDTopicHomeRaw[STT]+',"title"'in PhoiDulieuTrangHomeDaTachDong[i]:
                # Thu hep Vung Tim Kiem
                VungTimKiemCategory = PhoiDulieuTrangHomeDaTachDong[i][
                    PhoiDulieuTrangHomeDaTachDong[i].find(ChuoiDinhViChuaIDTopic):]
                if "category_id" in VungTimKiemCategory:
                    ViTriChuoiTimCategory = VungTimKiemCategory.find(
                        "category_id")
                    VungTimKiemCategory = VungTimKiemCategory[
                        ViTriChuoiTimCategory+len("category_id")+2:ViTriChuoiTimCategory+len("category_id")+2+6]
                    CategoryIDofThisPage = ""
                    GioiHanSoKiTuCuaID = 0
                    while VungTimKiemCategory[0:1].isdigit() and GioiHanSoKiTuCuaID < 5:
                        GioiHanSoKiTuCuaID += 1
                        CategoryIDofThisPage += VungTimKiemCategory[0:1]
                        VungTimKiemCategory = VungTimKiemCategory[1:]
                    CategoryID.append(CategoryIDofThisPage)
        # Trich xuat Replies (So comment)
        if LayChuoi(PhoiDulieuTrangHomeDaTachDong[i], "<span title='posts'>(", ")") != "nothing":
            NumCommentTopicHome.append(LayChuoi(PhoiDulieuTrangHomeDaTachDong[i], "<span title='posts'>(", ")"))

        # Trich xuat Users(user tham gia thao luan topic do)

        # Trich xuat Views(So luot View)


        
    # for i in range(0,30):
    #     print NumCommentTopicHome[i]



    # luu vao tempHome.txt
    # fileTempHome=open('tempHome.txt','w')
    # fileTempHome.write(sourcetext(domain))
    # fileTempHome.close()
    # Load tung dong du lieu tu temp.txt ra de xu li theo tung dong

# Cap nhat toan bo du lieu cua cac topic, danh cho ket noi tot


def updateFullDataHome():

    print SoTopic

# 2.Show du lieu: In Danh sach Topic, In Topic, In Commment, ...
# ===============================================================
# Ham show ra danh sach topic moi nhat tren trang chu


def showhome():
    if True:
        for STTTopic in range(0, SoTopic // 2):
            if STTTopic < 10:
                print "\n[0" + str(STTTopic) + "]: " + str(TenTopicHome[STTTopic]) + " ["+CategoryTextID[CategoryID[STTTopic]]+"]"
            else:
                print "\n[" + str(STTTopic) + "]: " + str(TenTopicHome[STTTopic]) + " ["+CategoryTextID[CategoryID[STTTopic]]+"]"
        print "\n\n\n  Enter de xem tiep!!!"
        raw_input()
        for STTTopic in range(SoTopic//2, SoTopic):
            if STTTopic < 10:
                print "\n[0"+str(STTTopic)+"]: " + str(TenTopicHome[STTTopic]) + " ["+CategoryTextID[CategoryID[STTTopic]]+"]"
            else:
                print "\n["+str(STTTopic)+"]: " + str(TenTopicHome[STTTopic]) + " ["+CategoryTextID[CategoryID[STTTopic]]+"]"
# Ham show ra noi dung topic, an enter de chuyen


def see(ID):
    if LinkTopicHomeRaw[ID] == "":
        updateDataHome()
    print WaitString
    import urllib2
    web = urllib2.urlopen(LinkTopicHomeRaw[ID])
    tep = open('tempDNHpage.txt', "w")
    tep.write(web.read())
    tep.close()

    import unicodedata
    input = open('tempDNHpage.txt').read().decode('UTF-8')
    output = unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')

    tep = open('tempDNHpage.txt', "w")
    tep.write(output)
    tep.close()
    tep = open('tempDNHpage.txt', "r")

    print "\n\n\n"
    print "===================================================="
    print "===================================================="
    print "===================================================="
    print "\n\n\n"
    print "  "+"["+str(ID)+"]:"+TenTopicHome[ID]
    print "\n"
    for i in range(0, GioiHanDong):
        textline = tep.readline()
        if textline != "":
            print textline
            raw_input()
    print "\n\n\n"
    print "===================================================="
    print "===================================================="
    print "===================================================="
    print "\n\n\n"
    tep.close()
# Ham show ra TAT CA noi dung topic

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
# Ham show ra noi dung comment thu STT cua topic co ma so la ID


def seecomment(ID, STT):
    if str(LinkTopicHomeRaw[int(ID)]) == '':
        print "Link Trang Home bi trong"
        updateDataHome()
    link = LinkTopicHomeRaw[int(ID)]+"/"+str(STT)

    print WaitString

    import urllib2
    web = urllib2.urlopen(link)
    tep = open('tempDNHpage.txt', "w")
    tep.write(web.read())
    tep.close()

    import unicodedata
    input = open('tempDNHpage.txt').read().decode('UTF-8')
    output = unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')

    tep = open('tempDNHpage.txt', "w")
    tep.write(output)
    tep.close()

    tep = open('tempDNHpage.txt', "r")

    print "\n\n\n"
    print "===================================================="
    print "===================================================="
    print "===================================================="
    print "\n\n\n"
    print "  Comment["+str(STT)+"]:"+"["+str(ID)+"]"+":"+TenTopicHome[int(ID)]
    print "\n"
    for i in range(0, GioiHanDong):
        textline = tep.readline()
        if textline != "":
            print textline
            raw_input()
    print "\n\n\n"
    print "===================================================="
    print "===================================================="
    print "===================================================="
    print "\n\n\n"
    tep.close()
