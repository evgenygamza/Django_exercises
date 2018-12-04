# -*- coding: cp1251 -*-

import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import matplotlib.pyplot as plt

root = Tk()  # Tkinter window
root.withdraw()  # We make it invisible

# importing part of file
openlist = askopenfilenames(
    title="�������� *.csv ����",
    filetypes=(("csv files", "*.csv"),
               ("all files", "*.*")))

root.destroy()  # closing the invisible window

# # some openlists for testing:
# # short single file:
# openlist = ['C:/Users/Evgeny/PycharmProjects/ffprocessing/test.csv']

# # file with cyrillic path:
# openlist = ['C:/Users/Evgeny/YandexDisk/!�������/������������ �������������/SPB_20180900_60pp.csv']

# # list of three files:
# openlist = ['C:/Users/Evgeny/YandexDisk/!�������/������������ �������������/SPB_20180900_60pp.csv',
#             'C:/Users/Evgeny/YandexDisk/!�������/������������ �������������/ALK_20180900_60pp.csv',
#             'C:/Users/Evgeny/PycharmProjects/ffprocessing/test.csv']


# main part of file
def csv_plot(filename):  # reading and plotting function
    print('Now processing:  %s' % filename.split('/')[-1])
    df = pd.read_csv(filename, sep=';', engine='python', encoding='utf8',
                     index_col='date and time', parse_dates=True)
    # "engine" and "encoding" parameters were added to solve the problem with cyrillic path to file
    # todo make a "window" filter for invalid values (00100) (someday)
    print(df.info())
    for col in df.columns:
        df[col] -= df[col].mean()  # subtract average value from column
        # df[col] -= df[col].loc[df[col].first_valid_index()]  # subtract first valid value from column
    try:
        df.filter(regex=r'..._[HX]').plot(ax=axes[0])  # add components to relevant subplots
        df.filter(regex=r'..._[EY]').plot(ax=axes[1])  # using regular expressions as a filter parameter
        df.filter(regex=r'..._Z').plot(ax=axes[2])
    except:
        df.filter(regex=r'A[UEL]').plot(ax=axes[3])


# executive part todo make a 3 or 4 subplots window
fig, axes = plt.subplots(4, 1, figsize=(10, 5), sharex=True)
for file in openlist:
    csv_plot(file)
plt.style.use('ggplot')
plt.show()

print('Done')
