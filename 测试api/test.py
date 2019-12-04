import requests
from logger import LOG
from dataclasses import dataclass

class Base:    
    def __init__(self):
        self.ip = ''
        self.host = f'https://{self.ip}:xxxx'
        self.logging = LOG()
        self._url = ''
        
    def run(self,method='',data=''):
        headers = {'Content-Type': 'application/json'}
        requests.packages.urllib3.disable_warnings()    
        r = requests.request(method,self._url,data='', verify=False,headers=headers)
        self.logging.info(r.text)

class Test_get(Base):
    def __init__(self,id='1'):
        super().__init__()
        self._url =  self.host + f'xxx'    

    def run(self):
        super().run(method='GET')


class Test_post(Base):
    def __init__(self):
        super().__init__()
        self._url =  self.host + f'xxx'
    
    def run(self):
        data = {}
        super().run(method='POST',data = data)

class Test_put(Base):
    def __init__(self,id='1'):
        super().__init__()
        self._url =  self.host + f'xxx'
    
    def run(self):
        data = {}
        super().run(method='PUT',data = data)

class Test_delete(Base):
    def __init__(self,id='1'):
        super().__init__()
        self._url =  self.host + f'xxx'

    def run(self):
        super().run(method='DELETE')

C = Test_delete('166')
C.run()
