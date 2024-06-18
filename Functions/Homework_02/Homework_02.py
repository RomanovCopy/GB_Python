# �������� ������� key_params, ����������� �� ���� ������ �������� ��������� � ������������ �������, 
# ��� ���� - �������� ����������� ���������, � �������� - ��� ���������.
# ���� ���� �� ��������, ����������� ��� ��������� �������������.

# ������ �������������.
# �� �����:

# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)

# �� ������:

# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

def key_params(**kargs):
    my_dict={}
    for key, value in kargs.items():
        if not isinstance(value, (int, float, str, tuple, frozenset, type(None))):
            value=str(value)
        my_dict[value]=key
    return my_dict

print( key_params(a = None, b = '', c = [], d = {}))


