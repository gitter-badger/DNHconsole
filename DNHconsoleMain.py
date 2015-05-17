import DNHconsolelib
import os
# Cap nhat du lieu lan dau tien, lay cac thong so can thiet
DNHconsolelib.updateDataHome()
# Gioi Han Tham So Truyen Trang Home
MangSoTopic = []
for i in range(0, DNHconsolelib.SoTopic):
    MangSoTopic.append(str(i))

GioiHanThamSoTruyenTrangHome = ['m', 'i', 'l', 'c', 'h', 'x'] + MangSoTopic
# Gioi Han Tham So Truyen Trang Comment Khi Chon STT Comment
MangSoComment = []
# Show ra gioi thieu ve DNHconsole
DNHconsolelib.help()
commander = raw_input('\nEnter de mo trang chu!')
DNHconsolelib.showhome()
commander = ''
while commander != 'x':
    print """

    Go m de doi mau chu(Chuc nang nay co the bi Antivirus Warning)
    Go i de xem lai trang gioi thieu
    Go l de mo topic moi nhat
    Go cac so trong khoang 1-30 de xem cac topic tuong ung
    Go c de xem comment
    Go h de ve trang chu
    Go x de thoat
    """
    commander = str(raw_input('\nBan muon lam gi tiep theo? : '))
    # DUNG TRY de bo loi, khi DEBUG phai thay pass bang raise
    # Kiem tra tinh dung dan cua lenh truyen vao
    if commander in GioiHanThamSoTruyenTrangHome:
        if commander == 'm':
            DNHconsolelib.showhome()
            os.system(
                'color ' + str(raw_input('Go 1 trong cac so 1-9 de chon mau\
, hoac tu a den f: ')))
            continue
        if commander == 'h':
            DNHconsolelib.showhome()
        elif commander == 'i':
            DNHconsolelib.help()
        elif commander == 'l':
            DNHconsolelib.showhome()
            DNHconsolelib.see(4)
        elif commander == 'x':
            break
        elif commander == 'c':
            idTopicComment = ''
            while idTopicComment != 'b':

                idTopicComment = str(raw_input("\n   Go cac so trong khoang 0-29 tuong ung voi topic ban muon xem comment:\n   \
Go b de quay lai\n"))

                if idTopicComment == 'b' or idTopicComment in MangSoTopic:
                    if idTopicComment == 'b':
                        break
                    elif idTopicComment.isdigit():
                        DaXem1Comment = False
                        cmdComment = ''
                        while cmdComment != 'b':
                            if DaXem1Comment:
                                print """
\n\nEnter de xem comment TIEP THEO!!!!!
Go f de xem comment dau tien
Go l de xem comment cuoi cung
Go so thu tu comment ma ban muon xem
Go b de quay lai
"""                             
                                if cmdComment != '':
                                    cmdCommentBefore = cmdComment
                                cmdComment = str(raw_input('\nBan muon xem comment nao? : '))
                                if cmdComment in ['f', 'l', 'b', ''] or (cmdComment >= 0 and cmdComment < int(DNHconsolelib.NumCommentTopicHome[int(idTopicComment)])):
                                    if cmdComment == 'b':
                                        break
                                    elif cmdComment == '' and (cmdCommentBefore < int(DNHconsolelib.NumCommentTopicHome[int(idTopicComment)] )- 1):
                                        DNHconsolelib.seecomment(idTopicComment, int(cmdCommentBefore) + 1)
                                        cmdComment = int(cmdCommentBefore) + 1
                                    elif cmdComment == 'l':
                                        DNHconsolelib.seecomment(DNHconsolelib.NumCommentTopicHome[idTopicComment] - 1)
                                    elif cmdComment == 'f':
                                        cmdComment = 2
                                        DNHconsolelib.seecomment(idTopicComment, cmdComment)
                                        DaXem1Comment = True
                                    elif cmdComment in range(0, int(DNHconsolelib.NumCommentTopicHome[int(idTopicComment)])):
                                        DNHconsolelib.seecomment(int(idTopicComment), cmdComment)
                                        DaXem1Comment = True
                            else:
                                print """

Go f de xem comment dau tien
Go l de xem comment cuoi cung
Go so thu tu comment ma ban muon xem
Go b de quay lai
"""
                                cmdComment = str(raw_input('\nBan muon xem comment nao? : '))

                                if cmdComment in (['f', 'l', 'b', ''] + range(0, int(DNHconsolelib.NumCommentTopicHome[int(idTopicComment)]))):
                                    if cmdComment == 'b':
                                        break
                                    elif cmdComment == '':
                                        continue
                                    elif cmdComment == 'l':
                                        DNHconsolelib.seecomment(idTopicComment, DNHconsolelib.NumCommentTopicHome[idTopicComment] - 1)
                                    elif cmdComment == 'f':
                                        cmdComment = 2
                                        DNHconsolelib.seecomment(idTopicComment, cmdComment)
                                        DaXem1Comment = True
                                    elif int(cmdComment) >= 0 and int(cmdComment) < DNHconsolelib.NumCommentTopicHome[idTopicComment]:
                                        DNHconsolelib.seecomment(int(idTopicComment), cmdComment)
                                        DaXem1Comment = True
        elif int(commander) >=0 and int(commander) < DNHconsolelib.SoTopic:
            DNHconsolelib.see(int(commander))