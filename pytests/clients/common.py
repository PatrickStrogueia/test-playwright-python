import random
import string


class Common:

    @staticmethod
    def incorrect_payload(incorrect_payloads):
        match incorrect_payloads:
            case "payload_vazio":
                return ""
            case "None":
                return None
            case "null":
                return "null"
            case "hash_vazio":
                return {}
            case "array_vazio":
                return []
            case "hash_vazio_string":
                return "{}"
            case "array_vazio_string":
                return "[]"
            case "payload_number":
                return 1
            case "payload_boolean_true":
                return True
            case "payload_boolean_false":
                return False

    @staticmethod
    def values_change(value):
        if ".to_i" in value:
            return int(value.split(".")[0])
        elif ".to_f" in value:
            return float(value.split(".")[0])
        elif value == "None":
            return None
        elif value == "number_negative":
            return -1
        elif value == "boolean_true":
            return True
        elif value == "boolean_false":
            return False
        elif ".characters_type_string" in value:
            letters = string.ascii_lowercase
            number = int(value.split(".")[0])
            return "".join(random.choice(letters) for i in range(number))
        elif ".characters_type_numbers" in value:
            number = int(value.split(".")[0])
            return "".join(random.choice("123456789") for i in range(number))
        elif value == "Array":
            return []
        elif value == "Hash":
            return {}
        else:
            return value

    @staticmethod
    def change_fields_payload(payload, field, value):
        count = field.count(".")
        if count == 1:
            fields = field.split(".")
            if type(payload[fields[0]]) == list:
                payload[fields[0]][0][fields[1]] = Common.values_change(value)
            if type(payload[fields[0]]) == dict:
                payload[fields[0]][fields[1]] = Common.values_change(value)
        elif count == 2:
            fields = field.split(".")
            if type(payload[fields[0]]) == list:
                payload[fields[0]][0][fields[1]][fields[2]] = Common.values_change(
                    value
                )
            if type(payload[fields[0]][fields[1]]) == list:
                payload[fields[0]][fields[1]][0][fields[2]] = Common.values_change(
                    value
                )
            if type(payload[fields[0]][fields[1]]) == dict:
                payload[fields[0]][fields[1]][fields[2]] = Common.values_change(value)
            else:
                payload[field] = Common.values_change(value)
            return payload

    @staticmethod
    def remove_fields_payload(payload, field):
        count = field.count(".")
        if count == 1:
            fields = field.split(".")
            if type(payload[fields[0]]) == list:
                del payload[fields[0]][0][fields[1]]
            if type(payload[fields[0]]) == dict:
                del payload[fields[0]][fields[1]]
        elif count == 2:
            fields = field.split(".")
            if type(payload[fields[0]]) == list:
                del payload[fields[0]][0][fields[1]][fields[2]]
            if type(payload[fields[0]][fields[1]]) == list:
                del payload[fields[0]][fields[1]][0][fields[2]]
            if type(payload[fields[0]][fields[1]]) == dict:
                payload[fields[0]][fields[1]][fields[2]]
            else:
                del payload[field]
            return payload
