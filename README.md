# 📘 Comandos Essenciais de Git e GitHub

## 🔧 Configuração Inicial
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
# Define seu nome e email para identificar seus commits

## 📁 Criando e Clonando Repositórios
git init
# Inicia um repositório Git na pasta atual

git clone <url-do-repositorio>
# Copia um repositório remoto para sua máquina

## 📌 Monitorando Arquivos
git status
# Mostra o estado atual dos arquivos

git add <arquivo>
# Adiciona um arquivo específico para commit

git add .
# Adiciona todos os arquivos modificados

## 💾 Salvando Alterações
git commit -m "mensagem"
# Salva as alterações com uma mensagem

## 🔄 Enviando e Recebendo Atualizações
git push
# Envia commits para o repositório remoto

git pull
# Atualiza o repositório local com mudanças do remoto

## 🌿 Trabalhando com Branches
git branch
# Lista as branches

git branch <nome-da-branch>
# Cria uma nova branch

git checkout <nome-da-branch>
# Muda para outra branch

git checkout -b <nome-da-branch>
# Cria e já muda para a nova branch

git merge <nome-da-branch>
# Mescla uma branch na atual

## 🔍 Histórico
git log
# Mostra o histórico de commits

git log --oneline
# Histórico resumido

## 🚫 Desfazendo Coisas
git restore <arquivo>
# Descarta alterações em um arquivo

git reset HEAD <arquivo>
# Remove arquivo da área de staging

git reset --hard
# Apaga TODAS as alterações locais (cuidado!)

## 🌐 Conectando ao GitHub
git remote add origin <url>
# Conecta repositório local ao GitHub

git push -u origin main
# Primeiro envio para o GitHub

## 💡 Dicas Importantes
# - Escreva commits claros
# - Use branches para novas features
# - Sempre faça git pull antes de começar
# - Evite usar --hard sem entender

# Incluindo uma pasta vazia no repositorio:
# Devemos incluir o arquivo .gitkeep em cada pasta

# Alterando o nome de uma branch no repositorio remoto:
# git branch -m nome novo nome

# Verificando as  diferenças de duas branches:
# com git diff branch nome da outra branch
