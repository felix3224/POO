from pathlib import Path
import hashlib


def gerar_hash_pasta(pasta=".", extensao=".py"):
    arquivos = sorted(
        [
            arquivo
            for arquivo in Path(pasta).rglob(f"*{extensao}")
            if arquivo.name != "integrity.py"
        ]
    )

    print(arquivos)
    
    hash_global = hashlib.sha256()

    for arquivo in arquivos:
        # inclui nome/caminho do arquivo no hash
        hash_global.update(str(arquivo.relative_to(pasta)).encode())

        # inclui conteúdo
        with open(arquivo, "rb") as f:
            while bloco := f.read(4096):
                hash_global.update(bloco)

    return hash_global.hexdigest()


if __name__ == "__main__":
    resultado = gerar_hash_pasta()
    print(resultado)