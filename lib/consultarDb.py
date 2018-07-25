from SPARQLWrapper import SPARQLWrapper2, JSON


class consultar:
    def __init__(self, dbC):
        self.sparql = SPARQLWrapper2(dbC, "http://localhost:8890/plantasmedicinales")

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
            return 0

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
            return 0