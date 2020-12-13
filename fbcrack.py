print("""\033[0;31;40m
 _____ ____     ____ ____      _    ____ _  __
|  ___| __ )   / ___|  _ \    / \  / ___| |/ /
| |_  |  _ \  | |   | |_) |  / _ \| |   | ' / 
|  _| | |_) | | |___|  _ <  / ___ \ |___| . \ 
|_|   |____/   \____|_| \_\/_/   \_\____|_|\_\
""")
f = open("password.txt","r")
v = input("\033[1;32;40menter the facebook link : ")
while True:
    l = f.readline()
    print("\033[1;32;40m trying password [{}] ... \n".format(l))
    print("\033[1;31;40m Passwod [{}] Failed \n".format(l))
