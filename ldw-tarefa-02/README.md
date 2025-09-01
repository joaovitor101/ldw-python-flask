# Valorant Manager

Uma aplicação Flask para gerenciamento de agentes e mapas do Valorant, desenvolvida seguindo o padrão MVC.

## 🎮 Sobre o Projeto

Esta aplicação permite gerenciar agentes e mapas do jogo Valorant, oferecendo uma interface moderna e responsiva com tema personalizado baseado nas cores oficiais do jogo.

## 🚀 Funcionalidades

- **Página Inicial**: Apresentação da aplicação com navegação
- **Gerenciamento de Agentes**: Adicionar e visualizar agentes em formato de lista
- **Gerenciamento de Mapas**: Adicionar e visualizar mapas em formato de tabela
- **Interface Responsiva**: Design adaptável para diferentes dispositivos
- **Tema Personalizado**: Cores e estilos baseados no Valorant

## 🛠️ Tecnologias Utilizadas

- **Flask**: Framework web Python
- **Bootstrap 5**: Framework CSS para interface responsiva
- **Font Awesome**: Ícones
- **HTML5/CSS3**: Estrutura e estilização

## 📁 Estrutura do Projeto

```
ldw-tarefa-02/
├── app.py                 # Arquivo principal da aplicação
├── controllers/
│   ├── __init__.py        # Inicializador do módulo
│   └── routes.py          # Rotas e lógica da aplicação
├── views/
│   ├── base.html          # Template base com navbar
│   ├── index.html         # Página inicial
│   ├── agents.html        # Página de agentes (lista)
│   └── maps.html          # Página de mapas (tabela)
├── static/
│   └── css/
│       └── style.css      # Estilos personalizados
└── README.md              # Documentação
```

## 🎯 Rotas da Aplicação

1. **`/`** - Página inicial com navegação
2. **`/agents`** - Gerenciamento de agentes (lista + formulário)
3. **`/maps`** - Gerenciamento de mapas (tabela + formulário)

## 🎨 Tema e Design

A aplicação utiliza as cores oficiais do Valorant:
- **Vermelho Valorant**: #ff4655
- **Dourado**: #ffd700
- **Escuro**: #0f1419
- **Claro**: #ece8e1

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado
2. Instale o Flask: `pip install flask`
3. Execute a aplicação: `python app.py`
4. Acesse: `http://localhost:4000`

## ⚙️ Configurações

- **Porta**: 4000
- **Host**: 0.0.0.0 (acessibilidade externa)
- **Modo Debug**: Ativo

## 📝 Funcionalidades Implementadas

### ✅ Requisitos Atendidos

- [x] 3 rotas implementadas
- [x] Página inicial com navbar
- [x] Inclusão e exibição de dados em lista (agentes)
- [x] Inclusão e exibição de dados em tabela (mapas)
- [x] Arquivos estáticos (CSS personalizado)
- [x] Bootstrap integrado
- [x] Porta 4000 com host 0.0.0.0
- [x] Modo debug ativo

### 🎮 Dados Iniciais

**Agentes**: Jett, Phoenix, Sage, Omen, Reyna
**Mapas**: Ascent (Itália, 2020)

## 👨‍💻 Desenvolvido por

Aplicação desenvolvida seguindo o padrão da aula `ldw-aula-02-mvc-controllers` com tema do Valorant. 