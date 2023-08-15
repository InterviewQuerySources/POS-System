import pip

# run this file first to install the required dependencies

dependency_list = ['mysql-connector-python', 'flask']


def main():
    print('Now retrieving project dependencies...')
    for dependency in dependency_list:
        print('Installing package:', dependency)
        pip.main(['install', dependency])
        print('Installed package:', dependency)
    print('Now creating the database')


if __name__ == '__main__':
    main()
