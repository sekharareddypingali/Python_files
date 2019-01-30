try:
    with open('hello.txt','r') as f:
        x=f.reads()
except I/Oerror:
    print "error"
else:
    print x
finally:
    print "Done my job!"


