#!/bin/sh
while inotifywait -e modify -e create -e delete /var/www/joker/data/www/marvelmind.tjo.biz/licensescron; do
    cd /var/www/joker/data/www/marvelmind.tjo.biz/licensescron/
    /usr/bin/php getExitCodePython.php
done