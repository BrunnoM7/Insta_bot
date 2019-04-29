import sys

def get_user_name(url):
    user_name = url[26:].rstrip('/')
    return user_name

def create_new_file(name):
    file = open(name, 'w+')
    return file

def create_clean_list(user_url):
    raw = open('raw_list', 'r+')
    raw_lines = raw.readlines()

    file_name = get_user_name(user_url)
    clean_list = create_new_file(file_name)

    for line in raw_lines:
        if("Foto do perfil de " in line):
            clean_list.write(line[18:])

    clean_list.close()
    raw.close()

    return file_name

if __name__ == "__main__":
    
    nome_arquivo = sys.argv[1]

    create_clean_list(nome_arquivo)