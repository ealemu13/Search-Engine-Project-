from pathlib import Path

def collect_JSON_file_path():
    # given a folder name = DEV
    dev_folder_path = "C:/Users/qnluo/Downloads/DEV"            
    
    subdomain_path_set = set([])
    file_path_set = set([])
    
    # inside the DEV folder, there are ~88 folders, where its name is the subdomain
    # save each folder's path to subdomain_path_set
    for folder_path in Path(dev_folder_path).iterdir():
        subdomain_path_set.add(folder_path)
        print("Save subdomain", folder_path, "to the set")
    
    # inside a subdomain folder, there are JSON files
    # save each file path to file_path_set
    for subdomain_path in subdomain_path_set:
        for file_path in Path(subdomain_path).iterdir():
            file_path_set.add(file_path)
            print("Save file path", file_path, "to the set")

    print("Collecting JSON file path finished.")
    
    return file_path_set

def write_file_path_to_txt(file_path_set):
    with open("JSON_file_path.txt", 'a') as file:
        for file_path in file_path_set:
            file.write(str(file_path))
            file.write("\n")
    print("Finished writing to file.")

if __name__ == '__main__':
    file_path_set = collect_JSON_file_path()
    write_file_path_to_txt(file_path_set)