FROM agrigorev/zoomcamp-model:2025

WORKDIR /code

COPY app.py .


RUN pip install --no-cache-dir requests fastapi uvicorn

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
