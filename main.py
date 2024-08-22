def main():
    path_to_file = "./books/frankenstein.txt"

    text = get_text_from_file(path_to_file)
    total_words = get_word_count(text)
    symbols_count = get_symbol_count(text)

    print(f"There were {total_words} words found in the text.")
    print_report(path_to_file, total_words, symbols_count)
        

def get_word_count(text:str):
    return len(text.split())


def get_symbol_count(text:str):
    symbols = {}

    for symbol in text:
        symbols[symbol.lower()] = symbols.setdefault(symbol.lower(), 0) + 1
    
    return symbols


def get_text_from_file(path_to_text:str):
    with open(path_to_text) as f:
        return f.read()


def print_report(path_to_file:str, word_count:int, symbols:dict):
    print(f"--- Begin report of {path_to_file} ---")

    for key, item in sorted(symbols.items(), reverse=True, key=lambda x: x[1]):
        if key.isalpha():
            print(f"The '{key}' character was found {item} times")

    print("--- End report ---")


main()