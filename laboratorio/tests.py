from django.test import TestCase
from .models import Laboratorio

class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio(nombre = "Lab X",
                                      ciudad = "Bio Bio",
                                      pais = "Chile")
        
        cls.laboratorio.save() #se guarda en la BD

    def test_nombre_correcto(self):
        '''
        En el setup se creo un Laboratorio, ahora al consultar 
        debe existir un laboratorio.

        '''

        labs = Laboratorio.objects.all()
        print("numero de labs: ", labs.count())

        self.assertEqual(labs.count(), 1)
        self.assertNotEqual(labs.count(),2)
        self.assertEqual(labs.first().nombre, "Lab X")

    

    def test_crear_retorna_status_200(self):
        '''
        Envio una peticion a /laboratorio/laboratorio/create
        retorna status 200 y crea un nuevo laboratorio.
        '''
        response = self.client.post("/laboratorio/laboratorio/create", {
            "nombre": "Lab z",
            "ciudad": "Octava Region",
            "pais": "Chile"
        }, follow = True)
        self.assertEqual(response.status_code, 200)

        labs = Laboratorio.objects.all()
        self.assertEqual(labs.count(), 2)
        self.assertEqual(labs.last().nombre,"Lab z")
        self.assertTemplateUsed(response, "laboratorio_list.html")

