import course_finder as cf 
import pathway as p 
import average_gpa as ag 

def main():
    # pathway = p.pathway_msg()
    args = cf.cli()
    if(args.f is not None): 
        file = ag.course_list(args.f)
        avg = ag.avg_gpa(file)
        print("Projected GPA: " + str(avg))
    path = str(args.p)
    path_courses = p.csv_create(path, args.p)
    course_name, gpas = cf.course_finder(path_courses)
    cf.write(course_name, gpas)
    cf.sort()
    print("Data sorted in output.csv file") 

if __name__ == "__main__": 
    main() 