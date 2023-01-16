'''
mp3 플레이어 클래스를 만들고 노래 등록 후 재생해보자
Player
    addSong
    play
    suffle
    setIsLoop
    
Song
    printSongInfo
'''

import mp3player as mp3

song1 = mp3.Song('신호등', '이무진', 3)
song2 = mp3.Song('봄여름가을겨울', '빅뱅', 4)
song3 = mp3.Song('Butter', 'BTS', 2)
song4 = mp3.Song('좋아좋아', '조정석', 4)
song5 = mp3.Song('너와같이', '지바노프', 3)

player = mp3.Player()
player.addSong(song1)
player.addSong(song2)
player.addSong(song3)
player.addSong(song4)
player.addSong(song5)

player.setIsLoop(False)
player.shuffle()
player.play()