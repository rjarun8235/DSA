class Node():
    def __init__(self,data=None):
        self.data = data 
        self.next = None

class HashTableChaining:
    def __init__(self):
        self.SIZE = 7
        self.chain = [None] * self.SIZE

    def insert(self,value):
        key = value % self.SIZE
        newNode = Node(value)

        if self.chain[key] == None:
            self.chain[key] = newNode
            
        else:
            temp = self.chain[key]

            while temp.next != None:
                temp = temp.next

            temp.next = newNode
        return True
        

    def print(self):
        for i in range(self.SIZE):
            temp = self.chain[i]

            while temp != None:
                print(temp.data,end=" ")
                temp = temp.next

            print("None", end=" ")

    def search(self,value):
        key = value % self.SIZE

        temp = self.chain[key]
        while temp != None:
            if temp.data == value:
                return 1
            temp = temp.next

        return 0

    def delete(self,value):
        key = value % self.SIZE
        temp = self.chain[key]

        while temp != None:
            if temp.data == value:
                temp = temp.next
                self.chain[key] = temp
                return 1
            else:
                while temp.next != None:
                    if temp.next.data == value:
                        temp.next = temp.next.next
                        return 1
                    else:
                        temp = temp.next

            return 0

if __name__ == "__main__":
    obj = HashTableChaining()
    
    obj.insert(7)
    obj.insert(0)
    obj.insert(3)
    obj.insert(10)
    obj.insert(4)
    obj.insert(5)
    
    obj.print()
    
    if obj.search(10) == 1:
        print("Search Found")
    else: 
        print("Search Not Found")
        
    key = 10
    if obj.delete(key) == 1: 
        print("Deleted Node: " + str(key))
        obj.print()
    else:
        print(key + " Not Found");




