# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def nuevo():
    return dict()

@auth.requires_login()
def editar():
    return dict()

@auth.requires_login()
def buscar():
    return dict()


@auth.requires_membership("Super Admin")
def admin():
    if request.args(0) == 'select':
        redirect(URL('tabla',args=[request.args(1)]))
    else:
        tables = crud.tables()
        return dict(tables = tables)

@auth.requires_membership("Super Admin")
def tabla():
    table=db[request.args(0)]
    form = crud.update(table,request.args(1))
    table.id.represent = lambda id, row:        A('Editar: ',id,_href=URL(args=(request.args(0),id)))
    search, rows = crud.search(table)
    return dict(form=form,search=search,rows=rows)

@auth.requires_membership("Administrador de empresa")
def crear_usuarios():
    for empresa in db(db.auth_user.id==auth.user.id).select(db.auth_user.f_empresa):
        idEmpresa = empresa.f_empresa
    table=db["auth_user"]
    form = crud.update(table,request.args(1), fields=['id', 'first_name', 'last_name', 'email', 'password'], hidden=dict(empresa=idEmpresa))
    table.id.represent = lambda id, row:        A('Editar: ',id,_href=URL(args=("auth_user",id)))
    search, rows = crud.search(table,query=(db.auth_user.f_empresa==idEmpresa), fields=['id', 'first_name', 'last_name', 'email'])
    return dict(form=form,search=search,rows=rows)
