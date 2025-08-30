def scanstr(string:str):
    numbs = range(10)
    qush = list(string)
    ch,nu = 0,0
    for i in qush:
        try:
            if int(i) in numbs:
                nu += 1
        except:
            if i != ' ':
                ch += 1            
    return {'Characters':ch,'Numbers':nu}
