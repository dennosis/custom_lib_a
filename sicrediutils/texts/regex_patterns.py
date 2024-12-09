import re


def phone_numbers(text):
    phone_pattern = r"(\(?\d{2}\)?[\s-]?\d{4,5}[-]?\d{4})"
    return re.findall(phone_pattern, text)
