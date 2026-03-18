#!/bin/bash

echo "🔍 Verificando si estás en un repositorio Git..."
if [ ! -d ".git" ]; then
    echo "❌ Error: No estás dentro de un repositorio Git"
    exit 1
fi

echo "📂 Verificando cambios en el repositorio..."
if [ -z "$(git status --porcelain)" ]; then
    echo "⚠️ No hay cambios para hacer commit"
    exit 0
fi

echo "✍️ Ingresa el mensaje del commit:"
read commit_message

if [ -z "$commit_message" ]; then
    echo "❌ El mensaje del commit no puede estar vacío"
    exit 1
fi

echo "➕ Agregando cambios..."
git add .

if [ $? -ne 0 ]; then
    echo "❌ Error al hacer git add"
    exit 1
fi

echo "📝 Creando commit..."
git commit -m "$commit_message"

if [ $? -ne 0 ]; then
    echo "❌ Error al hacer commit"
    exit 1
fi

echo "📤 ¿Quieres hacer push? (y/n)"
read push_confirm

if [[ "$push_confirm" == "y" || "$push_confirm" == "Y" ]]; then
    echo "🚀 Haciendo push a la rama actual..."
    
    current_branch=$(git branch --show-current)

    if [ -z "$current_branch" ]; then
        echo "❌ No se pudo detectar la rama actual"
        exit 1
    fi

    git push origin "$current_branch"

    if [ $? -ne 0 ]; then
        echo "❌ Error al hacer push"
        exit 1
    fi

    echo "✅ Push completado correctamente 🚀"
else
    echo "👍 Commit realizado, push omitido"
fi

echo "🎉 Proceso terminado"
