def fun(s):#lara@hackerrank.com
    try:
        userName,url = s.split('@') #u: lara, #u:hackerrank.com
        ws,ext = url.split('.') #c:hackerrank, e:com
    except Exception as e:
        return False

    if userName.replace('-','').replace('_','').isalnum() is False:
        return False
    elif ws.isalnum() is False:
        return False
    elif ext.isalpha() is False:
        return False
    elif len(ext) > 3:
        return False
    else:
        return True
