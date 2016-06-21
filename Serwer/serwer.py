#-*- coding: utf-8 -*-
import web
import json
import sys
sys.path.append('/home/krzysztof/Pulpit/Projekt/Silnik')
import handleText as ht
        
urls = (
    '/(.*)', 'comment'
)
app = web.application(urls, globals())

textHandler = ht.CommentHandler()

class comment:        
    #def GET(self, name):
    #    if not name: 
    #        name = 'World'
    #    return 'Hello, ' + name + '!'

    def POST(self, name):
        i = web.input().comm
        web.header('Content-Type', 'application/json')
        web.header("Access-Control-Allow-Methods", "GET, POST")   
        print name + i
        resp = textHandler.classify(i)
        return json.dumps({'response':resp})

if __name__ == "__main__":
    app.run()
