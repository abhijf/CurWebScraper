'''
Created on Dec 13, 2015

@author: abhijit
'''
import csv
fp = open('F:/Abhi/pythonWorkspace/data/merged/cleaning_stage4.csv', 'r')
reader = csv.DictReader(fp)
# create a new dict which will be used to clean the data
cleanDict = {}
row_count = 0
# initialize the previous value
prev_US_Industrial_Production_Actual = ' '
prev_EUR_Industrial_Production_Actual = ' '
prev_US_Markit_Manufacturing_PMI_Actual = ' '
prev_EUR_Markit_Manufacturing_PMI_Actual = ' '
prev_US_Trade_Balance_Actual = ' '
prev_EUR_Trade_Balance_Actual = ' '
prev_US_Consumer_Price_Index_Actual = ' '
prev_EUR_Consumer_Price_Index_Actual = ' '
prev_US_Fed_Interest_Rate_Actual = ' '
prev_EUR_ECB_Interest_Rate_Actual = ' '

# read the value from the csv, and if there is a blank value in the news related 
# columns replace it with the previous value
for row in reader:
    row_count = row_count + 1   
    cleanDict[row_count,0] = row['Date']
    cleanDict[row_count,1] = row['Price']
    cleanDict[row_count,2] = row['Open']
    cleanDict[row_count,3] = row['High']
    cleanDict[row_count,4] = row['Low']
    cleanDict[row_count,5] = row['Change %']
    
    if((row['US_Industrial_Production_Actual'] is not None) and (row['US_Industrial_Production_Actual'].strip() != '') and (len(row['US_Industrial_Production_Actual']) > 0)):
        prev_US_Industrial_Production_Actual = row['US_Industrial_Production_Actual']   
    cleanDict[row_count,6] = prev_US_Industrial_Production_Actual
    if((row['US_Industrial_Production_Actual'] is not None) and (row['EUR_Industrial_Production_Actual'].strip() != '') and (len(row['EUR_Industrial_Production_Actual']) > 0)):
        prev_EUR_Industrial_Production_Actual = row['EUR_Industrial_Production_Actual']    
    cleanDict[row_count,7] = prev_EUR_Industrial_Production_Actual    
    if((row['US_Industrial_Production_Actual'] is not None) and (row['US_ISM_Manufacturing_PMI_Actual'].strip() != '') and (len(row['US_ISM_Manufacturing_PMI_Actual']) > 0)):
        prev_US_Markit_Manufacturing_PMI_Actual = row['US_ISM_Manufacturing_PMI_Actual']    
    cleanDict[row_count,8] = prev_US_Markit_Manufacturing_PMI_Actual
    if((row['US_Industrial_Production_Actual'] is not None) and (row['EUR_Markit_Manufacturing_PMI_Actual'].strip() != '') and (len(row['EUR_Markit_Manufacturing_PMI_Actual']) > 0)):
        prev_EUR_Markit_Manufacturing_PMI_Actual = row['EUR_Markit_Manufacturing_PMI_Actual']    
    cleanDict[row_count,9] = prev_EUR_Markit_Manufacturing_PMI_Actual
    if((row['US_Industrial_Production_Actual'] is not None) and (row['US_Trade_Balance_Actual'].strip() != '') and (len(row['US_Trade_Balance_Actual']) > 0)):
        prev_US_Trade_Balance_Actual = row['US_Trade_Balance_Actual']
    cleanDict[row_count,10] = prev_US_Trade_Balance_Actual
    if((row['US_Industrial_Production_Actual'] is not None) and (row['EUR_Trade_Balance_Actual'].strip() != '') and (len(row['EUR_Trade_Balance_Actual']) > 0)):
        prev_EUR_Trade_Balance_Actual = row['EUR_Trade_Balance_Actual']    
    cleanDict[row_count,11] = prev_EUR_Trade_Balance_Actual
    if((row['US_Industrial_Production_Actual'] is not None) and (row['US_Consumer_Price_Index_Actual'].strip() != '') and (len(row['US_Consumer_Price_Index_Actual']) > 0)):
        prev_US_Consumer_Price_Index_Actual = row['US_Consumer_Price_Index_Actual']    
    cleanDict[row_count,12] = prev_US_Consumer_Price_Index_Actual
    if((row['US_Industrial_Production_Actual'] is not None) and (row['EUR_Consumer_Price_Index_Actual'].strip() != '') and (len(row['EUR_Consumer_Price_Index_Actual']) > 0)):
        prev_EUR_Consumer_Price_Index_Actual = row['EUR_Consumer_Price_Index_Actual']    
    cleanDict[row_count,13] = prev_EUR_Consumer_Price_Index_Actual
    if((row['US_Industrial_Production_Actual'] is not None) and (row['US_Fed_Interest_Rate_Actual'].strip() != '') and (len(row['US_Fed_Interest_Rate_Actual']) > 0)):
        prev_US_Fed_Interest_Rate_Actual = row['US_Fed_Interest_Rate_Actual']    
    cleanDict[row_count,14] = prev_US_Fed_Interest_Rate_Actual  
    if((row['US_Industrial_Production_Actual'] is not None) and (row['EUR_ECB_Interest_Rate_Actual'].strip() != '') and (len(row['EUR_ECB_Interest_Rate_Actual']) > 0)):
        prev_EUR_ECB_Interest_Rate_Actual = row['EUR_ECB_Interest_Rate_Actual']        
    cleanDict[row_count,15] = prev_EUR_ECB_Interest_Rate_Actual
    #print(cleanDict[row_count,15])

fwp = open('F:/Abhi/pythonWorkspace/data/merged/cleaning_stage5.csv', 'w', newline='')
csvfile = csv.writer(fwp, delimiter=',')  
fieldnames = [['Date','Price','Open','High','Low','Change %','US_Industrial_Production_Actual','EUR_Industrial_Production_Actual','US_Markit_Manufacturing_PMI_Actual','EUR_Markit_Manufacturing_PMI_Actual','US_Trade_Balance_Actual','EUR_Trade_Balance_Actual','US_Consumer_Price_Index_Actual','EUR_Consumer_Price_Index_Actual','US_Fed_Interest_Rate_Actual','EUR_ECB_Interest_Rate_Actual']]
csvfile.writerows(fieldnames)
finalRow=[]
for i in range(1,row_count):
        for j in range(0,16):  
            if (cleanDict.get((i,j),'NotExist') != 'NotExist'):
                finalRow = finalRow + [cleanDict[i,j]]
            else:
                finalRow = finalRow + [' ']       
            if (j == 15):
                csvfile.writerows([finalRow])
                finalRow = []
print('end')           
