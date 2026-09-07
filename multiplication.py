#!/usr/bin/env python3
"""
Multiplication Drill Sheet Generator
- No title - just problems
- Filename: multiplication_drill_YYYYMMDD_HHMM.tex
"""

import os
import random
from datetime import datetime


def generate_problem():
    """Generate multiplication problem with factors both 2-15."""
    factor1 = random.randint(2, 15)
    factor2 = random.randint(2, 15)
    # Randomly switch the order of return
    if random.choice([True, False]):
        return factor1, factor2
    else:
        return factor2, factor1


def generate_drill_sheet():
    """Generate LaTeX with 60 problems - no title."""
    problems = [generate_problem() for _ in range(120)]
    
    lines = []
    
    lines.append(r'\documentclass[11pt]{article}')
    lines.append(r'\usepackage[margin=0.35in]{geometry}')
    lines.append(r'\usepackage{amsmath}')
    lines.append(r'\usepackage{array}')
    lines.append(r'\pagestyle{empty}')
    lines.append(r'\setlength{\parindent}{0pt}')
    lines.append(r'\setlength{\parskip}{0pt}')
    lines.append('')
    
    lines.append(r'\begin{document}')
    lines.append('')
    
    # Problems only - no title section
    lines.append(r'\begin{center}')
    lines.append(r'\renewcommand{\arraystretch}{2.2}')
    lines.append(r'\begin{tabular}{' + 'c@{\\hspace{22pt}}' * 5 + 'c}')
    
    problem_idx = 0

    for row in range(20):  # 10 rows × 6 columns = 60 problems
        row_content = []
        for col in range(6):
            factor1, factor2 = problems[problem_idx]
            cell = r'$%d \times %d = \underline{\hspace{1cm}}$' % (factor1, factor2)
            row_content.append(cell)
            problem_idx += 1
        lines.append(' & '.join(row_content) + r' \\')
    
    lines.append(r'\end{tabular}')
    lines.append(r'\end{center}')
    lines.append('')
    lines.append(r'\end{document}')
    
    return '\n'.join(lines)


if __name__ == '__main__':
    os.makedirs('tex', exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    filename = f'multiplication_drill_{timestamp}.tex'
    output_path = os.path.join('tex', filename)
    
    with open(output_path, 'w') as f:
        f.write(generate_drill_sheet())
    
    print(f'Created: {output_path}')