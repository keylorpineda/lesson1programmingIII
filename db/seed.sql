INSERT INTO clientes (nombre, email) VALUES
 ('Ana López', 'ana@example.com'),
 ('Carlos Pérez', 'carlos@example.com'),
 ('María Gómez', 'maria@example.com');

INSERT INTO compras (cliente_id, fecha, total) VALUES
 (1, datetime('now', '-2 days'), 120.50),
 (1, datetime('now', '-1 days'),  75.00),
 (2, datetime('now'),             210.99);
