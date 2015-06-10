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
def nuevoConPersona():
    form=FORM(DIV(FIELDSET(LEGEND('Datos Personales'),
                       DIV(LABEL('Nombres Completos'),INPUT(_name='nombres', _placeholder='Nombres Completos', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Apellidos Completos'),INPUT(_name='apellidos', _placeholder='Apellidos Completos', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Documento de Identidad'),INPUT(_name='idPersona', _type='number', _placeholder='Documento de Identidad', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Teléfono'),INPUT(_name='telefono', _type='number', _placeholder='Teléfono', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Profesión'),INPUT(_name='profesion', _placeholder='Profesión', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Experiencia'), TEXTAREA(_name='experienciaX', _placeholder='Experiencia', requires=IS_NOT_EMPTY())),
                       DIV(LEGEND('Domicilio Personal'),
                           DIV(LABEL('Direccion'),INPUT(_name='direccionX', _placeholder='Direccion', requires=IS_NOT_EMPTY())),
                           DIV(LABEL('Ciudad'),INPUT(_name='ciudad', _placeholder='Ciudad', requires=IS_NOT_EMPTY())),
                           DIV(LABEL('Pais'),INPUT(_name='paisPersona', _placeholder='Pais', requires=IS_NOT_EMPTY())),
                          ),
                      ),
                  FIELDSET(LEGEND('Objeto'),
                       DIV(LABEL('Nombre de la Consultoría'),INPUT(_name='consultoria', _placeholder='Nombre de la Consultoría', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Descripción'), TEXTAREA(_name='descripcionX', _placeholder='Descripción', requires=IS_NOT_EMPTY())),
                       DIV(LEGEND('Obligaciones Adicionales'),
                           DIV(INPUT(_type='radio', _name='rbnObligaciones', _value=True), ' Existen'),
                           DIV(INPUT(_type='radio', _name='rbnObligaciones', _value=False, _checked=True), ' No Existen'),
                           DIV(TEXTAREA(_name='obligacionesAdicionalesX', _placeholder='Si aplica')),
                          ),
                      ),
                 _class='columna',
                 ),
              DIV(FIELDSET(LEGEND('Duracion y Honorarios'),
                       DIV(LABEL('Fecha de Inicio'),INPUT(_name='fechaInicio', _type='date', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Fecha de Fin'),INPUT(_name='fechaFin', _type='date', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Monto'), INPUT(_name='monto', _type='number', _placeholder='Monto', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Pais'),INPUT(_name='paisContrato', _placeholder='Pais', requires=IS_NOT_EMPTY())),
                       DIV(LEGEND('IVA'),
                           DIV(INPUT(_type='radio', _name='rbnIVA', _value=True), ' Incluye'),
                           DIV(INPUT(_type='radio', _name='rbnIVA', _value=False, _checked=True), ' No Incluye'),
                           _class='honorarios',
                          ),
                       DIV(LEGEND('IR'),
                           DIV(INPUT(_type='radio', _name='rbnIR', _value=True), ' Incluye'),
                           DIV(INPUT(_type='radio', _name='rbnIR', _value=False, _checked=True), ' No Incluye'),
                           _class='honorarios',
                          ),
                       DIV(LEGEND('Gastos de Viaje'),
                           DIV(INPUT(_type='radio', _name='rbnGastos', _value=True), ' Incluye'),
                           DIV(INPUT(_type='radio', _name='rbnGastos', _value=False, _checked=True), ' No Incluye'),
                           _class='honorarios',
                          ),
                       DIV(LABEL('Forma de Pago'), SPAN('En caso de ser pagos parciales indicar porcentajes o valores, productos y fechas previstas separados con punto y coma (;)'), TEXTAREA(_name='formaPagoX', _placeholder='Forma de Pago', requires=IS_NOT_EMPTY())),
                      ),
                  FIELDSET(LEGEND('Datos Bancarios'),
                       DIV(LABEL('Nombre del Banco'),INPUT(_name='nombreBanco', _placeholder='Nombre del Banco', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Número de Cuenta'),INPUT(_name='numeroCuenta', _type='number', _placeholder='Número de Cuenta', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Tipo de Cuenta'),INPUT(_name='tipo', _placeholder='Si aplica')),
                       DIV(LABEL('Código SWIFT'),INPUT(_name='swift', _placeholder='Si aplica')),
                      ),
                  FIELDSET(LEGEND('Datos Internos'),
                       DIV(LABEL('Fecha de Firma'),INPUT(_name='fechaFirma', _type='date', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Proyecto'),INPUT(_name='proyecto', _placeholder='Proyecto', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Fecha de Elaboracion'),INPUT(_name='fechaElaboracionX', _type='date', requires=IS_NOT_EMPTY())),
                      ),
                 _class='columna',
                 ),
              DIV(INPUT(_type='submit',_value='Crear', _class='btnEnviar'))
             )
    if form.accepts(request,session):
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    return dict(form=form)

@auth.requires_login()
def nuevoConEmpresa():
    form=FORM(DIV(FIELDSET(LEGEND('Datos Generales'),
                       DIV(LABEL('Nombre del Representante'),INPUT(_name='nombresPersona', _placeholder='Nombre del Representante', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Apellido  del Representante'),INPUT(_name='apellidosPersona', _placeholder='Apellido del Representante', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Documento de Identidad del Representante'),INPUT(_name='idPersona', _type='number', _placeholder='Documento de Identidad del Representante', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Nombre de la Empresa'),INPUT(_name='nombreEmpresa', _placeholder='Nombre de la Empresa', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('RUC de la Empresa'),INPUT(_name='ruc', _type='number', _placeholder='RUC de la Empresa', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Teléfono'),INPUT(_name='telefono', _type='number', _placeholder='Teléfono', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Especialización'),INPUT(_name='especializacion', _placeholder='Especialización', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Experiencia'), TEXTAREA(_name='experienciaX', _placeholder='Experiencia', requires=IS_NOT_EMPTY())),
                       DIV(LEGEND('Ubicación Empresa'),
                           DIV(LABEL('Direccion'),INPUT(_name='direccionX', _placeholder='Direccion', requires=IS_NOT_EMPTY())),
                           DIV(LABEL('Ciudad'),INPUT(_name='ciudad', _placeholder='Ciudad', requires=IS_NOT_EMPTY())),
                           DIV(LABEL('Pais'),INPUT(_name='paisEmpresa', _placeholder='Pais', requires=IS_NOT_EMPTY())),
                          ),
                      ),
                  FIELDSET(LEGEND('Objeto'),
                       DIV(LABEL('Nombre de la Consultoría'),INPUT(_name='consultoria', _placeholder='Nombre de la Consultoría', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Descripción'), TEXTAREA(_name='descripcionX', _placeholder='Descripción', requires=IS_NOT_EMPTY())),
                       DIV(LEGEND('Obligaciones Adicionales'),
                           DIV(INPUT(_type='radio', _name='rbnObligaciones', _value=True), ' Existen'),
                           DIV(INPUT(_type='radio', _name='rbnObligaciones', _value=False, _checked=True), ' No Existen'),
                           DIV(TEXTAREA(_name='obligacionesAdicionalesX', _placeholder='Si aplica')),
                          ),
                      ),
                 _class='columna',
                 ),
              DIV(FIELDSET(LEGEND('Duracion y Honorarios'),
                       DIV(LABEL('Fecha de Inicio'),INPUT(_name='fechaInicio', _type='date', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Fecha de Fin'),INPUT(_name='fechaFin', _type='date', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Monto'), INPUT(_name='monto', _type='number', _placeholder='Monto', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Pais'),INPUT(_name='paisContrato', _placeholder='Pais', requires=IS_NOT_EMPTY())),
                       DIV(LEGEND('IVA'),
                           DIV(INPUT(_type='radio', _name='rbnIVA', _value=True), ' Incluye'),
                           DIV(INPUT(_type='radio', _name='rbnIVA', _value=False, _checked=True), ' No Incluye'),
                           _class='honorarios',
                          ),
                       DIV(LEGEND('IR'),
                           DIV(INPUT(_type='radio', _name='rbnIR', _value=True), ' Incluye'),
                           DIV(INPUT(_type='radio', _name='rbnIR', _value=False, _checked=True), ' No Incluye'),
                           _class='honorarios',
                          ),
                       DIV(LEGEND('Gastos de Viaje'),
                           DIV(INPUT(_type='radio', _name='rbnGastos', _value=True), ' Incluye'),
                           DIV(INPUT(_type='radio', _name='rbnGastos', _value=False, _checked=True), ' No Incluye'),
                           _class='honorarios',
                          ),
                       DIV(LABEL('Forma de Pago'), SPAN('En caso de ser pagos parciales indicar porcentajes o valores, productos y fechas previstas separados con punto y coma (;)'), TEXTAREA(_name='formaPagoX', _placeholder='Forma de Pago', requires=IS_NOT_EMPTY())),
                      ),
                  FIELDSET(LEGEND('Datos Bancarios'),
                       DIV(LABEL('Nombre del Banco'),INPUT(_name='nombreBanco', _placeholder='Nombre del Banco', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Número de Cuenta'),INPUT(_name='numeroCuenta', _type='number', _placeholder='Número de Cuenta', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Tipo de Cuenta'),INPUT(_name='tipo', _placeholder='Si aplica')),
                       DIV(LABEL('Código SWIFT'),INPUT(_name='swift', _placeholder='Si aplica')),
                      ),
                  FIELDSET(LEGEND('Datos Internos'),
                       DIV(LABEL('Fecha de Firma'),INPUT(_name='fechaFirma', _type='date', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Proyecto'),INPUT(_name='proyecto', _placeholder='Proyecto', requires=IS_NOT_EMPTY())),
                       DIV(LABEL('Fecha de Elaboracion'),INPUT(_name='fechaElaboracionX', _type='date', requires=IS_NOT_EMPTY())),
                      ),
                 _class='columna',
                 ),
              DIV(INPUT(_type='submit',_value='Crear', _class='btnEnviar'))
             )
    if form.accepts(request,session):
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    return dict(form=form)

@auth.requires_login()
def nuevaEnmienda():
    form1=FORM(FIELDSET(LEGEND('Contrato'),
                        DIV(
                            DIV(LABEL('Número de Contrato'),INPUT(_name='contrato', _type='number', _placeholder='Número de Contrato', requires=IS_NOT_EMPTY())),
                            DIV(INPUT(_type='submit',_value='IR')),
                            _class='columna',
                           ),
                        DIV(
                            DIV(LABEL('Nombre Contratista'),INPUT(_name='nombres', _readonly=ON)),
                            DIV(LABEL('Documento de Identidad'),INPUT(_name='documentoId', _readonly=ON)),
                            DIV(LABEL('Fecha Contrato'),INPUT(_name='fechaFirmaContrato', _type='date', _readonly=ON)),
                            _class='columna',
                           )
                       )
              )
    form2=FORM(DIV(FIELDSET(LEGEND('Objeto'),
                           DIV(LABEL('Nombre de la Consultoría'),INPUT(_name='consultoria', _placeholder='Nombre de la Consultoría', requires=IS_NOT_EMPTY())),
                           DIV(LABEL('Descripción'), TEXTAREA(_name='descripcionX', _placeholder='Descripción', requires=IS_NOT_EMPTY())),
                           DIV(LEGEND('Obligaciones Adicionales'),
                               DIV(INPUT(_type='radio', _name='rbnObligaciones', _value=True), ' Existen'),
                               DIV(INPUT(_type='radio', _name='rbnObligaciones', _value=False, _checked=True), ' No Existen'),
                               DIV(TEXTAREA(_name='obligacionesAdicionalesX', _placeholder='Si aplica')),
                              ),
                           ),
                   FIELDSET(LEGEND('Duración'),
                            DIV(LABEL('Fecha de Inicio'),INPUT(_name='fechaInicio', _type='date', requires=IS_NOT_EMPTY())),
                            DIV(LABEL('Fecha de Fin'),INPUT(_name='fechaFin', _type='date', requires=IS_NOT_EMPTY())),
                           ),
                 _class='columna',
                 ),
               DIV(FIELDSET(LEGEND('Honorarios'),
                            DIV(LABEL('Monto'), INPUT(_name='monto', _type='number', _placeholder='Monto', requires=IS_NOT_EMPTY())),
                            DIV(LEGEND('IVA'),
                                DIV(INPUT(_type='radio', _name='rbnIVA', _value=True), ' Incluye'),
                                DIV(INPUT(_type='radio', _name='rbnIVA', _value=False, _checked=True), ' No Incluye'),
                                _class='honorarios',
                               ),
                            DIV(LEGEND('IR'),
                                DIV(INPUT(_type='radio', _name='rbnIR', _value=True), ' Incluye'),
                                DIV(INPUT(_type='radio', _name='rbnIR', _value=False, _checked=True), ' No Incluye'),
                                _class='honorarios',
                               ),
                            DIV(LEGEND('Gastos de Viaje'),
                                DIV(INPUT(_type='radio', _name='rbnGastos', _value=True), ' Incluye'),
                                DIV(INPUT(_type='radio', _name='rbnGastos', _value=False, _checked=True), ' No Incluye'),
                                _class='honorarios',
                               ),
                            DIV(LABEL('Forma de Pago'), SPAN('En caso de ser pagos parciales indicar porcentajes o valores, productos y fechas previstas separados con punto y coma (;)'), TEXTAREA(_name='formaPagoX', _placeholder='Forma de Pago', requires=IS_NOT_EMPTY())),
                           ),
                   FIELDSET(LEGEND('Datos Internos'),
                            DIV(LABEL('Fecha de Firma'),INPUT(_name='fechaFirma', _type='date', requires=IS_NOT_EMPTY())),
                            DIV(LABEL('Proyecto'),INPUT(_name='proyecto', _placeholder='Proyecto', requires=IS_NOT_EMPTY())),
                            DIV(LABEL('Fecha de Elaboracion'),INPUT(_name='fechaElaboracionX', _type='date', requires=IS_NOT_EMPTY())),
                           ),
                   _class='columna',
                  ),
               DIV(INPUT(_type='submit',_value='Crear', _class='btnEnviar'))
              )
    if form1.accepts(request,session):
        response.flash = 'form1 accepted'
    elif form1.errors:
        response.flash = 'form1 has errors'
    if form2.accepts(request,session):
        response.flash = 'form accepted'
    elif form2.errors:
        response.flash = 'form has errors'
    return dict(form1=form1, form2=form2)

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
