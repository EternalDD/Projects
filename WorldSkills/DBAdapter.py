import sqlite3
import lib

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class DBAdapter():
    def __init__(self):
        self.creation()

    '''
    creation - создание таблиц
    '''

    def creation(self):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        try:
            cursor.execute(lib.CreateTablePublicUsers)
            cursor.execute(lib.CreateTablePrivateUsers)
            cursor.execute(lib.CreateTablePublicVotes)
            cursor.execute(lib.CreateTablePrivateVotes)
            cursor.execute(lib.CreateTableVotes)
            cursor.execute(lib.CreateTableBlocks)
            cursor.execute(lib.CreateTableConfTrans)
            cursor.execute(lib.CreateTableUnconfTrans)
            cursor.execute(lib.CreateTableAddresses)
            conn.commit()
            cursor.close()
            conn.close()
            return print(lib.Message)
        except sqlite3.OperationalError as error:
            return error

    '''
    AddUserToPublicUser - добавить пользователя в таблицу пользователей для открытых голосований
    '''

    def AddUserToPublicUsers(self, PublicKey, FIO, Role, IsIk):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO PublicUsers (PublicKey, FIO, Role, IsIk) VALUES(?,?,?,?)", (PublicKey, FIO, Role, IsIk))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    AddUserToPrivateUsers - добавить пользователя в таблицу пользователей для тайных голосований
    '''

    def AddUserToPrivateUsers(self, PublicKey, Role, IsIk):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO PrivateUsers (PublicKey, Role, IsIk) VALUES (?,?,?)", (PublicKey, Role, IsIk))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    DeleteUser - удалить пользователя из таблиц пользователей
    '''

    def DeleteUser(self, PublicKey):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM PublicUsers WHERE PublicKey = ?", (PublicKey,))
        cursor.execute("DELETE FROM PrivateUsers WHERE PublicKey = ?", (PublicKey,))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    DeleteUnconfTrans - удалить неподтверждённую транзакцию из таблицы неподтверждённых транзакций
    '''

    def DeleteUnconfTrans(self, ID):
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute("DELETE FROM UnconfTrans WHERE ID = ?", (ID,))
        rows = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    AddPublicVote - добавить данные об открытом голосовании в таблицу открытых голосований
    '''

    def AddPublicVote(self, Author, VotingUser, Start, During):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO PublicVotes(Author, VotingUser, Start, During) VALUES(?,?,?,?)", (Author, VotingUser, Start, During))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    AddResultToPublicVotes - добавить результат открытого голосования в таблицу открытых голосований
    '''

    def AddResultToPublicVotes(self, ID, Result):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("UPDATE PublicVotes SET Result = ? WHERE ID = ?", (Result, ID))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    AddPrivateVote - добавить данные о тайном голосовании в таблицу тайных голосований
    '''

    def AddPrivateVote(self, Content, VotingUser, Start, During):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO PrivateVotes (Content, VotingUser, Start, During) VALUES (?,?,?,?)", (Content, VotingUser, Start, During))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    AddResultToPrivateVotes - добавить результат тайного голосования в таблицу тайных голосований
    '''

    def AddResultToPrivateVotes(self, ID, Result):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("UPDATE PrivateVotes SET Result = ? WHERE ID = ?", (Result, ID))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    AddVote - добавить голос в таблицу голосов
    '''

    def AddVote(self, PublicKey, Type, VoteID, Vote):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Votes (PublicKey, Type, VoteID, Vote) VALUES (?,?,?,?)", (PublicKey, Type, VoteID, Vote))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    EditRole - изменить роль в таблицах пользователей
    '''

    def EditRole(self, PublicKey, Role):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("UPDATE PublicUsers SET Role = ? WHERE PublicKey = ?", (Role, PublicKey))
        cursor.execute("UPDATE PrivateUsers SET Role = ? WHERE PublicKey = ?", (Role, PublicKey))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    EditIsIk - изменить параметр присутствия в избирательном комитете в таблицах пользователей
    '''

    def EditIsIk(self, PublicKey, IsIk):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("UPDATE PublicUsers SET IsIk = ? WHERE PublicKey = ?", (IsIk, PublicKey))
        cursor.execute("UPDATE PrivateUsers SET IsIk = ? WHERE PublicKey = ?", (IsIk, PublicKey))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    EditUser - изменить данные о пользователе в таблице пользователей
    '''

    def EditUser(self, PublicKey, FIO):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("UPDATE PublicUsers SET FIO = ? WHERE PublicKey = ?", (FIO, PublicKey))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    AddBlock - добавить блок в таблицу блоков
    '''

    def AddBlock(self, PrevBlockHash, Hash, Timestamp, Nonce, PublicKey, Signature):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Blocks (PrevBlockHash, Hash, Timestamp, Nonce, PublicKey, Signature) VALUES (?,?,?,?,?,?)", (PrevBlockHash, Hash, Timestamp, Nonce, PublicKey, Signature))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    AddConfTrans - добавить подтверждённую транзакцию в таблицу подтверждённых транзакций
    '''

    def AddConfTrans(self, IDBlock, Type, Data, PublicKey, Signature):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ConfTrans (IDBlock, Type, Data, PublicKey, Signature) VALUES (?,?,?,?,?)", (IDBlock, Type, Data, PublicKey, Signature))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    AddUnconfTrans - добавить неподтверждённую транзакцию в таблицу неподтверждённых транзакций
    '''

    def AddUnconfTrans(self, Type, Data, PublicKey, Signature):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO UnconfTrans (Type, Data, PublicKey, Signature) VALUES (?,?,?,?)", (Type, Data, PublicKey, Signature))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    '''
    GetCountOfUnconfTrans - получить количество неподтверждённых транзакций из таблицы неподтверждённых транзакций
    '''

    def GetCountOfUnconfTrans(self):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM UnconfTrans")
        rows = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return rows

    '''
    GetUnconfTransList - получить список неподтверждённых транзакций из таблицы неподтверждённых транзакций
    '''

    def GetUnconfTransList(self):
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM UnconfTrans")
        rows = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return rows

    '''
    GetLastBlock - получить последний блок из таблицы блоков
    '''

    def GetLastBlock(self):
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Blocks order by ID desc limit 1")
        rows = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return rows

    '''
    GetBlockByHash - получить блок по заданному хэшу из таблицы блоков
    '''

    def GetBlockByHash(self, Hash):
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Blocks WHERE Hash = ?", (Hash,))
        rows = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return rows

    '''
    GetHash - получить список хэшей из таблицы блоков
    '''

    def GetHashList(self):
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT Hash FROM Blocks")
        rows = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return rows

    '''
    GetUserByPublicKey - получить данные о пользователе по открытому ключу из таблицы пользователей
    '''

    def GetUserByPublicKey(self, PublicKey):
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PublicUsers WHERE PublicKey = ?", (PublicKey,))
        rows = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return rows

    '''
    GetPublicVotesList - получить список открытых голосов из таблицы открытых голосов
    '''

    def GetPublicVotesList(self):
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PublicVotes")
        rows = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return rows

    '''
    GetPrivateVotesList - получить список тайных голосов из таблицы тайных голосов
    '''

    def GetPrivateVotesList(self):
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PrivateVotes")
        rows = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return rows

    '''
    GetPublicVoteByID - получить информацию об открытом голосе по ID из таблицы открытых голосов
    '''

    def GetPublicVoteByID(self, ID):
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PublicVotes WHERE ID = ?", (ID,))
        rows = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return rows

    '''
    GetPrivateVoteByID - получить информацию о тайном голосе по ID из таблицы тайных голосов
    '''

    def GetPrivateVoteByID(self,ID):
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PrivateVotes WHERE ID = ?", (ID,))
        rows = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return rows

    '''
    UpRole - Повысить роль пользователя в таблице пользователей
    '''

    def UpRole(self, PublicKey):
        Student = ('Student',)
        Aspirant = ('Aspirant',)
        PPSnotUSU = ('PPSnotUSU',)
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT Role FROM PublicUsers WHERE PublicKey = ?", (PublicKey,))
        rows = cursor.fetchone()
        if (rows == Student):
            cursor.execute("UPDATE PublicUsers SET Role = 'Aspirant' WHERE PublicKey = ?", (PublicKey,))
            cursor.execute("UPDATE PrivateUsers SET Role = 'Aspirant' WHERE PublicKey = ?", (PublicKey,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        if (rows == Aspirant):
            cursor.execute("UPDATE PublicUsers SET Role = 'PPSnotUSU' WHERE PublicKey = ?", (PublicKey,))
            cursor.execute("UPDATE PrivateUsers SET Role = 'PPSnotUSU' WHERE PublicKey = ?", (PublicKey,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        if (rows == PPSnotUSU):
            cursor.execute("UPDATE PublicUsers SET Role = 'PPSUSU' WHERE PublicKey = ?", (PublicKey,))
            cursor.execute("UPDATE PrivateUsers SET Role = 'PPSUSU' WHERE PublicKey = ?", (PublicKey,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        else:
            conn.commit()
            cursor.close()
            conn.close()
            return False

    '''
    DownRole - понизить роль пользователя в таблице пользователей
    '''

    def DownRole(self, PublicKey):
        PPSUSU = ('PPSUSU',)
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT Role FROM PublicUsers WHERE PublicKey = ?", (PublicKey,))
        rows = cursor.fetchone()
        if (rows == PPSUSU):
            cursor.execute("UPDATE PublicUsers SET Role = 'PPSnotUSU' WHERE PublicKey = ?", (PublicKey,))
            cursor.execute("UPDATE PrivateUsers SET Role = 'PPSnotUSU' WHERE PublicKey = ?", (PublicKey,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        else:
            conn.commit()
            cursor.close()
            conn.close()
            return False



Exe = DBAdapter()
#Exe.AddUserToPublicUsers("123123", "User", "Student", "1")