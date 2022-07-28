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
    df.csv_create(path)
    df.fix()
    if args.uni is not None:  
        university = args.uni 
    else: 
        university = input("University ID in Anaanu: ")
    if args.f is not None: 
        file = args.f 
    else: 
        file = input("File location: ")
    courses, gpas = cf.course_finder(university, file)
    cf.write(courses, gpas)
    cf.sort()
    print("Data sorted in result.csv file") 

if __name__ == "__main__": 
    main() 