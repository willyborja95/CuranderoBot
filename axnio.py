import lib.consultarDb as cdb
import lib.pText as pT
import json
import snips_nlu, json, io
from snips_nlu import load_resources, SnipsNLUEngine, SnipsNLUEngine, load_resources
from snips_nlu.default_configs import CONFIG_EN


c = cdb.consultar("http://localhost:8890/sparql")

def consultaBeneficiosPlanta(strNoun):
    lstRespuesta = c.consultaBeneficiosPlantaDb(strNoun)
    strRespuesta = ""
    strRespuestaInd = "Las propiedades curativas de la planta "+strNoun+" son:\n"
    for respuesta in lstRespuesta:
        strRespuesta = strRespuesta + " - "+respuesta + "\n"
        #r = "Hablas de "+str(str(pais["nombre"]))
    return strRespuestaInd + strRespuesta

def conversacion(m):

    with io.open("datase.json") as f:
        sample_dataset = json.load(f)

    load_resources("en")
    nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
    nlu_engine.fit(sample_dataset)

    text = (u""+m.text.lower()+"")
    listaResultado = nlu_engine.parse(text)
    return procesarRespuesta(listaResultado)
    
def procesarRespuesta(data):
    #print(json.dumps(data, indent=2))
    if data["intent"] is not None:
        intent=data["intent"]["intentName"]
        print(intent)
        if intent=="Saludo":
            return ("Hola, yo tengo información acerca de plantas medicinales\n"+consultarTodasPlantas())

        if intent=="ListarPlantas":
            slots= data["slots"]
            return consultarTodasPlantas()
        
        if intent=="listarBeneficiosSalud":
            slots= data["slots"]
            return consultarTodosBeneficiosSalud()

        if intent=="BeneficiosPlantas":
            if(len(data["slots"])>1):
                planta= data["slots"][1]["rawValue"]
                return(consultarBeneficiosPlantas(planta))
            else:
                planta= data["slots"][0]["rawValue"]
                respuesta = consultarBeneficiosPlantas(planta)
                if respuesta is None:
                    return ("No tengo registros de esa planta")
                else:
                    return(respuesta)

    else:
        return "Disculpa, aun estoy aprendiendo, me decias?"
 

def consultarBeneficiosPlantas(strPlanta):
    lstRespuesta = c.consultaBeneficiosPlantaDb(strPlanta)
    strRespuesta = ""
    strRespuestaInd = "Las propiedades curativas de la planta "+strPlanta+" son:\n"
    if (len(lstRespuesta))>0:
        for respuesta in lstRespuesta:
            strRespuesta = strRespuesta + " - "+respuesta + "\n"
            #r = "Hablas de "+str(str(pais["nombre"]))
        return strRespuestaInd + strRespuesta
    else:
        return "Lo siento, aún no tengo registrada esa planta"

def consultarTodasPlantas():
    lstRespuesta = c.consultaTodasPlantas()
    strRespuesta = ""
    strRespuestaInd = "Las plantas de las que puedes consultarme son:\n"
    for respuesta in lstRespuesta:
        strRespuesta = strRespuesta + " - "+respuesta + "\n"
        #r = "Hablas de "+str(str(pais["nombre"]))
    return strRespuestaInd + strRespuesta

def consultarTodosBeneficiosSalud():
    lstRespuesta = c.consultaTodosBeneficios()
    strRespuesta = ""
    strRespuestaInd = "Las beneficios registrados son:\n"
    for respuesta in lstRespuesta:
        strRespuesta = strRespuesta + " - "+respuesta + "\n"
        #r = "Hablas de "+str(str(pais["nombre"]))
    return strRespuestaInd + strRespuesta


def consultarPalabraCompuesta(strTexto):
    lstPalabrasCompuestas = []
    lstPalabrasCompuestas.append('antiespasmódico estomacal')
    lstPalabrasCompuestas.append('antiespasmódico estomacal')
    lstPalabrasCompuestas.append('ácido úrico')
    lstPalabrasCompuestas.append('tránsito intestinal')
    lstPalabrasCompuestas.append('desinflamante del colon')
    lstPalabrasCompuestas.append('dolor de cabeza')
    lstPalabrasCompuestas.append('desinflamante del colon')
    lstPalabrasCompuestas.append('diurético natural')

    for palabra in strTexto:
        for indexElemento in range(len(lstPalabrasCompuestas)):
            strFraseElemento = lstPalabrasCompuestas[indexElemento]
            for indexPalabraElemento in range(len(strFraseElemento[indexElemento])):
                print(strFraseElemento[indexPalabraElemento])


    """
    if len(lstNoun)>1:
        bndVentaja = False
        strNombrePlanta = ""
        for noun in lstNoun:
            if ((noun == "ventaja") or 
            (noun == "bondad") or 
            (noun == "propiedad")):
                bndVentaja = True
            strNombrePlanta = noun

        lstRespuesta = c.consultaBeneficiosPlantaDb(strNombrePlanta)
        strRespuesta = ""
        strRespuestaInd = "Las propiedades curativas de la planta "+strNombrePlanta+" son:\n"
        for respuesta in lstRespuesta:
            strRespuesta = strRespuesta + " - "+respuesta + "\n"
            #r = "Hablas de "+str(str(pais["nombre"]))
        return strRespuestaInd + strRespuesta

    
        
    elif (len(lstNoun)==1 and strVerbo!="") or (len(lstNoun)==1 and strAdj!="") or (len(lstNoun)==1 and strAdv!=""):        
        if ((strVerbo == "curar") or 
        (strVerbo == "tener" and strAdj == "curativo") or 
        (strVerbo == "quitar" ) or
        (strVerbo == "utilizar") or
        (strVerbo == "aliviar") or
        (strVerbo == "quito") or
        (strVerbo == "usar") or
        (strVerbo == "servir") or
        (strAdj == "bueno")):
            strNombrePlanta = ""
            for noun in lstNoun:
                strNombrePlanta = noun
            lstRespuesta = c.consultaBeneficiosPlantaDb(strNombrePlanta)
            strRespuesta = ""
            strRespuestaInd = "Las propiedades curativas de la planta "+strNombrePlanta+" son:\n"
            for respuesta in lstRespuesta:
                strRespuesta = strRespuesta + " - "+respuesta + "\n"
                #r = "Hablas de "+str(str(pais["nombre"]))
            return strRespuestaInd + strRespuesta

        if ((strVerbo == "listar" and lstNoun[0]=="planta" )or
        (strVerbo == "ver" and lstNoun[0]=="planta") or
        (strAdj == "dame" and lstNoun[0]=="planta") or
        (strAdv == "listame" and lstNoun[0]=="planta")):
            

    elif len(lstNoun)==1:
        if lstNoun[0]=="planta":
            return "Hola, ¿Quieres saber los beneficios que tienen las plantas medicinales? o ¿deseas saber de sus propiedades curativas?"
    else:
        return "Ups .. ¿podrías repetirmelo?"

"""

""""
    if m.text == "ecuador" or m.text == "Ecuador":

        pais = c.cPais("Ecuador")
        r = "Hablas de "+str(pais["nombre"] +
                             "\n Yo se su uri: "+str(pais["uri"]))
        return r
    if m.text == "Julio Jaramillo":
        person = c.cPersonas("Julio Jaramillo")
        if person != 0:
            r = "Hablas de "+str(person["nombre"] +
                                 "\n Yo se su uri: "+str(person["uri"]))
            return r
        else:
            return "No encuentro a la persona"
    elif m.text == "Chao":
        return "Adios"
    elif m.text == "Hola":
        return "Hola :D"
    else:
        return "No te entiendo, como te puedo ayudar"
"""