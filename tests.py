import unittest
from ejercicios import es_multiplo_de,es_par, cantidad_de_pizzas, alguno_es_0, ambos_son_0, es_nombre_largo, año_bisiesto, peso_pino, es_peso_util, sirve_pino, devolver_el_doble_si_es_par, devolver_valor_si_es_par_sino_el_que_sigue, devolver_doble_simultiplode3_devolvertriple_simultiplode9
class tests_esmultiplode(unittest.TestCase):
    def test_multiplos(self):
        self.assertTrue(es_multiplo_de(2,4))
        
    def test_nomultiplos(self):
        self.assertFalse(es_multiplo_de(3,10))
        
class tests_par(unittest.TestCase):
    def test_numero_par(self):
        self.assertTrue(es_par(10))
        
    def test_numero_impar(self):
        self.assertFalse(es_par(19))
    
    def test_0(self):
        self.assertTrue(es_par(0))
        
        
class test_cantidad_de_pizzas(unittest.TestCase):
    def test_cantidad_de_pizzas_5personas(self):
        self.assertEqual(cantidad_de_pizzas(5,3),2)
        
class test_alguno_escero(unittest.TestCase):
    def test_ceroizq(self):
        self.assertTrue(alguno_es_0(0,1))
        
    def test_ceroder(self):
        self.assertTrue(alguno_es_0(1,0))
        
    def test_todos_cero(self):
        self.assertTrue(alguno_es_0(0,0))
        
    def test_ningun_cero(self):
        self.assertFalse(alguno_es_0(1,1))
        
class tests_ambos_cero(unittest.TestCase):
    def test_amboscero(self):
        self.assertTrue(ambos_son_0(0,0))
        
    def test_ningun_cero(self):
        self.assertFalse(ambos_son_0(1,1))
        
    def test_uncero(self):
        self.assertFalse(ambos_son_0(0,9))
        
        
class tests_es_nombre_largo(unittest.TestCase):
    def test_nombre_largo_false(self):
        self.assertFalse(es_nombre_largo("sebastian"))
        
    def test_nombre_largo_true(self):
        self.assertTrue(es_nombre_largo("coco"))
        
        
class test_año_bisiesto(unittest.TestCase):
    def test_año_bisiesto_true(self):
        self.assertTrue(año_bisiesto(2020))
        
    def test_año_bisiesto_false(self):
        self.assertFalse(año_bisiesto(2021))
        
class tests_peso_pino(unittest.TestCase):
    def test_peso_pino_ejemplo1(self):
        self.assertEqual(peso_pino(200),600)
    def test_peso_pino_ejemplo2(self):
        self.assertEqual(peso_pino(500),1300)
        
        
class tests_peso_util(unittest.TestCase):
    def test_peso_util_menor400(self):
        self.assertFalse(es_peso_util(355))
    def test_peso_util_mayor400(self):
        self.assertTrue(es_peso_util(555))
    def test_peso_util_mayor1000(self):
        self.assertFalse(es_peso_util(1555))
       
               
class tests_peso_pino(unittest.TestCase):
    def test_sirve_peso_pino(self):
        self.assertTrue(sirve_pino(200))
    def test_sirve_peso_pino2(self):
        self.assertFalse(sirve_pino(500))
        
class test_devolver_doble_si_es_par(unittest.TestCase):
    def test_devolver_doble_par(self):
        self.assertEqual(devolver_el_doble_si_es_par(4),8)
        
    def test_devolver_doble_impar(self):
        self.assertEqual(devolver_el_doble_si_es_par(3),3)
        
class test_devolver_elquesigue(unittest.TestCase):
    def test_devolver_elquesigue_par(self):
        self.assertEqual(devolver_valor_si_es_par_sino_el_que_sigue(2),2)
        
    def test_devolver_elquesigue_impar(self):
        self.assertEqual(devolver_valor_si_es_par_sino_el_que_sigue(3),4)
        
class tests_devolver_doble_o_triple(unittest.TestCase):
    def test_multiplode3(self):
        self.assertEqual(devolver_doble_simultiplode3_devolvertriple_simultiplode9(18),36)
        
    def test_multiplode9(self):
        self.assertEqual(devolver_doble_simultiplode3_devolvertriple_simultiplode9(27),54)#nunca va a llegar a la condicion de 9 pues el 3 siempre va a dividir cualq numero de 9
      
    def test_no_multiplo_de3ni9(self):
        self.assertEqual(devolver_doble_simultiplode3_devolvertriple_simultiplode9(43),43)    
if __name__ == '__main__':
    unittest.main(verbosity=2)