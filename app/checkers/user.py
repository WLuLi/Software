# -*- coding: utf-8 -*-

def register_params_check(content):
    """
    TODO: 进行参数检查
    """
    # print('type of content is',type(content))
    # "content is none"
    # type of content is nonetype

    import re

    # username 
    length=len(content['username'])
    if length<5 or length>12:
        return "username", False
    if not re.match("[a-zA-Z]+[0-9]+",content['username']):
        return "username", False
    
    # password
    length=len(content['password'])
    if length<8 or length>15:
        return "password", False
    if not re.match('''
                        [a-z]+[A-Z]+[0-9]+[-_\*\^]+[a-zA-Z0-9-_\*\^]*|
                        [a-z]+[A-Z]+[-_\*\^]+[0-9]+[a-zA-Z0-9-_\*\^]*|
                        [a-z]+[0-9]+[A-Z]+[-_\*\^]+[a-zA-Z0-9-_\*\^]*|
                        [a-z]+[0-9]+[-_\*\^]+[A-Z]+[a-zA-Z0-9-_\*\^]*|
                        [a-z]+[-_\*\^]+[0-9]+[A-Z]+[a-zA-Z0-9-_\*\^]*|
                        [a-z]+[-_\*\^]+[A-Z]+[0-9]+[a-zA-Z0-9-_\*\^]*|
                        [A-Z]+[a-z]+[0-9]+[-_\*\^]+[a-zA-Z0-9-_\*\^]*|
                        [A-Z]+[a-z]+[-_\*\^]+[0-9]+[a-zA-Z0-9-_\*\^]*|
                        [A-Z]+[0-9]+[a-z]+[-_\*\^]+[a-zA-Z0-9-_\*\^]*|
                        [A-Z]+[0-9]+[-_\*\^]+[a-z]+[a-zA-Z0-9-_\*\^]*|
                        [A-Z]+[-_\*\^]+[0-9]+[a-z]+[a-zA-Z0-9-_\*\^]*|
                        [A-Z]+[-_\*\^]+[a-z]+[0-9]+[a-zA-Z0-9-_\*\^]*|
                        [0-9]+[a-z]+[A-Z]+[-_\*\^]+[a-zA-Z0-9-_\*\^]*|
                        [0-9]+[a-z]+[-_\*\^]+[A-Z]+[a-zA-Z0-9-_\*\^]*|
                        [0-9]+[A-Z]+[a-z]+[-_\*\^]+[a-zA-Z0-9-_\*\^]*|
                        [0-9]+[A-Z]+[-_\*\^]+[a-z]+[a-zA-Z0-9-_\*\^]*|
                        [0-9]+[-_\*\^]+[A-Z]+[a-z]+[a-zA-Z0-9-_\*\^]*|
                        [0-9]+[-_\*\^]+[a-z]+[A-Z]+[a-zA-Z0-9-_\*\^]*|
                        [-_\*\^]+[a-z]+[A-Z]+[0-9]+[a-zA-Z0-9-_\*\^]*|
                        [-_\*\^]+[a-z]+[0-9]+[A-Z]+[a-zA-Z0-9-_\*\^]*|
                        [-_\*\^]+[A-Z]+[a-z]+[0-9]+[a-zA-Z0-9-_\*\^]*|
                        [-_\*\^]+[A-Z]+[0-9]+[a-z]+[a-zA-Z0-9-_\*\^]*|
                        [-_\*\^]+[0-9]+[a-z]+[A-Z]+[a-zA-Z0-9-_\*\^]*|
                        [-_\*\^]+[0-9]+[A-Z]+[a-z]+[a-zA-Z0-9-_\*\^]*
                    ''',content['password'],flags=re.VERBOSE):
        return "password", False

    # mobile
    if not re.match("\+[0-9]{2}\.[0-9]{12}",content['mobile']):
        return "mobile", False
    
    # url
    if re.match("https://",content['url']):
        if len(content['url'])>56:
            #return "url is too long 56", False
            return "url", False
    elif re.match("http://",content['url']):
        if len(content['url'])>55:
            #return "url is too long 55", False
            return "url", False
    if not re.match("https?://(([a-zA-Z0-9]+|([a-zA-Z0-9]+(-[a-zA-Z0-9]+)+))\.)+[a-z]+",content['url']):
        return "url", False

    # magic_number
    
    if 'magic_number' not in content.keys():
        content['magic_number'] = 0
    if int(content['magic_number'])<0:
        return "magic_number", False
    return "ok", True
