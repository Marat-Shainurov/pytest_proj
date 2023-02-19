
def get_val(collection, key, default="git"):

    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default.
    """

    if collection.get(key) != None:
        return collection[key]
    else:
        return default
