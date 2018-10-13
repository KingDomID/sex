#($$$   ทำขึ้นมาแจกให้ได้ใช้กัน  $$$)#

from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
import traceback
from googletrans import Translator

#==============================================================================#
botStart = time.time()

#($$$   ทำขึ้นมาแจกให้ได้ใช้กัน  $$$)#

#(***บอทหลักและร่าง***)#
nadya = LINE('ExALcirRmPkQDpxnuQe6.cwctUx8+wBx4GhMbM7wVvG.wm7q6wjwy+l+QbodUc6SOkRUkZAWups+wbkSswlf8Nk=')
choke01 = LINE('ExAUaeXEUKLyloMemoy1.yEsAgNVgqDhLX7iHGKJDaq.j+tO8LVykjS1RPEsRrPTmnnbKIgnZZIuyNc72gJWPpI=')
#=================#

#===========================#
nadyaMID = nadya.profile.mid
choke01MID = choke01.profile.mid
#===========================#

#+++++ บอทผีเตะกันดำ +++++#
chokepee = LINE('ExCNjEp0TLXDI9DKOFp2.J1jj48SAuthXcZK7eYeqSG.SBFnzYLmqUvIn2QGQsV4Ypmf6ChSYXm2GY8ssij6k/g=')
#*****************************#

#++++++++++++++++++++++++++++#
nadyaProfile = nadya.getProfile()
choke01Profile = choke01.getProfile()
#++++++++++++++++++++++++++++#

#+++++++++++++++++++++++++++++++#
lineSettings = nadya.getSettings()
choke01Settings = choke01.getSettings()
#++++++++++++++++++++++++++++++++#

#++++++++++++++++++++#
oepoll = OEPoll(nadya)
oepoll1 = OEPoll(choke01)
#++++++++++++++++++++#

#+++++++++++บอท++++++++#
Bots1 = ['nadyaMID','choke01MID']
Chokekick = []
Chokejoin = []
CHOKE = ['choke01','nadya']
#ต้องใส่ MID  ถึงจะโหดนะครับ ติดตามไลน์คนสร้าง #
# LINE ID: nipon24082535#

chokeadmin = ['u096093b97f3f59b5f88079819bb5af56']
admin = ['u096093b97f3f59b5f88079819bb5af56']
#==============================================================================#
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")


read = json.load(readOpen)
settings = json.load(settingsOpen)

settings = {
	"chokeblack": {},
	}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = nadyaProfile.displayName
myProfile["statusMessage"] = nadyaProfile.statusMessage
myProfile["pictureStatus"] = nadyaProfile.pictureStatus
def helpmessage():
    helpMessage =   "" + "\n" + \
                  "!แอดบอท" + "\n" + \
                  "!sp" + "\n" + \
                  "!กันดำ เปิด/ปิด" + "\n" + \
                  "!หี" + "\n" + \
                  "!ควย" + "\n" + \
                  "!ดูเวลา" + "\n" + \
                  "***" + "\n" + \
                  "" + "\n" + \
                  ""
    return helpMessage
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
#    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True       
    except Exception as error:
        logError(error)
        return False    
    
def logError(text):
    nadya.log("[ ข้อผิดพลาด ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        traceback.print_exc()
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        nadya.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        

    

#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] จบสูมบรูณ์ไม่มีปัญหา")
            return
        
        
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                nadya.leaveRoom(op.param1)
        if op.type == 25:
            print ("[ 25 ] ส่งข้อความ")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if text.lower() == '!รายการ':
                    helpMessage = helpmessage()
                    nadya.sendMessage(to, str(helpMessage))
                
                elif text.lower() in ["!ควย"]:               
                    choke01.leaveGroup(msg.to)
                elif text.lower() in ["!หี"]:    
                    G = nadya.getGroup(msg.to)
                    ginfo = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    nadya.updateGroup(G)
                    invsend = 0
                    Choke = nadya.reissueGroupTicket(msg.to)
                    choke01.acceptGroupInvitationByTicket(msg.to,Choke)
                    G = choke01.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    choke01.updateGroup(G)
                elif '!กันดำ ' in msg.text:              
                      spl = msg.text.replace('!กันดำ ','')
                      if spl == 'เปิด':
                          if msg.to in Chokejoin:
                              msgs = "เปิดระบบลบคนติดดำออกเฉพาะกลุ่ม"
                          else:
                              Chokejoin.append(msg.to)
                              ginfo = nadya.getGroup(msg.to)
                              msgs = "เปิดระบบลบคนติดดำเฉพาะกลุ่ม\n GM ผู้ดูแลประจำกลุ่ม : " +str(ginfo.name)
                          nadya.sendMessage(msg.to, "「พร้อมรักษาความปลอดภัยให้แล้ว」\n" + msgs)
                          
                          
                      elif spl == 'ปิด':
                           if msg.to in Chokejoin:
                               Chokejoin.remove(msg.to)
                               ginfo = nadya.getGroup(msg.to)
                               msgs = "ปิดระบบลบคนติดดำเฉพาะกลุ่ม\n GM ผู้ดูแลประจำกลุ่ม : " +str(ginfo.name)
                           else:
                               msgs = "ปิดระบบลบคนติดดำเฉพาะกลุ่ม"
                           nadya.sendMessage(msg.to, "「ไม่พร้อมรักษาความปลอดภัยให้แล้ว」\n" + msgs)       
                           
#==============================================================================#
                elif text.lower() == '!Sp':
                    start = time.time()
                    nadya.sendMessage(to, "กำลังทดสอบ..")
                    elapsed_time = time.time() - start
                    nadya.sendMessage(to,format(str(elapsed_time)))
                
                
                elif "!แอดบอท" in msg.text.lower():
                     nadya.findAndAddContactsByMid(choke01MID)                    
                     nadya.sendMessage(msg.to,'เพิ่มเพื่อนบอทเรียบร้อบครับ')

                     choke01.findAndAddContactsByMid(nadyaMID)                     
                     choke01.sendMessage(msg.to,'เพิ่มเพื่อนบอทเรียบร้อบครับ')
                elif text.lower() == '!ดูเวลา':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    nadya.sendMessage(to, "บอทกำลังทำงานขณะนี้ {}".format(str(runtime)))
                
                 
#==============================================================================#
                
                
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    nadya.sendMessage(to, str(ret_))
                    
            elif msg.contentType == 13:
                if settings["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = nadya.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Copy")
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        nadya.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                nadya.cloneContactProfile(target)
                                nadya.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                                settings['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     settings["copy"] = False
                                     break                     
                    
                    
#==============================================================================#
        if op.type == 19:
            print ("[ 19 ] ระบบดูแลคนลบ")
            if op.param2 in Bots1:
            	pass
            else:
              try:
                 if op.param1 in Chokeprotect:
                     settings["chokeblack"][op.param2] = True
                     G = random.choice(CHOKE).getGroup(op.param1)
                     random.choice(CHOKE).kickoutFromGroup(op.param1,[op.param2])
                     choke01.findAndAddContactsByMid(op.param3)
                     choke01.inviteIntoGroup(op.param1,[op.param3])
                 else:
                   pass
              except:
                try:
                    G = random.choice(CHOKE).getGroup(op.param1)
                    random.choice(CHOKE).kickoutFromGroup(op.param1,[op.param2])
                    nadya.findAndAddContactsByMid(op.param3)
                    nadya.inviteIntoGroup(op.param1,[op.param3])
                    settings["chokeblack"][op.param2] = True
                except:
                    pass
        if op.type == 19:
            print ("[ 19 ] ระบบดึงสัมพันธ์กัน")
            if nadyaMID in op.param3:
                if op.param2 in Bots1:
                    pass
                if op.param2 in chokeadmin:
                    pass
                    choke01.findAndAddContactsByMid(op.param3)
                    choke01.inviteIntoGroup(op.param1,[op.param3])
                    nadya.acceptGroupInvitation(op.param1)
                else:
                    settings["chokeblack"][op.param2] = True
                    try:
                        choke01.findAndAddContactsByMid(op.param3)
                        choke01.kickoutFromGroup(op.param1,[op.param2])
                        choke01.inviteIntoGroup(op.param1,[op.param3])
                        nadya.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if choke01MID in op.param3:
                if op.param2 in Bots1:
                    pass
                if op.param2 in chokeadmin:
                    pass
                    nadya.findAndAddContactsByMid(op.param3)
                    nadya.inviteIntoGroup(op.param1,[op.param3])
                    choke01.acceptGroupInvitation(op.param1)
                else:
                    settings["chokeblack"][op.param2] = True
                    try:
                        nadya.findAndAddContactsByMid(op.param3)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        nadya.inviteIntoGroup(op.param1,[op.param3])
                        choke01.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if admin in op.param3:
                if op.param2 in Bots1:
                    pass          
                if op.param2 in chokeadmin:
                    pass               
                else:
                    settings["chokeblack"][op.param2] = True
                    try:
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        nadya.findAndAddContactsByMid(op.param1,admin)
                        nadya.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            choke01.kickoutFromGroup(op.param1,[op.param2])
                            choke01.findAndAddContactsByMid(op.param1,admin)
                            choke01.inviteIntoGroup(op.param1,admin)
                        except: 
                            pass
            return
        if op.type == 17:
            print ("[ 17 ] ระบบดูแลกันดำ")
            if op.param1 in Chokejoin:
                try:
                    if nadya.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots1 and op.param2 not in chokeadmin:
                            G = nadya.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            nadya.updateGroup(G)
                            Choke = nadya.reissueGroupTicket(op.param1)
                            chokepee.acceptGroupInvitationByTicket(op.param1,Choke)
                            chokepee.kickoutFromGroup(op.param1,[op.param2])
                            chokepee.leaveGroup(op.param1)
                            G = choke01.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            choke01.updateGroup(G)                          
                except:   
                    pass  
        if op.type == 26:       
            print ("[ 26 ] ระบบแปลภาษา")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.to in translateen:
                try:
                    if msg.text is not None:
                        kata = msg.text                           
                        translator = Translator()
                        hasil = translator.translate(kata, dest='en')
                        hasil1 = translator.translate(kata, dest='th')
                        A = hasil.text
                        A1 = hasil1.text
                        nadya.sendMessage(receiver, 'แปลภาษาไทยเป็นอังกฤษ: ' + A)
                        nadya.sendMessage(receiver, 'แปลภาษาอังกฤษเป็นไทย: ' + A1)
                except Exception as error:
                    pass                           
                           
            
        if op.type == 26:       
            print ("[ 26 ] รับ ข้อความ")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            
                    
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    nadya.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                
                
                
                           
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        nadya.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in nadyaMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if nadyaMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = nadya.getContact(sender)
                                    nadya.sendMessage(to, "Tag??")
                                    sendMessageWithMention(to, contact.mid)
                                break
#==============================================================================#
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
