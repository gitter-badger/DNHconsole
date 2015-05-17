import DNHconsolelib
import os
import msvcrt
import time
# Cap nhat du lieu lan dau tien, lay cac thong so can thiet
DNHconsolelib.update_data_home()
# Show ra gioi thieu ve DNHconsole
DNHconsolelib.help()
commander = raw_input('\nEnter de mo trang chu!')
DNHconsolelib.showhome()

# Bat dau nhan lenh
commander = ''
while not commander in['x', 'X']:
    print """
    Go l de mo topic moi nhat

    Go m de doi mau chu
    Go i de xem lai trang gioi thieu
    Go 00-29 de xem cac topic tuong ung, go 2 so lien tiep nhau (00, 09, 28,..)

    Go c de xem comment
    Go r de xoa man hinh
    Go h de ve trang chu
    Go x de thoat
    """
    print '\nBan muon lam gi tiep theo? : '
    # Truyen tham so vao bien commander, bo qua khi enter
    while True:
        commander = msvcrt.getch()
        if ord(commander) != 13:
            break
    if commander.isdigit():
        if commander == '0':
            commander = msvcrt.getch()
        else:
            commander = commander + str(msvcrt.getch())

    # Kiem tra tinh dung dan cua lenh truyen vao
    MangSoTopic = []
    for i in range(0, DNHconsolelib.SoTopic):
        MangSoTopic.append(str(i))
    if commander in ['m', 'i', 'l', 'c', 'h', 'x', 'r'] + MangSoTopic:
        if commander == 'm':
            print "\nGo 1 trong nhung ki tu sau" + \
                  " 1,2,3,4,5,6,7,8,9,a,b,c,d,e,f. Go x de quay lai"
            while True:
                chonmau = msvcrt.getch()
                os.system('color ' + chonmau)
                print "\nGo x de quay lai"
                if chonmau in ['x', 'X']:
                    DNHconsolelib.clear_screen()
                    break
            continue
        elif commander in MangSoTopic:
            DNHconsolelib.see(int(commander))
            print " Cho chut :D ...."
            time.sleep(2)
            print '\n Go x de quay lai, Enter de xem tiep'
            DNHconsolelib.flush_input()
            key = msvcrt.getch()
            for i in range(2, int(DNHconsolelib.NumTopic[int(commander)]) + 1):
                if ord(key) != 13:
                    break
                DNHconsolelib.clear_screen()
                DNHconsolelib.seecomment(commander, i)
                print " Cho chut :D ...."
                time.sleep(2)
                print '\n Go x de quay lai, Enter de xem tiep'
                DNHconsolelib.flush_input()
                key = msvcrt.getch()

        elif commander == 'h':
            DNHconsolelib.showhome()
        elif commander == 'i':
            DNHconsolelib.help()
        elif commander == 'l':
            DNHconsolelib.showhome()
            commander = 3
            DNHconsolelib.see(int(commander))
            print " Cho chut :D ...."
            time.sleep(2)
            print '\n Go x de quay lai, Enter de xem tiep'
            DNHconsolelib.flush_input()
            key = msvcrt.getch()
            for i in range(2, int(DNHconsolelib.NumTopic[int(commander)]) + 1):
                if ord(key) != 13:
                    break
                DNHconsolelib.clear_screen()
                DNHconsolelib.seecomment(commander, i)
                print " Cho chut :D ...."
                time.sleep(2)
                print '\n Go x de quay lai, Enter de xem tiep'
                DNHconsolelib.flush_input()
                key = msvcrt.getch()
        elif commander == 'x':
            break
        elif commander == 'r':
            DNHconsolelib.clear_screen()
        elif commander == 'c':
            idtopic = ''
            while idtopic != 'x':

                print ("\n   Go cac so trong khoang 00-29," +
                       " chu y go 2 so lien tiep nhau (VD: 00, 09, 28,..)" +
                       " tuong ung voi topic ban muon xem comment:\n   " +
                       "Go x de quay lai\n")
                while True:
                    idtopic = msvcrt.getch()
                    if ord(idtopic) != 13:
                        break
                if idtopic.isdigit():
                    if idtopic == '0':
                        idtopic = msvcrt.getch()
                    else:
                        idtopic = idtopic + str(msvcrt.getch())

                if idtopic in ['x', 'X'] or \
                        idtopic in MangSoTopic:
                    if idtopic == 'x':
                        break
                    elif idtopic.isdigit():
                        cmdComment = ''
                        while cmdComment != 'x':
                            print """

Go f de xem comment dau tien
Go l de xem comment cuoi cung
Go so thu tu comment ma ban muon xem
Go x de quay lai
"""
                            print "Ban muon xem commment nao?: "
                            while True:
                                cmdComment = msvcrt.getch()
                                if ord(cmdComment) != 13:
                                    break
                            if cmdComment.isdigit():
                                key = msvcrt.getch()
                                if cmdComment == '0':
                                    cmdComment = key
                                elif key.isdigit():
                                    cmdComment = cmdComment + str(key)
                                else:
                                    cmdComment = 'f'

                            if cmdComment in ['f', 'l', 'x'] or int(cmdComment) in \
                                    range(2, int(DNHconsolelib.NumTopic[
                                        int(idtopic)]) + 1):
                                if cmdComment == 'x':
                                    break
                                elif cmdComment == 'l':
                                    DNHconsolelib.seecomment(idtopic, int(
                                        DNHconsolelib.NumTopic[
                                            int(idtopic)]))
                                elif cmdComment == 'f':
                                    cmdComment = 2
                                    if int(cmdComment) in range(0, int(
                                        DNHconsolelib.NumTopic[int(
                                            idtopic)])):
                                        DNHconsolelib.seecomment(
                                            idtopic, cmdComment)
                                elif int(cmdComment) in \
                                        range(2, int(DNHconsolelib.NumTopic[
                                            int(idtopic)]) + 1):
                                    DNHconsolelib.seecomment(
                                        int(idtopic), cmdComment)
