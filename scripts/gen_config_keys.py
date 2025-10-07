import os, io, json

SCHEMA = os.path.join("config","settings_schema.json")
OUT    = os.path.join("gpt","contexts","config-keys.md")

def main():
    if not os.path.exists(SCHEMA):
        print("settings_schema.json not found.")
        return
    with io.open(SCHEMA, "r", encoding="utf-8") as f:
        data = json.load(f)

    lines = ["# settings_schema 关键配置快照","","| id | type | label | default | section |","|---|---|---|---|---|"]
    # settings_schema 是一个数组（多个分组/区块）
    for group in data:
        section_name = group.get("name","")
        for setting in group.get("settings",[]):
            _id = setting.get("id","")
            _type = setting.get("type","")
            _label = setting.get("label","")
            _default = json.dumps(setting.get("default",""), ensure_ascii=False)
            lines.append(f"| `{_id}` | `{_type}` | {str(_label)} | {str(_default)} | {section_name} |")
        # 某些主题把 blocks/blocks.settings 里也塞了配置
        for block in group.get("blocks",[]):
            btype = block.get("type","")
            for setting in block.get("settings",[]):
                _id = setting.get("id","")
                _type = setting.get("type","")
                _label = setting.get("label","")
                _default = json.dumps(setting.get("default",""), ensure_ascii=False)
                lines.append(f"| `{_id}` | `{_type}` | {str(_label)} | {str(_default)} | block:{btype} |")

    with io.open(OUT, "w", encoding="utf-8") as f:
        f.write("\\n".join(lines))
    print("wrote:", OUT)

if __name__ == "__main__":
    main()
