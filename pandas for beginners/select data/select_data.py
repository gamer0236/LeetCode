import pandas as pd

student_list = [[101,"Ulysses" ,13],
                [53,"William",10 ],
                [128,"Henry",6],
                [3,"Henry",11]]


def create_df(student_list:list[list[int]]):
    student_df = pd.DataFrame(student_list,columns=["student_id","name","age"])
    return student_df



def selectData(student_df: pd.DataFrame) -> pd.DataFrame:
    return student_df.loc[student_df["student_id"] == 101,["name","age"]]
    

student_df = create_df(student_list)
print(selectData(student_df))