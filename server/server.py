#-*- coding: utf-8 -*-
import web
import json
import sys
sys.path.append('/home/krzysztof/Pulpit/Projekt/engine')
import engine.handle_text as ht
        
urls = (
    '/(.*)', 'comment'
)
app = web.application(urls, globals())

text_handler = ht.CommentHandler()


class comment:        
    def POST(self, name):
        i = web.input().comm
        web.header('Content-Type', 'application/json')
        web.header("Access-Control-Allow-Methods", "GET, POST")   
        print(name + i)
        resp = text_handler.classify(i)
        return json.dumps({'response':resp})


if __name__ == "__main__":
    app.run()
