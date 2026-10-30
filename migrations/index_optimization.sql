-- Fix: Add index to remove table scan bottleneck
CREATE INDEX IF NOT EXISTS idx_users_status ON users(status);