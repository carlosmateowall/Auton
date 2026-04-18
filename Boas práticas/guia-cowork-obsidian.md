# Guia de Boas Práticas — Claude Cowork + Obsidian

> Documento para leitura periódica. Criado em abril de 2026.

---

## 1. A Lógica Central do Sistema

Antes de qualquer prática, entenda a arquitetura:

```
Você fala → Cowork processa → Vault guarda
     ↑                              ↓
     └─────── Cowork consulta ──────┘
```

- **A conversa é efêmera.** Ela é o canal de entrada, não a memória.
- **O vault é permanente.** Ele é o cérebro que cresce com o tempo.
- **O Cowork é o assistente.** Ele lê, escreve e organiza o vault por você.

Nunca deixe informação importante apenas na conversa. Sempre instrua o Cowork a registrar no vault.

---

## 2. Estrutura de Pastas Recomendada

Simples é melhor. Estruturas complexas são abandonadas.

```
📁 00 - Inbox/         → captura rápida, sem pensar em organização
📁 01 - Diário/        → notas diárias automáticas (Daily Notes)
📁 02 - Pessoas/       → uma nota por pessoa relevante
📁 03 - Projetos/      → projetos ativos com contexto completo
📁 04 - Áreas/         → vida profissional, saúde, finanças, social
📁 05 - Recursos/      → aprendizados, referências, ideias soltas
📁 06 - Arquivo/       → projetos encerrados, notas antigas
```

**Regra de ouro:** se ficou em dúvida onde colocar, jogue no `00 - Inbox/`. O Cowork organiza depois.

---

## 3. Boas Práticas para Escrever Notas

### Escreva para o futuro Claude, não para você

Evite abreviações pessoais. Contexto é tudo.

❌ "reunião com JC — produto atrasado"
✅ "Reunião com João Carlos (CEO da Empresa X) — produto Y está atrasado, prazo revisado para maio"

### Use frontmatter YAML em toda nota

Coloque isso no topo de cada nota. É o que permite filtrar e buscar por atributos.

```yaml
---
data: 2026-04-17
tipo: reunião
pessoas: [João Carlos, Maria Silva]
projeto: Produto Y
status: em andamento
tags: [trabalho, urgente]
---
```

### Uma nota por pessoa

Crie um arquivo para cada pessoa relevante da sua vida profissional e social. Vá acumulando contexto conforme interage.

```
02 - Pessoas/
  João Carlos.md
  Maria Silva.md
  Ana Costa.md
```

Dentro de cada nota: cargo, empresa, histórico de interações, pendências, observações pessoais.

### Capture sem fricção no Inbox

Não pense em organização na hora de capturar. Jogue no Inbox e siga em frente. Reserve um momento semanal (ou instrua o Cowork) para processar o Inbox.

---

## 4. Como Instruir o Cowork

### Instrução permanente recomendada

Configure isso como comportamento padrão do seu Cowork:

> "Sempre que eu te passar informações sobre reuniões, pessoas, projetos ou decisões, registra automaticamente no vault na pasta correspondente, com data e contexto completo. Nunca deixe informação importante apenas na conversa."

### Comandos úteis do dia a dia

| O que você fala | O que o Cowork faz |
|---|---|
| "Tive uma reunião com X sobre Y, decidimos Z" | Cria nota estruturada, atualiza nota da pessoa, vincula ao projeto |
| "Processa meu Inbox" | Lê todas as notas da pasta Inbox e organiza nas pastas corretas |
| "Me lembra o que está pendente com João" | Vasculha o vault e traz um resumo |
| "Resumo da semana" | Lê o diário dos últimos 7 dias e sintetiza |
| "Prepara briefing sobre a Empresa X" | Reúne todas as notas relacionadas à empresa |
| "Quais projetos estão ativos?" | Lista projetos com status atual |

---

## 5. O Vault como CRM Pessoal

Para o uso social e profissional, trate o Obsidian como um CRM (gerenciador de relacionamentos).

**Modelo de nota de pessoa:**

```markdown
---
tipo: pessoa
empresa: Empresa X
cargo: CEO
primeira_interacao: 2026-01-10
tags: [cliente, decisor]
---

# João Carlos

## Contexto
CEO da Empresa X desde 2024. Conheci via indicação da Maria.

## Histórico de Interações
- **2026-04-17** — Reunião sobre produto Y. Pediu proposta até sexta. Orçamento: 50k.
- **2026-03-05** — Almoço de apresentação. Interesse em parceria no Q3.

## Pendências
- [ ] Enviar proposta até 19/04
- [ ] Agendar call de follow-up

## Observações
Prefere comunicação por WhatsApp. Viaja bastante em março/abril.
```

---

## 6. Tarefas Agendadas — O Poder Real do Cowork

Configure rotinas automáticas. Exemplos práticos:

- **Toda manhã:** "Leia meu calendário e email, me dê um briefing do dia"
- **Toda sexta:** "Processa o Inbox e me dê um resumo semanal"
- **Todo domingo:** "Liste as pendências abertas de todas as notas de pessoas e projetos"

Você acorda com o trabalho já organizado.

---

## 7. Sobre Conversas e Armazenamento

- **Não crie uma conversa por tema.** O Cowork é orientado a tarefas, não a chats contínuos.
- **O contexto persiste via vault + memória do Cowork**, não via histórico de chat.
- **Grave no vault em tempo real.** Instrua sempre o Cowork a registrar durante a sessão — assim as conversas podem ser descartadas tranquilamente.
- O armazenamento das conversas fica nos servidores da Anthropic, não no seu computador. O que pesa no seu HD é só o vault, que é leve (arquivos de texto).

---

## 8. Plugins Essenciais do Obsidian

Instale esses para potencializar o sistema:

| Plugin | Para que serve |
|---|---|
| **Daily Notes** (nativo) | Cria nota do dia automaticamente — sua base de captura |
| **Dataview** | Consulta notas como banco de dados (ex: "todos os projetos ativos") |
| **Templater** | Templates automáticos para notas de reunião, pessoas, projetos |
| **Calendar** | Visualização de diário em calendário |
| **QuickAdd** | Captura rápida sem abrir o vault |
| **Graph View** (nativo) | Visualiza conexões entre notas |

---

## 9. Checklist Semanal

Use isso como ritual de manutenção do sistema:

- [ ] Processar o Inbox (via Cowork ou manualmente)
- [ ] Atualizar status dos projetos ativos
- [ ] Verificar pendências nas notas de pessoas
- [ ] Revisar o diário da semana
- [ ] Arquivar projetos encerrados

---

## 10. Armadilhas para Evitar

❌ **Estrutura de pastas muito complexa** — você vai abandonar.
❌ **Muitas tags** — 5 a 10 bem definidas valem mais que 50.
❌ **Deixar informação só na conversa** — sempre gravar no vault.
❌ **Perfeccionismo na organização** — capture agora, organize depois.
❌ **Notas muito longas e monolíticas** — prefira notas menores e bem linkadas.
❌ **Começar com sistema elaborado** — comece simples, evolua com o uso.

---

## 11. Requisitos Técnicos (para quando for implementar)

- **Computador:** Mac com Apple Silicon (M1/M2/M3/M4) ou Windows
- **Sistema:** macOS Sonoma ou mais recente (para Mac)
- **App:** Claude Desktop (versão mais recente)
- **Plano:** Claude Pro ($20/mês) ou Max ($100/mês)
- **RAM recomendada:** mínimo 8GB

---

*Leia este documento periodicamente. O sistema só funciona se você acreditar nele e for consistente nos primeiros 30 dias.*
