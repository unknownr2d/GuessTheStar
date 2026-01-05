import os

IMAGE_FOLDER = "updateFolder"
OUTPUT_FILE = "celebrities.txt"

def format_name(filename):
    # taylor_swift -> Taylor Swift
    name = os.path.splitext(filename)[0]
    return name.replace("_", " ").title()

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write("const celebrities = {\n")

    for filename in sorted(os.listdir(IMAGE_FOLDER)):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            key = os.path.splitext(filename)[0]
            name = format_name(filename)

            file.write(f"    '{key}': {{\n")
            file.write(f"        name: '{name}',\n")
            file.write(f"        full: 'img/full/{filename}',\n")
            file.write(f"        quiz: 'img/quizImg/{filename}'\n")
            file.write("    },\n")

    file.write("};\n")

print("✅ celebrities.txt created successfully!")
