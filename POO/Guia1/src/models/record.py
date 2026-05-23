class Record:
    def __init__(self, record_id: int, name: str, address: str):
        try:
            id = int(record_id)
        except (ValueError, TypeError):
            raise ValueError("ID deve ser um número inteiro válido.")

        if id <= 0:
            raise ValueError("ID inválido.")

        if not name or name.strip() == "":
            raise ValueError("Nome inválido.Dont can be void")

        if not address or address.strip() == "":
            raise ValueError("Endereço invalido. Dont can be void")

        self._id = id
        self._name = name.strip()
        self._address = address.strip()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    def __repr__(self):
        return f"Record(id={self._id}, name='{self._name}', address='{self._address}')"
