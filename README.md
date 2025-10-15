<h1 align="center">🧠 Playwright MCP + Semantic Kernel – Intelligent Test Generation</h1>

## 📘 Overview / Visão Geral

This project integrates Microsoft Playwright MCP (Model Context Protocol) with Semantic Kernel to assist Quality Assurance (QA) engineers in semi-automating test creation.
Instead of generating every single automated test, the system helps reduce the time spent writing repetitive scripts, allowing QA professionals to focus on strategic test planning and high-value scenarios.

Este projeto integra o Playwright MCP (Model Context Protocol da Microsoft) com o Semantic Kernel para auxiliar engenheiros de QA na geração semi-automatizada de testes.
O objetivo não é automatizar tudo, mas reduzir o tempo gasto com tarefas repetitivas, permitindo que o QA concentre-se em planejar e priorizar cenários de teste críticos.

## 🎯 Goals / Objetivos

### ✅ English

- Use LLMs via Semantic Kernel to suggest test cases based on user stories or acceptance criteria.
- Automatically generate partial Playwright test scripts following the MCP protocol.
- Allow human review and editing before execution.
- Reduce automation setup time without sacrificing test quality.

### ✅ Português

- Utilizar LLMs via Semantic Kernel para sugerir casos de teste a partir de histórias de usuário ou critérios de aceitação.
- Gerar automaticamente scripts de teste parciais no Playwright seguindo o protocolo MCP.
- Permitir revisão e edição humana antes da execução.
- Reduzir o tempo de setup de automação sem comprometer a qualidade.

## 🧩 Architecture / Arquitetura
```bash
┌──────────────────────────┐
│ User Story / Test Input  │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│ Semantic Kernel (LLM)    │
│ - Context understanding  │
│ - Test suggestion        │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│ Playwright MCP           │
│ - Test generation bridge │
│ - Script assembly        │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│ QA Engineer Review       │
│ - Adjusts/finalizes      │
│ - Executes tests         │
└──────────────────────────┘
```

## ⚙️ Setup / Instalação

### Prerequisites / Pré-requisitos

- Node.js ≥ 18
- Python ≥ 3.10 (if Semantic Kernel Python SDK is used)
- Playwright ≥ 1.45
- Semantic Kernel SDK (JS or Python)
- Access to an OpenAI-compatible LLM endpoint

## Installation / Instalação
### Clone the repository

```bash
git clone https://github.com/m4rri4nne/playwright-mcp-semantic-kernel.git
cd playwright-mcp-semantic-kernel
```

### Install dependencies

```bash
npm install
# or
pip install semantic-kernel playwright
```

## 🚀 Usage / Uso
Generate Test Suggestions / Gerar Sugestões de Teste

```bash
npm run generate-tests
```

You’ll be prompted to enter a user story or acceptance criteria, and the system will:
- Use the Semantic Kernel to interpret context.
- Propose relevant test cases.
- Generate partial Playwright test files under /tests/generated/.

Você será solicitado a inserir uma história de usuário ou critérios de aceitação, e o sistema irá:
- Usar o Semantic Kernel para interpretar o contexto.
- Propor casos de teste relevantes.
- Gerar arquivos de teste Playwright parciais em /tests/generated/.

## 💡 Example / Exemplo

Input:

```
As a user, I want to log in with my email and password so I can access my dashboard.
```

Output (Generated Test Snippet):
```typescript
import { test, expect } from '@playwright/test';

test('User can log in with valid credentials', async ({ page }) => {
  await page.goto('/login');
  await page.fill('#email', 'user@example.com');
  await page.fill('#password', 'password123');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL('/dashboard');
});
```

## 🧠 Philosophy / Filosofia

“Not everything needs to be automated — but what is automated should be faster and smarter.”

The goal is augmentation, not replacement.
This tool empowers QA engineers to spend more time designing better tests and less time writing boilerplate code.

O objetivo é aumentar a produtividade, não substituir o analista de QA.
A ferramenta permite mais tempo para planejar e priorizar testes e menos tempo escrevendo código repetitivo.

## 🤝 Contributing / Contribuindo

Pull requests are welcome!
Please follow conventional commit messages and ensure all changes are tested before submitting.

Contribuições são bem-vindas!
Siga o padrão de commits convencionais e garanta que todas as alterações estejam testadas antes de enviar.
