with open("a.txt" ,'r') as f:
    cnt =0
    for count, line in enumerate(f):
        for i in line:
            try :
                if int(i):
                    cnt = cnt + 10*(int(i))
                    break
            except:
                continue
        line = line[::-1]
        for i in line:
            try :
                if int(i):
                    cnt = cnt + (int(i))
                    break
            except:
                continue
    
    print(cnt)
    
    