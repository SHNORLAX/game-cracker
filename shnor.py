from urllib import request, parse

def req(mode,score,nick):
        data = parse.urlencode({'gameid':'145','gameMode':mode,'score':score,'nickname':nick}).encode()
        req =  request.Request('http://www.littlebigplay.com/submitAir.php', data=data)
        resp = request.urlopen(req)
        return True

nick = input("Nick: ")
mode = input("\nLevel: ")
score = input("\nScore: ")

req(mode,score,nick)

if req:
        print("\nOK.")
