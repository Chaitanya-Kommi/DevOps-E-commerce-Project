FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

# Multi-stage build starts here
FROM python:3.12-slim
WORKDIR /app
# Copy the installed packages from the builder stage
COPY --from=builder /install /usr/local
COPY app.py .
EXPOSE 5003
CMD ["python","app.py"]