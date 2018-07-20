from SPARQLWrapper import SPARQLWrapper2, JSON


class consultar:
    def __init__(self, dbC):
        # Variables de inicio
        self.sparql = SPARQLWrapper2(dbC, "http://localhost:8890/plantasmedicinales2")
    # Metodos

    def cPais(self, pais):
        r = ""
        self.sparql.setQuery("""
            SELECT ?pais, ?nombre WHERE{
            ?pais rdfs:label ?nombre .
            FILTER (?nombre =\""""+pais+"""\"@es) .
            } ORDER BY ?nombre
        """)
        dic = {}
        for result in self.sparql.query().bindings:
            dic = {'nombre': result["nombre"].value, 'uri': result["pais"].value}
        if len(dic) != 0:
            return dic
        else:
            # print("No encuentro el Pais")
            return 0

    def consultaBeneficiosPlantaDb(self, planta):
        r = ""
        self.sparql.setQuery("""
            SELECT DISTINCT ?nombreBeneficio WHERE{
            ?uri <http://www.example.org/UTPL/ontology/hasName> \""""+planta+"""\"@es .
            ?uri <http://www.example.org/UTPL/ontology/hasBenefit> ?uriNombreBeneficio .
            ?uriNombreBeneficio <http://www.example.org/UTPL/ontology/hasName> ?nombreBeneficio
            }
        """)
        lista = []
        for result in self.sparql.query().bindings:
            lista.append(result["nombreBeneficio"].value)
        return lista

    def consultaTodasPlantas(self):
        r = ""
        self.sparql.setQuery("""
            SELECT ?nombrePlanta 
            WHERE{
            ?uri rdf:type <http://www.example.org/UTPL/ontology/MedicalPlant> .
            ?uri <http://www.example.org/UTPL/ontology/hasName> ?nombrePlanta .
            FILTER (lang(?nombrePlanta) = 'es') .
            }
        """)
        lista = []
        for result in self.sparql.query().bindings:
            lista.append(result["nombrePlanta"].value)
        if len(lista) != 0:
            return lista
        else:
            # print("No encuentro el Pais")
            return 0

    def consultaTodosBeneficios(self):
        r = ""
        self.sparql.setQuery("""
            SELECT ?nombreBeneficio 
            WHERE{
            ?uri rdf:type <http://www.example.org/UTPL/ontology/HealthBenefit> .
            ?uri <http://www.example.org/UTPL/ontology/hasName> ?nombreBeneficio .
            }
        """)
        lista = []
        for result in self.sparql.query().bindings:
            lista.append(result["nombreBeneficio"].value)
        if len(lista) != 0:
            return lista
        else:
            # print("No encuentro el Pais")
            return 0

    def consultaTipo(self, nombreElemento):
        r = ""
        self.sparql.setQuery("""
            SELECT ?nombreTipo 
            WHERE{
            ?uri <http://www.example.org/UTPL/ontology/hasName> \""""+nombreElemento+"""\"@es . 
            ?uri rdf:type ?tipo .
            ?tipo <http://www.example.org/UTPL/ontology/hasName> ?nombreTipo .
            }
        """)
        strTipo = ""
        for result in self.sparql.query().bindings:
            strTipo = result["nombreTipo"].value
        return strTipo

    def consultaPlantasDadoBeneficio(self, nombreBeneficio):
        r = ""
        self.sparql.setQuery("""
            SELECT ?nombrePlanta
            WHERE{
            ?uriBeneficio <http://www.example.org/UTPL/ontology/hasName> \""""+nombreBeneficio+"""\"@es .
            ?uriPlanta <http://www.example.org/UTPL/ontology/hasBenefit> ?uriBeneficio.
            ?uriPlanta <http://www.example.org/UTPL/ontology/hasName> ?nombrePlanta.
            }
        """)
        lista = []
        for result in self.sparql.query().bindings:
            lista.append(result["nombrePlanta"].value)
        if len(lista) != 0:
            return lista
        else:
            # print("No encuentro el Pais")
            return 0