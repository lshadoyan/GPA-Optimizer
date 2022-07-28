import pandas as pd
import tabula
import course_finder as cf

def pathway_msg(): 
    p = open('pathways.txt', 'r')
    pathway = p.read()
    p.close()
    return pathway
  

#pathway = input("Pathway Concept: ")

def csv_create(pathway):
    file_path = r"Pathways Course Guide by Alpha.pdf"
    dfs = tabula.read_pdf(file_path, pages="all", lattice=True, multiple_tables=True, pandas_options={'header': None}) 

    data = []
    for df in dfs:
        df["Course"] = df[0].astype(str) +" "+ df[1].astype(str)
        n_df = df.loc[df[3].str.contains(pathway, na=False)]
        data.append(n_df["Course"])

    data = pd.concat(data)
    # print(data)
    data.to_csv('output.csv', index=False, header=False)

def fix(): 
    with open('output.csv', 'r') as f_in, open('my_file.txt', 'w') as f_out:
        content = f_in.read().strip().replace("\n", ",")
        f_out.write(content)

if __name__ == "__main__": 
    ... 