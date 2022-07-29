import course_finder as cf 
import data_frame as df  

def main():
    pathway = df.pathway_msg()
    args = cf.cli()
    if args.p is not None: 
        path = str(args.p)
    else:
        print(pathway)
        path = input("Pathway Concept: ")
    path_courses = df.csv_create(path)
    if args.uni is not None:  
        university = args.uni 
    else: 
        university = input("University ID in Anaanu: ")
    if args.f is not None: 
        file = args.f 
    else: 
        file = input("File location: ")
    course_name, gpas = cf.course_finder(university, file, path_courses)
    cf.write(course_name, gpas)
    cf.sort()
    print("Data sorted in output.csv file") 

if __name__ == "__main__": 
    main() 