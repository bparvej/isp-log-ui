CREATE TABLE IF NOT EXISTS isp_logs (
    id SERIAL PRIMARY KEY,
    log_date DATE,
    log_time TIME,
    ip_address VARCHAR(45),
    username VARCHAR(100),
    message TEXT
);

INSERT INTO isp_logs (log_date, log_time, ip_address, username, message)
VALUES
('2026-01-15','10:22:01','103.12.45.10','pppoe01','User login successful'),
('2026-01-15','11:05:12','103.12.45.11','pppoe02','User disconnected'),
('2026-01-16','09:45:44','103.12.45.10','corpA','Authentication failed');
('2026-01-15','10:22:01','103.12.45.10','pppoe01','User login successful'),
('2026-01-15','11:05:12','103.12.45.11','pppoe02','User disconnected'),
('2026-01-16','09:45:44','103.12.45.10','corpA','Authentication failed');
('2026-01-15','10:22:01','103.12.45.10','pppoe01','User login successful'),
('2026-01-15','11:05:12','103.12.45.11','pppoe02','User disconnected'),
('2026-01-16','09:45:44','103.12.45.10','corpA','Authentication failed');
('2026-01-15','10:22:01','103.12.45.10','pppoe01','User login successful'),
('2026-01-15','11:05:12','103.12.45.11','pppoe02','User disconnected'),
('2026-01-16','09:45:44','103.12.45.10','corpA','Authentication failed');
