import re

with open('02_score_calibration.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix table ends
content = re.sub(r' \\?\n\\midrule', r' \\\\\n\\midrule', content)
content = re.sub(r'&\s*([0-9.]+)\s*\\?\n', r'& \1 \\\\\n', content)
# It's safer to just fix all trailing \ on table lines
content = re.sub(r'(Min DCF) \\\n', r'\1 \\\\\n', content)
content = re.sub(r'(0\.372) \\\n', r'\1 \\\\\n', content)
content = re.sub(r'(0\.181) \\\n', r'\1 \\\\\n', content)
content = re.sub(r'(0\.444) \\\n', r'\1 \\\\\n', content)
content = re.sub(r'(0\.319) \\\n', r'\1 \\\\\n', content)
content = re.sub(r'(0\.151) \\\n', r'\1 \\\\\n', content)
content = re.sub(r'(0\.397) \\\n', r'\1 \\\\\n', content)
content = re.sub(r'(0\.265) \\\n', r'\1 \\\\\n', content)
content = re.sub(r'(0\.135) \\\n', r'\1 \\\\\n', content)
content = re.sub(r'(0\.353) \\\n', r'\1 \\\\\n', content)

# Fix multirow syntax
content = content.replace(r'\multirow{3}{}{\textbf{Logistic Regression}}', r'\multirow{3}{*}{\textbf{Logistic Regression}}')
content = content.replace(r'\multirow{3}{}{\textbf{SVM (RBF)}}', r'\multirow{3}{*}{\textbf{SVM (RBF)}}')

# Fix math symbols and bad text
content = re.sub(r'\(\s*\nπ\n~\n\s*\)', r'($\\tilde{\\pi}$)', content)
content = re.sub(r'At\s*\nπ\n~\n\s*=', r'At $\\tilde{\\pi}=$', content)
content = re.sub(r'at\s*\nπ\n~\n\s*=', r'at $\\tilde{\\pi}=$', content)

# Fix p_T
content = re.sub(r'\(p \nT\n[\u200B\s]*=0\.5\)', r'($p_T=0.5$)', content)

# Fix the big equation
# Calibration seeks to find a mapping s ...
eq_pattern = r'Calibration seeks to find a mapping s \ncal\n[\u200B\s]*=αs\+β−log \n1− \nπ\n~\n \nπ\n~\n \n[\u200B\s]*such that'
content = re.sub(eq_pattern, r'Calibration seeks to find a mapping $s_{cal} = \\alpha s + \\beta - \\log \\frac{\\tilde{\\pi}}{1-\\tilde{\\pi}}$ such that', content, flags=re.MULTILINE)

# Fix the slope and bias text
content = re.sub(r'\(α\n\s*\)', r'($\\alpha$)', content)
content = re.sub(r'\(α\)', r'($\\alpha$)', content)
content = re.sub(r'\(β\n\s*\)', r'($\\beta$)', content)
content = re.sub(r'\(β\)', r'($\\beta$)', content)

with open('02_score_calibration.tex', 'w', encoding='utf-8') as f:
    f.write(content)
