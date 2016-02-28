'''
Created on Dec 11, 2015

@author: abhijit
'''
import grabOHLC
import grabCurrencyNews
import mergeNewsOhlc
import getInput
from time import sleep

# print inputs
inp_start_dt,inp_end_dt,inp_year = getInput.get_inputs()
print("start_dt ",inp_start_dt)
print("end_dt ",inp_end_dt)
print("year ",inp_year)
# get ohlc info for the year
grabOHLC.getOhlc()
print("OHLC data received")
sleep(5)
# get news info for the year
grabCurrencyNews.getCurrencyNews()
print("News data received")
sleep(5)
# merge and export to output folder 
mergeNewsOhlc.mergeFiles()
print("Merge completed for year ",inp_year)