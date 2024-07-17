git:
	git pull
	git add -A
	git commit
	git push

format:
	black *.py

run:
	streamlit run main.py

install:
	pip --upgrade pip&&\
	pip install -r requirements.txt

	