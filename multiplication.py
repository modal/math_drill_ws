#!/usr/bin/env python3
"""
Multiplication Drill Sheet Generator
- No title - just problems
- Filename: multiplication_drill_YYYYMMDD_HHMM.tex
"""

import os
import random
import subprocess
from datetime import datetime

# CONFIG: Set total number of problems (must be divisible by 6)
NUM_PROBLEMS = 120


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
    """Generate LaTeX with configurable number of problems."""
    if NUM_PROBLEMS % 6 != 0:
        raise ValueError(f"NUM_PROBLEMS ({NUM_PROBLEMS}) must be divisible by 6")
    
    num_rows = NUM_PROBLEMS // 6
    
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
    
    for row in range(num_rows):
        row_content = []
        for col in range(6):
            factor1, factor2 = generate_problem()  # Generate on-the-fly
            cell = r'$%d \times %d = \underline{\hspace{1cm}}$' % (factor1, factor2)
            row_content.append(cell)
        lines.append(' & '.join(row_content) + r' \\')
    
    lines.append(r'\end{tabular}')
    lines.append(r'\end{center}')
    lines.append('')
    lines.append(r'\end{document}')
    
    return '\n'.join(lines)


def compile_tex_to_pdf(tex_path, pdf_dir):
    """Compile .tex file to PDF using pdflatex, output to pdf_dir."""
    tex_dir = os.path.dirname(tex_path)
    tex_file = os.path.basename(tex_path)
    
    try:
        # Run pdflatex twice to resolve references (standard practice)
        for _ in range(2):
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', '-output-directory', pdf_dir, tex_path],
                capture_output=True,
                text=True,
                check=True
            )
        
        pdf_filename = tex_file.replace('.tex', '.pdf')
        pdf_path = os.path.join(pdf_dir, pdf_filename)
        print(f'PDF created: {pdf_path}')
        return pdf_path
        
    except subprocess.CalledProcessError as e:
        print(f'Error compiling PDF: {e}')
        print(f'stdout: {e.stdout[-500:]}')  # Last 500 chars
        print(f'stderr: {e.stderr[-500:]}')
        return None
    except FileNotFoundError:
        print('ERROR: pdflatex not found in PATH')
        print('Make sure MiKTeX or TeX Live is installed and pdflatex is in your system PATH')
        return None


if __name__ == '__main__':
    # Create output directories
    tex_dir = 'tex'
    pdf_dir = 'pdf'
    os.makedirs(tex_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    filename = f'multiplication_drill_{timestamp}.tex'
    tex_path = os.path.join(tex_dir, filename)
    
    # Generate .tex file
    with open(tex_path, 'w') as f:
        f.write(generate_drill_sheet())
    
    print(f'Created: {tex_path} with {NUM_PROBLEMS} problems ({NUM_PROBLEMS//6} rows)')
    
    # Auto-compile to PDF (saved to pdf/ directory)
    print('Compiling to PDF...')
    compile_tex_to_pdf(tex_path, pdf_dir)