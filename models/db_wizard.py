### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_empresa',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_dbname', type='string',
          label=T('Dbname')),
    Field('f_start_subscription_date', type='datetime',
          label=T('Start Subscription Date')),
    Field('f_end_subscription_date', type='datetime',
          label=T('End Subscription Date')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_empresa_archive',db.t_empresa,Field('current_record','reference t_empresa',readable=False,writable=False))
