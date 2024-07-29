with open(0, "r", encoding="utf-8") as f:
    data = f.readlines()

print(
    """
      
 <!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        p {
            margin: 0; /* Removes default margin */
            padding: 10px 0; /* Adds padding for vertical spacing */
            line-height: .25; /* Sets line spacing */
            font-family: Roboto, sans-serif; /* Changes the font */
        }
    </style>
</head>
<body>

"""
)

maxlength = 160
for x in data:
    i = 1
    while True:
        start = i * maxlength - maxlength
        end = i * maxlength

        if not x[start:end]:
            # theres no lines
            break

        print(f"<p>{x[start:end]}</p>")
        i += 1

print(
    """
</body>
</html>
      """
)
