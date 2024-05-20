import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    Student_Dataframe = pd.DataFrame(student_data,columns = ["student_id","age"])
    return Student_Dataframe

student_data = [
                    [1, 15],
                    [2, 11],
                    [3, 11],
                    [4, 20]
                ]

Student_df = createDataframe(student_data)
print(Student_df)