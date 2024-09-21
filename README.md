# Dash React Simple Maps

Demo:

```sh
python usage.py
```

Open: http://localhost:8050

## Setup

```sh
npm install
pip install -r requirements.txt
pip install -r tests/requirements.txt
```

## Development

```sh
npm run build
python usage.py
```


## Release

```sh
# generate
npm run build
python setup.py sdist bdist_wheel
ls dist

# test artifact
pip install dash dist/dash_react_simple_maps-0.0.1.tar.gz
python usage.py

# upload
pip install twine
twine upload dist/*

# clean up
rm -rf dist
```

To upgrade the version change `version` in `package.json`

5. Share your component with the community! https://community.plotly.com/c/dash
    1. Publish this repository to GitHub
    2. Tag your GitHub repository with the plotly-dash tag so that it appears here: https://github.com/topics/plotly-dash
    3. Create a post in the Dash community forum: https://community.plotly.com/c/dash
