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
    response.menu += [(T('Crear Contrato'),False, '', [['Persona', URL('default','nuevoConPersona')==URL(),URL('default','nuevoConPersona')], 
                                              ['Empresa', URL('default','nuevoConEmpresa')==URL(),URL('default','nuevoConEmpresa')]
                                             ]),
                      (T('Enmendar Contrato'),URL('default','nuevaEnmienda')==URL(),URL('default','nuevaEnmienda'), []),
                      (T('Consultar'),False, '', [['Contratos', URL('default','contratos')==URL(),URL('default','contratos')], 
                                                  ['Enmiendas', URL('default','enmiendas')==URL(),URL('default','enmiendas')]
                                                 ]),
                     ]
