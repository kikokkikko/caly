source envCaly/bin/activate 
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program \
celery -A sync_worker worker --loglevel=debug -f log/log_sync_worker.log -n firstSyncWorker


