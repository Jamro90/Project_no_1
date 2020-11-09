make:
	python data.py
install:
	pyinstaller data.py --onefile
	rm -r data.spec build
remove:
	rm data
change:
	mv data.txt data.dat
