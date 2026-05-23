from src.services.record_service import RecordService
from src.config.settings import Settings

def main():
    service = RecordService(Settings.DATA_FILE)

    print("=== CARREGANDO REGISTROS ===")
    try:
        records = service.get_all_records()
        for r in records:
            print(r)
    except Exception as e:
        print(f"Erro: {e}")
        return

    print("\n=== BUSCA ===")
    term = input("Digite nome ou endereço: ")

    try:
        results = service.search(term)
        if results:
            for r in results:
                print(r)
        else:
            print("Nenhum registro encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()