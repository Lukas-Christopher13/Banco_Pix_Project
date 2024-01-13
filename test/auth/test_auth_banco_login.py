from . import TestAuthClass

class TestAuthBancoLogin(TestAuthClass):
    def test_banco_login(self):
        self.create_banco()
        request = self.client.post("auth/banco-login", json={
            "username": "test",
            "password": "123"
        })

        self.assertEqual(200, request.status_code)
    
    def test_banco_invalid_username(self):
        self.create_banco()
        request = self.client.post("auth/banco-login", json={
            "username": "invalido",
            "password": "123"
        })

        json = request.get_json()

        self.assertEqual(json["msg"], "invalid username")
        self.assertEqual(401, request.status_code)

    def test_banco_invalid_password(self):
        self.create_banco()
        request = self.client.post("auth/banco-login", json={
            "username": "test",
            "password": "invalido"
        })

        json = request.get_json()

        self.assertEqual(json["msg"], "invalid password")
        self.assertEqual(401, request.status_code)
