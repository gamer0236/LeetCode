import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    numOfColumns = len(players.columns)
    numOfRows = len(players.index)
    rows_columns_list = []
    rows_columns_list.append(numOfRows)
    rows_columns_list.append(numOfColumns)
    return rows_columns_list


def createDataframe(players: list[list[int]]) -> pd.DataFrame:
    Players_Dataframe = pd.DataFrame(players,columns = ["player_id ","name","age","position","team"])
    return Players_Dataframe
    

players = [
            [846 ,'Mason' , 21 ,'Forward','RealMadrid'],
            [749 ,'Riley' ,30, 'Winger','Barcelona'  ],
            [155 , 'Bob' , 28  ,'Striker' ,'ManchesterUnited' ],
            [583 ,'Isabella', 32 , 'Goalkeeper' ,'Liverpool'],
            [388 , 'Zachary', 24, 'Midfielder' ,'BayernMunich'],
            [883 , 'Ava' ,23 ,'Defender' ,'Chelsea' ],
            [ 355 , 'Violet' , 18 ,'Striker','Juventus' ],
            [ 247 ,'Thomas',27 ,'Striker', 'ParisSaint-Germain'],
            [761, 'Jack' ,33 ,'Midfielder', 'ManchesterCity'],
            [642 ,'Charlie' , 36 ,'Center-back','Arsenal']

]

Players_Dataframe = createDataframe(players)
print(getDataframeSize(Players_Dataframe))