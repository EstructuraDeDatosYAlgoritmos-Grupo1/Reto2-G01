﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'videos': None,
               'videoIds': None,
               'categoryIds': None,
               'countries' : None,
               'likes' : None,
               'views' : None}
    catalog["videos"] = lt.newList('SINGLE_LINKED', cmpVideoIds)

    catalog["videoIds"]=mp.newMap(185650, maptype='CHAINING',loadfactor=2.0,comparefunction=cmpMapVideoIds)

    catalog["categoryIds"]= mp.newMap(67, maptype='PROBING',loadfactor=0.5,comparefunction=cmpCategoryIds)

    catalog["countries"]=mp.newMap(241, maptype='PROBING',loadfactor=0.5,comparefunction=cmpMapCountries)

    catalog["likes"]=mp.newMap(185650, maptype='CHAINING', loadfactor= 2.0 comparefunction=cmpMapLikes)

    catalog["views"]=mp.newMap(185650, maptype='CHAINING', loadfactor= 2.0 comparefunction=cmpMapViews)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog["videos"], video)
    mp.put(catalog["videoIds"], video["video_id"], video)
    if mp.contains(catalog["likes"], video["likes"])
        
    mp.put(catalog["likes"], video["likes"], video)


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideoIds(id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def cmpMapVideoIds(id, entry):
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def cmpCategoryIds(id, catid):
    catentry = me.getKey(catid)
    if (int(id) == int(catentry)):
        return 0
    elif (int(id) > int(catentry)):
        return 1
    else:
        return 0

def cmpMapCountries(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0

def cmpMapLikes(likes, entry):
    likesentry = me.getKey(entry)
    if (int(likes) == int(likesentry)):
        return 0
    elif (int(likes) > int(likesentry)):
        return 1
    else:
        return -1

def cmpMapViews(views, entry):
    viewsentry = me.getKey(entry)
    if (int(views) == int(viewsentry)):
        return 0
    elif (int(views) > int(viewsentry)):
        return 1
    else:
        return -1

# Funciones de ordenamiento
