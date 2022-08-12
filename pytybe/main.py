# установка пакета: pip install pytube

import pytube

yt = pytube.YouTube('https://www.youtube.com/watch?v=xtZOnyYu16U')

fn = yt.filename #информация о данном видео, для просмотра нужно ввести в концоли 
# имя переменной (fn) и нажать Enter

videos = yt.get_videos()
for v in videos:
    print(v) #доступные для скачивания видео
    
    for v in videos:
    print(type(v))
    
    first_video = videos[0]
print(first_video)

first_video.download('/Users/Denis/Desktop') #скачивает видео на рабочий стол