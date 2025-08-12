# Clientes-Compras (Flask + SQLite + JavaFX)

## Ejecutar la API (Docker)
```bash
docker compose build
docker compose up -d
# cargar esquema y datos iniciales dentro del volumen (una vez)
docker exec -i api-service sh -c "sqlite3 /data/app.db < /app/../db/schema.sql"
docker exec -i api-service sh -c "sqlite3 /data/app.db < /app/../db/seed.sql"
# probar
curl http://localhost:8000/clientes
```

## Ejecutar el cliente JavaFX
```bash
cd frontend-javafx
mvn -q javafx:run
```
