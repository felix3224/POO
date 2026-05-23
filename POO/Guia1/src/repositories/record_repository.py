import unicodedata

from src.repositories.abstract_repository import AbstractRepository
from src.models.record import Record
from src.utils.file_loader import FileLoader


def _normalize_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch)).lower()


class RecordRepository(AbstractRepository):
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._records = []

    def load_all(self):
        data = FileLoader.load_csv(self._file_path)
        self._records = []
        for row in data:
            try:
                novo_registro = Record(row["id"], row["name"], row["address"])
                self._records.append(novo_registro)
            except ValueError:
                print(
                    f"Registro inválido ignorado: {{'id': '{row['id']}', 'name': '{row['name']}', 'address': '{row['address']}'}}"
                )
                continue

        return self._records

    def search(self, term: str):
        term = _normalize_text(term)

        termos = term.split()

        if not termos:
            return []

        resultados = []

        for r in self._records:
            palavras_do_registro = (
                _normalize_text(r.name).split() + _normalize_text(r.address).split()
            )

            if all(palavra in palavras_do_registro for palavra in termos):
                resultados.append(r)

        return resultados
