
def main():
    
    #reads the book
    def get_book_text(path):
        with open(path) as f:
            return f.read()
        
    #counts the words
    def word_counter(text):
        print (f"The number of words: {len(text.split())}")

    """ gets the number of letter by input
        def letter_counter(text):
        counter = 0
        letter = input("Please enter a letter: ")
        for i in text:
            if letter.lower() == i.lower():
                counter += 1

        print(f"{letter}: {counter}") """
    
    #creates a dictionary of letters found
    def letter_counter_dict(text):
        lettersDict = {
               
            }
        for i in text.lower():
            if i.isalpha():
                if i in lettersDict:
                    lettersDict[i] += 1
                else:
                    lettersDict[i] = 1
        #lettersTuple = lettersDict.items()
        return lettersDict
    
    #sorts dictionary by max count of words
    def sort_max(dict):
        tuples = dict.items()
        sorted_tuples = sorted(tuples, key=lambda item: item[1], reverse=True)
        return sorted_tuples 

    #======================================#    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    word_counter(text)
    #print(letter_counter_dict(text))
    for letter, count in (sort_max(letter_counter_dict(text))):
        print(f"The letter {letter} was found {count} times!")

main()