from hash import hash_table as HashTable



if __name__ == "__main__":
    
    hash_table = HashTable()              
 
    # INSERT
    if(hash_table.insert(10) == 1):
        print("10 is inserted")
    if(hash_table.insert(4) == 1):
        print("4 is inserted")
    if(hash_table.insert(2) == 1):
        print("2 is inserted")
    if(hash_table.insert(15) == 1):
        print("15 is inserted")
    if(hash_table.insert(5) == 1):
        print("5 is inserted")
    
    # DELETE
    hash_table.delete(5) 
    hash_table.delete(50)
    
    # SEARCH
    if hash_table.search(4) == 1:
        print("4 - Found")
    else:
        print("4 - Not Found")
    if hash_table.search(12) == 1:
        print("12 - Found")
    else:
        print("12 - Not Found")
    