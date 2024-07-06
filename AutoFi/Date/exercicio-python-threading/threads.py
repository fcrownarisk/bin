import threading

def msg(msg='None'): 
    print(msg)

thread = [
        threading.Thread(msg('1025'), list['thread']),
        threading.Thread(msg('1028'), list['thread']),
        threading.Thread(msg('1111'), list['thread']),
        threading.Thread(msg('1117'), list['thread']),
        ]


if __name__ == '__main__':
    for i in thread:
        i.start()









