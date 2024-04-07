import pytest
from typing import Tuple
from Types import DataType
from JsonDataReader import JsonDataReader


class TestJsonDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> Tuple[str, DataType]:
        text = """{
    "Иванов Константин Дмитриевич" : {
            "математика": 91, "химия":100
    },
    "Петров Петр Семенович" : {
            "русский язык":87, "литература":78
    }
}"""
        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: Tuple[str,
                                                       DataType],
                          tmpdir) -> Tuple[str,
                                           DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.json")
        p.write(file_and_data_content[0])
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data:
                  Tuple[str, DataType]) -> None:
        filepath, expected_data = filepath_and_data
        file_content = JsonDataReader().read(filepath)
        assert file_content == expected_data
