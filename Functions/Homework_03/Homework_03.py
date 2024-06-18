# � ��� ���� ���������� ����� � ��������� �������� ������ 0 �.�.
# �� ������ ��������� ���� ������, �������� ��������� ��������, ��� ���������� ������� ���������� �������� ��������� �������:

# check_multiplicity(amount): �������� ��������� ����� ��� ���������� � ������.
# deposit(amount): ���������� �����.
# withdraw(amount): ������ �����.
# exit(): ���������� ������ � ����� �������� ���������� � ��������� ����� � ����������� ���������.

# ���������� �����:

# ������� deposit(amount) ��������� ������� ��������� ���� ���� �� ������������ �����.
# ���������� ����� �������� ������ �� �����, ������� ������ MULTIPLICITY.

# ������ �������:

# ������� withdraw(amount) ��������� ������� ������� �������� �� �����. ����� ������ ����� ������ ���� ������� MULTIPLICITY.
# ��� ������ ������� ����������� �������� � ��������� �� ��������� �����, ������� ����� ������������� �� MIN_REMOVAL �� MAX_REMOVAL.

# ���������� ������:

# ������� exit() ��������� ������ � ���������� ������. ����� �����������, ���� �� ����� ������ RICHNESS_SUM,
# ����������� ����� �� ��������� � ������� RICHNESS_PERCENT ���������.

# �������� ��������� �����:

# ������� check_multiplicity(amount) ���������, ������ �� ����� amount ��������� ��������� MULTIPLICITY.
# ���������� ��������� ��� ���������� ���������� ������, ��������� ���������� decimal ��� ������ ����������.

# ������

# �� �����:


# deposit(10000)
# withdraw(4000)
# exit()

# print(operations)
# �� ������:


#  ['���������� ����� �� 10000 �.�. ����� 10000 �.�.', '������ � ����� 4000 �.�. ������� �� ������ 60 �.�.. ����� 5940 �.�.']
# �� �����:


# deposit(1000)
# withdraw(200)
# exit()

# print(operations)
# �� ������:


#  ['���������� ����� �� 1000 �.�. ����� 1000 �.�.', '������ � ����� 200 �.�. ������� �� ������ 30 �.�.. ����� 770 �.�.', '�������� ����� �� ������� 770 �.�.']
# �� �����:


# deposit(1000)
# withdraw(200)
# withdraw(300)
# deposit(500)
# withdraw(3000)
# exit()

# print(operations)
# �� ������:


# ['���������� ����� �� 1000 �.�. ����� 1000 �.�.', '������ � ����� 200 �.�. ������� �� ������ 30 �.�.. ����� 770 �.�.', '������ � ����� 300 �.�. ������� �� ������ 30 �.�.. ����� 440 �.�.', '���������� ����� �� 500 �.�. ����� 940 �.�.', '������������ �������. ����� � ��������� 3045.000 �.�. �� ����� 940 �.�.', '�������� ����� �� ������� 940 �.�.']
# �� �����:


# deposit(173)
# withdraw(21)
# exit()

# print(operations)
# �� ������:


# ����� ������ ���� ������� 50 �.�.
# ����� ������ ���� ������� 50 �.�.
# ['������������ �������. ����� � ��������� 51 �.�. �� ����� 0 �.�.', '�������� ����� �� ������� 0 �.�.']
# �� �����:


# deposit(1000000000000000)
# withdraw(200)
# withdraw(300)
# deposit(500)
# withdraw(3000)
# exit()

# print(operations)
# �� ������:


# ['���������� ����� �� 1000000000000000 �.�. ����� 1000000000000000 �.�.', '������ � ����� 200 �.�. ������� �� ������ 30 �.�.. ����� 999999999999770 �.�.', '������ � ����� 300 �.�. ������� �� ������ 30 �.�.. ����� 999999999999440 �.�.', '���������� ����� �� 500 �.�. ����� 999999999999940 �.�.', '������ � ����� 3000 �.�. ������� �� ������ 45.000 �.�.. ����� 999999999996895.000 �.�.', '������ ����� �� ��������� 0.1% � ����� 99999999999689.5000 �.�. ����� 899999999997205.5000 �.�.', '�������� ����� �� ������� 899999999997205.5000 �.�.']


import decimal

MULTIPLICITY = 50#����. ��������� ����� ��� ���������� � ������
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)#������� ��� ������ ��������
MIN_REMOVAL = decimal.Decimal(30)#����������� ����� �������� �� ������ ��������
MAX_REMOVAL = decimal.Decimal(600)#������������ ����� �������� �� ������ ��������
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)#������ ��������
COUNTER4PERCENTAGES = 3#������� ���������
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)#����� �� ���������
RICHNESS_SUM = decimal.Decimal(10_000_000)#��������� ����� ������ �� ���������

bank_account = decimal.Decimal(0)#
count = 0#
operations = []#


# �������� ��������� ����� ��� ���������� � ������
def check_multiplicity(amount):
    if isinstance(amount, decimal.Decimal):
        return decimal.Decimal(str(amount)) % decimal.Decimal(str(MULTIPLICITY)) == decimal.Decimal(0)
    else:
        return False

# ���������� �����
def deposit(amount):
    response=""
    if check_multiplicity(amount):
        bank_account+=decimal.Decimal(decimal.Decimal(str(amount)))
        response=f"���������� ����� �� {amount} �.�. ����� {bank_account} �.�."
    else:
        response=f"����� ������ ���� ������� {MULTIPLICITY} �.�"
    operations.append(response)
    print(response)

# ������ �����.
def withdraw(amount):
    response=""
    if check_multiplicity(amount):
        removal_percent=decimal.Decimal(str(amount))*decimal.Decimal(str(PERCENT_REMOVAL))
        if decimal.Decimal(str(removal_percent))<MIN_REMOVAL:
            removal_percent=MIN_REMOVAL
        elif decimal.Decimal(str(amount))>MAX_REMOVAL:
            removal_percent=MAX_REMOVAL
        removal_summ=decimal.Decimal(str(amount))+removal_percent
        temp=bank_account-removal_summ
        if temp>=decimal.Decimal(0):
            bank_account=temp
            response =f"������ � ����� {amount} �.�. ������� �� ������ {removal_percent} �.�.. ����� {bank_account} �.�."
        else:
            response=f"������������ �������. ����� � ��������� {removal_summ} �.�. �� ����� {bank_account} �.�."
            
    else:
        response=f"����� ������ ���� ������� {MULTIPLICITY} �.�"
    operations.append(response)
    print(response)

# ���������� ������ � ����� �������� ���������� � ��������� ����� � ����������� ���������.
def exit():
    