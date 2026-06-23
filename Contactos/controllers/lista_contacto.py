import web

render = web.template.render('views')

class Lista_contacto:
    def GET(self):
        return render.lista_contacto()