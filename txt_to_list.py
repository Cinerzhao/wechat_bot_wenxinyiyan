#utf-8
#输入路径可以将TXT读为list列表
def white_list_reader(path):
    with open(path, 'r',encoding = "utf-8") as file_object:
        white_list = file_object.read().split('\n')
        
    return white_list
