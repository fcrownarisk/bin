import threading

def msg(msg='None'): 
    print(msg)

thread = [
        threading.Thread(msg('1025'), list['thread 1']),
        threading.Thread(msg('1028'), list['thread 2']),
        threading.Thread(msg('1111'), list['thread 3']),
        threading.Thread(msg('1117'), list['thread 4']),
        ]


if __name__ == '__main__':
    for i in thread:
        i.start()









