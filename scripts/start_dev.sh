#!/bin/bash
echo "🚀 Backend: uvicorn"
uvicorn app.backend.main:app --host 0.0.0.0 --port 8000 --reload &
echo "🚀 Frontend: python -m http.server 5173"
cd app/frontend && python -m http.server 5173
