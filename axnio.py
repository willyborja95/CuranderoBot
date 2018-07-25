import lib.consultarDb as cdb
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
    return strRespuestaInd + strRespuesta

def conversacion(m):

    with io.open("training.json") as f:
        sample_dataset = json.load(f)

    load_resources("en")
    nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
    nlu_engine.fit(sample_dataset)

    text = (u""+m.text.lower()+"")
    listaResultado = nlu_engine.parse(text)
    return procesarRespuesta(listaResultado)
    
def procesarRespuesta(data):
    #print(json.dumps(data, indent=2))
    print(data["intent"])
    if data["intent"] is not None:
        intent=data["intent"]["intentName"]
        print(intent)
        if intent=="Saludo":
            return ("Hola, yo tengo información acerca de plantas medicinales\n"+consultarTodasPlantas())

        if intent=="ListarPlantas":
            return consultarTodasPlantas()
        
        if intent=="ListarBeneficiosSalud":
            return consultarTodosBeneficiosSalud()

        if intent=="ConsultarBeneficiosPlanta":
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
        return strRespuestaInd + strRespuesta
    else:
        return "Lo siento, aún no tengo registrada esa planta"

def consultarTodasPlantas():
    lstRespuesta = c.consultaTodasPlantas()
    strRespuesta = ""
    strRespuestaInd = "Las plantas de las que puedes consultarme son:\n"
    for respuesta in lstRespuesta:
        strRespuesta = strRespuesta + " - "+respuesta + "\n"
    return strRespuestaInd + strRespuesta

def consultarTodosBeneficiosSalud():
    print("holas")
    lstRespuesta = c.consultaTodosBeneficios()
    strRespuesta = ""
    strRespuestaInd = "Las beneficios registrados son:\n"
    for respuesta in lstRespuesta:
        strRespuesta = strRespuesta + " - "+respuesta + "\n"
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
