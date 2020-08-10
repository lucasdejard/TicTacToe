import json
log = '0'
arqWrite = open('logs.json', 'ab')
arqRead = open('logs.json', 'r')
lines = 0
dictlogs = str(arqRead.read()).split('}')
while log == '0':
    log = input('Log in - TYPE 1\n'
                'Log on - TYPE 2')
    if log == '1':
        user = input('insert your user name:')
        key = input('insert your key:')
        'print(arqRead.read())'
        print(dictlogs)
        print(len(dictlogs))
        while lines < len(dictlogs):
            if dictlogs[lines].count('user:' + user + '"') == 1:
                print('user confirmed')
                if dictlogs[lines].count(key) == 1:
                    print('key confirmed')
            lines = lines + 1
            arqRead.close()
    while log == '2':
        user = input('create a user name:')
        key = input('create a key:')
        '''test of equality'''
        print(dictlogs)
        while lines < len(dictlogs):
            if dictlogs[lines].count('user:' + user + '"') == 1:
                print('user confirmed')
                log = 3
            lines = lines + 1
        lines = 0
        if log != 3:
            Fdump = {"user:" + user: key}
            Fdump = json.dumps(Fdump)
            print(Fdump)
            'arqWrite.write(str(Fdump))'
            arqWrite.write(Fdump.encode())
            log = 4
        else:
            print('This user name is unavailable')
            log = '2'
