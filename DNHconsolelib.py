# Date first code: 2015/5/11
# Thanh Pham - @thanhmssl10 - DNH
# DNHconsole module - Truy cap Daynhauhoc.com qua giao dien console
import os
import msvcrt


domain = 'http://daynhauhoc.com'
# Thoi gian thuc hien nhung cau lenh lay du lieu kha lau nen phai co WaitString
WaitString = "\nCho chut nhe :D ......"

GioiHanDong = 999
# Mang chua Ten cua cac Topic
TenTopicHome = []
# So Topic da lay duoc, thuong la 30 topic
SoTopic = 0
# So luong comment cua cac Topic
NumTopic = []
# Manrg chua ID topic o trang home
IDTopicHomeRaw = []
# Mang chua link topic da convert sang link raw
LinkTopicHomeRaw = []
# Mang chua CategoryID cua topic, mamg nay di cung tu dien CategoryTextID
CategoryID = []
CategoryTextID = {'1': 'Uncategorized', '3': 'Meta', '5': 'Videos', '6': 'Fun',
                  '7': 'HackerNews', '9': 'Programming', '20': 'English',
                  '29': 'Unix-Linux', '34': 'Windows', '32': 'Share',
                  '33': 'Computer', '31': 'Writes', '21': 'Jobs',
                  '23': 'Devchat'}


# In nhung dong dau tien ma user nhin thay
def clear_screen():
    os.system('cls')


def flush_input():
    while msvcrt.kbhit():
        msvcrt.getch()


def help():
    clear_screen()
    print """

    #Gioi thieu chung cac chuc nang cua DNHconsole """


# 1.Lay du lieu cua cac topic nhu: Ten topic, link thuong dung,
# so comment, user tham gia thao luan, so view, thoi gian active
# lan cuoi,...
# ===============================================================


# Ham ho tro viec boc tach du lieu
# Ham tach du lieu ra khoi mot chuoi co day dinh vi la ki tu ket thuc
def laychuoi(daygoc, daydinhvi, kituketthuc):

    vi_tri_day_dinh_vi = daygoc.find(daydinhvi)
    vi_tri_cua_ki_tu_ket_thuc = 0
    if vi_tri_day_dinh_vi > 0:
        vi_tri_cua_ki_tu_ket_thuc = daygoc.find(
            kituketthuc, (vi_tri_day_dinh_vi + len(daydinhvi)))

    dayoutput = ""
    if vi_tri_cua_ki_tu_ket_thuc > 0:
        dayoutput = daygoc[
            (vi_tri_day_dinh_vi + len(daydinhvi)):vi_tri_cua_ki_tu_ket_thuc]

    if dayoutput != "":
        return dayoutput
    else:
        # Khong tach duoc thi xuat "nothing"
        return "nothing"


# Ham lay ID cua topic, ho tro cho ham linktoraw
def lay_id_topic(link):
    vi_tri_ki_tu_bat_dau = link.find("/", len(domain) + 5)
    dem_so_ki_tu_can_cat = 0
    for i in range(0, 200):
        try:

            if link[vi_tri_ki_tu_bat_dau:][i].isdigit:
                dem_so_ki_tu_can_cat += 1
            else:
                break
        except:
            break
    return link[vi_tri_ki_tu_bat_dau + 1:
                vi_tri_ki_tu_bat_dau + dem_so_ki_tu_can_cat]


# Ham chuyen doi link thuong dung sang link raw de dang dang lay noi dung topic
def linktoraw(link):
    return domain + "/raw/" + str(lay_id_topic(link))


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
def update_data_home():
    # Dung sourcetext de lay du lieu tu trang chu
    # Tach dong tu du lieu cua sourcetext dua vao mang
    source_linebyline = sourcetext(domain).splitlines()
    # Trich xuat du lieu cua moi topic, gan ID cho moi topic
    # Duyet tung dong cua Phoi Du Lieu
    for i in range(0, source_linebyline.__len__()):
        # Trich xuat Ten topic

        # Dung ham lay chuoi de tach du lieu theo tung dong
        if laychuoi(source_linebyline[i],
                    "<span itemprop='name'>", "<") != "nothing":
            TenTopicHome.append(
                laychuoi(source_linebyline[i], "<span itemprop='name'>", "<"))

        # Trich xuat so topic
        if (i == source_linebyline.__len__() - 1):
            global SoTopic
            SoTopic = TenTopicHome.__len__()

        # Trich xuat ID topic
        if laychuoi(source_linebyline[i],
                    "<meta itemprop='url' content='", "'") != "nothing":
            IDTopicHomeRaw.append(lay_id_topic(laychuoi(
                source_linebyline[i], "<meta itemprop='url' content='", "'")))

        # Trich xuat Link toptic (sau do tach ra Link raw)
        if laychuoi(source_linebyline[i],
                    "<meta itemprop='url' content='", "'") != "nothing":
            LinkTopicHomeRaw.append(linktoraw(laychuoi(
                source_linebyline[i], "<meta itemprop='url' content='", "'")))

    # Duyet lai tung dong cua Phoi Du Lieu de trich xuat cac du lieu con lai
    for i in range(0, source_linebyline.__len__()):

        # Trich xuat Category
        for STT in range(0, SoTopic):

            # Tim kiem theo ID cua topic
            day_dinh_vi_idtopic = '"id":' + IDTopicHomeRaw[STT] + ',"title"'
            if '"id":' + IDTopicHomeRaw[STT]\
                       + ',"title"' in source_linebyline[i]:

                # Thu hep Vung Tim Kiem
                vung_tim_kiem_category = source_linebyline[i][
                    source_linebyline[i].find(day_dinh_vi_idtopic):]

                if "category_id" in vung_tim_kiem_category:
                    vi_tri_dinh_vi_category = vung_tim_kiem_category.find(
                        "category_id")
                    vung_tim_kiem_category = vung_tim_kiem_category[
                        vi_tri_dinh_vi_category + len("category_id") + 2:
                        vi_tri_dinh_vi_category + len("category_id") + 2 + 6
                    ]

                    category_id = ""
                    gioi_han_so_ki_tu_id = 0
                    while vung_tim_kiem_category[0:1].isdigit() and \
                            gioi_han_so_ki_tu_id < 5:
                        gioi_han_so_ki_tu_id += 1
                        category_id += vung_tim_kiem_category[0:1]
                        vung_tim_kiem_category = vung_tim_kiem_category[1:]

                    CategoryID.append(category_id)

        # Trich xuat Replies (So comment)
        if laychuoi(source_linebyline[i],
                    "<span title='posts'>(", ")") != "nothing":
            NumTopic.append(
                laychuoi(source_linebyline[i], "<span title='posts'>(", ")"))

        # Trich xuat Users(user tham gia thao luan topic do)

        # Trich xuat Views(So luot View)


# 2.Show du lieu: In Danh sach Topic, In Topic, In Commment, ...
# ===============================================================

# Ham show ra danh sach topic moi nhat tren trang chu
def showhome():
    clear_screen()
    for STTTopic in range(0, SoTopic):
        if STTTopic < 10:
            print "\n[0" + str(STTTopic) + "]: " + str(TenTopicHome[STTTopic]) +\
                  " [" + CategoryTextID[CategoryID[STTTopic]] + "]"
        else:
            print "\n[" + str(STTTopic) + "]: " + str(TenTopicHome[STTTopic]) + \
                  " [" + CategoryTextID[CategoryID[STTTopic]] + "]"


# Ham show ra noi dung topic, an enter de chuyen
def see(ms):
    clear_screen()
    if LinkTopicHomeRaw[ms] == "":
        update_data_home()
    print WaitString
    import urllib2
    web = urllib2.urlopen(LinkTopicHomeRaw[ms])
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
    print "=========        Enter de xem tiep!!      =========="
    print "\n\n\n"
    print "  " + "[" + str(ms) + "]:" + TenTopicHome[ms]
    print "\n"

    for i in range(0, GioiHanDong):
        tempreadline = tep.readline()
        if tempreadline != "":
            print tempreadline

            # Thay the do while
            while True:
                key = msvcrt.getch()
                if ord(key) == 13:
                    break
            continue

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


# Ham show ra noi dung comment thu stt cua topic co ma so la ms
def seecomment(ms, stt):
    if str(LinkTopicHomeRaw[int(ms)]) == '':
        print "Link Trang Home bi trong"
        update_data_home()
    link = LinkTopicHomeRaw[int(ms)] + "/" + str(stt)

    print WaitString
    clear_screen()

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
    print "  Comment[" + str(stt) + "]:" + "[" + str(ms) + "]" + ":" +\
        TenTopicHome[int(ms)]
    print "\n"
    for i in range(0, GioiHanDong):
        tempreadline = tep.readline()
        if tempreadline != "":
            print tempreadline
            # Thay the do while
            while True:
                key = msvcrt.getch()
                if ord(key) == 13:
                    break
            continue
    print "\n\n\n"
    print "===================================================="
    print "===================================================="
    print "===================================================="
    print "\n\n\n"
    tep.close()
