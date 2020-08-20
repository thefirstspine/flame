#!/bin/sh

# Import base data to PostgreSQL
if [ "${FLAME_POSTGRESQL_DUMP_FILE}" ]; then
  service postgresql start 1> /dev/null
  sudo -u postgres psql -c "CREATE USER flame WITH password 'flame'" 1> /dev/null
  sudo -u postgres psql -c "GRANT postgres TO flame" 1> /dev/null
  sudo -u postgres psql -c "CREATE DATABASE flame" 1> /dev/null
  sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE flame TO flame" 1> /dev/null
  psql "postgresql://flame:flame@localhost/flame" < "/flame-volume/${FLAME_POSTGRESQL_DUMP_FILE}" 1> /dev/null
fi

eval "$@"
