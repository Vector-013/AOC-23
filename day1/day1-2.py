num_list  ={"one":"one1one", "two":"two2two", "three":"three3three", "four":"four4four", "five":"five5five", "six":"six6six", "seven":"seven7seven", "eight":"eight8eight", "nine":"nine9nine"}


with open("day1.txt" ,'r') as f:
    cnt =0
    for count, line in enumerate(f):
        
        for a,b in num_list.items():
            line = line.replace(a, b)
        
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