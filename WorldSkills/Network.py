import json
import sqlite3
import socket
import lib

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Network():

    def __init__(self, blockchain):
        self.blockchain = blockchain

    '''
    SendMessage - отправить сообщение пользователю по сетевому адресу
    '''

    def SendMessage(self, type, data, address):
        dict = {
            'type': type,
            'data': data
        }
        BytesData = json.dumps(dict)
        sock = socket.socket()
        try:
            sock.connect((address, 9090))
            sock.send(BytesData.encode())
            sock.close()
        except:
            sock.close()
            pass

    '''
    SendMessageAll - отправить сообщение всем адресам в базе данных
    '''

    def SendMessageAll(self, data, type):
        addresses = self.GetNetwork()
        for addr in addresses:
            self.SendMessage(data, type, addr[0])

    '''
    ReceiveMessage - получить сообщение
    '''

    def ReceiveMessage(self):
        while True:
            sock = socket.socket()
            sock.bind(('', 9090))
            sock.listen(10)
            while True:
                conn, addr = sock.accept()
                self.AddAddress(addr[0])
                data = conn.recv(16388)
                #print(data)
                dict = json.loads(data)
                self.ParserAndRunQuery(dict)

    '''
    ParserAndRunQuery - парсинг, анализ и работа с сообщениями
    '''

    def ParserAndRunQuery(self, dictionary):
        type = dictionary.get('type')
        data = dictionary.get('data')
        if (type == lib.TypeNetQuery.get('transaction')):
            self.blockchain.AddTransactFromNet(data)
            return
        if (type == lib.TypeNetQuery.get('block')):
            self.blockchain.AddBlockFromNet(data)
            return

    '''
    GetNetwork - получить все адреса из таблицы адресов
    '''

    def GetNetwork(self):
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT Address FROM Addresses")
        rows = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return rows

    '''
    AddAddress - добавить адрес в таблицу адресов
    '''

    def AddAddress(self, Address):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Addresses (Address) VALUES (?)", (Address,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
