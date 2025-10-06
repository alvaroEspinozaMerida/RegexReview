import re


# Level 1: Basics

# 1. Match all 3-digit numbers
# strings_1 = [
#     "The code is 123.",
#     "Room number 45 is smaller than 6789.",
#     "Serial: 007",
# ]
#
# pattern = re.compile(r"\b\d{3}\b")
#
# for s in strings_1:
#     print(s, re.search(pattern, s))



# 2. Match words that start with a capital letter

# strings_2 = [
#     "Alice went to Wonderland.",
#     "the quick Brown fox.",
#     "NASA launched Apollo.",
# ]
#
# pattern = re.compile(r"[A-Z]{1}[A-Za-z]+")
#
#
# for s in strings_2:
#     print(s, re.findall(pattern, s))


# 3. Extract all email addresses from a paragraph
# strings_3 = [
#     "Contact us at support@example.com or sales@company.org.",
#     "My email is test.user123@gmail.com.",
# ]
#
#
#
# pattern = re.compile(r"\w+@\w+.\w+")
#
#
# for s in strings_3:
#     print(s, re.findall(pattern, s))




# 4. Match strings ending with .jpg or .png
# strings_4 = [
#     "photo.jpg",
#     "image.PNG",
#     "graphic.jpeg",
#     "icon.png",
# ]
#
# pattern = re.compile(r"^\w+.(?i:.jpg|.png)$")
#
# for s in strings_4:
#     print(s, re.match(pattern, s))




# Level 2: Intermediate

# 5. Validate dates in YYYY-MM-DD format
# strings_5 = [
#     "2025-10-03",
#     "1999-12-31",
#     "2025-13-01",
#     "21-05-07",
# ]
#
# pattern = re.compile(r"[0-9]{4}-[0-3]{1}[0-9]{1}-[0-3]{1}[0-9]{1}")
#
# for s in strings_5:
#     print(s, bool(re.match(pattern, s)))



# 6. Extract all hashtags from text (#Python, #AI)
# strings_6 = [
#     "I love #Python and #MachineLearning.",
#     "#AI is trending.",
#     "Hashtags: #fun #code #100DaysOfCode",
# ]
#
# pattern = re.compile(r"#{1}\w+")
#
# for s in strings_6:
#     print(s, re.findall(pattern, s))



# 7. Find duplicated words (e.g., "the the")
# strings_7 = [
#     "This is is a test.",
#     "No duplicates here.",
#     "And and then it happened.",
# ]
#
# pattern = re.compile(r"\b(?i)(\w+)\s+\1\b")
#
#
# for s in strings_7:
#     print(s, re.findall(pattern, s))


# 8. Split a sentence into words but keep punctuation separate
# strings_8 = [
#     "Hello, world!",
#     "Regex is fun, right?",
#     "Wait...what?!",
# ]
#
# pattern = re.compile(r"\b\w+\b")
#
#
# for s in strings_8:
#     print(s, re.findall(pattern, s))



# 9. Match floating point numbers with optional +/-
# strings_9 = [
#     "+3.14",
#     "-0.99",
#     "42",
#     ".5",
#     "6.",
# ]
# pattern = re.compile(r"[+-]?\d?\.\d*")
#
#
# for s in strings_9:
#     print(s, re.findall(pattern, s))






# Level 3: Advanced

# 10. Extract all quoted text (double quotes)
# strings_10 = [
#     "He said \"hello\"",
#     "Quotes can be tricky: \"yes\" or \"no\"?",
# ]
#
# pattern = re.compile(r"\"\w+\"")
#
#
# for s in strings_10:
#     print(s, re.findall(pattern, s))


# 11. Match valid US phone numbers with optional +1
# strings_11 = [
#     "+1-800-555-1234",
#     "(800) 555-1234",
#     "800.555.1234",
#     "5551234",
# ]
#
# pattern = re.compile(r"[+1]*[-\s\\.]*[(]?[0-9]{3}[)]?[-\s\\.][0-9]{3}[-\s\\.][0-9]{4}")
#
# for s in strings_11:
#     print(s, re.findall(pattern, s))


# 12. Extract domain names from URLs
# strings_12 = [
#     "Visit https://www.example.com/page.",
#     "Check http://test.org.",
#     "Secure site: https://secure.net/login",
# ]
#
# pattern = re.compile(r"http[s]?://\w*\.?\w+\.{1}\w{2,3}")
#
# for s in strings_12:
#     print(s, re.findall(pattern, s))


# 13. Match hex color codes in CSS
# strings_13 = [
#     "Color: #fff;",
#     "Background: #123456;",
#     "Invalid: #abcd;",
# ]
#
# pattern = re.compile(r"\w+:\s*#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6});")
#
# for s in strings_13:
#     print(s, bool(re.match(pattern, s)))

# 14. Use a lookahead to match numbers only if followed by kg or lb
strings_14 = [
    "Weight: 70kg",
    "Height: 180cm",
    "Mass: 150 lbs",
    "Value: 123",
]

# Level 4: Challenge

# 15. Extract key-value pairs from text
strings_15 = [
    "user=alvaro id=42 status=active",
    "session=xyz123 token=abc456",
]

# 16. Match times in HH:MM (24-hour)
strings_16 = [
    "09:45",
    "23:59",
    "25:00",
    "7:30",
]

# 17. Extract all <tag>...</tag> pairs from an HTML snippet
strings_17 = [
    "<div>Hello</div>",
    "<p class='text'>This is a paragraph</p>",
    "<span>Inline</span>",
]

# 18. Match any word containing repeated letters
strings_18 = [
    "coffee",
    "book",
    "regex",
    "letter",
    "fun",
]

# 19. Validate passwords with >=8 chars, 1 digit, 1 uppercase, 1 special
strings_19 = [
    "Password1!",
    "weakpass",
    "STRONGpass123$",
]

# 20. Write a regex that does not match lines starting with #
strings_20 = [
    "# This is a comment",
    "print('Hello World')",
    "# Another comment",
    "x = 42",
]
