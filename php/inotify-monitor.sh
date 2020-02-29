#!/bin/sh
while inotifywait -e modify -e create -e delete /var/www/joker/data/www/marvelmind.tjo.biz/licensescron; do
    /var/www/joker/data/www/marvelmind.tjo.biz/licensescron/./incrontab.sh
done