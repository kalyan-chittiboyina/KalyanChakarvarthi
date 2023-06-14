import logging
from function import try_except
logging.basicConfig(filename='execution.log', filemode='a', level=logging.DEBUG,format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='Date%m-%d-%yTime%H:%M:%S')
print(try_except(1,0))
