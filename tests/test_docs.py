from tasks.docs import get_name, get_directory, add_doc


class TestMyDocs:
    def setup_method(self):
        self.documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
            {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
        ]
        self.directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }

    def test_get_name(self):
        assert get_name(self.documents, "10006") == "Аристарх Павлов"

    def test_get_directory(self):
        assert get_directory(self.directories, "11-2") == "1"

    def test_add_doc(self):
        result = add_doc(self.documents, self.directories, 'international passport',
                         '311 020203', 'Александр Пушкин', 3)

        assert result == "Документ успешно добавлен"
        assert {"type": "international passport", "number": "311 020203", "name": "Александр Пушкин"} in self.documents
        assert "311 020203" in self.directories['3']
        assert len(self.directories['3']) == 1
