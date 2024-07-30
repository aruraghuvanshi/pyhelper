import pandas as pd
from datetime import datetime
import pytz


def edit_df(df, unique_id_col, row_item, col, edit, save=False, filepath='', index=False):
    '''
    df : dataframe
    unique_id_col : name of the column that holds the unique row identifier
    row_item : value of the record item in the unique_id column
    col: name of the column whose record needs the edit
    edit: str: value (str) that needs to be edited
    save: bool: save file to csv (default false)
    filepath: str: path of the file to be saved to (default '')
    index: bool whether saved file should have index (default false)
    '''
    df.loc[df[unique_id_col] == row_item, col] = edit

    if save:
        df.to_csv(filepath, index=index)

    return df


def add_to_df(df, lst, save=False, filepath='', index=False):
    '''
    df: dataframe to delete row from
    lst: list: complete list of the values to be entered into the dataframe, one element per column of df
    save: bool: save to csv (default false)
    filepath: str: filepath to save the csv file to (default '')
    index: bool: whether to save the index to csv file (default false)
    '''
    try:
        dx = pd.DataFrame([lst], columns=df.columns)
        df = pd.concat([df, dx]).reset_index(drop=True)

        if save:
            df.to_csv(filepath, index=index)

    except Exception as e:
        print(f'Data Adding unsuccessful')
        print(e)

    return df


def delete_row_from_df(df, unique_id_col, row_item, save=False, filepath='', index=False):
    '''
    df: dataframe to delete row from
    unique_id_col: name of the column that holds the unique_id of the row
    row_item: value of the unique_id
    save: bool: save to csv (default false)
    filepath: str: filepath to save the csv file to (default '')
    index: bool: whether to save the index to csv file (default false)
    '''
    dx = df[df[unique_id_col] == row_item]
    dx.index[0]
    df = df.drop(dx.index[0])

    if save:
        df.to_csv(filepath, index=index)

    return df


def cprint(text, c='w'):
    '''
    Author: Aru Raghuvanshi
    Use this function to debug and print statements in different colours
    :param text: str
    :param c: str: one of [b, g, r, v, y, c, w, bb, gg, rr, vv, yy, cc, ww, u, s, i]
        s: strikethru, u:underline, i:italics)
        default: white
    :return: none

    '''
    if c == 'b':
        print(f'\033[0;94m{text}\033[0m')
    elif c == 'g':
        print(f'\033[0;92m{text}\033[0m')
    elif c == 'r':
        print(f'\033[0;91m{text}\033[0m')
    elif c == 'v':
        print(f'\033[0;95m{text}\033[0m')
    elif c == 'y':
        print(f'\033[0;93m{text}\033[0m')
    elif c == 'c':
        print(f'\033[0;96m{text}\033[0m')
    elif c == 'w':
        print(f'\033[0;97m{text}\033[0m')
    elif c == 'bb':
        print(f'\033[1;94m{text}\033[0m')
    elif c == 'gg':
        print(f'\033[1;92m{text}\033[0m')
    elif c == 'rr':
        print(f'\033[1;91m{text}\033[0m')
    elif c == 'vv':
        print(f'\033[1;95m{text}\033[0m')
    elif c == 'yy':
        print(f'\033[1;93m{text}\033[0m')
    elif c == 'cc':
        print(f'\033[1;96m{text}\033[0m')
    elif c == 'ww':
        print(f'\033[1;97m{text}\033[0m')
    elif c == 'u':
        print(f'\033[0;4m{text}\033[0m')
    elif c == 's':
        print(f'\033[0;9m{text}\033[0m')
    elif c == 'i':
        print(f'\033[0;3m{text}\033[0m')
    else:
        pass


def string_to_dt(date_string, date_format="%Y-%m-%d"):
    '''
    date_string: str: incoming date string in format set by date_format
    date_format: str: expected format of incoming date
    return: datetime obj with timestamp 00:00:00 if not specified in format
    '''
    dobj = datetime.strptime(date_string, date_format)
    return dobj


def dt_to_string(dobj, format="%Y-%m-%d"):
    '''
    dobj: datetime obj
    format: str: expected format of returned date
    return: str date in format set
    '''
    formatted_date = dobj.strftime(format)
    return formatted_date


def utc2local(tz='Asia/Kolkata', date_format='%d-%m-%Y %H:%M:%S'):
    '''
    Get local time from any timezone

    tz = ETC/GMT+4 etc. (default: 'Asia/Kolkata')
        US/Pacific, US/Mountain, US/Hawaii, Europe/Poland, Europe/Berlin
        Pacific/Palau, Indian/Maldives, Europe/countryname

    More tz list at https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568

    date_format='%d-%m-%Y %H:%M:%S' (Enter full format)
    '''
    # utc = datetime.utcnow()
    tzInfo = pytz.timezone(tz)
    dttm = datetime.now(tz=tzInfo)
    try:
        dttm = dttm.strftime(date_format)
        dttm = str(dttm)[:16]
        dt = dttm.split(' ')[0]
        tm = dttm.split(' ')[1]
        return dt, tm
    except:
        print('Enter full date_format field including time, check help docstring.')