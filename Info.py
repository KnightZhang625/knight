import time
import platform

class Info(object):
    def __init__(self):
        self._judge()
        if self.n == 1:
            self.type_1()
        elif self.n == 2:
            self.type_2()
        elif self.n == 3:
            self.type_3()

    def _judge(self):
        os_type = platform.platform().split('-')[0]
        if os_type == 'Darwin':
            self.n = 1
        elif os_type == 'Linux':
            self.n = 2
        elif os_type == 'Windows':
            self.n = 3
        else:
            self.n = 2

    def type_1(self):
        info = '''
    __ __       _       __    __     ___    ____  ____
   / //_/____  (_)___ _/ /_  / /_   /   |  / __ \\/  _/
  / ,<  / __ \\/ / __ `/ __ \\/ __/  / /| | / /_/ // /  
 / /| |/ / / / / /_/ / / / / /_   / ___ |/ ____// /   
/_/ |_/_/ /_/_/\\__, /_/ /_/\\__/  /_/  |_/_/   /___/       
              /____/                                        
                     MacOS version 1.0.2 
                  produced by KnightZhang
                '''
        print(info)
        time.sleep(2)

    def type_2(self):

        info = '''
██╗  ██╗███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗     █████╗ ██████╗ ██╗
██║ ██╔╝████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝    ██╔══██╗██╔══██╗██║
█████╔╝ ██╔██╗ ██║██║██║  ███╗███████║   ██║       ███████║██████╔╝██║
██╔═██╗ ██║╚██╗██║██║██║   ██║██╔══██║   ██║       ██╔══██║██╔═══╝ ██║
██║  ██╗██║ ╚████║██║╚██████╔╝██║  ██║   ██║       ██║  ██║██║     ██║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝     ╚═╝
                        Linux version 1.0.2 
                    produced by KnightZhang
                '''
        print(info)
        time.sleep(2)

    def type_3(self):
        info = '''
 _   __      _       _     _      ___  ______ _____ 
| | / /     (_)     | |   | |    / _ \\ | ___ \\_   _|
| |/ / _ __  _  __ _| |__ | |_  / /_\\ \\| |_/ / | |  
|    \\| '_ \\| |/ _` | '_ \\| __| |  _  ||  __/  | |  
| |\\  \\ | | | | (_| | | | | |_  | | | || |    _| |_ 
\\_| \\_/_| |_|_|\\__, |_| |_|\\__| \\_| |_/\\_|    \\___/ 
                __/ |                               
               |___/                                
                  Windows version 1.0.2
                produced by KnightZhang
'''
        print(info)
        time.sleep(2)
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                               
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                               
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                








