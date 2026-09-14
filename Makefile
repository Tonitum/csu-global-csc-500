module%:
	cd modules/module1/
	pandoc -f markdown -t docx -o module1.docx README.md
	ls | grep *.docx

