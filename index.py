def start():
    content = {'searchTerm': askAndReturnSearchTerm(),
               'prefix': askAndReturnPrefix}

    print(content)


def askAndReturnSearchTerm():
    return raw_input('Type a Wikipedia search term: ')

def askAndReturnPrefix():

start()
