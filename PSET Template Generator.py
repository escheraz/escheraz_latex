from os import path

_class = input("Enter Class: ")
psetnum = input("Enter PSET number: ")
filename = _class + " PSET " + psetnum + ".tex"

if(path.exists(filename)):
	s = input("File " + filename + " already exists! Overwrite? (y/n): ")
	if s != "y":
		exit()
collab = input("Include Collaborators? (y/n): ")
alph = input("Number Problems Alphabetically? (y/n): ")
zeroidx = None
if alph == 'n':
	zeroidx = input("Zero-index problem numbers? (y/n): ")

output = r"""\documentclass{article}
\usepackage{enumitem}
\usepackage{amsmath}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{amssymb}
\usepackage{tcolorbox}
\usepackage[edges]{forest}
\usepackage{fancyhdr}
\usepackage[margin=1in, top=1.35in]{geometry}
\usepackage{tikz}
\setlength{\parindent}{0pt}
\setlength{\parskip}{7pt plus 1pt minus 1pt}
\newcounter{problemnum}
\setcounter{problemnum}{0}
\pagestyle{fancy}
\renewcommand{\headrulewidth}{1.5pt}
\newcommand{\problem}{\stepcounter{problemnum} \begin{center} \Large \textbf{Problem \Alph{problemnum}} \normalsize \\\vspace{0.2cm} \textit{Collaborators: #1}\\\vspace{0.2cm}\end{center}}
\newcommand\name{Name}
\newcommand\email{Email}
\newcommand\class{_class}
\newcommand\psetnum{psetnuminput}
\lhead{\name}
\chead{\email}
\rhead{\class\, Problem Set \psetnum}
\begin{document}
"""
if alph == 'n':
	output = output.replace(r'\Alph{problemnum}', r'\theproblemnum')
	if zeroidx == 'y':
		output = output.replace(r'\stepcounter{problemnum} ', '')
if collab == 'n':
	output = output.replace(r' \textit{Collaborators: #1}\\\vspace{0.2cm}', '')

output = output.replace('_class', _class)
output = output.replace('psetnuminput', psetnum)

numProbs = int(input("Enter number of problems: "))

for i in range(numProbs):
	if collab == "y":
		output += "\n\\problem{none}\n"
	else:
		output += "\n\\problem\n"

	n = int(input("Number of subparts for problem " + str(i + (0 if zeroidx=='y' else 1)) + ": "))
	if n != 1:
		if alph == "y":
			output += "\\begin{enumerate}\n"
		else:
			output += "\\begin{enumerate}[label=(\\alph*)]\n"
		for i in range(n):
			output += "\t\\item \n"
		output += "\\end{enumerate}\n"		
	output += "\\newpage\n"
output += "\n\\end{document}"

f = open(f"{_class}/{filename}", "w")
f.write(output)
f.close()
print("File " + filename + " successfully written.")
