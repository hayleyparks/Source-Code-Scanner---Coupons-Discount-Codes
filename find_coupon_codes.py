import requests
import re

KEYWORDS = ["coupon", "discount", "promo", "voucher", "code", "offer"]
CODE_REGEX = r'([A-Z0-9]{5,12})'

def find_codes_in_text(text):
    probable_codes = []
    for keyword in KEYWORDS:
        pattern = rf'({keyword})\s*[:\-]?\s*{CODE_REGEX}'
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            probable_codes.append(match[-1])
    return list(set(probable_codes))

def main():
    url = input("Enter the website URL to scan for coupon codes: ")
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        codes = find_codes_in_text(html)
        if codes:
            print("Possible coupon codes found:")
            for code in codes:
                print(f"- {code}")
        else:
            print("No coupon codes found.")
    except Exception as e:
        print(f"Error fetching or scanning the site: {e}")

if __name__ == "__main__":
    main()
