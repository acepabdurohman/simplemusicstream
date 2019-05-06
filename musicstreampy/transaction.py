from . import Registration, Package

class Transaction:

    def __init__(self, email, package_id):
        self.email = email
        self.package_id = package_id
        self.trx_file = open("transaction.txt", 'w')

    def add_transaction(self):
        try:
            email = self.email
            package_id = self.package_id

            registration = Registration()
            is_member = registration.is_member(email)
            if is_member:

                package = Package()
                pkg = package.get_package_by_id(package_id)
                if pkg is not None:
                    registration.update_saldo(email, int(pkg['price']))                    
                    data = '{}|{}'.format(email, package_id)
                    self.trx_file.write(data)
                else:
                    return "Package not found"                
            else:
                return "Member not found"            
        except Exception as e:
            print(e)
        finally:
            self.trx_file.close()
        return "Transaction success, your balance has been updated"