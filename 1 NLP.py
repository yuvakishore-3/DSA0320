import re
text = "Email: support@example.com, Website: https://www.python.org"
emails = re.findall(r'\S+@\S+', text)
urls = re.findall(r'https?://\S+', text)
print("Emails:", emails)
print("URLs:", urls)
