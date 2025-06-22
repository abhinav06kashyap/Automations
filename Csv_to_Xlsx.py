"""
Hi user this script will convert any csv file(s) into excel and store the converted files in Xlsx Files folder (created by script). 
It can be used as a stand alone or included in your other script where this functionality/conversion is required.

Your system should have python installed to run this script.
You would need to install openpyxl in your system/virtual environment. command 'pip install openpyxl'

To run the script:
1. Save the sacript in your folde where you have csv files. 
2. Go to your terminal/command prompt
3. Change to the directory where you have saved this file.
4. Give command 'python Csv_to_Xlsx.py'. If you changed the filename, give the same to this commmand.
5. Input data as asked in prompt
6. Script will create Xlsx Files folder and save the files.

To stop the script execution in middle, do a 'ctrl+c' or 'ctrl+alt+delete' if former didnt work.
"""

import pandas as pd
import os

if not os.path.exists('Xlsx Files'):
    os.makedirs('Xlsx Files')
try:
    def CSV_to_XLSX(csv_list, xlsx_list):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        for csv, xlsx in zip(csv_list, xlsx_list):
            csv_file = os.path.join(current_directory, csv)
            xlsx_file = os.path.join(current_directory, "Xlsx Files/"+xlsx)
            df = pd.read_csv(csv_file)
            df.to_excel(xlsx_file, index = False)
            print(f"New Xlsx File created: {xlsx_file}")

    csv_checker = False
    xlsx_checker = False
    while (csv_checker and xlsx_checker) == False:
        #collecting csv filenames
        csv_name = input("Enter CSV filename with .csv extention (if multiple use ',' for seperation): ")
        if ',' in csv_name:
            csv_files = csv_name.split(',')
        elif csv_name.count('.csv') > 1:
            print("Use commas to seperate the filenames")
            continue
        else:
            csv_files = [csv_name]
            
        #check csv filenames for extention
        csv_list = []
        for file in csv_files:
            if ".csv" in file:
                csv_checker = True
                csv_list.append(file) 
            else:
                csv_checker = False
                print(f"Wrong CSV extention for {file}, use '.csv'.")
                continue
        if csv_checker == True:
            #check if user wants same name for xlsx as csv
            xlsx_list = []  
            user_req_for_xlsx_name = input("\nDo you want same name for XLSX file as CSV (y or n): ")
            if user_req_for_xlsx_name == 'n':
                #collecting xlsx filenames
                xlsx_name = input("\nEnter new Excel filename with .xlsx extention \n(if you entered multiple csv enter the xlsx names in same order with ',' as seperation): ")
                if ',' in xlsx_name:
                    xlsx_files = xlsx_name.split(',')
                elif xlsx_name.count('.csv') > 1:
                    print("Use commas to seperate the filenames")
                    continue
                else:
                    xlsx_files = [xlsx_name]
                
                #check if filenames provided are equal for both extentions.
                if len(csv_files) != len(xlsx_files):
                    print('No of filenames do not match')
                    continue
                else:
                    pass
                
                #check xlsx filenames for extention  
                for file in xlsx_files:
                    if ".xlsx" in xlsx_name:
                        xlsx_checker = True
                        xlsx_list.append(file)
                    else:
                        print("Wrong XLSX extention, use '.xlsx'.")
                        continue  
                
            elif user_req_for_xlsx_name == 'y':
                xlsx_checker = True
                for item in csv_files:
                    name = item.split('.csv')[0]
                    xlsx_list.append(name + '.xlsx')

            print(xlsx_list)
        else:
            continue
    CSV_to_XLSX(csv_list, xlsx_list)

except Exception as e:
    print(f"Error occured {e}")