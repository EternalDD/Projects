Message = "Done"

UsersColumns = {
    'PublicKey': 0,
    'FIO': 1,
    'Role': 2,
    'IsIk': 3
}

EventsColumns = {
    'idEvent': 0,
    'creator': 1,
    'name': 2,
    'date': 3,
    'competence': 4,
    'rating': 5,
    'data': 6,
    'numOfExperts': 7,
    'idExpertGroup': 8,
    'idUsersGroup': 9,
    'version': 10,
    'currentUpdateIndex': 11,
    'timestamp': 12
}

GroupColumns = {
    'idGroup': 0,
    'address': 1,
    'usersGroup': 2,
    'typeGroup': 3
}

RequestColumns = {
    'idRequest': 0,
    'addressFrom': 1,
    'addressTo': 2,
    'idConfirmExpertGroups': 3,
    'typeRequest': 4,
    'quantityAccepted': 5,
    'date': 6
}

EventsUpdateColumns = {
    'idUnconfirmedUpdate': 0,
    'idEvent': 1,
    'name': 2,
    'data': 3,
    'date': 4,
    'competence': 5,
    'numOfExperts': 6,
    'idExpertsGroup': 7,
    'idUsersGroup': 8,
    'updateIndex': 9,
    'timestamp': 10,
    'idConfirmExpertGroup': 11,
    'version': 12
}

UncTransaction = {
    'ID': 0,
    'Type': 1,
    'Data': 2,
    'PublicKey': 3,
    'Signature': 4
}

Transaction = {
    'ID': 0,
    'IDBlock': 1,
    'Type': 2,
    'Data': 3,
    'PublicKey': 4,
    'Signature': 5
}

BlockColumns = {
    'ID': 0,
    'PrevBlockHash': 1,
    'Hash': 2,
    'Timestamp': 3,
    'Nonce': 4,
    'PublicKey': 5,
    'Signature': 6
}

TypeNetQuery = {
    'transaction': 1,
    'block': 2,
    'length': 3,
    'fullChain': 4,
    'isEqChain': 5,
    'eqChain': 51,
    'notEqChain': 52,
    'addUser': 6,
    'error': 7,
    'SendHashChain': 8,
    'SendBlockList': 9,
    'ShowNet': 10,
}

'''
CreateTablePublicUsers - создание таблицы пользователей для открытых голосований с полями:
PublicKey(Открытый ключ), FIO(ФИО пользователя), Role(Роль пользователя),
IsIk(Параметр присутствия в избирательном комитете)
'''

CreateTablePublicUsers = '''
CREATE TABLE PublicUsers (
PublicKey VARCHAR PRIMARY KEY NOT NULL,
FIO VARCHAR,
Role VARCHAR,
IsIk INTEGER
)
'''

'''
CreateTablePrivateUsers - создание таблицы пользователей для тайных голосований с полями:
PublicKey(Открытый ключ), Role(Роль пользователя) и IsIk(Параметр присутствия в избирательном комитете)
'''

CreateTablePrivateUsers = '''
CREATE TABLE PrivateUsers (
PublicKey VARCHAR PRIMARY KEY NOT NULL,
Role VARCHAR,
IsIk INTEGER
)
'''

'''
CreateTablePublicVotes - создание таблицы для открытых голосований с полями:
ID, Author(Создатель голосования), VotingUser(Голосующий пользователь), Start(Время начала), During(Длительность
голосования), Result(Результат голосования)
'''

CreateTablePublicVotes = '''
CREATE TABLE PublicVotes (
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Author VARCHAR,
VotingUser VARCHAR,
Start INTEGER,
During INTEGER,
Result VARCHAR
)
'''

'''
CreateTablePrivateVotes - создание таблицы для тайных голосований с полями:
ID, Content(Содержимое голосования), VotingUser(Голосующий пользователь), Start(Время начала), During(Длительность
голосования), Result(Результат голосования)
'''

CreateTablePrivateVotes = '''
CREATE TABLE PrivateVotes (
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Content VARCHAR,
VotingUser VARCHAR,
Start INTEGER,
During INTEGER,
Result VARCHAR
)
'''

'''
CreateTableBlocks - создание таблицы блоков с полями:
ID, PrevBlockHash(Хэш предыдущего блока), Hash(Хэш), Timestamp(Время создания), Nonce(Число для механзма PoW),
PublicKey(Открытый ключ), Signature(Подпись)
'''

CreateTableBlocks = '''
CREATE TABLE Blocks (
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
PrevBlockHash VARCHAR,
Hash VARCHAR,
Timestamp INTEGER,
Nonce VARCHAR,
PublicKey VARCHAR,
Signature VARCHAR
)
'''

'''
CreateTableVotes - создание таблицы голосов с полями:
PublicKey(Открытый ключ), Type(Тип голосования), VoteID(ID голосования), Vote(Выбор, решение)
'''

CreateTableVotes = '''
CREATE TABLE Votes (
PublicKey VARCHAR,
Type VARCHAR,
VoteID INTEGER,
Vote VARCHAR
)
'''

'''
CreateTableConfTrans - создание таблицы подтверждённых транзакций с полями:
ID, IDBlock(ID блока), Type(Тип транзакции), Data(Данные), PublicKey(Открытый ключ), Signature(Подпись)
'''

CreateTableConfTrans = '''
CREATE TABLE ConfTrans (
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
IDBlock VARCHAR,
Type VARCHAR,
Data VARCHAR,
PublicKey VARCHAR,
Signature VARCHAR
)
'''

'''
CreateTableUnconfTrans - создание таблицы неподтверждённых транзакций с полями:
ID, Type(Тип транзакции), Data(Данные), PublicKey(Открытый ключ), Signature(Подпись)
'''

CreateTableUnconfTrans = '''
CREATE TABLE UnconfTrans (
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Type VARCHAR,
Data VARCHAR,
PublicKey VARCHAR,
Signature VARCHAR
)
'''

'''
CreateTableAddresses - Создание таблицы IP-адресов с полями:
ID, Address(IP-адрес)
'''

CreateTableAddresses = '''
CREATE TABLE Addresses (
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Address VARCHAR
)
'''