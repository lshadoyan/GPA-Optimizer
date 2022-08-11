# GPA Optimizer 
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
A simple CLI to help the average college student optimize their course-load and GPA. 

This program has two main functions: 
```
1. Specifying a specific pathway and sorting those classes from highest to lowest GPA.  

2. Allowing the user to specify specific courses in a .txt file and returning an average GPA based on those courses.  
```
## How to Use: 
1. Install `python` and `git`

2. Clone the Repository: 
	````
	git clone https://github.com/lshadoyan/VT-Course-Finder.git
	````   
3. Navigate to the repository from command line and all of the required Python libraries can be installed using: 
	  ````
	pip install -r requirements.txt
	````
4. Specify a pathway using: 
	```` 
	python3 main.py -p 4
	````
	*Pathway 4 was used in this example. 
5. Specify your own courses in a `.txt` file by typing the acronym for a subject, its course number and the last name of the professor that teaches that class. Different courses should be on separate lines. Subject, course number and professor should separated by commas. 

	Note: If the last name of any of the professors are missing the result will become less accurate. That being said, <u>the professor last names are not a requirement.</u>  
	
	*see `sample_courses.txt` for an accurate example of the layout. 

	Get the average GPA using: 
	```` 
	python3 main.py -f sample_courses.txt
	````
	In this command, `sample_courses.txt` can be substituted for a path to your specified file.   

## Pathway Concepts: 
Use these characters to specify which pathway to look for: 
- 1f = Foundational Discourse Environments 
- 1a = Advanced/Applied Discourse 
- 2 = Critical Thinking in the Humanities
- 3 = Reasoning in the Social Sciences 
- 4 = Reasoning in the Natural Sciences Food Systems
- 5f = Foundational Quantitative and Computational Thinking 
- 5a = Advanced/Applied Quantitative and Computational Engagement Thinking 
- 6a = Critique and Practice in the Arts 
- 6d = Critique and Practice in Design 
- 7 = Critical Analysis of Identity and Equity in the United States

## Dependencies:
- Install [Python](https://www.python.org/downloads/) 
- Install [git](https://git-scm.com/downloads) 

## Future Functionality
Potentially finding a more updated website to request information from instead of [Anaanu](https://anaanu.com/) which seems to have somewhat outdated scores.
   
 Allowing the option for a more interactive approach to input information, instead of just CLI commands.  
 
Improving average GPA finder functionality: 

- In the case of request failure still giving the user a GPA based on the requests that didn't fail, even if that GPA would be inaccurate.
- Finding a better source of course information to parse through. Finding a source that contains both the course and course credit would allow my program to get the weighted GPA of provided courses. 
