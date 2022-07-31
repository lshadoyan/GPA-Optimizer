import pandas as pd
import tabula

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
    return data

if __name__ == "__main__": 
    ... 