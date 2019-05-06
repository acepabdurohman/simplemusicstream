from musicstreampy import Registration, Package, Transaction, MusicPlayer
import threading, time

class _MusicStream():

    def main(self):
        registration = Registration()
        result = registration.register()
        if result:
            print('Success insert data')        
            self.show_package()
            print('++++Enter Package ID++++')
            pkg_input = input()
            print('++++Enter Email++++')
            email_input = input()
            result = self.do_transaction(email_input, pkg_input)
            print(result)
            if 'success' in result:
                music_player = MusicPlayer()
                self.show_music_list(music_player)
                c = True
                while(c):
                    print('++++Enter ID to play music++++')                
                    music_id = input()
                    res = music_player.check_music_exists(music_id)
                    if res:
                        music_thread = threading.Thread(target=self.listen_song, 
                        args=(music_player, music_id, email_input))    
                        music_thread.start()
                        # use thread method join() to wait until other thread finished
                        # music_thread.join()                
                    else:
                        c = False
        else:
            print('Failed insert data') 

    def listen_song(self, music_player, music_id, email_input):
        current_music = music_player.play_music(music_id)
        print('{} is listening {} by {}'.format(email_input, current_music['title'], current_music['artist']))
        duration = int(current_music['duration'])
        time.sleep(duration)
        print('\nsong with title {} finished'.format(current_music['title']))


    def show_music_list(self, music_player):
        music_player.add_music_list()
        print('List of Music')
        for bankmusic in music_player.bankmusic_list:
            print('Music ID {}, {}, {}, with duration {} seconds'.format(bankmusic['id'], 
            bankmusic['artist'], bankmusic['title'], bankmusic['duration']))

    def show_package(self):
        print("++++Choose package++++")
        package = Package()
        for pkg in package.pkg_data:
            print('Package ID {}, {}, {}'.format(pkg['id'], pkg['name'], pkg['price']))

    def do_transaction(self, email, package):    
        transaction = Transaction(email, package)
        return transaction.add_transaction()

if __name__=='__main__':
    music_stream = _MusicStream()
    music_stream.main()