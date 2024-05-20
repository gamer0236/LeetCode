import pandas as pd

def createDataframe(employees: list[list[int]]) -> pd.DataFrame:
    employees_Dataframe = pd.DataFrame(employees,columns = ["employee_id ","name","department","salary"])
    return employees_Dataframe

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.loc[0:2]


employees  = [
               [ 3 , 'Bob' ,'Operations' ,48675 ], 
                [90,'Alice','Sales' , 11096],
                [9,'Tatiana', 'Engineering', 33805 ],
                [60 ,'Annabelle','InformationTechnology',37678],
                [49 ,'Jonathan', 'HumanResources',23793 ],
                [43 ,'Khaled', 'Administration' ,40454]
]

employees_Dataframe = createDataframe(employees)
print(selectFirstRows(employees_Dataframe))