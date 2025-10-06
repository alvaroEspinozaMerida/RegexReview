import re

# 1) Usernames (start with a letter, then letters/digits/underscore, length 3–15 total)
strings_1 = [
    "alice_01",
    "A9",
    "9lives",
    "user__name",
    "AdminUser007",
    "toolong_username_exceeds",
]
# pattern = re.compile(r"^[A-Za-z][A-Za-z0-9_]{3,15}$")
#
# for s in strings_1:
#     print(s, re.match(pattern, s))



# 2) Filenames ending with .jpg, .jpeg, or .png (case-insensitive); ignore others
strings_2 = [
    "photo.JPG",
    "banner.jpeg",
    "sprite.png",
    "vector.svg",
    "archive.tar.gz",
    "icon.PNG?size=128",
]

# pattern = re.compile(r"\w+\.(?:jpg|png|jpeg)")
# for s in strings_2:
#     print(s, re.match(pattern, s))

# 3) U.S. currency amounts (with optional commas and 2 decimals): $1,234.56, $12, $0.99
# strings_3 = [
#     "$1,234.56",
#     "$12",
#     "$0.99",
#     "$12.3",
#     "$01,234.56",
#     "USD 15.00",
# ]
#
# pattern = re.compile(r"(?i)(usd|\$)*\s*\d+\.*\d*")
# for s in strings_3:
#     print(s, re.match(pattern, s))




# 4) Dates in MM/DD/YYYY (basic format check, not calendar-accurate)
# strings_4 = [
#     "01/31/2025",
#     "13/01/2025",
#     "2/29/2024",
#     "12-25-2025",
#     "00/10/2025",
# ]
#
# pattern = re.compile(r"\d{1,2}[-,\/]\d{1,2}[-,\/]\d{4}")
# for s in strings_4:
#     print(s, re.match(pattern, s))



# 5) Times in 12-hour clock with AM/PM (e.g., 09:45 AM, 9:05 pm)
# strings_5 = [
#     "09:45 AM",
#     "9:05 pm",
#     "12:00 PM",
#     "00:30 AM",
#     "13:20 PM",
# ]
#
# pattern = re.compile(r"\d{1,2}:\d{2}\s{1}(?:)(AM|PM)")
# for s in strings_5:
#     print(s, re.match(pattern, s))



# 6) IPv4 octets (0–255) embedded in potential IPs (extract valid full IPs)
# strings_6 = [
#     "Valid: 192.168.1.1",
#     "Loopback 127.0.0.1 works",
#     "Bad 256.100.1.1 and 1.2.3.999",
#     "Edge 0.0.0.0 and 255.255.255.255",
# ]
#
# pattern = re.compile(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
# for s in strings_6:
#     print(s, re.findall(pattern, s))



# 7) Simple HTML tags and their inner text (e.g., <h1>Title</h1>) — single-line
# strings_7 = [
#     "<h1>Title</h1>",
#     "<p class='lead'>Hello</p>",
#     "<div>Block <span>inline</span></div>",
#     "<br>",
# ]
#
# pattern = re.compile(r"<[\sA-Za-z0-9=\']+>\w+</[\sA-Za-z0-9=\']+>")
# for s in strings_7:
#     print(s, re.findall(pattern, s))




# 8) Key=value pairs (keys: letters/_, values: non-space; multiple pairs per line)
strings_8 = [
    "user=alvaro id=42 status=active",
    "token=abc123 expires=2025-10-05",
    "path=/home/user debug=true verbose",
]

pattern = re.compile(r"\w+\s*=/*\s*\w+[-/]*\w*[-/]*\w*\s*\b")
for s in strings_8:
    print(s, re.findall(pattern, s))

# 9) Email-like strings (good-enough extraction; multiple per line)
strings_9 = [
    "Contact: admin@test.io, support@example.com",
    "Bad: name@@example.com",
    "Mixed: user.name+tag@domain.co.uk and x@y.z",
]

# 10) URLs with http/https and optional path/query
strings_10 = [
    "Visit https://example.com",
    "Docs at http://site.org/docs?id=42",
    "Invalid: ftp://server.com",
    "Also see https://sub.domain.co/path/to/page#anchor",
]

# 11) U.S. phone numbers (various separators) with optional +1
strings_11 = [
    "+1-800-555-1212",
    "(415) 555 9876",
    "212.555.0000",
    "5551234",
    "1 (310) 555-4321",
]

# 12) Hex color codes (#RGB or #RRGGBB) — anywhere in string
strings_12 = [
    "Primary: #09f; Secondary: #1122CC;",
    "Bad: #abcd",
    "Edge: #000, #ffffff, #ABC",
]

# 13) Duplicate adjacent words (case-insensitive), allowing punctuation in between
strings_13 = [
    "This is is a test.",
    "Wait, wait, don't tell me.",
    "No duplicates here.",
    "And—and then we go.",
]

# 14) Windows & POSIX file paths (basic extraction; not exhaustive)
strings_14 = [
    r"C:\\Users\\Alice\\Documents\\file.txt",
    r"/usr/local/bin/python3",
    r"relative\\path\\to\\file",
    r"./script.sh",
]

# 15) GUID/UUID v4-like strings
strings_15 = [
    "ID: 123e4567-e89b-12d3-a456-426614174000",
    "Not a UUID: 123e4567e89b12d3a456426614174000",
    "Upper: 123E4567-E89B-12D3-A456-426614174000",
]

# 16) Extract quoted text (double quotes), including escaped quotes inside
strings_16 = [
    r"He said, \"hello\".",
    r"\"Quoted \\\"inside\\\" quotes\"",
    r"No quotes here",
    r"\"Unclosed quote",
]

# 17) Roman numerals (I, V, X, L, C, D, M) — moderate validation
strings_17 = [
    "I",
    "IV",
    "XII",
    "MCMXCIX",
    "IIII",
    "VX",
]

# 18) Base64-like chunks (A–Z, a–z, 0–9, +, / with = padding) in text
strings_18 = [
    "Token: QWx2YXJvRWxpdGU=",
    "Not base64: hello_world",
    "JWT part: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
]

# 19) Lines that are NOT comments (exclude lines starting with #, allowing leading spaces)
strings_19 = [
    "# full comment",
    "   # indented comment",
    "code line",
    "   code with indent",
]

# 20) Words with hyphens or apostrophes (don't split 'don't' or 'state-of-the-art')
strings_20 = [
    "Don't split contractions.",
    "State-of-the-art methods are common.",
    "Mixed-Case and hyphen-words appear.",
    "Plain words only here",
]
