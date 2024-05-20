import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(bonus=2 * employees['salary'])

# my dataframe name is employees
# create a new dataframe and give that dataframe as a parameter for creatBonusColumn()
# bonus is the new column and its 2x like salary column values in my dataframe