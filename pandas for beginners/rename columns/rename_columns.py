import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.columns = ["student_id","first_name","last_name","age_in_years"]
    return students

# you  can test your function by calling it here
# students is a pandas DataFrame