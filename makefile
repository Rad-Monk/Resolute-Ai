git:
	git pull
	git add *
	git commit
	git push

format:
	black *.py

run:
	streamlit run main.py

	