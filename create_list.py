import sys
import os

def define_path(rel_path):
    script_dir = os.path.dirname(__file__) 
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path

#cria lista bruta
def create_raw_list(path, content):
    file = open(path+'raw_list', 'w')
    file.write(content)
    file.close()

def get_user_name(name):
    if ('https://www.instagram.com/' in name):
        user_name = name[26:].rstrip('/')
    else:
        user_name = name
    return user_name

def create_new_file(path, name):
    file = open(path+name, 'w+')
    return file

def create_clean_list(path, user_url):
    raw = open(path+'raw_list', 'r+')
    raw_lines = raw.readlines()

    file_name = get_user_name(user_url)
    clean_list = create_new_file(path, file_name)
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
    path = define_path('bases/seguidores/')

    create_clean_list(path,nome_arquivo)