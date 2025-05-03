MAX_TERM_VALUE = 15  

def main():
    curr_term, next_term = 0, 1 
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ") 
        curr_term, next_term = next_term, curr_term + next_term

if __name__ == '__main__':
    main()
