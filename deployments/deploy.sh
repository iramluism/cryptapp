#!/bin/sh
# start.sh

# Iniciar el servidor
exec uvicorn main:create_app --port 8000 --loop asyncio --reload