import pytube
link="https://www.youtube.com/watch?v=IUTGFQpKaPU"
yt=pytube.YouTube(link)
yt.streams.get_highest_resolution().download()
print("downloaded",link)