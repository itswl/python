import requests
from logger import LOG
from dataclasses import dataclass

@dataclass
class Base:    
    ip:str = ''
    host:str = f'https://{ip}:xxxx'
    _url:str = ''
    logging = LOG()
       
    def run(self,method='',data=''):
        headers = {'Content-Type': 'application/json'}
        requests.packages.urllib3.disable_warnings()    
        r = requests.request(method,self._url,data='', verify=False,headers=headers)
        self.logging.info(r.text)

@dataclass
class Test_get(Base):
    id:str = '1'
    _url:str = Base.host + f'xxx'    

    def run(self):
        super().run(method='GET')

@dataclass
class Test_post(Base):
    _url:str =  Base.host + f'xxx'
    
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

@dataclass
class Test_delete(Base):
    id:str = '1'
    _url:str = Base.host + f'xxx'    

    def run(self):
        super().run(method='DELETE')


# C = Test_delete('159')
C = Test_get('159')
C.run()
