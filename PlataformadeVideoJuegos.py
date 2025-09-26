
#Aplicando las reglas a la tabla: 
#user01 (Combate, Victoria) → Acción exitosa 
#user02 (Exploración, Descubrimiento) → Acción exitosa 
#user03 (Interacción social, Mensaje enviado) → Acción colaborativa 
#user04 (Combate, Derrota) → Acción fallida 
#user05 (Exploración, Sin hallazgos) → Acción neutral 

import pandas as pd 

# Datos simulados 

data = { 
    "Usuario": ["user01", "user02", "user03", "user04", "user05"], 
    "Accion": ["Combate", "Exploracion", "Interaccion social", "Combate", "Exploracion"], 
    "Duracion": [120, 300, 180, 90, 240], 
    "Resultado": ["Victoria", "Descubrimiento", "Mensaje enviado", "Derrota", "Sin hallazgos"] 
} 

df = pd.DataFrame(data) 

def clasificar_accion(accion, duracion, resultado):
    if accion == "Combate":
        if resultado == "Victoria":
            return "Acción exitosa"
        else:
            return "Acción fallida"
    elif accion == "Exploración":
        if resultado == "Descubrimiento":
            return "Acción exitosa"
        else:
            return "Acción neutral"
    elif accion == "Interacción social":
        return "Acción colaborativa"
    else:
        return "Acción desconocida"


# Clasificación 

df["Clasificacion"] = df.apply(lambda row: clasificar_accion(row["Accion"], row["Duracion"], row["Resultado"]), axis=1) 


print(df) 


