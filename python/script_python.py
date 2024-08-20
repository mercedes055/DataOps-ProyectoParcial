import os

######Carpeta dataset#####
location="C:/Users/Mercedes/OneDrive/Documentos/CERTUS/3_OPS/proyecto_parcial/dataset"

#######Validar si existe la carpeta ########
if not os.path.exists(location):## si no existe
    #creo carpeta
    os.mkdir(location)
else:## si existe carpeta
    ##borramos contenido
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name))#eliminar archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name))# eliminar carpetas


#####descargar dataset###
from kaggle.api.kaggle_api_extended import KaggleApi

### Autenticarnos###
api=KaggleApi()
api.authenticate()

print(api.dataset_list(search=''))

api.dataset_download_files('youssefismail20/olympic-games-1994-2024',path=location, force=True, quiet=False, unzip=True)







