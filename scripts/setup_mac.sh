#!/bin/bash
set -e
echo "🔧 Встановлюємо Ollama"
brew install ollama || echo "⚠️  Вже встановлено"
echo "📦 Завантажуємо модель"
ollama pull mamaylm-ukr          # 7B українська
echo "✅ Готово! Запускай ./start_dev.sh"
