def progress(curr,total):
     persent=(curr/total)*100
     barlen=20
     filled=int(barlen*curr//total)
     bar="#"*filled+"."*(barlen-filled)
     print(f"\r[ {bar} ] {persent:2f}%",end="")


    