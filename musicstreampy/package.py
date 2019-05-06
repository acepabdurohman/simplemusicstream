class Package:

    pkg_data = []

    def __init__(self):
        pkg_file = open('package.txt')
        self.add_data(pkg_file)

    def add_data(self, pkg_file):
        for line in pkg_file:
            package = line.split('|')
            id = package[0]
            name = package[1]
            price = package[2]
            pr = price.replace('\n', '')
            pkg_dict = {
                'id': id,
                'name': name,
                'price': pr
            }
            self.pkg_data.append(pkg_dict)
        pkg_file.close()

    def get_package_by_id(self, id):
        for pkg in self.pkg_data:
            if pkg['id'] == id:
                return pkg
        return None