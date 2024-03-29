from stack import stack_obj

def main():
    s = stack_obj()
    s.push(1)
    s.push(2)
    s.push(3)
    print("size of the stack :" , s.size())
    print("the top element :", s.peek())
    print("Is stack empty ? ", s.is_empty())
    print("Pop the top element : ",s.pop())
    s.clear()

if __name__ == "__main__":
    main()