import csv

class FileLoader:

    @staticmethod
    def load_csv(file_path: str):
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            raise Exception(f"Arquivo não encontrado: {file_path}")
        except Exception as e:
            raise Exception(f"Erro ao ler arquivo: {str(e)}")