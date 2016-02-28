'''
Created on Nov 25, 2015

@author: abhijit
'''
from idlelib.ClassBrowser import file_open
def get_inputs():
    txt_obj = open('C:/Users/abhijit/Desktop/CurrencyInput.txt', 'r')
    txt_lines =txt_obj.readlines()
    for line in txt_lines:
        if (str(line).find('start_dt') != -1):
            inp_start_dt = str(line)[len('start_dt') +1:].rstrip()
            #print(inp_start_dt)
        elif (str(line).find('end_dt') != -1):
            inp_end_dt = str(line)[len('end_dt') +1:].rstrip()
            #print(inp_end_dt)  
        elif (str(line).find('year') != -1):
            inp_year = str(line)[len('year') +1:].rstrip()
            #print(inp_end_dt)             
    return inp_start_dt,inp_end_dt, inp_year
# inp1_start_dt = '';inp1_end_dt= '';inp1_year=''
# inp1_start_dt,inp1_end_dt,inp1_year = get_inputs()
# print("new")
# print(inp1_start_dt)
# print(inp1_end_dt)
# print(inp1_year)
#if(txt_lines)