import json
log = '0'
arqWrite = open('logs.json', 'ab')
arqRead = open('logs.json', 'r')
lines = 0
dictlogs = str(arqRead.read()).split('}')
stest = "%gfd@"
substring = '!', '@', '#', '$', '%', '¨', '&', '*'


class Nome:

    def nomever(userver):
        testing = "'", '"', '!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '-', '_', '+', '=', '§', '´', '`', '[', \
            '{', 'ª', '^', '~', '}', ']', 'º', '/', '?', ';', ':', '.', '>', ',', '<', '|', '\\'
        i = 0
        while i < len(testing):
            if userver.count(testing[i]) >= 1:
                print("catch")
                return 3
            i = i + 1
        return 2


while log == '0':
    log = input('Log in - TYPE 1\n'
                'Log on - TYPE 2')
    while log == '1':
        user = input('insert your user name:')
        key = input('insert your key:')
        'print(arqRead.read())'
        print(dictlogs)
        print(len(dictlogs))
        while lines < len(dictlogs):
            if dictlogs[lines].count('user:' + user + '"') == 1:
                print('user confirmed')
                log = 3
                if dictlogs[lines].count(key) == 1:
                    print('key confirmed')
                else:
                    print("Key not found")
            lines = lines + 1
            arqRead.close()
        if log != 3:
            print("invalid user or key")

    while log == '2':
        user = input('create a user name:')
        key = input('create a key:')
        '''test of equality'''
        while lines < len(dictlogs):
            if dictlogs[lines].count('user:' + user + '"') == 1:
                print(dictlogs)
                log = 3
            lines = lines + 1
        lines = 0
        log = Nome.nomever(user)
        if log != 3:
            Fdump = {"user:" + user: key}
            Fdump = json.dumps(Fdump)
            print(Fdump)
            print('user confirmed')
            'arqWrite.write(str(Fdump))'
            arqWrite.write(Fdump.encode())
            log = 4
        else:
            print('This username is unavailable')
            log = '2'
