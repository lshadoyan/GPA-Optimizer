from importlib.resources import path
import requests
import os 
import sys 
import argparse
import pandas as pd 
import csv 

def cli(): 
    parser = argparse.ArgumentParser(description="Pathways: 1f, 1a, 2, 3, 4, 5, 6a, 6d, and 7")
    parser.add_argument('-uni', help='University id used in Anaanu')
    parser.add_argument('-f', help='Path to file with courses' )
    parser.add_argument('-p', help='Pathways concept chosen', type=str)
    # parser.add_argument(dest="Pathways: 1f, 1a, 2, 3, 4, 5, 6a, 6d, and 7")
    args = parser.parse_args()
    return args

def get_gpa(university, subject, course_number):
    req = requests.get("https://anaanu.com/api/v1/course?university="+university+"&subject="+subject+"&course="+course_number)
    r_json = req.json()
    try:
        gpa = r_json['course']['average']['gpa']
    except:
        gpa = None
    return gpa

def sort():
    df = pd.read_csv('output.csv', header=None)
    # print(df.head())
    df = df.sort_values(by=1, ascending=False)
    df.to_csv('output.csv')
    
def write(course_name, grades):
    with open('output.csv','w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(course_name, grades))
        f.close()

def course_finder(university, course_file, pathway_courses): 
    if(not (os.path.exists(course_file))):
        print("File doesn't exist")
        sys.exit()
    courses = pathway_courses.tolist()
    gpas = []  
    for elem in list(courses):
        subject, number = elem.split(' ')
        gpa = get_gpa(university, subject, number)
        if(gpa == None):
            courses.remove(elem)
            continue
        print("Subject: "+subject+" Course Number: "+ number + " GPA: " +str(gpa))
        gpas.append(gpa)
    return courses, gpas 

   # write(courses, gpas)
   # sort() 

if __name__ == "__main__": 
    ...  