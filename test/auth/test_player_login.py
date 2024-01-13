from . import TestAuthClass

class TestPlayerLogin(TestAuthClass):
    def test_player_insert_code(self):
        self.create_sala()
        sala_code = "1234"

        response = self.client.post("auth/sala-code", json={
            "code": sala_code
        })

        self.assertEqual(200, response.status_code)

        json_response = response.get_json()
        self.assertEqual(sala_code, json_response["code"])

    def test_palyer_insert_invalid_code(self):
        self.create_sala()
        invalid_code = "1111"

        response = self.client.post("auth/sala-code", json={
            "code": invalid_code
        })

        self.assertEqual(401, response.status_code)

        json_response = response.get_json()
        self.assertEqual("sala inexistente", json_response["msg"])

    def test_create_player(self):
        self.create_sala()
        valid_code = "1234"

        response = self.client.post(f"auth/create-player/{valid_code}", json={
            "username": "test-player"
        })

        self.assertEqual(200, response.status_code)

    def test_create_player_invalid_sala_code(self):
        self.create_sala()
        invalid_code = "1111"

        response = self.client.post(f"auth/create-player/{invalid_code}", json={
            "username": "test-player"
        })

        self.assertEqual(401, response.status_code)

        json_response = response.get_json()
        self.assertEqual("sala inexistente",  json_response["msg"])

