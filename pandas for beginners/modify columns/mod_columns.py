import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees
    
# I have a employees df and i want to modify the salary column by multiplying it by 2
# I want to return the modified df
# you can use the modifySalaryColumn function and replace items according to your needs