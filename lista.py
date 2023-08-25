from fastapi import FastAPI #Importar FastAPI

app = FastAPI() #app variable como instancia de la clase FastAPI


#Ruta para obtener la lista de celulares

@app.get("/obtener-celular") #Definimos el decorador de operacion de ruta

async def obtener_celular(): #Definimos funcion de operacion

    return celulares #Devolver contenido

#obtener toda la lista de marcas que hay
@app.get("/obtener-marcas")
async def obtener_marcas():
    lista = []
    for i in celulares:
        lista.append(i["marca"])
    return lista

#obtener toda la lista de modelos que hay
@app.get("/obtener-modelos")
async def obtener_modelos():
    lista = []
    for i in celulares:
        lista.append(i["modelo"])
    return lista

#obtener todos los procesadores que hay en la lista
@app.get("/obtener-procesador")
async def obtener_procesador():
    lista = []
    for i in celulares:
        lista.append(i["procesador"])
    return lista


#Ruta para obtener un celular por su ID

@app.get("/obtener-celular/{item_id}")

async def obtener_celular(item_id: int):

    for item in celulares:

        if item["id"] == item_id:

            return item

    return {"mensaje": "Item no encontrado"}

 
#Ruta para obtener celulares por marca

@app.get("/obtener-celular-por-marca/{marca}")

async def obtener_celular_por_marca(marca: str):

    celular_por_marca = [item for item in celulares if item["marca"].lower() == marca.lower()]

    if celular_por_marca:

        return celular_por_marca

    return {"mensaje": "No se encontraron celulares para la marca especificada"}

#Ruta para obtener celulares por modelo
@app.get("/obtener-celular-por-modelo/{modelo}")

async def obtener_celular_por_modelo(modelo: str):

    celular_por_modelo = [item for item in celulares if item["modelo"].lower() == modelo.lower()]

    if celular_por_modelo:

        return celular_por_modelo

    return {"mensaje": "No se encontraron celulares para el modelo especificado"}

#Ruta para obtener por procesador
@app.get("/obtener-celular-por-procesador/{procesador}")

async def obtener_celular_por_procesador(procesador: str):

    celular_por_procesador = [item for item in celulares if item["procesador"].lower() == procesador.lower()]

    if celular_por_procesador:

        return celular_por_procesador




#obtener los primeros diez elementos de "celulares"
@app.get("/primeros10")
async def obtener_10elementos():
    lista = []
    contador = 1
    for celular in celulares:
        if contador <= 10:
            lista.append(celular)
            contador += 1
    return lista

#obtener los ultimos diez elementos de "celulares"
@app.get("/intermedios10")
async def obtener_intermedios10():
    lista = []
    contador = 1
    for celular in celulares:
        if contador >= 180 and contador <= 190:
            lista.append(celular)
        contador += 1        
    return lista  

# uvicorn lista:app --reload       para levantar servidor api


 
#Diccionario de items con 3 caracteristicas

celulares = [
    
    {"id": 1, "marca": "Samsung", "modelo": "Galaxy A34", "procesador": "Octa-core"}, 

    {"id": 2, "marca": "Motorola", "modelo": "Edge 20 Lite", "procesador": "MediaTek Dimensity 720"}, 

    {"id": 3, "marca": "Xiaomi", "modelo": "Redmi Note 12", "procesador": "Qualcomm SM4375 Snapdragon"}, 

    {"id": 4, "marca": "Apple", "modelo": "14 Pro Max", "procesador": "Apple A16 Bionic"}, 

    {"id": 5, "marca": "Samsung", "modelo": "S23 Ultra", "procesador": "Qualcomm Snapdragon SM8550"}, 

    {"id": 6, "marca": "Samsung", "modelo": "Galaxy S10e", "procesador": "Qualcomm Snapdragon 855"}, 

    {"id": 7, "marca": "Motorola", "modelo": "Moto G42", "procesador": "8 núcleos"}, 

    {"id": 8, "marca": "Xiaomi", "modelo": "Redmi Note 12S", "procesador": "MediaTek Helio G96"}, 

    {"id": 9, "marca": "Apple", "modelo": "11", "procesador": "Apple A13"}, 

    {"id": 10, "marca": "Samsung", "modelo": "Galaxy Z Flip 4", "procesador": "Octa-core"}, 

    {"id": 11, "marca": "Xiaomi", "modelo": "Redmi A2", "procesador": "MediaTek Helio G35"}, 

    {"id": 12, "marca": "Hisense", "modelo": "Hisense E20", "procesador": "8 núcleos"}, 

    {"id": 13, "marca": "Huawei", "modelo": "Mate 50 Pro", "procesador": "Snapdragon 865+"}, 

    {"id": 14, "marca": "Nokia", "modelo": "C20", "procesador": "8 núcleos"}, 

    {"id": 15, "marca": "Apple", "modelo": "XS", "procesador": "Apple A12"}, 

    {"id": 16, "marca": "Samsung", "modelo": "Galaxy A04E", "procesador": "MediaTek Helio P35"}, 

    {"id": 17, "marca": "Motorola", "modelo": "Moto G82 5G", "procesador": "8 núcleos"}, 

    {"id": 18, "marca": "Huawei", "modelo": "Nova Y61", "procesador": "Huawei kirin 710f octa-core"}, 

    {"id": 19, "marca": "Huawei", "modelo": "Nova 11i", "procesador": "Huawei kirin 710f octa-core"}, 

    {"id": 20, "marca": "Xiaomi", "modelo": "Redmi A1", "procesador": "8 núcleos"}, 

    {"id": 21, "marca": "Samsung", "modelo": "Galaxy S21+", "procesador": "8 núcleos"}, 

    {"id": 22, "marca": "Motorola", "modelo": "g52", "procesador": "Octa-Core Qualcomm"}, 

    {"id": 23, "marca": "Samsung", "modelo": "Galaxy A14", "procesador": "Exynos 1200"}, 

    {"id": 24, "marca": "Xiaomi", "modelo": "Poco X5", "procesador": "Snapdragon 695"}, 

    {"id": 25, "marca": "Apple", "modelo": "iPhone 13", "procesador": "Chip a15 bionic"}, 

    {"id": 26, "marca": "Samsung", "modelo": "Galaxy A53 5G", "procesador": "Samsung Exynos 1280"}, 

    {"id": 27, "marca": "Apple", "modelo": "iPhone 12", "procesador": "A14 Bionic"}, 

    {"id": 28, "marca": "Huawei", "modelo": "P60 Pro", "procesador": "Qualcomm snapdragon 8+ gen1"}, 

    {"id": 29, "marca": "Xiaomi", "modelo": "Redmi Note 11", "procesador": "Qualcomm Sanpdragon 680 Octacore"}, 

    {"id": 30, "marca": "Motorola", "modelo": "Moto G41", "procesador": "Mediatek Helio G85"}, 

    {"id": 31, "marca": "Xiaomi", "modelo": "Redmi A2", "procesador": "MediaTek Helio G37"}, 

    {"id": 32, "marca": "Apple", "modelo": "XR", "procesador": "Apple A12"}, 

    {"id": 33, "marca": "Samsung", "modelo": "Galaxy A53", "procesador": "Octacore"}, 

    {"id": 34, "marca": "Samsung", "modelo": "Galaxy S22 Ultra", "procesador": "Dynamic AMOLED 2X"}, 

    {"id": 35, "marca": "Motorola", "modelo": "Moto G60", "procesador": "Apple A12"}, 

    {"id": 36, "marca": "Motorola", "modelo": "Moto G31", "procesador": "MediaTek Helio G85"}, 

    {"id": 37, "marca": "Apple", "modelo": "iPhone X", "procesador": "iOS"}, 

    {"id": 38, "marca": "Apple", "modelo": "iPhone 13 Pro Max", "procesador": "Apple A14"}, 

    {"id": 39, "marca": "Honor", "modelo": "X7A", "procesador": "MediaTek Helio G37"}, 

    {"id": 40, "marca": "Samsung", "modelo": "Galaxy A33", "procesador": "Exynos 1280"}, 

    {"id": 41, "marca": "Honor", "modelo": "Honor X6", "procesador": "Mediatek helio"}, 

    {"id": 42, "marca": "Honor", "modelo": "Honor X8A", "procesador": "8 núcleos"}, 

    {"id": 43, "marca": "Apple", "modelo": "iPhone 12 Pro", "procesador": "iOS"}, 

    {"id": 44, "marca": "Motorola", "modelo": "Motorola G13", "procesador": "8 núcleos"}, 

    {"id": 45, "marca": "Xiaomi", "modelo": "Redmi 9A", "procesador": "MediaTek Helio G25"}, 

    {"id": 46, "marca": "Xiaomi", "modelo": "Redmi Note 10S", "procesador": "MediaTek Helio G95"}, 

    {"id": 47, "marca": "Motorola", "modelo": "Moto e13", "procesador": "8 núcleos"}, 

    {"id": 48, "marca": "Xiaomi", "modelo": "Redmi Note 11S", "procesador": "MediaTek Helio G96"}, 

    {"id": 49, "marca": "Samsung", "modelo": "Galaxy S22 Ultra 5G", "procesador": "Samsung Exynos 2200"}, 

    {"id": 50, "marca": "Motorola", "modelo": "Moto G41", "procesador": "Helio G85"}, 

    {"id": 51, "marca": "Xiaomi", "modelo": "Xiaomi Redmi K50 Gaming", "procesador": "Snapdragon 8"}, 

    {"id": 52, "marca": "Apple", "modelo": "iPhone 11 Pro", "procesador": "Apple A13"}, 
    
    {"id": 53, "marca": "Samsung", "modelo": "Galaxy A03 Core", "procesador": "Unisoc SC9863A"}, 

    {"id": 54, "marca": "Xiaomi", "modelo": "Redimi 9T", "procesador": "Octa Core"}, 

    {"id": 55, "marca": "Samsung", "modelo": "Galaxy A03 Core", "procesador": "Unisoc SC9863A"}, 

    {"id": 56, "marca": "Xiaomi", "modelo": "Redmi Note 11S", "procesador": "Octa Core"}, 

    {"id": 57, "marca": "Xiaomi", "modelo": "Redmi A2", "procesador": "Octa Core"}, 

    {"id": 58, "marca": "Huawei", "modelo": "Nova 11l", "procesador": "Octa Core"}, 

    {"id": 59, "marca": "Oppo", "modelo": "Reno 7", "procesador": "Octa Core"}, 

    {"id": 60, "marca": "Motorola", "modelo": "Moto G13", "procesador": "Octa Core"}, 

    {"id": 61, "marca": "Huawei", "modelo": "Y7A", "procesador": "Octa Core"}, 

    {"id": 62, "marca": "Honor", "modelo": "9x", "procesador": "Octa Core"}, 

    {"id": 63, "marca": "OnePlus", "modelo": "N10", "procesador": "Octa Core"}, 

    {"id": 64, "marca": "Motorola", "modelo": "G72", "procesador": "Octa Core"}, 

    {"id": 65, "marca": "Oppo", "modelo": "A77", "procesador": "Octa Core"}, 

    {"id": 66, "marca": "Honor", "modelo": "X7A", "procesador": "Octa Core"}, 

    {"id": 67, "marca": "Huawei", "modelo": "Nova 10 SE", "procesador": "Octa Core"}, 

    {"id": 68, "marca": "Zuum", "modelo": "Magno C2", "procesador": "Quad Core"}, 

    {"id": 69, "marca": "Huawei", "modelo": "Y9 2018", "procesador": "Octa Core"}, 

    {"id": 70, "marca": "Huawei", "modelo": "Y8s", "procesador": "HiSilicon Kirin"}, 

    {"id": 71, "marca": "Huawei", "modelo": "P30 Lite Dual", "procesador": "Kirin 710 Octa core"}, 

    {"id": 72, "marca": "Samsung", "modelo": "M12", "procesador": "Exynos 850"}, 

    {"id": 73, "marca": "Samsung", "modelo": "Galaxy A04", "procesador": "Unisoc SC9863A Octa core"}, 

    {"id": 74, "marca": "Samsung", "modelo": "Galaxy S22 Ultra", "procesador": "Exynos 2200 a 2,8GHz"}, 

    {"id": 75, "marca": "Samsung", "modelo": "Galaxy A13", "procesador": "Exynos 850"}, 

    {"id": 76, "marca": "Samsung", "modelo": "Galaxy S22 Ultra", "procesador": "Dynamic AMOLED 2X"}, 

    {"id": 77, "marca": "Samsung", "modelo": "Galaxy A03s", "procesador": "Qualcomm, SDM450"}, 

    {"id": 78, "marca": "Samsung", "modelo": "Galaxy A33", "procesador": "Exynos 1280"}, 

    {"id": 79, "marca": "Samsung", "modelo": "Galaxy A22", "procesador": "MediaTek MT6769T (Helio G80) Octa Core"},
    
    {"id": 80, "marca": "Samsung", "modelo": "Galaxy Z Flip4", "procesador": "Snapdragon 8 + Gen 1 (4nm)"}, 

    {"id": 81, "marca": "Motorola", "modelo": "G50", "procesador": "Snapdragon 662"}, 

    {"id": 82, "marca": "Motorola", "modelo": "Edge 30 Neo", "procesador": "Qualcomm SD3675"}, 

    {"id": 83, "marca": "Motorola", "modelo": "Moto E7 PLUS", "procesador": "Snapdragon 460"}, 

    {"id": 84, "marca": "Motorola", "modelo": "Edge 30", "procesador": "Qualcomm Snapdragon"}, 

    {"id": 85, "marca": "Motorola", "modelo": "G42", "procesador": "Qualcomm Snapdragon 680 ocho núcleos"}, 

    {"id": 86, "marca": "Xiaomi", "modelo": "Redmi A1", "procesador": "Mediatek MT6761/4 CUADCORE"}, 

    {"id": 87, "marca": "Samsung", "modelo": "Galaxy A04E", "procesador": "Exynos 1280"}, 

    {"id": 88, "marca": "Motorola", "modelo": "G42", "procesador": "Snapdragon 680"}, 

    {"id": 89, "marca": "ZTE", "modelo": "Blade L9", "procesador": "Quad Core"}, 

    {"id": 90, "marca": "Zuum", "modelo": "Magno C2", "procesador": "Quad Core"}, 

    {"id": 91, "marca": "Motorola", "modelo": "E20", "procesador": "Octa Core"}, 

    {"id": 92, "marca": "Zuum", "modelo": "Rocket III", "procesador": "Quad Core"}, 

    {"id": 93, "marca": "Bmobile", "modelo": "AX751", "procesador": "Quad Core"}, 

    {"id": 94, "marca": "Lanix", "modelo": "X1", "procesador": "Quad Core"}, 

    {"id": 95, "marca": "Zuum", "modelo": "Stellar M4", "procesador": "Octa Core"}, 

    {"id": 96, "marca": "Zuum", "modelo": "Akus P1", "procesador": "Octa Core de 1.5 GHz"}, 

    {"id": 97, "marca": "Bmobile", "modelo": "AX751", "procesador": "Quad Core"}, 

    {"id": 98, "marca": "ZTE", "modelo": "Blade A31", "procesador": "Octa Core"}, 

    {"id": 99, "marca": "Zuum", "modelo": "Hidra X", "procesador": "Octa Core"}, 

    {"id": 100, "marca": "ZTE", "modelo": "Blade V40 Smart", "procesador": "Octa Core"},
    
    {"id": 101, "marca": "Samsung", "modelo": "Galaxy A54 5G", "procesador": "Samsung exynos 1280"},
    
    {"id": 102, "marca": "Apple", "modelo": "13 Mini", "procesador": "Chip a15 bionic"},
    
    {"id": 103, "marca": "Apple", "modelo": "iPhone 14 Pro", "procesador": "Apple A16 Bionic"},
    
    {"id": 104, "marca": "Samsung", "modelo": "S23 Ultra", "procesador": "Qualcomm Snapdragon SM8550"},
    
    {"id": 105, "marca": "Samsung", "modelo": "Galaxy Z Flip5", "procesador": "Qualcomm Snapdragon SM8550"},
    
    {"id": 106, "marca": "Hisense", "modelo": "Hisemse E50", "procesador": "Spreadtrum Unisoc SC9832E"}, 
    
    {"id": 107, "marca": "Motorola", "modelo": "Edge 30 Pro o Edge+", "procesador": "Snapdragon 8 Gen 1"}, 

    {"id": 108, "marca": "OnePlus", "modelo": "10 Pro", "procesador": "Snapdragon 8 Gen 1"}, 

    {"id": 109, "marca": "Realme", "modelo": "GT 2 Pro", "procesador": "Snapdragon 8 Gen 1"}, 

    {"id": 110, "marca": "Honor", "modelo": "Magic V", "procesador": "Snapdragon 8 Gen 1"}, 

    {"id": 111, "marca": "Samsung", "modelo": "Galaxy Z Fold 3", "procesador": "Qualcomm Snapdragon SM8550"}, 
    
    {"id": 112, "marca": "Samsung", "modelo": "Galaxy S22 Ultra", "procesador": "Snapdragon 8 Gen 1"}, 

    {"id": 113, "marca": "Motorola", "modelo": "Moto G42", "procesador": "Snapdragon 8 Gen 1"}, 

    {"id": 114, "marca": "Honor", "modelo": "Magic 4", "procesador": "Snapdragon 8 Gen 1"}, 

    {"id": 115, "marca": "Oppo", "modelo": "Find X5 Pro", "procesador": "Snapdragon 8 Gen 1"}, 

    {"id": 116, "marca": "Samsung", "modelo": "Galaxy Note", "procesador": "Octa Core"}, 

    {"id": 117, "marca": "Samsung", "modelo": "Galaxy A32 5G", "procesador": "MediaTek Dimensity 720"}, 

    {"id": 118, "marca": "Nokia", "modelo": "2.4", "procesador": "MediaTek Helio P22"}, 

    {"id": 119, "marca": "Xiaomi", "modelo": "13 Pro", "procesador": "Qualcomm Snapdragon 8 Gen 2"}, 

    {"id": 120, "marca": "OnePlus", "modelo": "11", "procesador": "Qualcomm Snapdragon 8 Gen 2"}, 

    {"id": 121, "marca": "Samsung", "modelo": "Galaxy S23 Ultra", "procesador": "Qualcomm Snapdragon 8 Gen 2"}, 

    {"id": 122, "marca": "Apple", "modelo": "iPhone 14 Pro", "procesador": "Apple A16 Bionic"}, 

    {"id": 123, "marca": "Apple", "modelo": "iPhone 14 Pro Max", "procesador": "Apple A16 Bionic"}, 

    {"id": 124, "marca": "Samsung", "modelo": "Galaxy S22 Ultra", "procesador": "Exynos 2200"}, 

    {"id": 125, "marca": "Samsung", "modelo": "Galaxy S22", "procesador": "Exynos 2200"}, 

    {"id": 126, "marca": "Xiaomi", "modelo": "Redmi A1", "procesador": "8 núcleos"}, 

    {"id": 127, "marca": "Google", "modelo": "Pixel 7", "procesador": "Tensor G2"}, 

    {"id": 128, "marca": "Google", "modelo": "Pixel 7 Pro", "procesador": "Tensor G2"}, 

    {"id": 129, "marca": "Huawei", "modelo": "Mate 40", "procesador": "HiSilicon Kirin 9000"}, 

    {"id": 130, "marca": "Huawei", "modelo": "Mate 40 Pro", "procesador": "HiSilicon Kirin 9000"}, 

    {"id": 131, "marca": "Vivo", "modelo": "X80 Pro 5G", "procesador": "MediaTek Dimensity 9000"}, 

    {"id": 132, "marca": "Honor", "modelo": "70 Pro", "procesador": "MediaTek Dimensity 9000"}, 

    {"id": 133, "marca": "Honor", "modelo": "70 Pro+", "procesador": "MediaTek Dimensity 9000"}, 

    {"id": 134, "marca": "Xiaomi", "modelo": "Redmi K50 Pro", "procesador": "MediaTek Dimensity 9000"}, 

    {"id": 135, "marca": "Apple", "modelo": "iPhone 14", "procesador": "Apple A14"}, 

    {"id": 136, "marca": "Apple", "modelo": "iPhone 14 Plus", "procesador": "Apple A14"}, 

    {"id": 137, "marca": "Apple", "modelo": "iPhone 14 Pro", "procesador": "Apple A14"}, 

    {"id": 138, "marca": "Apple", "modelo": "iPhone 14 Pro Max", "procesador": "Apple A14"}, 

    {"id": 139, "marca": "Samsung", "modelo": "Galaxy S23 Ultra", "procesador": "Octacore"}, 

    {"id": 140, "marca": "Xiaomi", "modelo": "13 Pro", "procesador": "Dynamic AMOLED 2X"}, 

    {"id": 141, "marca": "OnePlus", "modelo": "11", "procesador": "Apple A12"}, 

    {"id": 142, "marca": "Google", "modelo": "Pixel 7 Pro", "procesador": "MediaTek Helio G85"}, 

    {"id": 143, "marca": "Apple", "modelo": "iPhone X", "procesador": "iOS"}, 

    {"id": 144, "marca": "Apple", "modelo": "iPhone 13 Pro Max", "procesador": "Apple A14"}, 

    {"id": 145, "marca": "Honor", "modelo": "X7A", "procesador": "MediaTek Helio G37"}, 

    {"id": 146, "marca": "Samsung", "modelo": "Galaxy S", "procesador": "Exynos"}, 

    {"id": 147, "marca": "Samsung", "modelo": "Galaxy SII", "procesador": "SoC Exynos 4210"}, 

    {"id": 148, "marca": "Samsung", "modelo": "Galaxy Note 20", "procesador": "Exynos 990"}, 

    {"id": 149, "marca": "Apple", "modelo": "iPhone 12 Pro", "procesador": "iOS"}, 

    {"id": 150, "marca": "Motorola", "modelo": "Moto G100", "procesador": "Snapdragon 870"}, 

    {"id": 151, "marca": "Xiaomi", "modelo": "Redmi Note 10 Pro", "procesador": "Snapdragon 732G"}, 

    {"id": 152, "marca": "Samsung", "modelo": "Galaxy S20 FE", "procesador": "Snapdragon 865"}, 
    
    {"id": 153, "marca": "Vivo", "modelo": "V20", "procesador": "Snapdragon 720G"}, 

    {"id": 154, "marca": "Xiaomi", "modelo": "Redmi 9A", "procesador": "MediaTek Helio G25"}, 

    {"id": 155, "marca": "Xiaomi", "modelo": "Redmi Note 10S", "procesador": "MediaTek Helio G95"},

    {"id": 156, "marca": "Motorola", "modelo": "Moto e13", "procesador": "8 núcleos"}, 

    {"id": 157, "marca": "Xiaomi", "modelo": "Redmi Note 11S", "procesador": "MediaTek Helio G96"}, 

    {"id": 158, "marca": "Samsung", "modelo": "Galaxy S22 Ultra 5G", "procesador": "Samsung Exynos 2200"}, 

    {"id": 159, "marca": "Motorola", "modelo": "Moto G41", "procesador": "Helio G85"}, 

    {"id": 160, "marca": "Xiaomi", "modelo": "Xiaomi Redmi K50 Gaming", "procesador": "Snapdragon 8"}, 

    {"id": 161, "marca": "Apple", "modelo": "iPhone 11 Pro", "procesador": "Apple A13"}, 
    
    {"id": 162, "marca": "Samsung", "modelo": "Galaxy A03 Core", "procesador": "Unisoc SC9863A"}, 

    {"id": 163, "marca": "Xiaomi", "modelo": "Redimi 9T", "procesador": "Octa Core"}, 

    {"id": 164, "marca": "Samsung", "modelo": "Galaxy A03 Core", "procesador": "Unisoc SC9863A"}, 

    {"id": 165, "marca": "Xiaomi", "modelo": "Redmi Note 11S", "procesador": "Octa Core"}, 

    {"id": 166, "marca": "Xiaomi", "modelo": "Redmi A2", "procesador": "Octa Core"}, 

    {"id": 167, "marca": "Huawei", "modelo": "Nova 11l", "procesador": "Octa Core"}, 

    {"id": 168, "marca": "Honor", "modelo": "90 Lite", "procesador": "Octa Core"}, 

    {"id": 169, "marca": "itel", "modelo": "Vision 2S", "procesador": "Octa Core"}, 

    {"id": 170, "marca": "itel", "modelo": "Vision 3 Turbo", "procesador": "Octa Core"}, 

    {"id": 171, "marca": "itel", "modelo": "A23S", "procesador": "Quad-core 1.4 GHz"}, 

    {"id": 172, "marca": "OnePlus", "modelo": "N10", "procesador": "Octa Core"}, 

    {"id": 173, "marca": "Motorola", "modelo": "G72", "procesador": "Octa Core"}, 

    {"id": 174, "marca": "Oppo", "modelo": "A54", "procesador": "Octa Core"}, 

    {"id": 175, "marca": "Honor", "modelo": "X7A", "procesador": "Octa Core"}, 

    {"id": 176, "marca": "Motorola", "modelo": "G41", "procesador": "Octa Core"}, 

    {"id": 177, "marca": "Vivo", "modelo": "Y100", "procesador": "Mediatek MT6877"}, 
    
    {"id": 178, "marca": "Asus", "modelo": "ROG Phone 7 Ultimate", "procesador": "Octa Core"}, 

    {"id": 179, "marca": "Google", "modelo": "Pixel 6a", "procesador": "8 núcleos"}, 

    {"id": 180, "marca": "Huawei", "modelo": "P30 Lite Dual", "procesador": "Kirin 710 Octa core"}, 

    {"id": 181, "marca": "Huawei", "modelo": "Nova 10 Pro", "procesador": "Qualcomm snapdragon 778g"}, 

    {"id": 182, "marca": "Samsung", "modelo": "Galaxy A04", "procesador": "Unisoc SC9863A Octa core"}, 

    {"id": 183, "marca": "Samsung", "modelo": "Galaxy S22 Ultra", "procesador": "Exynos 2200 a 2,8GHz"}, 

    {"id": 184, "marca": "Motorola", "modelo": "Moto G60S", "procesador": "8 núcleos"}, 

    {"id": 185, "marca": "Samsung", "modelo": "Galaxy S22 Ultra", "procesador": "Dynamic AMOLED 2X"}, 

    {"id": 186, "marca": "Honor", "modelo": "X5", "procesador": "Octa Core"}, 

    {"id": 187, "marca": "Samsung", "modelo": "Galaxy A33", "procesador": "Exynos 1280"}, 

    {"id": 188, "marca": "Oppo", "modelo": "Reno 6 5G", "procesador": "MediaTek Dimensity 900"},
    
    {"id": 189, "marca": "Samsung", "modelo": "Galaxy Z Flip4", "procesador": "Snapdragon 8 + Gen 1 (4nm)"}, 

    {"id": 190, "marca": "Motorola", "modelo": "G50", "procesador": "Snapdragon 662"}, 

    {"id": 191, "marca": "Xiaomi", "modelo": "11T Pro", "procesador": "Snapdragon 888"}, 

    {"id": 192, "marca": "Apple", "modelo": "iPhone 11 Pro Max", "procesador": "A13 Bionic"}, 

    {"id": 193, "marca": "Apple", "modelo": "iPhone 11", "procesador": "A13 Bionic"}, 

    {"id": 194, "marca": "Apple", "modelo": "iPhone 11 Pro", "procesador": "A13 Bionic"}, 

    {"id": 195, "marca": "Samsung", "modelo": "Galaxy S21+", "procesador": "Exynos 2100"}, 

    {"id": 196, "marca": "Samsung", "modelo": " Galaxy S21", "procesador": "Exynos 2100"}, 

    {"id": 197, "marca": "Samsung", "modelo": " Galaxy S21 Ultra", "procesador": "Exynos 2100"}, 

    {"id": 198, "marca": "Apple", "modelo": "iPhone 13", "procesador": "A15 Bionic"}, 

    {"id": 199, "marca": "Apple", "modelo": "iPhone 13 mini", "procesador": "A15 Bionic"}, 

    {"id": 200, "marca": "Apple", "modelo": "iPhone 13 Pro Max", "procesador": "A15 Bionic"}

]

 