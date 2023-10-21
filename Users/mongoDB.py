from pymongo import MongoClient

def userFind(userid, password):
    client = MongoClient(
        "mongodb+srv://HackTx:hackywacky@cluster0.s0vmfmm.mongodb.net/?retryWrites=true&w=majority")
    db = client.Users
    collection_name =  db.users
    user = collection_name.find_one({"userid": userid})
    if user:
         check = encrypt(password, 3,1)
         if check == user.get("password"):
           return 1
         else:
            return 0

    client.close()



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
    collection_name =  db["users"]
    user = {
        "userid": userid,
        "password": encrypt(password, 3, 1)
    }
    collection_name.insert_one(user)
    client.close()

def collectionMaker():
    client = MongoClient(
        "mongodb+srv://HackTx:hackywacky@cluster0.s0vmfmm.mongodb.net/?retryWrites=true&w=majority")
    db = client.Users
    collection_name = db["users"]
    user = {
        "Name": "P1",
        "ID": "test",
        "Description": "This is the test user"
    }
    collection_name.insert_one(user)
    client.close()

def characterFind(userid):
    client = MongoClient(
        "mongodb+srv://HackTx:hackywacky@cluster0.s0vmfmm.mongodb.net/?retryWrites=true&w=majority")
    db = client.Users
    collection_name =  db.users
    user = collection_name.find_one({"userid": userid})
    if user:
         print(user.get("character"))
    client.close()

def characterAdd(userid, char):
    client = MongoClient(
        "mongodb+srv://HackTx:hackywacky@cluster0.s0vmfmm.mongodb.net/?retryWrites=true&w=majority")
    db = client.Users
    collection_name =  db.users
    user = collection_name.find_one({"userid": userid})
    if user:
        collection_name.update_one({"userid": userid}, {"$push":{"character": char}})
    client.close()
