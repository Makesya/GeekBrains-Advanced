def get_file_info(file_path):
    """Принимает путь к файлу и возвращает информацию о нем
    :param path: путь к файлу
    :return: информация о файле
    """
    if file_path.split("/").__len__() < 2:
        fullpath = ""
    else:
        fullpath = "/".join(file_path.split("/")[0:-1])+"/"
    filename = file_path.split("/")[-1]
    name = ".".join(filename.split(".")[0:-1])
    extension = filename.split(".")[-1]
    extension = "." + extension
    res = (fullpath, name, extension)
    return res


print(get_file_info("C:/Users/User/Documents/example.txt"))
