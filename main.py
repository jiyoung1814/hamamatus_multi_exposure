import os

import Read_Cas_Data
import readData
import GetMergedSPD
import RemoveDarkCurrent
import Leveling_data
import Lagrange_interpolation
import Y_interpolation

import DrawEachExel
import Color
from openpyxl import Workbook
import pandas as pd

if __name__ == '__main__':
    # print(os.getcwd())  # 현재 경로 출력
    path = "data_hamamatus/"  # 폴더 경로
    os.chdir(path) #해당 경로로 이동

    cct_folder = os.listdir() #CCT 폴더 명들


    for cct in cct_folder:
        os.chdir(cct + "/")
        try_folder = os.listdir() #try 폴더 명들

        cas_data = Read_Cas_Data.Read_Cas_Data(cct).cas_data

        try_data = {}

        for t in try_folder:
            os.chdir(t + "/")
            files = os.listdir()

            data = readData.readData(files).data #{ intg.:[], 0:[spd1,spd2,spd3,spd4,spd5,spd6], ... 287:[]}
            merged_data = GetMergedSPD.GetMergedSPD(data).merged_data # {0: [spd, intg] ... 287:[]}
            remove_dark_current_data = RemoveDarkCurrent.RemoveDarkCurrent(merged_data).dark_current_removed_data  # {0: [spd, intg] ... 287:[]}
            leveling_data = Leveling_data.Leveling_data(remove_dark_current_data).leveling_data # {0: [spd, intg] ... 287:[]}

            lagrange_data = Lagrange_interpolation.Lagrange_interpolation(leveling_data, cas_data).lagrange_data  # {cas: [spd(380)...spd(780)], hamamatus: []}
            y_interpolation_data = Y_interpolation.Y_interpolation(lagrange_data['hamamtus']).y_interpolation_data #[]

            try_data[t]=DrawEachExel.DrawEachExel(cct, t, data, merged_data, remove_dark_current_data, leveling_data, lagrange_data, y_interpolation_data).final_data
            os.chdir("../")
            # break

        final_data = {}
        validation_data = {}

        for t in list(try_data.keys()):
            final_data['wavelength'] = list(range(380, 781))
            final_data[t+"_cas"] = try_data[t]['cas']
            final_data[t+"_hamamtus"] = try_data[t]['hamamtus']

            validation_data["값"] = ['lux', 'cct']
            validation_data[t+"_cas"] = Color.Color(try_data[t]['cas']).color_data
            validation_data[t+"_hamamtus"] = Color.Color(try_data[t]['hamamtus']).color_data


        df_final = pd.DataFrame(final_data)
        df_validation = pd.DataFrame(validation_data)

        with pd.ExcelWriter(cct+'_final.xlsx') as writer:
            df_final.to_excel(writer, sheet_name='최종', index=False)
            df_validation.to_excel(writer, sheet_name='검증', index=False)

        os.chdir("../")
        # break




