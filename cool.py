import re

text = "Interface: Gig0/0, IP: 10.0.0.1, status: up"


status = re.search(r"Interface:\s(Gig\d\/\d),status:(\s{2})", text)

print(status.group(1))