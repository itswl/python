import logging.handlers
import os 


class LOG(logging.Logger):
    def __init__(self, filename=None):
        super(LOG, self).__init__(self)

        if filename is None:
            filename = 'test.log'
        if not os.path.exists(os.path.join(os.path.split(os.path.realpath(__file__))[0],'logs')):
            os.makedirs(os.path.join(os.path.split(os.path.realpath(__file__))[0],'logs'), 0o700)
        self.filename = os.path.join(os.path.split(os.path.realpath(__file__))[0],'logs',filename)


        fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'D', 1, 30)
        fh.suffix = "%Y%m%d-%H%M.log"
        fh.setLevel(logging.DEBUG) 


        ch = logging.StreamHandler() 
        ch.setLevel(logging.DEBUG) 


        formatter = logging.Formatter("[%(asctime)s] [%(levelname)8s]  %(message)s")
        fh.setFormatter(formatter) 
        ch.setFormatter(formatter) 


        self.addHandler(fh) 
        self.addHandler(ch) 

if __name__ == '__main__':
    pass
