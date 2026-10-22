def parse_student(line):
    line = line.strip()
    if not line:
        raise ValueError("空行")
    
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量错误，期望2个，实际{len(parts)}个")
    
    name, score_str = parts[0].strip(), parts[1].strip()
    if not name:
        raise ValueError("姓名为空")
    
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩不是合法整数: '{score_str}'")
        
    if not (0 <= score <= 100):
        raise ValueError(f"成绩 {score} 超出 0~100 范围")
        
    return {"name": name, "score": score}