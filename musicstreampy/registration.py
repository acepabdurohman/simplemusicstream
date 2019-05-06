import fileinput

class Registration:

    reg_data = []

    def __init__(self):
        self.acc_file = open('account.txt')

    def register(self):
        try:
            for acc in self.acc_file:
                account = acc.split('|')
                s = account[5]
                saldo = s.replace('\n','')
                email = account[0]
                name = account[1]
                address = account[2]
                age = account[3]
                cc_number = account[4]
                # check whether reg data empty or not
                if len(self.reg_data) == 0:
                    self._add_data(email, name, address, age, cc_number, saldo)
                else:
                    is_member = self.is_member(email)        
                    if not is_member:
                        self._add_data(email, name, address, age, cc_number, saldo)
        except Exception as e:
            print(e)
            return False
        finally:
            self.acc_file.close()
        return True
        
        
    def _add_data(self, email, name, address, age, cc_number, saldo):
        reg = {
            'email': email,
            'name': name,
            'address': address,
            'age': age,
            'cc_number': cc_number,
            'saldo': saldo
        }
        self.reg_data.append(reg)


    def is_member(self, email):
        for r in self.reg_data:
            if email == r['email']:
                return True
        return False


    def update_saldo(self, email, price):
        acc_file = open('account.txt', 'r')
        for acc in acc_file:
            account = acc.split('|')
            if email == account[0]:
                s = account[5]
                saldo = s.replace('\n','')
                updated_saldo = int(saldo) - price
                new_acc = '{}|{}|{}|{}|{}|{}'.format(account[0], account[1], account[2], 
                account[3], account[4], updated_saldo)
            else:
                new_acc += '\n{}|{}|{}|{}|{}|{}'.format(account[0], account[1], account[2], 
                account[3], account[4], account[5])
        acc_file.close()
        
        acc_write = open('account.txt', 'w')
        acc_write.write(new_acc)
        acc_write.close()