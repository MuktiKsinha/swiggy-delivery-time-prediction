FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements-docker.txt .
RUN pip install --no-cache-dir -r requirements-docker.txt

FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY app.py ./
COPY models/preprocessor.joblib ./models/preprocessor.joblib
COPY scripts/data_clean_utils.py ./scripts/data_clean_utils.py
COPY run_information.json ./

EXPOSE 8000
CMD ["python", "app.py"]
