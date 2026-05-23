from src.repositories.record_repository import RecordRepository

class RecordService:

    def __init__(self, file_path: str):
        self._repository = RecordRepository(file_path)

    def get_all_records(self):
        return self._repository.load_all()

    def search(self, term: str):
        if not term or term.strip() == "":
            raise ValueError("Termo de busca inválido")
        return self._repository.search(term)