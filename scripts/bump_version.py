import re
from scriptkit import sh


def main():
    with sh.pipe():
        sh.cat('setup.py')
        version_line = sh.grep('version').lines[0]

    version_number = float(re.findall(r'\d+\.\d+', version_line)[0])
    new_version_line = version_line.replace(str(version_number), str(version_number + 0.1))

    sh.sed('-i', '', f's/{version_line}/{new_version_line}/g', 'setup.py')


if __name__ == '__main__':
    main()