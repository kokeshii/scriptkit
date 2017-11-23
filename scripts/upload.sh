python scripts/bump_version.py
rm -rf dist/
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*
