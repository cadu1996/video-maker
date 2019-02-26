def start():
    content = {'searchTerm': askAndReturnSearchTerm(),
               'prefix': askAndReturnPrefix()}

    print(content)


def askAndReturnSearchTerm():
    return input('Type a Wikipedia search term: ')

def askAndReturnPrefix():
    prefixes = ['CANCEL','Who is', 'What is', 'The history of']
    selectedPrefixIndex = int(input('[1] Whos is\n'
                     '[2] What is\n'
                     '[3] The history of\n'
                     '[0] CANCEL\n'
                     '\n'
                     'Choose one option [1, 2, 3, 0]: '))

    selectedPrefixText = prefixes[selectedPrefixIndex]

    return selectedPrefixText

start()
