from insurance.exception import InsuranceException
from insurance.logger import logging
import os,sys

def test_logger_and_exception():
    try:
        logging.info("Starting the test logger and exception")
        result = 3 / 0
        print(result)
        logging.info("End point of the test and logger exception")
    except Exception as e:
        logging.INFO(str(e))
        raise InsuranceException(e,sys) from e
    
    
if __name__=="__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)