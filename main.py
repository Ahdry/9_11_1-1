import inspect


def introspection_info(obj):
    # Определение типа объекта
    obj_type = type(obj).__name__

    # Получение атрибутов объекта
    attributes = dir(obj)

    # Получение методов объекта
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    # Получение модуля, к которому принадлежит объект
    module = getattr(obj, '__module__', None)

    # Создание словаря с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    # Дополнительные свойства (по желанию)
    if obj_type == 'list':
        info['length'] = len(obj)
    elif obj_type == 'dict':
        info['length'] = len(obj)
        info['keys'] = list(obj.keys())

    return info


# Пример использования
number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("Hello, world!")
print(string_info)

list_info = introspection_info([1, 2, 3])
print(list_info)

dict_info = introspection_info({'a': 1, 'b': 2})
print(dict_info)

