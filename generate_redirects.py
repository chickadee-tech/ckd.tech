import toml
from pathlib import Path

redirects = toml.load("redirects.toml")

template = Path("redirect_template.html").read_text()

site_root = Path("site/")
for redirect in redirects["redirects"]:
    from_path = redirect["from"]
    to_url = redirect["to"]
    if from_path[0] != "/":
        raise RuntimeError("From path must start with /")
    print(from_path + " -> " + to_url)
    page_directory = site_root / from_path[1:]
    page_directory.mkdir(parents=True, exist_ok=True)
    page = page_directory / "index.html"
    page.write_text(template.format(to_url=to_url))

