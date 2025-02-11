```
mkdir stock_app
cd stock_app
python -m venv venv
source venv/bin/activate  # On Windows use`venv\Scripts\activate`
pip install Flask yfinance matplotlib numpy
pip install Frozen-Flask
```

```
git init
git add .
git commit -m "Initial commit"
git branch -M gh-pages
git remote add origin https://github.com/yourusername/yourrepository.git
git push -u origin gh-pages
```
