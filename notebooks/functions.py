import os
def download_dataset():
    '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
    this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
    Takes: url from kaggle
    Returns: a folder with the downloaded csv
    '''
    
    #Gets the name of the dataset.zip
    url = input("Introduce la url: ")
    
    #Gets the name of the dataset.zip
    endopint = url.split("/")[-1]
    user = url.split("/")[-2]
    
    #Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {user}/{endopint}; say -v Monica 'descargando'"
    decompress = f"tar -xzvf {endopint}.zip; say -v Monica 'descomprimiendo'"
    delete = f"rm -rf {endopint}.zip; say -v Monica 'borrando el zip'"
    make_directory = "mkdir data"
    lista = "ls >> archivos.txt"
    
    for i in [download, decompress, delete, make_directory, lista]:
        os.system(i)
    
    #Gets the name of the csv (you should only have one csv when running this code)
    lista_archivos = open('archivos.txt').read()
    nueva = lista_archivos.split("\n")
    
    #Moves the .csv into the data directory
    for i in nueva:
        if i.endswith(".csv"):
            move_and_delete = f"mv {i} data/dataset.csv; rm archivos.txt; say -v Monica 'moviendo el dataset'"
            return os.system(move_and_delete)





#### Elimina las columnas con las que no vamos a trabajar
def drop_columns(tag):
    '''
    Delete columns that you don't need
    receives a dataset and returns a clean one
    '''
    tag = tag.drop(['Type 1', 'Type 2', 'Stage', 'Legendary'], axis=1)
    return tag


#### Cambia el nombre y la posicion del indice
def change_index(tag):
    tag=tag.rename(columns= {' ': 'indice'})
    tag.set_index('indice' )
    return tag

#
def is_pokemon_tag(tag):
    """
    Decides whether an Amazon div tag corresponds to a book or to other useless information
    Args:
        tag (bs4.element.Tag)
    Returns:
        bool: True if book
    """
    list_of_spans = tag.find_all("a", class_="ent-name")
    
    if len(list_of_spans) == 1:
        return True
    else:
        return False
#####
def get_pokemon_name(pokemon_tag):
    """
    Extracts book name
    Args:
        book_tag (bs4.element.Tag): corresponding to an Amazon book
    Returns:
        str: book title
    """
    pokemon_name_tag = pokemon_tag.find("a", class_="ent-name")
    pokemon_name = pokemon_name_tag.text
    
    return pokemon_name


def pokemon_type_tag(tag):
    """
    Decides whether an Amazon div tag corresponds to a book or to other useless information
    Args:
        tag (bs4.element.Tag)
    Returns:
        bool: True if book
    """
    list_types_spans = tag.find("a", class_="type-icon")
    
    if len(list_types_spans) == 1:
        return True
    else:
        return False


def get_pokemon_types(pokemon_tag):
    
    pokemon_types_tag = pokemon_tag.find_all("td", class_="cell-icon")
    pokemon_types = pokemon_tag.text
    
    return pokemon_types

def pokemon_stats2_tag(tag):
    """
    Decides whether an Amazon div tag corresponds to a book or to other useless information
    Args:
        tag (bs4.element.Tag)
    Returns:
        bool: True if book
    """
    list_stats_spans = tag.find("td", class_="cell-num")
    
    
    if list_stats_spans  != 0:
        return True
    else:
        return False

def get_pokemon_stats2(pokemon_tag):
    
    pokemon_stats_tag = pokemon_tag.find("td", class_="cell-num")
    pokemon_stats = pokemon_tag.text
    
    return pokemon_stats

def pokemon_stats_tag(tag):
    """
    Decides whether an Amazon div tag corresponds to a book or to other useless information
    Args:
        tag (bs4.element.Tag)
    Returns:
        bool: True if book
    """
    list_total_stats_spans = tag.find("td", class_="cell-total")
    list_stats_spans = tag.find("td", class_="cell-num")
    
    if list_stats_spans != 0:
        return True
    else:
        return False
    

def get_pokemon_stats(pokemon_tag):
    
    pokemon_stats_tag = pokemon_tag.find_all("td", class_="cell-total")
    pokemon_stats = pokemon_tag.text
    
    return pokemon_stats