# ��� ������ ������������� ��������� lst. ������� ������ � �������������� ����������. � �������������� ������ �� ������ ���� ����������.

# ������

# �� �����:


lst = [1, 2, 3, 4, 5, 4, 2]
# �� ������:


# [1, 2, 3]

result=set()
lst.sort()
length=len(lst)
if length>0:
    for i in range(length-1):
        if lst[i]==lst[i+1]:
            result.add(lst[i])

print(list(result))