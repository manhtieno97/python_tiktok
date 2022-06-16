import pytube
def download(link, path, name):
    try: 
        yt = pytube.YouTube(link)
    except: 
         print("Connection Error") #to handle exception 
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path = path, filename=name)