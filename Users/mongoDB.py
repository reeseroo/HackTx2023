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
            return 2

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
        "Password": "test"
    }
    collection_name.insert_one(user)
    client.close()

def characterFind(userid):
    client = MongoClient("mongodb+srv://HackTx:hackywacky@cluster0.s0vmfmm.mongodb.net/?retryWrites=true&w=majority")
    db = client.Users
    collection_name = db.users
    user = collection_name.find_one({"userid": userid})

    if user:
        characters = user.get("characters", [])
        char_names = [character["character"] for character in characters]
        return char_names[0]

    client.close()

def characterAdd(userid, char):
    client = MongoClient(
        "mongodb+srv://HackTx:hackywacky@cluster0.s0vmfmm.mongodb.net/?retryWrites=true&w=majority")
    db = client.Users
    collection_name =  db.users
    user = collection_name.find_one({"userid": userid})
    if user:
        new_character = {
            "character": char,
            "Health": 200,
            "Wealth": 500
        }
        collection_name.update_one({"userid": userid}, {"$push": {"characters": new_character}})
    client.close()

def updateCharacter(userid, char_name, new_health, new_wealth):
    client = MongoClient("mongodb+srv://HackTx:hackywacky@cluster0.s0vmfmm.mongodb.net/?retryWrites=true&w=majority")
    db = client.Users
    collection_name = db.users
    user = collection_name.find_one({"userid": userid})

    if user:
        existing_characters = user.get("characters", [])
        updated_character = None

        # Find the character with the specified name and update its fields
        for character in existing_characters:
            if character.get("character") == char_name:
                character["Health"] = new_health
                character["Wealth"] = new_wealth
                updated_character = character
                break

        # If the character was not found, create a new character object
        if updated_character is None:
            updated_character = {
                "character": char_name,
                "Health": new_health,
                "Wealth": new_wealth
            }

        # Update the characters array
        collection_name.update_one({"userid": userid}, {"$set": {"characters": existing_characters}})

    client.close()

def getCharacterWealth(userid, char_name):
    client = MongoClient("mongodb+srv://HackTx:hackywacky@cluster0.s0vmfmm.mongodb.net/?retryWrites=true&w=majority")
    db = client.Users
    collection_name = db.users
    user = collection_name.find_one({"userid": userid})

    if user:
        characters = user.get("characters", [])
        for character in characters:
            if character["character"] == char_name:
                return character["Wealth"]

    client.close()

def getCharacterHealth(userid, char_name):
    client = MongoClient("mongodb+srv://HackTx:hackywacky@cluster0.s0vmfmm.mongodb.net/?retryWrites=true&w=majority")
    db = client.Users
    collection_name = db.users
    user = collection_name.find_one({"userid": userid})

    if user:
        characters = user.get("characters", [])
        for character in characters:
            if character["character"] == char_name:
                return character["Health"]

    client.close()



if __name__ == '__main__':
    print(userFind("Jenna", "123"))
    print(characterFind("Jenna"))
    print(getCharacterWealth("Jenna", "Subuwu"))
