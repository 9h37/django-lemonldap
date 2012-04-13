# INSTALLATION

This projet was inspired of ``RemoteUser`` (middleware and backend from Django).

## Tools

* Python/Django
* LemonLDAP::NG
* apache2 + mod_wsgi

## Get the source

Copy the site files :

```
$ cd /var/www
$ git clone git://github.com/9h37/django-lemonldap.git
```

# CONFIGURATION

## Apache2

Copy that into /etc/apache2/django.conf :

```
<VirtualHost *:80>
	ServerName django.9h37-test.fr

	PerlHeaderParserHandler My::Package

	Alias /media/ /var/www/django-lemonldap/lemonsso/media/
	<Directory /var/www/django-lemonldap/lemonsso/media/>
		Order allow,deny
		Allow from all
	</Directory>

	WSGIScriptAlias / /var/www/django-lemonldap/apache/django.wsgi
	<Directory /var/www/django-lemonldap/apache/>
		Order allow,deny
		Allow from all
	</Directory>
</VirtualHost>
```

## LemonLDAP

Add a new virtual host : django.9h37-test.fr
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
