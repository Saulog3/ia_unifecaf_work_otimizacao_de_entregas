# Instruções: Configuração MCP -> GitHub

Este diretório contém um template de configuração para conectar um servidor MCP ao repositório GitHub.

- Arquivo de configuração: `mcp_github_config.jsonc` (template)

Cuidados importantes
- NÃO coloque tokens (PAT) diretamente no repositório.
- Use a variável de ambiente definida em `auth.tokenEnvVar` (por padrão `GITHUB_MCP_PAT`).

Como definir a variável de ambiente no PowerShell (apenas para sessão atual):

```powershell
$env:GITHUB_MCP_PAT = 'seu_token_aqui'
```

Para definir permanentemente (usuário), use this (PowerShell 5.1):

```powershell
[Environment]::SetEnvironmentVariable('GITHUB_MCP_PAT', 'seu_token_aqui', 'User')
```

Exemplo de uso segura (pseudocódigo)

1. A MCP server process lê `GITHUB_MCP_PAT` do ambiente onde roda.
2. Evite comitar tokens no repositório. Adicione `/.vscode/*.jsonc` ao `.gitignore` se necessário.

Se quiser, eu posso:
- adicionar uma entrada no `.gitignore` para evitar commitar acidentalmente.
- gerar um exemplo de script de inicialização que injeta a variável de ambiente ao iniciar o servidor MCP.
