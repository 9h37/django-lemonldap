# INSTALLATION

This projet was inspired of ``RemoteUser`` (middleware and backend from Django).

## Tools

* Python/Django
* LemonLDAP::NG
* apache2 + mod_wsgi

## Get the source

```
$ git clone git://github.com/9h37/django-lemonldap.git
$ cd django-lemonldap
# python setup.py install
```

The ``middleware`` and the ``backend`` are installed in ``/usr/local/lib/python2.7/dist-packages/``, you
just need to import the Django application ``django_lemonldap.lemonsso.auth``.

The sample website is located at ``/usr/local/share/django-lemonldap``, a sample apache2 configuration is
automatically installed.

## LemonLDAP

Add a new virtual host : django-test.example.com
Add new HTTP header :

* Auth-Name = $cn
* Auth-User = $uid
* Auth-Mail = $mail

Be sure that cn, uid and mail are exported :

```
.
`-+ Variables
  `-+ Attributes to export
    |-- cn = cn
    |-- uid = uid
    `-- mail = mail
```

