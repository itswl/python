import douyin 
from douyin.structures import Topic, Music
video_file_handler = douyin.handlers.VideoFileHandler(folder=' ./videos')
music_file_handler = douyin.handlers.MusicFileHandler(folder=' . /musics')
mongo_handler = douyin.handlers.MongoHandler()

#定义下载器，并将三个处理器当做参数传递

downloader = douyin.downloaders.VideoDownloader([mongo_handler,video_file_handler,music_file_handler])#循环爬取抖音 热榜信息并下载存储

for result in douyin.hot.trend() :

    for item in result .data:
        downloader.download(item.videos(max=100))




