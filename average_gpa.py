import pandas as pd
import os 
import sys
import requests
import course_finder as cf 

def course_check(course_file): 
    if not os.path.exists(course_file):
        print("File doesn't exist")
        sys.exit()

def space_replace(course_file): 
    with open(course_file, 'r+') as f:
        txt = f.read().replace(' ', '')
        f.seek(0)
        f.write(txt)
        f.truncate()
    
def course_list(course_file):
    df = pd.read_csv(course_file, delimiter=",", header=None, names =["course_name", "course_number", "professor"])
    return df

def avg_gpa(df, row1, row2):
    list = [] 
    for index, row in df.iterrows():
        list.append(cf.get_gpa(str(row[row1]), str(row[row2])))
    df[3] = list                                         
    try: 
        avg = sum(list) / len(list)
    except: 
        print("Sorry, an accurate gpa cannot be calculated.")
        avg = 0 
    return avg 

def course_info(subject, course_number):
    try:
        req = requests.get("https://anaanu.com/api/v1/course?university=virginia-tech-vt"+"&subject="+subject+"&course="+course_number)
    except:
        print("Sorry, an accurate gpa cannot be calculated.")
        return None

    r_json = req.json()
    prof = r_json['course']
    df = pd.json_normalize(prof, record_path =['instructors'], meta=[['average','gpa']])
    return df 

def spec_info(course_list):
    df = pd.DataFrame()
    for index, row in course_list.iterrows():
        try: 
            info = course_info(str(row['course_name']), str(row['course_number']))
        except: 
            return None
        professor = row["professor"]
        info = info.loc[info['instructor.lastName'] == professor]
        df = pd.concat([df, info], axis=0, ignore_index=True)
    return df

def prof_gpa(df, course_list): 
    prof_list = pd.concat([course_list, df], axis=1)
    list = [] 
    for index, row in prof_list.iterrows(): 
        print("\n" + str(row['course_name']) +" "+ str(row['course_number']) + ":\n" + "\nDistribution:" ) 
        print("A: " + str(round(row['a'], 2)) + "%") 
        print("B: " + str(round(row['b'], 2)) + "%") 
        print("C: " + str(round(row['c'], 2)) + "%") 
        print("D: " + str(round(row['d'], 2)) + "%") 
        print("F: " + str(round(row['f'], 2)) + "%") 
        print("GPA based on professor: " + str(round(row['gpa'], 3)) + "\n") 
        list.append(row['gpa'])
    try: 
        prof_avg = sum(list) / len(list)
    except: 
        return None
    return round(prof_avg, 3) 




        
        
