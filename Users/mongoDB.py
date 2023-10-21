from pymongo import MongoClient

def encrypt(inputText, N, D):
    encryptedText = ""
    if D == +1 or -1:
        if N < 1:
            return
        database = inputText
        textFlip = database[::-1]
        for L in textFlip:
            newChar = ord(L)
            if ord(L) != 32 and ord(L) != 33:
                if D == +1:
                    if (newChar + N) > 126:
                        newChar = newChar + N - 93
                    if newChar != 32 and newChar != 33:
                        newChar = newChar + N
                else:
                    if (newChar - N) > 126:
                        newChar = newChar - N - 93
                    if newChar != 32 and newChar != 33:
                        newChar = newChar - N
            encryptedText = encryptedText + chr(newChar)
    else:
        return
    return encryptedText

def addNewUser(userid, password):
    Client = client = MongoClient(
        "mongodb+srv://HackTx:hackywacky@cluster0.s0vmfmm.mongodb.net/?retryWrites=true&w=majority")
    db = client.Users
    collection_name =  db["reesewelty"]
    user = {
        "userid": userid,
        "password": encrypt(password, 3, 1)
    }
    collection_name.insert_one(user)
    client.close()

def collectionMaker():
    client = MongoClient(
        "mongodb+srv://HackTx:hackywacky@cluster0.s0vmfmm.mongodb.net/?retryWrites=true&w=majority")
    db = client.Projects
    collection_name = db["Project1"]
    user = {
        "Name": "P1",
        "ID": "as1234",
        "Description": "This is the first project"
    }
    collection_name.insert_one(user)
    client.close()

if __name__ == '__main__':
    queryHWSet1Availability()
    addNewUser("Reese", "1234")