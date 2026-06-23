import web 

render = web.template.render('views')

class index:
    def GET(self):
        return render.index()
