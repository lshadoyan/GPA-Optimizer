import course_finder as cf 
import pathway as p 
import average_gpa as ag 

def main():
    args = cf.cli()

    if(args.f is not None):
        ag.course_check(args.f)   
        file_data = ag.course_list(args.f)
        if "professor" in file_data.columns:
            prof_info = ag.spec_info(file_data)
            
            if (prof_info is not None) and (len(file_data.index) == len(prof_info.index)): 
                prof_avg = ag.prof_gpa(prof_info, file_data )
                print("\nProjected GPA Based on Professor: " + str(prof_avg))
            else: 
                avg = ag.avg_gpa(file_data, "course_name", "course_number")
                print("Projected GPA: " + str(avg))
        else:   
            avg = ag.avg_gpa(file_data, "course_name", "course_number")
            print("Projected GPA: " + str(avg))
    path = str(args.p)

    if args.p is not None: 
        path_courses = p.csv_create(path, args.p)
        course_name, gpas = cf.course_finder(path_courses)
        cf.write(course_name, gpas)
        cf.sort()
        print("Data sorted in output.csv file") 
    

if __name__ == "__main__": 
    main() 