'''
Created on Dec 9, 2015

@author: abhijit
'''
import csv
from time import sleep
from selenium import webdriver
from datetime import datetime
import getInput
def getOhlc():
    inp_start_dt,inp_end_dt,inp_year = getInput.get_inputs()
    driver = webdriver.Firefox()
    driver.maximize_window()
    ## open the site which has the open,high,low,close information
    driver.get("http://www.investing.com/currencies/eur-usd-historical-data")
    ## wait for the ad to load
    sleep(10)
    ## close the ad
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/a').click()
    ## filter the data
    ## click the date box
    sleep(7)
    #driver.find_element_by_xpath('/html/body/div[5]/section/div[9]/div[3]/div/div[1]/div[1]').click()
    driver.find_element_by_id('datePickerIconWrap').click()
    # set the start date
    sleep(2)
    start_date = driver.find_element_by_id('startDate')
    start_date.clear()
    start_date.send_keys(inp_start_dt)
    # set the end date
    end_date = driver.find_element_by_id('endDate')
    end_date.clear()
    end_date.send_keys(inp_end_dt)
    # click the apply button
    driver.find_element_by_id('applyBtn').click()
    # wait for data to Load
    sleep(15)
    
    ## export the data to csv
    fp = open('F:/Abhi/pythonWorkspace/data/'+inp_year+'/euro_usd_ohlc_'+inp_year+'.csv', 'w', newline='')
    csvfile = csv.writer(fp, delimiter=',')
    # set the header row
    fieldnames = [['Date','Price','Open','High','Low','Change %']]
    csvfile.writerows(fieldnames) 
    cur_row = []
    tbl = driver.find_element_by_id('curr_table')
    row_num = 0
    for row in tbl.find_elements_by_tag_name("tr"):
        row_num = row_num + 1
        # exclude header row
        if (row_num != 1):
            col_0 = row.find_elements_by_tag_name("td")[0]  
            col_1 = row.find_elements_by_tag_name("td")[1]
            col_2 = row.find_elements_by_tag_name("td")[2]
            col_3 = row.find_elements_by_tag_name("td")[3]
            col_4 = row.find_elements_by_tag_name("td")[4]
            col_5 = row.find_elements_by_tag_name("td")[5]  
            col_0_date = datetime.strptime(str(col_0.text), '%b %d, %Y').date()      
            cur_row = [col_0_date,str(col_1.text),str(col_2.text),str(col_3.text),str(col_4.text),str(col_5.text)]
            csvfile.writerows([cur_row])
            cur_row = []
            #print(cur_row)
    #print("export completed")
    driver.quit()    