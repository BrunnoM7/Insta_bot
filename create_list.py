import sys

def get_user_name(name):
    if ('https://www.instagram.com/' in name):
        user_name = name[26:].rstrip('/')
    else:
        user_name = name
    return user_name

def create_new_file(name):
    file = open(name, 'w+')
    return file

def create_clean_list(user_url):
    raw = open('raw_list', 'r+')
    raw_lines = raw.readlines()

    file_name = get_user_name(user_url)
    clean_list = create_new_file(file_name)
    phrase = "Foto do perfil de "
    phrase2 = "'s profile picture"


    for line in raw_lines:
        if(phrase in line):
            clean_list.write(line[len(phrase):])
        if(phrase2 in line):
            clean_list.write(f'{line[0:len(line)-len(phrase)-1]}\n')


    clean_list.close()
    raw.close()

    return file_name

if __name__ == "__main__":
    
    nome_arquivo = get_user_name(sys.argv[1])

    create_clean_list(nome_arquivo)