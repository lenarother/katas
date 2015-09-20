def prompt_quote():
    quote = input('What is the quore? ')
    author = input('Who is the author? ')
    return quote, author

def print_single_quote(quote, author):
    print(author + ' says, ' + '\'' + quote + '\'')

if __name__ == '__main__':
    quote, author = prompt_quote()
    print_single_quote(quote, author)
