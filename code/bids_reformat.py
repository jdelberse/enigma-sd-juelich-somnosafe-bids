import os
import sys
import pandas as pd

# %%
# path of the dataset
save_path = '/data/project/sleep_ENIGMA_Cognition/dataladstore/Test/Somnosafe_BIDS/'
reformat_path = '/data/project/sleep_ENIGMA_Cognition/dataladstore/Test/Somnosafe_BIDS/'

# %%
def get_folder_lists(save_path):
    # get the list of the folders
    folders = os.listdir(save_path)
    # only keep the real folders
    folders = [f for f in folders if os.path.isdir(os.path.join(save_path, f))]
    # remove the . start folders
    folders = [f for f in folders if not f.startswith('.')]
    # order the folders
    folders.sort()

    return folders

# %%
"""
Get subject lists from all sessions, 
1. make a dataframe based on the subject list from each session, column is the session name
2. compare and find whether which session has different or missed which subject
"""
# get the list of subjects folders
sess_folders = get_folder_lists(save_path)
df_sub_list = pd.DataFrame()

for sess in sess_folders:
    sub_folders = get_folder_lists(save_path + sess)
    print('Session: ', sess, ' has ', len(sub_folders), ' subjects')

    # for the elements in the list, like 'sub-105006003', remove the last 3 digits
    sub_folders = [sub[:-3] for sub in sub_folders]
    df_sub_list[sess] = sub_folders

# %%
# get each col compare the columns one by one, find the different subjects by where()
def compare_elements(element1, element2):
    if element1 != element2:
        return element1
    else:
        return "None"

# %%
for i in range(len(df_sub_list.columns)):
    for j in range(i+1, len(df_sub_list.columns)):
        col1 = df_sub_list.columns[i]
        col2 = df_sub_list.columns[j]
        print('Compare ', col1, ' and ', col2)

        # compare the two columns
        print(df_sub_list.apply(lambda x: compare_elements(x[col1], x[col2]), axis=1).value_counts())

sub_list = sub_folders

# %%
"""
Based on sub_list, reformat the data
"""
# create subject folders
for sub in sub_list:
    if not os.path.exists(reformat_path + sub):
        os.makedirs(reformat_path + sub)

# %%
# create session folders in each subject folder
for sub in sub_list:
    for sess in sess_folders:
        # if the session folder does not exist, create it
        if not os.path.exists(reformat_path + sub + '/' + 'ses-' + sess):
            os.makedirs(reformat_path + sub + '/' + 'ses-' + sess)
        # create the file type folders in each session folder
        if not os.path.exists(reformat_path + sub + '/' + 'ses-' + sess + '/anat'):
            os.makedirs(reformat_path + sub + '/' + 'ses-' + sess + '/' + 'anat')
        if not os.path.exists(reformat_path + sub + '/' + 'ses-' + sess + '/func'):
            os.makedirs(reformat_path + sub + '/' + 'ses-' + sess + '/' + 'func')

# %%
"""
Move files
"""
for sess in sess_folders:
    sub_folders = get_folder_lists(save_path + sess)
    for sub in sub_folders:
        # get the list of the file types
        file_types = get_folder_lists(save_path + sess + '/' + sub)
        for f_type in file_types:
            # get the list of the files
            files = os.listdir(save_path + sess + '/' + sub + '/' + f_type)
            for file in files:
                print(file)
                # sub remove the last 3 digits
                sub_re = sub[:-3]
                # file name, remove the digits before the first '_'
                file_name = file[file.find('_'):]
                # rename the file
                re_file_name = sub_re + '_' + 'ses-' + sess + file_name
                # if the file is already in the folder, skip it
                if os.path.exists(reformat_path + sub_re + '/' + 'ses-' + sess + '/' + f_type + '/' + re_file_name):
                    print('File already exists, skip it')
                    continue
                os.rename(save_path + sess + '/' + sub + '/' + f_type + '/' + file,
                          reformat_path + sub_re + '/' + 'ses-' + sess + '/' + f_type + '/' + re_file_name)

# %%
# remove the former session folders
for sess in sess_folders:
    command = 'rm -rf ' + save_path + sess
    os.system(command)