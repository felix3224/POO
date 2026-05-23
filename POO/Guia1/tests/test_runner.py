from src.services.record_service import RecordService
from src.config.settings import Settings

import os
import hashlib


class TestRunner:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.test_file = os.path.join(base_dir, "data", "records_teste.csv")
        self.service = RecordService(self.test_file)
        print(
            f"\n{calculate_file_hash(os.path.join(base_dir, 'tests', 'test_runner.py'))}"
        )

    def run(self):
        print("\n=== EXECUTANDO TESTES ===")

        self.test_load_valid_records()
        self.test_invalid_records_ignored()
        self.test_search_multiple_terms()

    def test_load_valid_records(self):
        print("\n[TESTE 1] Carregamento básico")

        try:
            records = self.service.get_all_records()
            if len(records) > 0:
                print("OK: Registros carregados")
            else:
                print("FALHA: Nenhum registro carregado")
        except Exception as e:
            print(f"FALHA: Erro ao carregar registros -> {e}")

    def test_invalid_records_ignored(self):
        print("\n[TESTE 2] Validação de registros inválidos")

        try:
            records = self.service.get_all_records()

            for r in records:
                if r.id <= 0 or not r.name or not r.address:
                    print("FALHA: Registro inválido não foi filtrado")
                    return

            print("OK: Registros inválidos ignorados corretamente")

        except Exception as e:
            print(f"FALHA: Erro durante validação -> {e}")

    def test_search_multiple_terms(self):
        print("\n[TESTE 3] Busca com múltiplos termos")

        try:
            self.service.get_all_records()

            results = self.service.search("joao rua a")

            if len(results) == 0:
                print("FALHA: Nenhum resultado encontrado")
                return

            for r in results:
                text = (r.name + " " + r.address).lower()
                if "joão" not in text or "rua" not in text or "a" not in text:
                    print("FALHA: Resultado incorreto na busca")
                    return

            print("OK: Busca múltiplos termos funcionando")

        except Exception as e:
            print(f"FALHA: Erro na busca -> {e}")


def calculate_file_hash(file_path):
    try:
        hash_md5 = hashlib.md5()

        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)

        return hash_md5.hexdigest()

    except Exception as e:
        print(f"Erro ao calcular hash: {e}")
        return None


if __name__ == "__main__":
    TestRunner().run()
