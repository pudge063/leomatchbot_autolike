import json
import os


class Checker:
    def __init__(self, list_file="list.json"):
        self.list_file = list_file

        if not os.path.exists(self.list_file):
            with open(self.list_file, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def check_in_list(self, target_data):
        """Проверяет, есть ли данные в списке и добавляет их при необходимости."""
        with open(self.list_file, "r+", encoding="utf-8") as f:
            data = json.load(f)

            if target_data in data:
                print("Анкета уже есть.")
                return True

            data.append(target_data)
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            print("Добавлена новая анкета.")
            return False
