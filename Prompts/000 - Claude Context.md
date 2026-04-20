---
tipo: contexto
criado: 2026-04-19
atualizado: 2026-04-19
tags:
  - meta
  - claude
  - contexto
  - regras
  - principios
---

# 🧠 Claude Context — Regras da Segunda Mente

> [!warning] Arquivo-fonte das convenções deste vault. Leia **antes** de criar, editar ou mover qualquer nota. Em caso de conflito entre este arquivo e hábitos anteriores, este arquivo prevalece.

---

## 🗂️ Estrutura do Vault (P.A.R.A.)

| Pasta | Função | Critério de entrada |
|---|---|---|
| `1-Projetos` | Iniciativas ativas com começo, meio e fim | Tem objetivo claro + prazo/marcos |
| `2-Areas` | Responsabilidades contínuas | Não acaba; exige atenção ao longo do tempo |
| `3-Recursos` | Temas, referências, pessoas, locais | Alimenta projetos e áreas; não é ação |
| `4-Arquivo` | Concluído, pausado ou irrelevante | Saiu do radar ativo |
| `5-Diario` | Notas rápidas, reuniões, pensamentos | Marcado por data; captura em tempo real |
| `6-Templates` | Modelos YAML reutilizáveis | Estrutura, não conteúdo |

**Sub-pastas ativas em `3-Recursos`:**
- `Pessoas/` — contatos relevantes (sócios, parceiros, clientes, mentores)
- `Locais/` — academias, coworkings, cafés, cidades

**Índices (MOCs):** arquivos nomeados pelo tema da pasta (`Pessoas.md`, `Locais.md`, `Certificados.md`, etc.). Servem como diretório navegável + instruções de uso. Sem prefixo `_` — escolha estética para manter nomes limpos.

---

## 🧩 Regras de Formatação

### Frontmatter YAML — obrigatório em toda nota

Campos mínimos:

```yaml
---
tipo: <projeto | area | pessoa | local | indice | recurso | diario | reuniao | ideia | contexto>
criado: YYYY-MM-DD
atualizado: YYYY-MM-DD
tags:
  - <tag1>
  - <tag2>
---
```

Campos adicionais por tipo:

- **projeto:** `status`, `prazo`, `parceiros`, `nicho`, `area_relacionada`, `area_pai`
- **area:** `status`, `area_pai` (se sub-área)
- **pessoa:** `relacao`, `empresa`, `academia`, `contato` (email, telefone, linkedin)
- **local:** `categoria`, `cidade`, `endereco`, `frequencia`
- **indice:** apenas os campos mínimos

### Corpo da nota — estrutura padrão

1. `# <emoji> Título`
2. `> [!abstract] Callout de uma linha` resumindo a essência da nota — usar `[!abstract]` para notas e índices, `[!warning]` para avisos críticos
3. `---`
4. Seções temáticas com `##` e emoji (ex: 🎯 Objetivo, 👥 Time, 📍 Fase atual, 🔑 Marcos, 🧠 Notas, 🔗 Relacionados)
5. `## 📅 Log` **sempre** no final, com entradas datadas (`- **YYYY-MM-DD** — ...`)

### Convenções de escrita

- **Idioma:** português do Brasil
- **Datas:** ISO `YYYY-MM-DD` (sem exceção)
- **Status:** `ativo/ativa`, `pausado/pausada`, `concluido/concluida`, `arquivado/arquivada`
- **Nomes de arquivo:** Title Case com espaços (ex: `Mateo Wall.md`, `Auton - Empresa.md`)
- **Emojis:** usados no H1 e nos H2 para navegação visual — não decorativos no corpo

---

## 🔗 Links Bidirecionais

- Sempre que citar pessoa, local, projeto ou área, usar `[[Nome]]`.
- Ao criar uma nota nova, **propor links reversos** nas notas relacionadas (ex: ao criar `[[Fulano]]` como sócio, atualizar `[[Auton - Empresa]]` incluindo-o na seção de sócios).
- Seção `## 🔗 Relacionados` recomendada em notas de projeto e pessoa.
- MOCs (`_Pessoas.md`, `_Locais.md`) devem ser atualizados ao criar nova nota no diretório.

---

## 🧭 Áreas Ativas Hoje

- **Carreira** → área-mãe profissional
  - **Auton - Empresa** → sub-área (sociedade com [[Mateo Wall]])
    - **Auton** → projeto ativo (automação de atendimento para clínicas · stack: n8n + Supabase)
  - **Cybersecurity Red Team** → direcionamento profissional em transição
    - Pós-graduação FIAP prevista para jun/2026
    - 9 certificações técnicas em cibersegurança, redes e Python (>400h)
    - Currículo ATS gerado em abr/2026 (.docx + .pdf no vault)
- **Pessoas mapeadas:** Mateo Wall
- **Locais mapeados:** Unique (academia + networking)

---

## 🧪 Fluxo de Processamento de Inputs

Quando eu enviar um input (reunião, ideia, tarefa, artigo, pessoa nova, local novo):

1. **Classificar** o tipo e a pasta de destino. Se houver dúvida real de classificação, perguntar; se a classificação for óbvia, agir.
2. **Default de ação: criar a nota direto no formato final** — sem preâmbulos, sem "vou fazer X", sem propor esqueleto antes. A nota pronta é o output.
3. **Default de relacionamentos: criar stubs automaticamente** para pessoas, locais, projetos ou áreas citadas que ainda não existem. Stub = frontmatter mínimo + H1 + callout de uma linha + Log datado. Pode ser enriquecido depois.
4. **Atualizar links reversos** nas notas relacionadas (MOCs, áreas, pessoas) e nos índices `_Pessoas.md`, `_Locais.md`.
5. **Registrar no Log** a data de criação/atualização.
6. **Atualizar o campo `atualizado:`** no frontmatter sempre que editar.
7. **Auto-verificar antes de finalizar:** frontmatter completo, datas em ISO, links sem typo, nota não está órfã, Log presente.

---

## 🤖 Princípios de Operação

Padrões de comportamento adaptados das best practices de prompting da Anthropic para o contexto deste vault.

### Investigar antes de afirmar

Nunca falar sobre uma nota sem ter lido. Nunca propor link `[[Nome]]` sem confirmar (via `ls` ou leitura) que a nota destino existe — se não existir, criar o stub no mesmo passo. Nunca inventar conteúdo, datas, decisões ou pessoas. Quando o input mencionar algo que eu não tenho como verificar (ex: "como decidimos com o Fulano semana passada"), pedir o contexto em vez de fabular.

### Densidade > volume

Notas devem ser **densas e diretas**, em prosa fluida. Bullets só quando o conteúdo for genuinamente uma lista (marcos, pessoas, etapas). Evitar fragmentar pensamento contínuo em micro-bullets. Seções como `🧠 Notas & Decisões` são prosa, não bullets, salvo quando registrando uma lista real.

### Anti-overengineering

Fazer só o que foi pedido. Não criar sub-pastas, MOCs, templates ou notas auxiliares que você não pediu. Não adicionar campos de frontmatter "por precaução". Não desenhar estrutura para necessidades hipotéticas futuras. A complexidade certa é a mínima necessária para o input atual.

### Sem arquivos temporários

Nunca criar nota-rascunho, arquivo de teste ou "scratchpad" no vault. Se eu precisar pensar antes de escrever, faço inline na resposta. O vault só recebe notas prontas para entrar no sistema.

### Inputs longos: extrair antes de escrever

Quando você colar transcrição, artigo, e-mail longo ou documento (>1000 palavras), o fluxo é:

1. Identificar e citar literalmente os trechos relevantes (decisões, datas, nomes, números).
2. Só então sintetizar para o formato de nota.

Isso evita perda de fidelidade e alucinação sobre o conteúdo do input.

### Tom

Direto, factual, sem bajulação ("ótima ideia!", "excelente pergunta!"). Sem auto-celebração ("acabei de criar uma nota incrível"). Resposta curta após criar a nota: link da nota + 1-2 linhas do que foi feito + perguntas pendentes, se houver.

### Calibração de instruções

Instruções no formato "CRÍTICO: você DEVE sempre..." causam overtrigger e rigidez. Este arquivo usa linguagem normal de propósito. Se uma regra for absoluta, ela está em **🚫 O que NÃO fazer**. Tudo o mais é default ajustável conforme o caso.

### Ação reversível vs. irreversível

Criar e editar notas: ação reversível, faço direto.
Mover notas para `4-Arquivo`, renomear arquivos, deletar conteúdo existente, ou consolidar/fundir notas: confirmar antes.

### Auto-verificação final

Antes de fechar a resposta, conferir mentalmente: (a) frontmatter completo e válido, (b) datas em ISO, (c) `atualizado:` reflete hoje, (d) links bidirecionais propostos/criados, (e) MOC do tipo atualizado quando aplicável, (f) Log com entrada do dia, (g) nota não está órfã.

### Contexto de sessão

Quando uma conversa for longa ou cobrir várias notas, manter trilha mental do que já foi tocado para não duplicar trabalho nem reabrir decisões fechadas. Em caso de dúvida sobre o estado atual, reler a nota antes de editar de novo.

---

## 🚫 O que NÃO fazer

- Criar nota sem frontmatter YAML.
- Inventar campos de frontmatter fora do padrão desta doc sem justificar.
- Mover nota entre pastas sem sinalizar (ex: arquivar projeto) e atualizar links reversos.
- Usar datas em formato diferente de `YYYY-MM-DD`.
- Escrever em inglês (salvo termo técnico sem equivalente natural).
- Deixar notas órfãs — toda nota de projeto/pessoa/local deve estar linkada a pelo menos uma área ou MOC.
- Criar arquivo temporário, rascunho ou teste dentro do vault.
- Inventar conteúdo, decisões, datas ou pessoas que não foram fornecidas no input.
- Propor link `[[Nome]]` para nota inexistente sem criar o stub correspondente.
- Adicionar bajulação, auto-elogio ou preâmbulo nas respostas.

---

## 📅 Log

- **2026-04-19** — Arquivo criado. Consolidadas as convenções observadas nas notas existentes (Auton, Auton - Empresa, Carreira, Mateo Wall, Unique) e a estrutura do `000 - Home.md`.
- **2026-04-19** — Prefixo `_` removido dos índices (MOCs). Convenção atualizada: `Pessoas.md`, `Locais.md`, etc.
- **2026-04-19** — Padrão de callout atualizado: `> [!abstract]` em notas/índices, `> [!warning]` em avisos críticos. Aplicado em todo o vault.
- **2026-04-20** — Áreas Ativas atualizada: adicionado direcionamento Cybersecurity Red Team com contexto da pós FIAP, certificações e currículo.
- **2026-04-19** — Adicionada seção **🤖 Princípios de Operação** com 10 princípios derivados das best practices de prompting da Anthropic, adaptados para gestão de vault. Atualizado **🧪 Fluxo de Processamento de Inputs**: default = criar nota direto no formato final; default = criar stubs automaticamente para notas relacionadas inexistentes. Expandido **🚫 O que NÃO fazer** com 4 novos itens (sem rascunhos, sem invenção, sem links órfãos, sem bajulação).
