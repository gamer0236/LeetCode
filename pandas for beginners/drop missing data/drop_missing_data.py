import pandas as pd

def create_df(student_list):
    students = pd.DataFrame(student_list,columns=["student_id","name","age"])
    return students


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=["name"],inplace=True)
    return students


student_list = [
    [ 1, "John", 20],
    [ 2, None, 45],
    [ 3, "Bob", 30],
    [ 4, "Alice", 56],
    [ 5, None, 40]
]

students  = create_df(student_list)
print(dropMissingData(students))