'''
Created on Dec 9, 2015

@author: abhijit
'''
import csv
import datetime
import getInput
def mergeFiles():
    inp_start_dt,inp_end_dt,inp_year = getInput.get_inputs()
    fp = open('F:/Abhi/pythonWorkspace/data/'+inp_year+'/euro_usd_ohlc_'+inp_year+'.csv', 'r')
    reader = csv.DictReader(fp)
    # create a new dict which will combine both files
    combinedDict = {}
    row_count = 0
    for row in reader:
    #     if(row_count==10):
    #         break
        row_count = row_count + 1   
        combinedDict[row_count,0] = row['Date']
        combinedDict[row_count,1] = row['Price']
        combinedDict[row_count,2] = row['Open']
        combinedDict[row_count,3] = row['High']
        combinedDict[row_count,4] = row['Low']
        combinedDict[row_count,5] = row['Change %']
    
    checkInput = []
    for i in range(1,10):
        for j in range (0,6):
            checkInput = checkInput + [combinedDict[i,j]]
            if (j == 5):
                checkInput = []
                
                
    # use row count to add new rows in singleRowNewsDict
    row_count_singleRow = 0
    # open the file to edit
    fp = open('F:/Abhi/pythonWorkspace/data/'+inp_year+'/euro_usd_news_'+inp_year+'.csv', 'r')
    newsDict = csv.DictReader(fp)
    #with open('F:/Abhi/pythonWorkspace/euro_usd_news_2015_part.csv', 'r') as csvfile:
        #newsDict = csv.reader(csvfile, delimiter=',', quotechar='|')
        #newsDict = csv.DictReader(csvfile)
    # convert rows to columns such that there is only single entry per date and put it in a dict
    singleRowNewsDict = {}
    #0     singleRowNewsDict = {'Date':'',
    #1                          'US_Industrial_Production_Actual':'','US_Industrial_Production_Consensus':'','US_Industrial_Production_Previous':'',
    #4                          'EUR_Industrial_Production_Actual':'','EUR_Industrial_Production_Consensus':'','EUR_Industrial_Production_Previous':'',
    #7                          'US_Markit_Manufacturing_PMI_Actual':'','US_Markit_Manufacturing_PMI_Consensus':'','US_Markit_Manufacturing_PMI_Previous':'',
    #10                          'EUR_Markit_Manufacturing_PMI_Actual':'','EUR_Markit_Manufacturing_PMI_Consensus':'','EUR_Markit_Manufacturing_PMI_Previous':'',
    #13                          'US_Trade_Balance_Actual':'','US_Trade_Balance_Consensus':'','US_Trade_Balance_Previous':'',
    #16                          'EUR_Trade_Balance_Actual':'','EUR_Trade_Balance_Consensus':'','EUR_Trade_Balance_Previous':'',
    #19                          'US_Consumer_Price_Index_Actual':'','US_Consumer_Price_Index_Consensus':'','US_Consumer_Price_Index_Previous':'',
    #22                          'EUR_Consumer_Price_Index_Actual':'','EUR_Consumer_Price_Index_Consensus':'','EUR_Consumer_Price_Index_Previous':'',
    #25                          'US_Fed_Interest_Rate_Actual':'','US_Fed_Interest_Rate_Consensus':'','US_Fed_Interest_Rate_Previous':'',
    #28                          'EUR_ECB_Interest_Rate_Actual':'','EUR_ECB_Interest_Rate_Consensus':'','EUR_ECB_Interest_Rate_Previous':''                         
    #                          }
    # need to know the key if the date already exists so that it can be updated.
    singleRowKey = ()
    
    insideIf = False
    for row in newsDict:
        if (row['Date'] in singleRowNewsDict.values()):
            for key,value in singleRowNewsDict.items():
                if (value == row['Date']):
                    # get the first key
                    singleRowKey = key[0]
                    insideIf = True
        else:
            insideIf = False
            row_count_singleRow = row_count_singleRow + 1
            # create a new row and update the date
            singleRowNewsDict[row_count_singleRow,0]=row['Date']
        # insideIf variable is used to know if the key is a new value or and existing value
        if(insideIf):
            primKey = singleRowKey
        else:
            primKey = row_count_singleRow
        # check the conditions and populate the index as per the variable
        if ((row['Event'].find('Industrial Production (MoM)') == 0) and (row['Currency'] == 'USD')):
            singleRowNewsDict[primKey,1]=row['Actual']
            singleRowNewsDict[primKey,2]=row['Consensus']
            singleRowNewsDict[primKey,3]=row['Previous']
        elif ((row['Event'].find('Industrial Production s.a. (MoM)') == 0) and (row['Currency'] == 'EUR')):
            singleRowNewsDict[primKey,4]=row['Actual']
            singleRowNewsDict[primKey,5]=row['Consensus']
            singleRowNewsDict[primKey,6]=row['Previous']
        elif ((row['Event'].find('ISM Manufacturing PMI') == 0) and (row['Currency'] == 'USD')):
            singleRowNewsDict[primKey,7]=row['Actual']
            singleRowNewsDict[primKey,8]=row['Consensus']
            singleRowNewsDict[primKey,9]=row['Previous']
        elif ((row['Event'].find('Markit Manufacturing PMI') == 0) and (row['Currency'] == 'EUR')):
            singleRowNewsDict[primKey,10]=row['Actual']
            singleRowNewsDict[primKey,11]=row['Consensus']
            singleRowNewsDict[primKey,12]=row['Previous']
        elif ((row['Event'].find('Trade Balance') == 0) and (row['Currency'] == 'USD')):
            singleRowNewsDict[primKey,13]=row['Actual']
            singleRowNewsDict[primKey,14]=row['Consensus']
            singleRowNewsDict[primKey,15]=row['Previous']
        elif ((row['Event'].find('Trade Balance s.a.') == 0) and (row['Currency'] == 'EUR')):
            singleRowNewsDict[primKey,16]=row['Actual']
            singleRowNewsDict[primKey,17]=row['Consensus']  
            singleRowNewsDict[primKey,18]=row['Previous']
        elif ((row['Event'].find('Consumer Price Index (MoM)') == 0) and (row['Currency'] == 'USD')):
            singleRowNewsDict[primKey,19]=row['Actual']
            singleRowNewsDict[primKey,20]=row['Consensus']
            singleRowNewsDict[primKey,21]=row['Previous']
        elif ((row['Event'].find('Consumer Price Index (MoM)') == 0) and (row['Currency'] == 'EUR')):
            singleRowNewsDict[primKey,22]=row['Actual']
            singleRowNewsDict[primKey,23]=row['Consensus']
            singleRowNewsDict[primKey,24]=row['Previous']
        elif ((row['Event'].find('Fed Interest Rate Decision') == 0) and (row['Currency'] == 'USD')):
            singleRowNewsDict[primKey,25]=row['Actual']
            singleRowNewsDict[primKey,26]=row['Consensus']
            singleRowNewsDict[primKey,27]=row['Previous']
        elif ((row['Event'].find('ECB Interest Rate Decision') == 0) and (row['Currency'] == 'EUR')):
            singleRowNewsDict[primKey,28]=row['Actual']
            singleRowNewsDict[primKey,29]=row['Consensus']
            singleRowNewsDict[primKey,30]=row['Previous']
        
    # for row in singleRowNewsDict:
    #     print(singleRowNewsDict[row])
    singleRow = []
    # export the rows to csv
    fp = open('F:/Abhi/pythonWorkspace/data/'+inp_year+'/euro_usd_news_'+inp_year+'_columns.csv', 'w', newline='')
    csvfile = csv.writer(fp, delimiter=',')
    fieldnames = [['Date',
                     'US_Industrial_Production_Actual','US_Industrial_Production_Consensus','US_Industrial_Production_Previous',
                     'EUR_Industrial_Production_Actual','EUR_Industrial_Production_Consensus','EUR_Industrial_Production_Previous',
                     'US_ISM_Manufacturing_PMI_Actual','US_ISM_Manufacturing_PMI_Consensus','US_ISM_Manufacturing_PMI_Previous',
                      'EUR_Markit_Manufacturing_PMI_Actual','EUR_Markit_Manufacturing_PMI_Consensus','EUR_Markit_Manufacturing_PMI_Previous',
                      'US_Trade_Balance_Actual','US_Trade_Balance_Consensus','US_Trade_Balance_Previous',
                      'EUR_Trade_Balance_Actual','EUR_Trade_Balance_Consensus','EUR_Trade_Balance_Previous',
                      'US_Consumer_Price_Index_Actual','US_Consumer_Price_Index_Consensus','US_Consumer_Price_Index_Previous',
                      'EUR_Consumer_Price_Index_Actual','EUR_Consumer_Price_Index_Consensus','EUR_Consumer_Price_Index_Previous',
                      'US_Fed_Interest_Rate_Actual','US_Fed_Interest_Rate_Consensus','US_Fed_Interest_Rate_Previous',
                      'EUR_ECB_Interest_Rate_Actual','EUR_ECB_Interest_Rate_Consensus','EUR_ECB_Interest_Rate_Previous'                         
                 ]]
    csvfile.writerows(fieldnames) 
    #cur_row = [cur_date,str(col_2.text),str(col_3.text),str(col_4.text),str(col_5.text),str(col_6.text),str(col_7.text),str(col_8.text),str(col_9.text)]
    # export to csv
    combinedRowKey = 0
    for i in range(1,row_count_singleRow):
        for j in range(0,31):   
            if (singleRowNewsDict.get((i,j),'NotExist') != 'NotExist'):
                singleRow = singleRow + [singleRowNewsDict[i,j]]
            else:
                singleRow = singleRow + [' ']
            if (j==30):
                csvfile.writerows([singleRow])
                # check the closest date equal or after the event and merge with the ohlc data                  
                if (singleRow[0] in combinedDict.values()):
                    for key,value in combinedDict.items():
                        if (value == singleRow[0]):
                            # get the first key
                            combinedRowKey = key[0]
                # date not available, pick nearest future date
                else:
                    # check the next 7 days until you get a match
                    breakOuter = False
                    for k in range(1,7):
                        if (breakOuter):
                            break
                        convDate = datetime.datetime.strptime(singleRow[0], "%Y-%m-%d")                    
                        nextDateTime = convDate + datetime.timedelta(days=k)
                        # get it into the format of the date in combinedDict so it can be looked up
                        nextDate = nextDateTime.date().strftime(" %m/ %d/%Y").replace(' 0', '').replace(' ', '')
                        if (nextDate in combinedDict.values()):
                            for key,value in combinedDict.items():
                                if (value == nextDate):
                                    # get the first key
                                    combinedRowKey = key[0]  
                                    breakOuter = True
                                    break 
                # update the row with the values in single row  
                # skip 6 columns as they contain ohlc data   
                if (combinedRowKey != 0):        
                    for m in range(0,31):
                        combinedDict[combinedRowKey,m+6] = singleRow[m]                
                singleRow = []  
                combinedRowKey = 0          
    finalRow = []    
    #print("export final data to csv")    
    fp = open('F:/Abhi/pythonWorkspace/data/'+inp_year+'/euro_usd_'+inp_year+'_final.csv', 'w', newline='')
    csvfile = csv.writer(fp, delimiter=',')   
    fieldnames = [['Date','Price','Open','High','Low','Change %','Date',
                     'US_Industrial_Production_Actual','US_Industrial_Production_Consensus','US_Industrial_Production_Previous',
                     'EUR_Industrial_Production_Actual','EUR_Industrial_Production_Consensus','EUR_Industrial_Production_Previous',
                     'US_ISM_Manufacturing_PMI_Actual','US_ISM_Manufacturing_PMI_Consensus','US_ISM_Manufacturing_PMI_Previous',
                      'EUR_Markit_Manufacturing_PMI_Actual','EUR_Markit_Manufacturing_PMI_Consensus','EUR_Markit_Manufacturing_PMI_Previous',
                      'US_Trade_Balance_Actual','US_Trade_Balance_Consensus','US_Trade_Balance_Previous',
                      'EUR_Trade_Balance_Actual','EUR_Trade_Balance_Consensus','EUR_Trade_Balance_Previous',
                      'US_Consumer_Price_Index_Actual','US_Consumer_Price_Index_Consensus','US_Consumer_Price_Index_Previous',
                      'EUR_Consumer_Price_Index_Actual','EUR_Consumer_Price_Index_Consensus','EUR_Consumer_Price_Index_Previous',
                      'US_Fed_Interest_Rate_Actual','US_Fed_Interest_Rate_Consensus','US_Fed_Interest_Rate_Previous',
                      'EUR_ECB_Interest_Rate_Actual','EUR_ECB_Interest_Rate_Consensus','EUR_ECB_Interest_Rate_Previous'                         
                 ]]
    csvfile.writerows(fieldnames)  
    for i in range(1,row_count):
        for j in range(0,37):  
            if (combinedDict.get((i,j),'NotExist') != 'NotExist'):
                finalRow = finalRow + [combinedDict[i,j]]
            else:
                finalRow = finalRow + [' ']       
            if (j == 36):
                csvfile.writerows([finalRow])
                finalRow = []
    
    #print("program completed")             