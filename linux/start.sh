systemctl start nginx
cd /mnt/cingta/new_cingtaweb/ct-web/
pm2 start npm [--name 'final-project'] -- start
su cingta
uwsgi --ini /mnt/cingta/new_cingtaweb/new_cingtaweb_uwsgi.ini &
