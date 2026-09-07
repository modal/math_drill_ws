#!/usr/bin/env python3
"""
Division Drill - Fixed bracket notation
Uses \overline for proper long division rendering
"""

import random


def generate_division_problem(min_dividend=2, max_dividend=15*15, 
                               min_divisor=2, max_divisor=15):
    """Generate a division problem with whole number result."""
    divisor = random.randint(min_divisor, max_divisor)
    quotient = random.randint(min_dividend // divisor, max_dividend // divisor)
    dividend = divisor * quotient
    return dividend, divisor, quotient


def generate_fixed_document(num_problems=90, problems_per_row=5):
    """Generate using proper \overline notation."""
    problems = []
    for _ in range(num_problems):
        dividend, divisor, quotient = generate_division_problem()
        problems.append((dividend, divisor, quotient))
    
    lines = []
    
    lines.append(r'\documentclass[12pt]{article}')
    lines.append(r'\usepackage[margin=0.75in]{geometry}')
    lines.append(r'\usepackage{amsmath}')
    lines.append(r'\usepackage{array}')
    lines.append(r'\pagestyle{empty}')
    lines.append(r'\setlength{\parindent}{0pt}')
    lines.append(r'\setlength{\parskip}{0pt}')
    lines.append('')
    
    lines.append(r'\begin{document}')
    lines.append(r'\begin{center}')
    lines.append(r'{\Large\textbf{Division Practice Drill Sheet}}\\[0.3cm]')
    lines.append(r'Name: \underline{\hspace{6cm}} \hspace{1cm} Date: \underline{\hspace{3cm}}')
    lines.append(r'\end{center}')
    lines.append(r'\vspace{0.5cm}')
    lines.append('')
    
    num_cols = problems_per_row
    total_rows = (num_problems + num_cols - 1) // num_cols
    
    lines.append(r'\begin{center}')
    lines.append(r'\renewcommand{\arraystretch}{2.5}')
    lines.append(r'\begin{tabular}{' + '|c' * num_cols + '|}')
    lines.append(r'\hline')
    
    problem_idx = 0
    for row in range(total_rows):
        row_content = []
        for col in range(num_cols):
            if problem_idx < num_problems:
                dividend, divisor, _ = problems[problem_idx]
                # CORRECT: divisor outside, overline on dividend
                # Format: divisor )̄ dividend  (with line over dividend)
                cell = r'$%d \overline{\smash{)}\, %d}$' % (divisor, dividend)
                row_content.append(cell)
                problem_idx += 1
            else:
                row_content.append('')
        lines.append(' & '.join(row_content) + r' \\ \hline')
    
    lines.append(r'\end{tabular}')
    lines.append(r'\end{center}')
    lines.append(r'\end{document}')
    
    return '\n'.join(lines)


if __name__ == '__main__':
    with open('division_drill.tex', 'w') as f:
        f.write(generate_fixed_document(90))
    print("Created: division_drill.tex")
