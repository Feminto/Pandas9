# Method 1
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    adict = {}
    for i in range(len(activity)):
        p = activity['player_id'][i]
        e = activity['event_date'][i]

        if p in adict:
            if adict[p] > e:
                adict[p] = e
        else:
            adict[p] = e
    
    result = []
    for k,v in adict.items():
        result.append([k,v])

    return pd.DataFrame(result, columns = ['player_id','first_login'])

# Method 2
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby('player_id')['event_date'].min().reset_index()

    return df.rename(columns = {'event_date':'first_login'})