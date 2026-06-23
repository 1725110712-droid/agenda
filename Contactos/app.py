import web

urls = (
    '/', 'controllers.index.index',
    '/borrar_contacto', 'controllers.borrar_contacto.borrar_contacto'
    '/editar_contacto', 'controllers.editar_contacto.editar_contacto'
    '/insertar_contacto', 'controllers.insertar_contacto.insertar_contacto'
    '/lista_contacto', 'controllers.lista_contacto.lista_contacto'
    '/ver_contacto', 'controllers.ver_contacto.ver_contacto'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
