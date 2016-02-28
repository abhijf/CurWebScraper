'''
Created on Nov 19, 2015

@author: abhijit
'''
# from selenium import webdriver
# driver = webdriver.PhantomJS()
# driver.set_window_size(1120, 550)

## using firefox
# from selenium import webdriver 
# driver = webdriver.Firefox()



## actual implementation
import collections
import csv
import datetime
import math
import getInput

from time import sleep
from warnings import catch_warnings

from selenium import webdriver
def getCurrencyNews():
    inp_start_dt,inp_end_dt,inp_year = getInput.get_inputs()
    # change preferences to turn off unresponsive script message
    fp = webdriver.FirefoxProfile()
    fp.set_preference("dom.max_chrome_script_run_time", 0)
    fp.set_preference("dom.max_script_run_time", 0)
    driver = webdriver.Firefox(firefox_profile=fp)
    
    #driver = webdriver.Firefox()
    driver.maximize_window()
    
    def getDateRowCol(dt):
    #     dt = '03/30/2013'
        month, day, year = (int(x) for x in dt.split('/'))    
        ans = datetime.date(year, month, day)
        day_num =0
        
        def getDayNum():    
            # Get the column num for the date in the date picker
            if ((ans.strftime("%A").lower())=="sunday"):
                day_num = 1
            elif ((ans.strftime("%A").lower())=="monday"):
                day_num = 2
            elif ((ans.strftime("%A").lower())=="tuesday"):
                day_num = 3     
            elif ((ans.strftime("%A").lower())=="wednesday"):
                day_num = 4
            elif ((ans.strftime("%A").lower())=="thursday"):
                day_num = 5 
            elif ((ans.strftime("%A").lower())=="friday"):
                day_num = 6
            elif ((ans.strftime("%A").lower())=="saturday"):
                day_num = 7              
            return day_num
        day_num = getDayNum()
        # get the row num for the date in the date picker
        # get the day num for the first date of that month
        ans = datetime.date(year, month, 1)
        first_dayNum = getDayNum()
        # add the days of the selected date minus 1
        calc_dayNum = first_dayNum - 1 + day 
        # divide by 7
        calc_dayNum = calc_dayNum / 7
        # round up
        week_num = math.ceil(calc_dayNum)
        return day_num, week_num
    
    
    
    ## get input parameters:
    
    ## open the site which has the news information
    driver.get("http://www.fxstreet.com/economic-calendar/default.aspx")
    ## wait for the ad to load
    sleep(10)
    ## close the ad
    driver.find_element_by_id('closeroadblock').click()
    
    filter_data = True
    ## add filter conditions 
    if (filter_data):
        ## click on show filters
        driver.find_element_by_id('fxit-advlink').click()
        ## set the start date
        start_date = inp_start_dt
        driver.find_element_by_id("fxit-start-advanced").clear()
        driver.find_element_by_id("fxit-start-advanced").send_keys(start_date)    
        start_col,start_row = getDateRowCol(start_date)
        driver.find_element_by_xpath("/html/body/div[17]/div[2]/table/tbody/tr["+str(start_row)+"]/td["+str(start_col)+"]").click()
        ## set the end date
        end_date = inp_end_dt
        driver.find_element_by_id("fxit-end-advanced").clear()
        driver.find_element_by_id("fxit-end-advanced").send_keys(end_date)
        end_col,end_row = getDateRowCol(end_date)
        driver.find_element_by_xpath("/html/body/div[17]/div[2]/table/tbody/tr["+str(end_row)+"]/td["+str(end_col)+"]").click()
        ## Select none for country
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/div[2]/div/div/div[3]/div[1]/div[1]/div/form/div[2]/fieldset[3]/div/span/a[2]").click()
        sleep(1)
        ## check US
        if (not driver.find_element_by_id("fxst-us").is_selected()):        
            driver.find_element_by_id("fxst-us").click()
        ## check emu
        sleep(1)
        if (not driver.find_element_by_id("fxst-emu").is_selected()):
            driver.find_element_by_id("fxst-emu").click()
        ## select all for type of indicators
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/div[2]/div/div/div[3]/div[1]/div[1]/div/form/div[2]/fieldset[4]/div/span/a[1]").click()
        ## apply the filters
        sleep(1)
        driver.find_element_by_id("fxit-filterbutton").click()
        sleep(10)
    
    # create a dict for storing 2 dimentional output
    output = {}
    #print("populate output dict")
    # get input filters
    inp_filter1 = 'Industrial Production s.a. (MoM)'
    inp_filter2 = 'Industrial Production (MoM)'
    inp_filter3 = 'Trade Balance'
    inp_filter4 = 'Trade Balance s.a.'
    inp_filter5 = 'ISM Manufacturing PMI'
    # inp_filter6 = 'Core Personal Consumption Expenditure - Price Index (MoM)'
    inp_filter7 = 'Fed Interest Rate Decision'
    inp_filter8 = 'ECB Interest Rate Decision'
    # while filtering check the length for filter9 since there are other paramters which start with same name
    inp_filter9 = 'Markit Manufacturing PMI'
    inp_filter10 = 'Consumer Price Index (MoM)'
    ## read the table data
    tbl = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div[2]/div/div/div[3]/div[1]/div[3]/div/table/tbody")
    row_num =0
    fp = open('F:/Abhi/pythonWorkspace/data/'+inp_year+'/euro_usd_news_'+inp_year+'.csv', 'w', newline='')
    csvfile = csv.writer(fp, delimiter=',')
    #skip columns 2 and 11
    fieldnames = [['Date','Country','Currency','Event','Volatility','Actual','Consensus','Previous','Revised']]
    csvfile.writerows(fieldnames) 
    cur_row = []
    cur_date=""
    for row in tbl.find_elements_by_tag_name("tr"):
        row_num = row_num + 1
        col_0 = row.find_elements_by_tag_name("td")[0]
        if (len(col_0.text) == 0): 
            row_num = row_num -1
        else:
            if (len(col_0.text) > 5): # this implies its a date row
                # store the date to enter in the first column
                # append year to the date
                dateWithYear = str(col_0.text) + ' '+inp_year
                strDate = datetime.datetime.strptime(dateWithYear,"%A, %b %d %Y").date()
                cur_date = strDate
                #output[row_num,0] = cur_date
            else:
                
                # grab the data from the other columns
                col_1 = row.find_elements_by_tag_name("td")[1]
                col_2 = row.find_elements_by_tag_name("td")[2]
                col_3 = row.find_elements_by_tag_name("td")[3]
                col_4 = row.find_elements_by_tag_name("td")[4]
                col_5 = row.find_elements_by_tag_name("td")[5]
                col_6 = row.find_elements_by_tag_name("td")[6]
                col_7 = row.find_elements_by_tag_name("td")[7]
                col_8 = row.find_elements_by_tag_name("td")[8]
                col_9 = row.find_elements_by_tag_name("td")[9]
                col_10 = row.find_elements_by_tag_name("td")[10]
                cur_row = [cur_date,str(col_2.text),str(col_3.text),str(col_4.text),str(col_5.text),str(col_6.text),str(col_7.text),str(col_8.text),str(col_9.text)]
                # filter the values that are required
                if ((col_4.text.find(inp_filter1) == 0) or (col_4.text.find(inp_filter2) == 0) or ((col_4.text.find(inp_filter3) == 0) and (col_3.text =='USD')) or
                    ((col_4.text.find(inp_filter4) == 0) and (col_3.text =='EUR')) or ((col_4.text.find(inp_filter5) == 0) and (col_3.text =='USD')) or #(col_4.text.find(inp_filter6) == 0) or
                    (col_4.text.find(inp_filter7) == 0) or (col_4.text.find(inp_filter8) == 0) or (col_4.text.find(inp_filter9) == 0) or
                    (col_4.text.find(inp_filter10) == 0)):        
                    csvfile.writerows([cur_row])
                    print(row_num)
                    #print(col_4.text)
                    cur_row = []
    #print("export completed")
    driver.quit()
