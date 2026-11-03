# Stage 1: Rust Builder
FROM rust:1.80-slim-bookworm AS rust-builder
WORKDIR /app
COPY . .
RUN cargo build --release

# Stage 2: Python/FastAPI Runtime
FROM python:3.12-slim-bookworm AS gateway
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=rust-builder /app/target/release/quantum_vault_core /usr/local/bin/core
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Stage 3: Frontend Builder
FROM node:20-slim AS node-builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 4: Nginx Production
FROM nginx:alpine
COPY --from=node-builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]