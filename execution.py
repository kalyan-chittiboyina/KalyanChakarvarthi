import logging 
logging.basicConfig(filename='execution.log', filemode='a', level=logging.DEBUG,format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='Date%m-%d-%yTime%H:%M:%S')

try:
    1/0
except Exception as e:
    print(e)
    print(type(e))
    f=str(e)
    if f == "division by zero":
        print("change denominator")
        logging.error('error due to %s',e, exc_info=True)
    elif "is not defined" in f:
        print("define denominator")
        logging.error('warning %s',e,exc_info=True)
finally:
    print("Code executed")