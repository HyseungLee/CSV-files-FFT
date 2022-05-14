import os
import pandas as pd
from pandas import DataFrame
import csv

class csv_files_post:
    def __init__(self, directory):
        self.directory = directory
        self.get_csv_files()
        self.print_info()
        self.csv_read()

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
                new_data = data.drop(index=[0,1])
                #lost_string = "Lost connection during download0.0"
                new_data.iloc[0][0] = 0.0


        except:
            print("csv 파일 읽기 오류 발생")




csv = csv_files_post("E:/Code/Python/csv_file_import/현용_Ver3_6.5mm_FL426_rough아스팔트")



