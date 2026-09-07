#!/usr/bin/env python3
"""
Division Drill Sheet Generator
- No title - just problems
- Filename: division_drill_YYYYMMDD_HHMM.tex
"""

import os
import random
from datetime import datetime


def generate_problem():
    """Generate division problem with divisor and quotient both 2-15."""
    divisor = random.randint(2, 15)
    quotient = random.randint(2, 15)
    dividend = divisor * quotient
    return dividend, divisor, quotient


def generate_drill_sheet():
    """Generate LaTeX with 90 problems - no title."""
    problems = [generate_problem() for _ in range(90)]
    
    lines = []
    
    lines.append(r'\documentclass[12pt]{article}')
    lines.append(r'\usepackage[margin=0.6in]{geometry}')
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
    lines.append(r'\renewcommand{\arraystretch}{3.2}')
    lines.append(r'\begin{tabular}{' + 'c@{\\hspace{45pt}}' * 5 + 'c}')
    
    problem_idx = 0
    for row in range(15):
        row_content = []
        for col in range(6):
            dividend, divisor, _ = problems[problem_idx]
            cell = r'$%d \overline{\smash{)}\, %d}$' % (divisor, dividend)
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
    filename = f'division_drill_{timestamp}.tex'
    output_path = os.path.join('tex', filename)
    
    with open(output_path, 'w') as f:
        f.write(generate_drill_sheet())
    
    print(f'Created: {output_path}')