from threading import Timer

def hello():
    print "hello, world"
    Timer(1.0, hello).start()


hello()
# Timer(5.0, hello).start()