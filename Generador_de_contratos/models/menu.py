response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
]
if(auth.has_membership(role = 'Super Admin')):
    response.menu += [(T('Administracion'),URL('default','admin')==URL(),URL('default','admin'),[]),
]
elif(auth.has_membership(role = 'Administrador de empresa')):
    response.menu += [(T('Administracion'),URL('default','crear_usuarios')==URL(),URL('default','crear_usuarios'),[]),
]
elif(auth.user_id != None ):
    response.menu += [(T('Nuevo'),URL('default','nuevo')==URL(),URL('default','nuevo'),[]),
(T('Editar'),URL('default','editar')==URL(),URL('default','editar'),[]),
(T('Buscar'),URL('default','buscar')==URL(),URL('default','buscar'),[]),
]
