import pandas as pd
import os 
import sys
import course_finder as cf 

def course_list(course_file):
    if not os.path.exists(course_file):
        print("File doesn't exist")
        sys.exit()
    df = pd.read_csv(course_file, delimiter=" ", header=None)
    return df

def avg_gpa(df):
    list = [] 
    for index, row in df.iterrows():
        list.append(cf.get_gpa(str(row[0]), str(row[1])))
    df[2] = list 
    print(list)
    try: 
        avg = sum(list) / len(list)
    except: 
        print("Sorry, one of the courses returned a null value for gpa.")
        avg = 0 
    return avg 
    # if("null" == df.values.any()): 
    #     print("Sorry, one of the courses returned a null value for gpa.")
    #     return 0 
    # else: 
    #     avg = sum(list) / len(list)
    # return avg


