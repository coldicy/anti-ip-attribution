import os
import re

# 读取文件
with open("./rules.yaml", "r") as file:
    rules = file.read()

# 创建文件夹
os.makedirs("./rules/clash", exist_ok=True)

# 正则
regex = r"# ======= (.*?) ======= #"
result = re.split(regex, rules)

# 拆分 yaml文件
for i in range(1, len(result), 2):
    ruleName = result[i]
    ruleContent = result[i + 1]

    # 清洗文本，转换成 clash 规则
    cleaned_lines = []
    # 按行切分并循环处理
    for line in ruleContent.splitlines():
        line_striped = line.strip()
        # 过滤空行
        if not line_striped:
            continue
        cleaned_lines.append("  " + line_striped)
    # 将列表拼接回标准文本
    cleaned_text = "\n".join(cleaned_lines)

    # 创建对应名称的文件
    filePath = f"./rules/clash/{ruleName}.yaml"

    # 添加原始文件内容
    yamlHead = "payload:"
    splitTAML = f"# ======= {ruleName} ======= #\n{yamlHead}\n{cleaned_text}"

    # 写入文件
    with open(filePath, "w") as file:
        file.write(splitTAML)
