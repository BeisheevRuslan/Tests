import pytest
from tasks.docs import get_name, get_directory, add_doc


class TestDocs:
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

    @pytest.mark.parametrize(
        "doc_number, expected",
        [
            ("10006", "Аристарх Павлов"),
            ("2207 876234", "Василий Гупкин"),
            ("11-2", "Геннадий Покемонов"),
            ("999999", "Документ не найден"),
        ],
    )
    def test_get_name(self, doc_number, expected):
        assert get_name(self.documents, doc_number) == expected

    @pytest.mark.parametrize(
        "doc_number, expected",
        [
            ("11-2", "1"),
            ("2207 876234", "1"),
            ("10006", "2"),
            ("999999", "Полки с таким документом не найдено"),
        ],
    )
    def test_get_directory(self, doc_number, expected):
        assert get_directory(self.directories, doc_number) == expected

    @pytest.mark.parametrize(
        "document_type, number, name, shelf_number, expected_shelf_length",
        [
            ('international passport', '311 020203', 'Александр Пушкин', 3, 1),
            ('driver license', '999 999999', 'Иван Иванов', 5, 1),
        ],
    )
    def test_add_doc(self, document_type, number, name, shelf_number, expected_shelf_length):
        result = add_doc(self.documents, self.directories, document_type, number, name, shelf_number)

        assert result == "Документ успешно добавлен"
        assert {"type": document_type, "number": number, "name": name} in self.documents
        assert number in self.directories[str(shelf_number)]
        assert len(self.directories[str(shelf_number)]) == expected_shelf_length
