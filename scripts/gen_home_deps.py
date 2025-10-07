import os, re, json, io

ROOT = "."
TEMPLATE_INDEX = os.path.join("templates","index.json")
SECTIONS_DIR = "sections"
SNIPPETS_DIR = "snippets"

ASSET_PATTERNS = [
    re.compile(r'assets/([A-Za-z0-9._\-]+)'),
    re.compile(r"['\"]([A-Za-z0-9._\-]+\.(?:js|css|svg|png|jpg|jpeg|webp|gif))['\"]"),
]
RENDER_SNIPPET = re.compile(r"{%\\s*render\\s+['\"]([A-Za-z0-9_\\-]+)['\"]")

def load_index_sections():
    if not os.path.exists(TEMPLATE_INDEX):
        return []
    with io.open(TEMPLATE_INDEX, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Online Store 2.0 JSON schema: sections listed under "sections"
    sections = data.get("sections", {})
    used = set()
    for sec_id, sec in sections.items():
        stype = sec.get("type")
        if stype: used.add(stype if stype.endswith(".liquid") else f"{stype}.liquid")
    return sorted(used)

def scan_file_assets(text):
    assets = set()
    for pat in ASSET_PATTERNS:
        for m in pat.findall(text):
            assets.add(m if isinstance(m, str) else m[0])
    return assets

def scan_renders(text):
    return set(RENDER_SNIPPET.findall(text))

def read(path):
    try:
        with io.open(path,"r",encoding="utf-8") as f:
            return f.read()
    except:
        return ""

def main():
    used_sections = load_index_sections()
    lines = []
    lines.append("# 首页依赖图 (templates/index.json)")
    lines.append("")
    if not used_sections:
        lines.append("> 未找到 templates/index.json 或没有可解析的 sections。")
    for sec in used_sections:
        sec_path = os.path.join(SECTIONS_DIR, sec)
        sec_exists = os.path.exists(sec_path)
        lines.append(f"## section: {sec} {'(不存在!)' if not sec_exists else ''}")
        if not sec_exists: 
            lines.append("")
            continue
        content = read(sec_path)
        renders = scan_renders(content)
        assets = scan_file_assets(content)

        # 追踪 snippets 的二级 render（简单扫描）
        sub_snippets = set()
        for sn in renders:
            sn_path = os.path.join(SNIPPETS_DIR, f\"{sn}.liquid\")
            if os.path.exists(sn_path):
                sn_text = read(sn_path)
                assets |= scan_file_assets(sn_text)
                sub_snippets |= scan_renders(sn_text)

        lines.append(f"- snippets: {', '.join(sorted(renders)) if renders else '(无)'}")
        if sub_snippets:
            lines.append(f\"  - nested snippets: {', '.join(sorted(sub_snippets))}\")
        lines.append(f\"- assets: {', '.join(sorted(assets)) if assets else '(无)'}\")
        lines.append(\"\")

    out_path = os.path.join(\"gpt\",\"contexts\",\"home-deps.md\")
    with io.open(out_path, \"w\", encoding=\"utf-8\") as f:
        f.write(\"\\n\".join(lines))
    print(\"wote:\", out_path)

if __name__ == \"__main__\":
    main()
