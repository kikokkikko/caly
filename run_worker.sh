source ./envCaly/bin/activate 
#NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program celery -A sync_worker worker --loglevel=debug -f log_sync_worker.log
celery -A cron_worker worker --beat