import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
inning_1 = pd.read_csv('../data/2018_pitchers_inning_1.csv')

data = pd.concat([
    pd.read_csv('../data/2018_pitchers_inning_1.csv'),
    pd.read_csv('../data/2018_pitchers_inning_2.csv'),
    pd.read_csv('../data/2018_pitchers_inning_3.csv'),
    pd.read_csv('../data/2018_pitchers_inning_4.csv'),
    pd.read_csv('../data/2018_pitchers_inning_5.csv'),
    pd.read_csv('../data/2018_pitchers_inning_6.csv'),
    pd.read_csv('../data/2018_pitchers_inning_7.csv'),
    pd.read_csv('../data/2018_pitchers_inning_8.csv'),
    pd.read_csv('../data/2018_pitchers_inning_9.csv'),
    pd.read_csv('../data/2018_pitchers_inning_extra.csv')
                 ])

data.to_csv('2018_pitchers_all.csv')

