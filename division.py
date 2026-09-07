#!/usr/bin/env python3
"""
Division Drill Sheet Generator
- Outputs to tex/ directory
- 90 problems evenly spread (6 cols x 15 rows)
- Divisors 2-15, quotients 2-15
"""

import os
import random


def generate_problem():
    """Generate division problem with divisor and quotient both 2-15."""
    divisor = random.randint(2, 15)
    quotient = random.randint(2, 15)
    dividend = divisor * quotient
    return dividend, divisor, quotient


def generate_drill_sheet():
    """Generate LaTeX with 90 problems evenly spread."""
    problems = [generate_problem() for _ in range(90)]
    
    lines = []
    
    lines.append(r'\documentclass[12pt]{article}')
    lines.append(r'\usepackage[margin=0.5in]{geometry}')
    lines.append(r'\usepackage{amsmath}')
    lines.append(r'\usepackage{array}')
    lines.append(r'\pagestyle{empty}')
    lines.append(r'\setlength{\parindent}{0pt}')
    lines.append(r'\setlength{\parskip}{0pt}')
    lines.append('')
    
    lines.append(r'\begin{document}')
    lines.append('')
    
    lines.append(r'\begin{center}')
    lines.append(r'\textbf{\Large Division Practice Drill}\\[0.3cm]')
    lines.append(r'\small Solve each problem. Show your work.')
    lines.append(r'\end{center}')
    lines.append(r'\vspace{0.4cm}')
    lines.append('')
    
    lines.append(r'\begin{center}')
    lines.append(r'\renewcommand{\arraystretch}{2.4}')
    lines.append(r'\begin{tabular}{' + 'c@{\\hspace{28pt}}' * 5 + 'c}')
    
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
    # Create tex directory if it doesn't exist
    os.makedirs('tex', exist_ok=True)
    
    # Generate and save to tex/ directory
    latex_code = generate_drill_sheet()
    output_path = os.path.join('tex', 'division_drill.tex')
    
    with open(output_path, 'w') as f:
        f.write(latex_code)
    
    print(f'Created: {output_path}')
    print('To compile: cd tex && pdflatex division_drill.tex')
