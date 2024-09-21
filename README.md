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
