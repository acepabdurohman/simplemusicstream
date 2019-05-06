class MusicPlayer:

    bankmusic_list = []

    def __init__(self):
        self.bm_file = open('bankmusic.txt', 'r')

    def add_music_list(self):
        bm_file = self.bm_file
        for data in bm_file:
            dt = data.split('|')
            duration = dt[3].replace('\n', '')
            bankmusic = {
                'id': dt[0],
                'artist': dt[1],
                'title': dt[2],
                'duration': duration
            }            
            self.bankmusic_list.append(bankmusic)
        self.bm_file.close()

    def check_music_exists(self, id):
        for bankmusic in self.bankmusic_list:
            if id == bankmusic['id']:
                return True
        return False

    def play_music(self, id):
        bankmusic_list = self.bankmusic_list
        size = len(bankmusic_list)
        for i in range(0, size, 1):
            if id == bankmusic_list[i]['id']:
                return bankmusic_list[i]
        return None