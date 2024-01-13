from . import TestBancoClass

class TestBancoViews(TestBancoClass):
    #posso usar a class para quebra em dois metodos de teste
    def test_criar_sala(self):
        token = self.get_banco_jwt()
        response = self.client.post("/banco/criar_sala", headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "code": "1234"
        })
        
        json_response = response.get_json()

        self.assertEqual("sala criada!", json_response["msg"])
        self.assertEqual(201, response.status_code)

        response = self.client.post("banco/criar_sala", headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "code": "1234"
        })

        json_response = response.get_json()

        self.assertEqual("essa sala já foi criada!", json_response["msg"])
        self.assertEqual(401, response.status_code)
    
    def test_deletar_sala(self):
        self.create_sala()

        sala_code = "1234"

        token = self.get_banco_jwt()
        response = self.client.delete(f"/banco/deletar_sala/{sala_code}", headers={
            "Authorization": f"Bearer {token}"
        })

        json_response = response.get_json()
        
        self.assertEqual("sala deletada", json_response["msg"])
        self.assertEqual(200, response.status_code)
    
    def test_listar_salas(self):
        self.create_salas()

        token = self.get_banco_jwt()
        response = self.client.get("/banco/listar_salas", headers={
            "Authorization": f"Bearer {token}"
        })

        self.assertEqual(200, response.status_code)

