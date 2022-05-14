import os
import pandas as pd
from pandas import DataFrame
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

class csv_files_post:
    def __init__(self, directory):
        self.directory = directory
        self.get_csv_files()
        self.print_info()
        self.csv_data_set = self.csv_read()

    def get_csv_files(self):
        path = self.directory
        file_list = os.listdir(path)
        self.file_list_csv = [file for file in file_list if file.endswith(".csv")]


    def print_info(self):
        print("----------------------------------------------------------------")
        print("Directory : ", self.directory)
        print("file_list_csv: {}".format(self.file_list_csv))


    def csv_read(self):

        try:
            for csv_file in self.file_list_csv:

                data = pd.read_csv(self.directory + '/' + csv_file, names=['Time', 'Pressure'], engine='python', header=None)

                df = data.drop(index=[0,1])
                #lost_string = "Lost connection during download0.0"
                df.iloc[0][0] = 0.0
                #df = df.set_index('Time')
                #df['Time'].round(1)
                plt.xlabel('Time ($sec$)')
                plt.ylabel('Amplitude ($Pa$)')
                df.plot('Time','Pressure')
                Y = np.fft.fft(df)
                plt.plot(Y)

        except:
            print("csv 파일 읽기 오류 발생")




csv = csv_files_post("E:/Code/Python/csv_file_import/현용_Ver3_6.5mm_FL426_rough아스팔트")



