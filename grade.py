import requests
from time import sleep

index_url = "http://10.10.10.2/"
url = "http://10.10.10.2/login_check.php"
attackPW = 'QNKCDZO'
incorrectPW = 'ABCDE'
correctPW = '240610708'

def test():
    try:
        req = requests.get(index_url)
        if (req.status_code == 200 and ("<!DOCTYPE html>" in req.text)):
            data = {'id':'admin', 'pw':attackPW, 'login':'Login'}
            req = requests.get(url, data)
            if (req.status_code == 200 and ('login.html' in req.text)):
                print('attack ok')
                #with open('/tmp/grade_result.txt', 'w') as f:
                    #f.write('connect Success!')
                return 2
            else:
                data = {'id':'admin', 'pw':correctPW, 'login':'Login'}
                req = requests.get(url, data)
                if(req.status_code == 200 and ('login.html' in req.text)):
                    print('patched')
                    with open('/tmp/grade_result.txt', 'w') as f:
                        f.write('{\'1\':\'True\'}')
                    return 0
                else:
                    print('something wrong')
                    with open('/tmp/grade_result.txt', 'w') as f:
                        f.write('3')
                    return 3
        else:
            #with open('/tmp/grade_result.txt', 'w') as f:
                #f.write('connect Error!')
            return 3
    except:
        print('error')
        #with open('/tmp/grade_result.txt', 'w') as f:
            #f.write('3')
        return 3
def main():
    test()

if __name__ == "__main__":
    main()