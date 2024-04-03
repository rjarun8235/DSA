class hash_table:

    def __init__(self,size=5):
        self.SIZE = size
        self.arr = [-1] * self.SIZE
        print(self.arr)

    def insert(self,value):
        key = value%self.SIZE
        index = key

        while self.arr[index] != -1:
            index = (index+1) % self.SIZE

            if index == key:
                print("Hash Table is Full")
                return False
        
        self.arr[index] = value

        return True


    def delete(self,value):
        key = value%self.SIZE
        index = key

        while self.arr[index] != value:
            index = (index+1) % self.SIZE

            if index == key:
              return False
        
        self.arr[index] = -1

        return True

    def search(self,value):
        key = value%self.SIZE
        index = key

        while self.arr[index] != value:
            index = (index+1) % self.SIZE

            if index == key:
                return False

        return True


