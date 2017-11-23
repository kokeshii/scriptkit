from scriptkit import sh


def release():
    sh.python('setup.py sdist')
    sh.python('setup.py bdist_wheel')
    sh.twine('upload', 'dist/*')


if __name__ == '__main__':
    release()
