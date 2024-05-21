import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students
    
# students dataframe has a column "grade" with float values
# by using the changeDatatype function, the column is converted to int