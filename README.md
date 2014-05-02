This program requires mod_wsgi and apache2.  It has been written and tested against python3.2

Here's a partial example config for apache2
The assumption is that you want to direct all traffic to this application and that the application
resides at /var/www/RecipeConverter

        <Directory /var/www/RecipeConverter>
                Options Indexes FollowSymLinks MultiViews
                AllowOverride None
                Order allow,deny
                allow from all
                DirectoryIndex handler.wsgi
        </Directory>
        WSGIScriptAlias /handler.wsgi /var/www/RecipeConverter/handler.wsgi
