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
        # 1. 过滤空行
        if not line_striped:
            continue
        # # 2. 过滤掉开头是 # 的纯注释行
        # if line_striped.startswith('#'):
        #     continue
        # 3. 只处理以 "- " 开头的 YAML 规则行
        # if line_striped.startswith('- '):
        #     # 剥离前面的 "- " 符号
        #     pure_rule = line_striped[2:].strip()
        #     # 去除规则右侧的行内注释（提取 # 号前面的部分）
        #     pure_rule = pure_rule.split('#')[0].strip()
        #     # 如果清洗后不为空，放入最终列表
        #     if pure_rule:
        #         cleaned_lines.append(pure_rule)
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
