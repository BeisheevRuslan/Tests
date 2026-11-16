import pytest
from tasks.yan_disk import YaDiskWorkspace


class TestYaDisk:
    def setup_method(self):
        """Выполняется ПЕРЕД каждым тестом"""
        self.ya_disk_client = YaDiskWorkspace()
        self.ya_disk_client.create_folder("test_folder")

    def teardown_method(self):
        """Выполняется ПОСЛЕ каждого теста для очистки"""
        self.ya_disk_client.delete_folder("test_folder")

    def test_create_folder(self):
        response = self.ya_disk_client.create_folder("test_folder_new")
        assert response.status_code == 201
        self.ya_disk_client.delete_folder("test_folder_new")

    def test_check_folder(self):
        response = self.ya_disk_client.check_folder("test_folder")
        assert response.status_code == 200

    def test_list_files(self):
        response = self.ya_disk_client.list_files()
        assert response.status_code == 200

        data = response.json()
        items = data.get("_embedded", {}).get("items", [])

        folder_names = [item["name"] for item in items]

        assert "test_folder" in folder_names, "Созданная папка не найдена в списке файлов"

    def test_delete_folder_success(self):
        self.ya_disk_client.create_folder("test_folder_to_delete")

        response = self.ya_disk_client.delete_folder("test_folder_to_delete")
        assert response.status_code == 204

    def test_delete_folder_not_found(self):
        response = self.ya_disk_client.delete_folder("test_folder_which_does_not_exist_999")
        assert response.status_code == 404

    def test_unauthorized(self):
        bad_client = YaDiskWorkspace(token="invalid_fake_token_12345")

        response = bad_client.create_folder("test_folder_auth")

        assert response.status_code == 401
