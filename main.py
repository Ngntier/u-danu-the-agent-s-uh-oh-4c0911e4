import os
ENTRY = "Oopsie"
assert ENTRY and ENTRY == ENTRY.strip() and "\n" not in ENTRY and len(ENTRY.split()) == 1 and 1 <= len(ENTRY) <= 99 and 1 <= len(ENTRY.encode("utf-8")) <= 99
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
path = os.path.join(output_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
with open(path, "rb") as f:
    data = f.read()
assert data == ENTRY.encode("utf-8") and len(data) == len(ENTRY.encode("utf-8")) and data.decode("utf-8") == ENTRY
