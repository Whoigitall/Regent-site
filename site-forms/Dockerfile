FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir "fastapi>=0.111" "uvicorn>=0.30" "email-validator>=2.1" \
 && pip cache purge || true
COPY main.py /app/main.py
RUN useradd --no-create-home forms
USER forms
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]
