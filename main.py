from datetime import datetime


class Operations:
    def __init__(self, option):
        self.option = option

    def data(self):
        data = self.option["date"]
        date_time = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
        new_format = date_time.strftime("%d.%m.%Y")
        return new_format

    def description(self):
        description = self.option["description"]
        return description

    def _from_(self):
        if "from" not in self.option:
            return f"Нет данных"
        _from_ = self.option["from"]
        if "Счет" in _from_:
            numbers = _from_[-20:]
            mod_string = "**" + numbers[-4:]
            return f"Счет {mod_string}"
        elif "Счет" not in _from_:
            card_numbers = _from_[-16:]
            return f"{_from_[:-17]} {card_numbers[:4]} {card_numbers[5:7]}** **** {card_numbers[12:16]}"

    def to(self):
        to = self.option["to"]
        if "Счет" in to:
            numbers = to[-20:]
            mod_string = "**" + numbers[-4:]
            return f"Счет {mod_string}"
        elif "Счет" not in to:
            card_numbers = to[-16:]
            return f"{to[:-17]} {card_numbers[:4]} {card_numbers[5:7]}** **** {card_numbers[12:16]}"

    def operationAmount(self):

        operation_amount = self.option['operationAmount']["amount"]
        operation_currency = self.option["operationAmount"]["currency"]["name"]
        return f"{operation_amount} {operation_currency}"
    def info(self):
        return f"{self.data()} {self.description()}\n{self._from_()} -> {self.to()}\n{self.operationAmount()}"