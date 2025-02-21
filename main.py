def get_book_content(book_path) :
    with open(book_path) as book:
        book_content = book.read()
        return book_content

def count_book_words(book_content) :
    words = book_content.split()
    return len(words)
    
def count_book_character_occurence(book_content) :
    character_occurences = {}
    book_content_santized = book_content.lower()
    for character in book_content_santized :
        if character in character_occurences :
            character_occurences[character] += 1
        else :
            character_occurences[character] = 1
    return character_occurences

def sort_filter_character_occurence(character_occurences) :
    character_dictionaries = []
    for character_occurence in character_occurences :
        character_dictionaries.append({"character" : character_occurence, "count" : character_occurences[character_occurence]})
    filtered_dictionaries = filter_alphabet(character_dictionaries)
    filtered_dictionaries.sort(reverse=True, key=sort_count)
    return filtered_dictionaries

def generate_book_report(book_path) :
    book_content = get_book_content(book_path)
    word_count = count_book_words(book_content)
    character_occurences = count_book_character_occurence(book_content)
    character_dictionaries = sort_filter_character_occurence(character_occurences)
    book_report = ""

    book_report += f"--- Begin report of {book_path} ---\n"
    book_report += f"{word_count} words found in the document\n\n"
    
    for character_dictionary in character_dictionaries :
        character = character_dictionary["character"]
        count = character_dictionary["count"]
        book_report += f"The '{character}' character was found {count} times\n"
    book_report += "--- End report ---"
    return book_report

def main() :
    book_report = generate_book_report("books/frankenstein.txt")
    print(book_report)

def sort_count(dictionary) :
    return dictionary["count"]

def filter_alphabet(dictionaries) :
    alpha_dictionaries = []
    for dictionary in dictionaries :
        if dictionary["character"].isalpha() :
            alpha_dictionaries.append(dictionary)
    return alpha_dictionaries

main()