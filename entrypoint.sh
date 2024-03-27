#!/bin/bash

echo "Executing supervisord command..."

# Load environment variables from .env file
echo "Loading environment variables from .env file..."
source /app/gitignored/.env

# Generate supervisord.conf dynamically with substituted values
echo "Generating supervisord.conf with substituted values..."
cat > /app/supervisor/supervisord.conf << EOF
[supervisord]
nodaemon=true
logfile=/dev/null
logfile_maxbytes=0

[unix_http_server]
file=/tmp/supervisor.sock

[supervisorctl]
serverurl=unix:///tmp/supervisor.sock

[program:gunicorn]
command=gunicorn MyFin50d_project.wsgi:application --bind 0.0.0.0:8000
autostart=true
autorestart=unexpected
stdout_logfile=/tmp/gunicorn.log
stderr_logfile=/tmp/gunicorn_error.log
stdout_logfile_maxbytes=10MB  ; Maximum size of stdout logfile before rotation
stderr_logfile_maxbytes=10MB  ; Maximum size of stderr logfile before rotation
stdout_logfile_backups=7      ; Number of stdout logfile backups to keep
stderr_logfile_backups=7      ; Number of stderr logfile backups to keep
redirect_stderr=true          ; Redirect stderr to stdout (to have both outputs in one file, set stderr_logfile to /dev/null if separate files are not needed)

[inet_http_server]
port=0.0.0.0:9001  # Make sure this port is exposed in your Docker container and docker-compose.yml
username=${SUPERVISOR_USERNAME}
password=${SUPERVISOR_PASSWORD}
EOF

# Start supervisord
echo "Starting supervisord..."
supervisord -c /app/supervisor/supervisord.conf
