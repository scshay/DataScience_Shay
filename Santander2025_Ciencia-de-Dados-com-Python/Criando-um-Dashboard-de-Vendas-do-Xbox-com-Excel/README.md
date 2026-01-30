# Dashboard de Faturamento 2024: Análise de Receita por Plano, Período e Características da Assinatura

## 📋 Visão Geral

Esta planilha foi criada para analisar receita/faturamento de assinaturas em 2024, com recortes por **Plano**, **Período (mês)** e **características da assinatura** (ex.: renovação automática e add-ons como EA Play Season Pass e Minecraft Season Pass). O arquivo já contém tabelas dinâmicas e um dashboard pronto.

---

## 📁 Estrutura do Arquivo (Abas)

### 1. Assets
**Aba de apoio visual (design)**

- Não foi alterada de forma alguma, mantém-se conforme o exercício original
- Contém a **Paleta de Cores** (ex.: `#9BC848`, `#22C55E`, `#2AE6B1`, `#5BF6A8`, `#E8E6E9`)
- Referências de Logos/ícones das empresas citadas na base de dados
- **Uso**: não interfere nos cálculos; serve para padronização visual do dashboard

### 2. Bases
**Aba principal de dados (base transacional / granular)**

Cada linha representa um assinante com informações de plano, período e valores.

#### Principais colunas:

| Coluna | Descrição | Tipo |
|--------|-----------|------|
| `Subscriber ID` | Identificador do assinante | Texto |
| `Name` | Nome do assinante | Texto |
| `Plan` | Plano contratado (Core, Standard, Ultimate) | Texto |
| `Start Date` | Data de início da assinatura | Data |
| `Auto Renewal` | Renovação automática (Yes/No) | Texto |
| `Subscription Price` | Preço da assinatura | Numérico |
| `Subscription Type` | Tipo de cobrança (Monthly, Quarterly, Annual) | Texto |
| `EA Play Season Pass` | Se possui add-on (Yes/No) | Texto |
| `EA Play Season Pass Price` | Valor do add-on EA Play | Numérico |
| `Minecraft Season Pass` | Se possui add-on (Yes/No) | Texto |
| `Minecraft Season Pass Price` | Valor do add-on Minecraft | Numérico |
| `Coupon Value` | Desconto/cupom aplicado | Numérico |
| `Total Value` | Total consolidado por assinante (valor final) | Numérico |

⚠️ **Observação de qualidade de dados**: Não modifiquei nada do arquivo original, mas vale salientar que em algumas linhas, campos de preço de add-on aparecem como `"-"` quando não aplicável. O ideal é manter como `0` (zero) e garantir que a coluna esteja como numérica para não quebrar somas/tabelas dinâmicas.

### 3. Tabelas Dinâmicas
**Aba de consolidação e análise (pivot tables)**

- Contém tabelas dinâmicas com `Soma de Total Value` por mês e por Plano
- **Filtros disponíveis**:
  - EA Play Season Pass (Tudo / Yes / No)
  - Minecraft Season Pass (Tudo / Yes / No)
- Inclui tabela de `Contagem de Plan` (distribuição/volume por categorias)

### 4. Dashboard
**Aba de visualização executiva**

- **Título**: "Faturamento 2024: Análise de Receita por Plano, Período e Características da Assinatura"
- Exibe o total consolidado do período
- Gráficos e KPIs interativos conectados aos filtros

---


## 🔍 Filtros e Recortes Disponíveis

- ✅ **Por Auto Renewal**: Yes/No (dependendo da configuração)
- ✅ **Por presença de add-ons**:
  - EA Play Season Pass (Yes/No)
  - Minecraft Season Pass (Yes/No)
- ✅ **Por mês**: jan, fev, mar, … dez
- ✅ **Por Plano**: Core, Standard, Ultimate
- ✅ **Por recorrência de assinatura**: Monthly, Quarterly, Annual

---

## ⚠️ Boas Práticas (Para Não "Quebrar" o Dashboard)

- ❌ Não renomeie colunas da aba **Bases** sem atualizar as tabelas dinâmicas
- ❌ Evite misturar texto e número em colunas de preço (ex.: `"-"`). Prefira `0`
- ✅ Mantenha `Start Date` como **data válida** (não texto)
- ✅ Use sempre os mesmos valores para categorias (ex.: não usar "Mensal" e "Monthly" ao mesmo tempo)

---

## ✅ Checklist Rápido de Atualização (1 minuto)

- [ ] Inseriu/atualizou linhas em **Bases**
- [ ] Garantiu que preços/cupom são **numéricos**
- [ ] Atualizou todas as tabelas dinâmicas em **Tabelas Dinâmicas**
- [ ] Conferiu o total no **Dashboard**

