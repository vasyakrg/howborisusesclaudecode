#!/usr/bin/env python3
"""Build translated content-chunk-A.json for parts 0-3."""
import json
import copy

SRC = '/Users/vasyansk/Developers/MyProject/IaaC/Realmanual/claude-rules/full-content.json'
OUT = '/Users/vasyansk/Developers/MyProject/IaaC/Realmanual/claude-rules/content-chunk-A.json'

SVG_PATH = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>'

T = {}

T[(0,0)] = '''
                <div class="intro-panel">
                    <h1>Как <span>Boris Cherny</span> использует Claude Code</h1>
                    <p class="subtitle">
                        Boris создал Claude Code в Anthropic. Когда его спросили, как он сам им пользуется, он поделился 13 практическими советами из повседневной работы. Его сетап «на удивление ванильный» — доказательство, что CC отлично работает из коробки.
                    </p>
                    <a href="https://x.com/bcherny/status/2007179832300581177" target="_blank" rel="noopener noreferrer" class="author-link">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>
                        Тред @bcherny от 2 января 2026
                    </a>
                    <div class="intro-cta">
                        Кликай по вкладкам выше, чтобы изучить каждый совет <span class="arrow">→</span>
                        <div style="margin-top: 8px; font-size: 11px; color: var(--text-muted);">или используй стрелки ← →</div>
                    </div>
                </div>
            '''

T[(0,1)] = '''
                <div class="step-header">
                    <div class="step-number">1</div>
                    <div class="step-title">Запускай 5 Claude параллельно</div>
                </div>
                <div class="step-body">
                    <p>Boris запускает <strong>5 инстансов Claude Code одновременно</strong> в терминале, используя <strong>5 отдельных git-чекаутов</strong> одного и того же репозитория. Табы пронумерованы 1–5 для удобства, а системные уведомления сообщают, когда какому-либо Claude нужен ввод.</p>

                    <div class="highlight-box">
                        <div class="label">Ключевая деталь</div>
                        Каждый таб работает в своём git-чекауте, поэтому Claude может вносить изменения параллельно без конфликтов. Настрой уведомления iTerm2, чтобы знать, когда какой-то Claude требует внимания.
                    </div>

                    <div class="code-block">
<span class="prompt">~/repo-1 $</span> <span class="comment"># Таб 1: работа над фичей</span>
<span class="prompt">~/repo-2 $</span> <span class="comment"># Таб 2: прогон тестов</span>
<span class="prompt">~/repo-3 $</span> <span class="comment"># Таб 3: код-ревью</span>
<span class="prompt">~/repo-4 $</span> <span class="comment"># Таб 4: отладка</span>
<span class="prompt">~/repo-5 $</span> <span class="comment"># Таб 5: документация</span>
                    </div>

                    <a href="https://x.com/bcherny/status/2007179833990885678" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(0)">← intro</button>
                    <button class="nav-btn" onclick="switchTab(2)">web+mobile →</button>
                </div>
            '''

T[(0,2)] = '''
                <div class="step-header">
                    <div class="step-number">2</div>
                    <div class="step-title">Параллельные сессии в вебе и на мобиле</div>
                </div>
                <div class="step-body">
                    <p>Помимо терминала Boris крутит <strong>ещё 5–10 сессий на claude.ai/code</strong>. Он легко переключается между локальным и веб-вариантом через команду <code>&amp;</code> или флаг <code>--teleport</code>.</p>

                    <p>Также он запускает сессии утром с телефона через iOS-приложение Claude, а потом подхватывает их на компьютере.</p>

                    <div class="highlight-box">
                        <div class="label">Ключевые команды</div>
                        <code>&amp;</code> — отправить сессию в фон<br>
                        <code>--teleport</code> — переключать контекст между локальным и веб
                    </div>

                    <a href="https://x.com/bcherny/status/2007179836704600237" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(1)">← parallel</button>
                    <button class="nav-btn" onclick="switchTab(3)">opus →</button>
                </div>
            '''

T[(0,3)] = '''
                <div class="step-header">
                    <div class="step-number">3</div>
                    <div class="step-title">Opus 4.5 с thinking-режимом — для всего</div>
                </div>
                <div class="step-body">
                    <p>Boris использует <strong>Opus 4.5 в режиме thinking</strong> для любой задачи. Его логика:</p>

                    <div class="highlight-box">
                        <div class="label">Почему Opus, а не Sonnet</div>
                        «Это лучшая модель для кода, которой я когда-либо пользовался. И хотя она крупнее и медленнее Sonnet, её приходится меньше направлять, она лучше работает с инструментами — в итоге почти всегда получается быстрее, чем с моделью поменьше».
                    </div>

                    <p>Главный вывод: <strong>меньше направления + лучше работа с инструментами = быстрее итоговый результат</strong>, даже с более крупной моделью.</p>

                    <a href="https://x.com/bcherny/status/2007179838864666847" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(2)">← web+mobile</button>
                    <button class="nav-btn" onclick="switchTab(4)">CLAUDE.md →</button>
                </div>
            '''

T[(0,4)] = '''
                <div class="step-header">
                    <div class="step-number">4</div>
                    <div class="step-title">Общий CLAUDE.md с документацией</div>
                </div>
                <div class="step-body">
                    <p>Команда ведёт один общий файл <strong>CLAUDE.md</strong> для репозитория Claude Code, закоммиченный в git. Вся команда дополняет его несколько раз в неделю.</p>

                    <div class="highlight-box">
                        <div class="label">Ключевая практика</div>
                        «Каждый раз, когда мы видим, что Claude делает что-то неправильно, мы добавляем это в CLAUDE.md — чтобы в следующий раз он этого не повторил».
                    </div>

                    <div class="code-block">
<span class="prompt">claude-cli $</span> cat CLAUDE.md
<span class="comment"># Процесс разработки</span>

<span class="string">**Всегда используй `bun`, а не `npm`.**</span>

<span class="comment"># 1. Вносим изменения</span>
<span class="comment"># 2. Typecheck (быстро)</span>
bun run typecheck

<span class="comment"># 3. Прогон тестов</span>
bun run test -- -t "test name"    <span class="comment"># отдельный набор</span>
bun run test:file -- "glob"       <span class="comment"># конкретные файлы</span>

<span class="comment"># 4. Линт перед коммитом</span>
bun run lint:file -- "file1.ts"   <span class="comment"># конкретные файлы</span>
bun run lint                      <span class="comment"># все файлы</span>

<span class="comment"># 5. Перед созданием PR</span>
bun run lint:claude &amp;&amp; bun run test
                    </div>

                    <a href="https://x.com/bcherny/status/2007179840848597422" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(3)">← opus</button>
                    <button class="nav-btn" onclick="switchTab(5)">@.claude →</button>
                </div>
            '''

T[(0,5)] = '''
                <div class="step-header">
                    <div class="step-number">5</div>
                    <div class="step-title">@.claude в код-ревью</div>
                </div>
                <div class="step-body">
                    <p>Во время код-ревью Boris тегает <strong>@.claude</strong> в PR, чтобы добавить выводы в CLAUDE.md прямо в рамках того же PR.</p>

                    <p>Для этого используется Claude Code GitHub Action (<code>/install-github-action</code>). Boris называет это их версией <strong>«Compounding Engineering»</strong> — по концепции Dan Shipper.</p>

                    <div class="code-block">
<span class="comment">// Пример комментария к PR:</span>
<span class="string">nit: используй строковый литерал, а не ts enum</span>

<span class="command">@claude</span> добавь в CLAUDE.md правило: никогда не использовать enum,
всегда предпочитать литеральные union-типы
                    </div>

                    <div class="highlight-box">
                        <div class="label">Результат</div>
                        Claude автоматически обновляет CLAUDE.md и коммитит: «Предпочитай `type` вместо `interface`; **никогда не используй `enum`** (вместо него — union из строковых литералов)».
                    </div>

                    <a href="https://x.com/bcherny/status/2007179842928947333" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(4)">← CLAUDE.md</button>
                    <button class="nav-btn" onclick="switchTab(6)">plan →</button>
                </div>
            '''

T[(0,6)] = '''
                <div class="step-header">
                    <div class="step-number">6</div>
                    <div class="step-title">Начинай в Plan mode</div>
                </div>
                <div class="step-body">
                    <p>Большинство сессий стартуют в <strong>Plan mode</strong> (shift+tab дважды). Boris итеративно дорабатывает план вместе с Claude, пока тот не станет надёжным, а затем переключается в auto-accept.</p>

                    <div class="highlight-box">
                        <div class="label">Рабочий процесс</div>
                        Plan mode → доработка плана → auto-accept правок → Claude делает всё с первого раза
                    </div>

                    <div class="code-block">
<span class="prompt">&gt;</span> хочу улучшить отрисовку уведомлений о прогрессе
  для skills. можешь сделать их по виду и ощущению
  ближе к прогрессу subagent'ов?<span class="cursor"></span>

<span class="command">▮▮ plan mode on</span> (shift+tab для переключения)
                    </div>

                    <p><strong>«Хороший план — это реально важно, чтобы избежать проблем дальше».</strong></p>

                    <a href="https://x.com/bcherny/status/2007179845336527000" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(5)">← @.claude</button>
                    <button class="nav-btn" onclick="switchTab(7)">slash →</button>
                </div>
            '''

T[(0,7)] = '''
                <div class="step-header">
                    <div class="step-number">7</div>
                    <div class="step-title">Slash-команды для внутренних циклов</div>
                </div>
                <div class="step-body">
                    <p>Boris использует slash-команды для задач, которые делает <strong>много раз в день</strong>. Это экономит повторяющиеся подсказки, и Claude тоже может их вызывать.</p>

                    <p>Команды закоммичены в git в <code>.claude/commands/</code> и расшарены на всю команду.</p>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">/commit-push-pr</span> <span class="cursor"></span>

  /commit-push-pr     Коммит, пуш и открытие PR
                    </div>

                    <div class="highlight-box">
                        <div class="label">Мощная фишка</div>
                        Slash-команды могут содержать inline Bash, чтобы заранее вычислить нужную инфу (например, git status) и выполниться без лишних вызовов модели.
                    </div>

                    <a href="https://x.com/bcherny/status/2007179847949500714" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(6)">← plan</button>
                    <button class="nav-btn" onclick="switchTab(8)">subagents →</button>
                </div>
            '''

T[(0,8)] = '''
                <div class="step-header">
                    <div class="step-number">8</div>
                    <div class="step-title">Subagent'ы под типовые процессы</div>
                </div>
                <div class="step-body">
                    <p>Boris воспринимает subagent'ов как <strong>автоматизации самых частых PR-сценариев</strong>:</p>

                    <div class="file-tree">
<span class="folder">▼ .claude</span>
  <span class="folder">▼ agents</span>
    <span class="file">↓ build-validator.md</span>
    <span class="file">↓ code-architect.md</span>
    <span class="file">↓ code-simplifier.md</span>
    <span class="file">↓ oncall-guide.md</span>
    <span class="file">↓ verify-app.md</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Примеры</div>
                        <strong>code-simplifier</strong> — причёсывает код после того, как Claude закончил<br>
                        <strong>verify-app</strong> — подробные инструкции для end-to-end тестирования
                    </div>

                    <a href="https://x.com/bcherny/status/2007179850139000872" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(7)">← slash</button>
                    <button class="nav-btn" onclick="switchTab(9)">hooks →</button>
                </div>
            '''

T[(0,9)] = '''
                <div class="step-header">
                    <div class="step-number">9</div>
                    <div class="step-title">PostToolUse-хуки для форматирования</div>
                </div>
                <div class="step-body">
                    <p>Команда использует <strong>PostToolUse-хук</strong> для автоформатирования кода от Claude. В 90% случаев Claude и так пишет аккуратно отформатированный код, но хук ловит краевые случаи и предотвращает падения CI.</p>

                    <div class="json-block">
<span class="key">"PostToolUse"</span>: [
  {
    <span class="key">"matcher"</span>: <span class="string">"Write|Edit"</span>,
    <span class="key">"hooks"</span>: [
      {
        <span class="key">"type"</span>: <span class="string">"command"</span>,
        <span class="key">"command"</span>: <span class="string">"bun run format || true"</span>
      }
    ]
  }
]
                    </div>

                    <a href="https://x.com/bcherny/status/2007179852047335529" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(8)">← subagents</button>
                    <button class="nav-btn" onclick="switchTab(10)">perms →</button>
                </div>
            '''

T[(0,10)] = '''
                <div class="step-header">
                    <div class="step-number">10</div>
                    <div class="step-title">Заранее разрешай безопасные команды</div>
                </div>
                <div class="step-body">
                    <p>Вместо <code>--dangerously-skip-permissions</code> Boris использует <strong>/permissions</strong>, чтобы заранее разрешить типовые безопасные команды. Большая часть расшарена в <code>.claude/settings.json</code>.</p>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">/permissions</span>

<span class="string">Permissions:</span> <span style="background: var(--green-success); color: black; padding: 2px 6px; border-radius: 3px;">Allow</span>  Ask  Deny  Workspace

Claude Code не будет спрашивать перед использованием разрешённых инструментов.

↑ 12.  Bash(bq query:*)
  13.  Bash(bun run build:*)
  14.  Bash(bun run lint:file:*)
  15.  Bash(bun run test:*)
  16.  Bash(bun run test:file:*)
  17.  Bash(bun run typecheck:*)
  18.  Bash(bun test:*)
  19.  Bash(cc:*)
  20.  Bash(comm:*)
<span class="command">&gt; 21.  Bash(find:*)</span>
                    </div>

                    <a href="https://x.com/bcherny/status/2007179854077407667" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(9)">← hooks</button>
                    <button class="nav-btn" onclick="switchTab(11)">tools →</button>
                </div>
            '''

T[(0,11)] = '''
                <div class="step-header">
                    <div class="step-number">11</div>
                    <div class="step-title">Интеграции с инструментами</div>
                </div>
                <div class="step-body">
                    <p>Claude Code автономно использует все инструменты Boris'а:</p>
                    <ul style="margin: 16px 0; padding-left: 20px; color: var(--text-secondary);">
                        <li>Ищет и постит в <strong>Slack</strong> (через MCP-сервер)</li>
                        <li>Запускает запросы к <strong>BigQuery</strong> через bq CLI</li>
                        <li>Вытаскивает логи ошибок из <strong>Sentry</strong></li>
                    </ul>

                    <div class="code-block">
<span class="prompt">claude-cli-2 $</span> cat .mcp.json
{
  <span class="key">"mcpServers"</span>: {
    <span class="key">"slack"</span>: {
      <span class="key">"type"</span>: <span class="string">"http"</span>,
      <span class="key">"url"</span>: <span class="string">"https://slack.mcp.anthropic.com/mcp"</span>
    }
  }
}
                    </div>

                    <a href="https://x.com/bcherny/status/2007179856266789204" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(10)">← perms</button>
                    <button class="nav-btn" onclick="switchTab(12)">long-run →</button>
                </div>
            '''

T[(0,12)] = '''
                <div class="step-header">
                    <div class="step-number">12</div>
                    <div class="step-title">Долгие задачи</div>
                </div>
                <div class="step-body">
                    <p>Для очень длительных задач Boris следит, чтобы Claude мог работать без прерываний:</p>

                    <div class="highlight-box">
                        <div class="label">Варианты</div>
                        <strong>(а)</strong> Попросить Claude валидировать результат через фоновый агент по завершении<br>
                        <strong>(б)</strong> Использовать Stop-хук агента для детерминированных проверок<br>
                        <strong>(в)</strong> Подключить плагин «ralph-wiggum» (идея сообщества от @GeoffreyHuntley)
                    </div>

                    <p>Для песочниц он использует <code>--permission-mode=dontAsk</code> или <code>--dangerously-skip-permissions</code>, чтобы избежать блокировок.</p>

                    <div class="code-block">
<span class="command">* Reticulating...</span> (1d 2h 47m · ↓ 2.4m tokens · thinking)

<span class="prompt">&gt;</span> <span class="cursor"></span>
                    </div>

                    <a href="https://x.com/bcherny/status/2007179858435281082" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(11)">← tools</button>
                    <button class="nav-btn" onclick="switchTab(13)">verify →</button>
                </div>
            '''

T[(0,13)] = '''
                <div class="step-header">
                    <div class="step-number">13</div>
                    <div class="step-title">Самый важный совет: верификация</div>
                </div>
                <div class="step-body">
                    <p><strong>Это совет №1 от Boris'а:</strong></p>

                    <div class="highlight-box">
                        <div class="label">Ключевая мысль</div>
                        «Наверное, самое важное, чтобы получать отличные результаты от Claude Code — дать Claude способ проверять свою работу. Если у Claude есть такой feedback-цикл, он <strong>повысит качество итогового результата в 2–3 раза</strong>».
                    </div>

                    <p>Для своих же правок в claude.ai/code Claude использует <strong>Claude Chrome extension</strong>, чтобы открыть браузер, протестировать UI-изменения и итеративно довести всё до идеала.</p>

                    <p>Верификация бывает разной: Bash-команды, тестовые прогоны, симуляторы, браузерные тесты и т.д. Главное — дать Claude возможность замкнуть feedback-цикл.</p>

                    <div class="highlight-box" style="background: rgba(74, 222, 128, 0.1); border-color: var(--green-success);">
                        <div class="label" style="color: var(--green-success);">Главный вывод</div>
                        Вложись в доменно-специфичную верификацию ради оптимальной производительности. Claude тестирует каждое изменение, которое Boris коммитит в claude.ai/code.
                    </div>

                    <a href="https://x.com/bcherny/status/2007179861115511237" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(12)">← long-run</button>
                    <button class="nav-btn" onclick="switchTab(0)">back to intro →</button>
                </div>
            '''

T[(1,0)] = '''
                <div class="intro-panel">
                    <h1>Ещё советы от <span>Boris Cherny</span></h1>
                    <p class="subtitle">
                        31 января 2026 Boris поделился ещё 10 советами. Это советы напрямую от команды Claude Code — не забывай, у всех свой сетап. Экспериментируй и смотри, что заходит именно тебе!
                    </p>
                    <a href="https://x.com/bcherny/status/2017742741636321619" target="_blank" rel="noopener noreferrer" class="author-link">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>
                        Тред @bcherny от 31 января 2026
                    </a>
                    <div class="intro-cta">
                        Кликай по вкладкам выше, чтобы изучить каждый совет <span class="arrow">→</span>
                        <div style="margin-top: 8px; font-size: 11px; color: var(--text-muted);">или используй стрелки ← →</div>
                    </div>
                </div>
            '''

T[(1,1)] = '''
                <div class="step-header">
                    <div class="step-number">1</div>
                    <div class="step-title">Делай больше параллельно</div>
                </div>
                <div class="step-body">
                    <p>Запускай <strong>3–5 git-worktree одновременно</strong>, каждый со своим Claude-сеансом параллельно. Это самый большой буст к продуктивности и главный совет команды.</p>

                    <div class="highlight-box">
                        <div class="label">Почему worktree, а не checkouts</div>
                        Большинство в команде Claude Code предпочитает worktree — именно поэтому @amorriscode встроил их нативную поддержку прямо в Claude Desktop!
                    </div>

                    <p>Некоторые дают worktree'ам имена и навешивают <strong>shell-алиасы (za, zb, zc)</strong>, чтобы прыгать между ними одним нажатием. У других есть отдельный «analysis» worktree только для чтения логов и BigQuery.</p>

                    <div class="code-block">
<span class="prompt">$</span> <span class="command">git worktree add</span> .claude/worktrees/my-worktree origin/main

<span class="prompt">$</span> <span class="command">cd</span> .claude/worktrees/my-worktree &amp;&amp; claude

<span class="comment"># Claude Code v2.1.29</span>
<span class="comment"># Opus 4.5 · Claude Enterprise</span>
<span class="comment"># .claude/worktrees/my-worktree</span>
                    </div>

                    <a href="https://x.com/bcherny/status/2017742743125299476" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(0)">← intro</button>
                    <button class="nav-btn" onclick="switchTab(2)">plan →</button>
                </div>
            '''

T[(1,2)] = '''
                <div class="step-header">
                    <div class="step-number">2</div>
                    <div class="step-title">Любую сложную задачу начинай в Plan mode</div>
                </div>
                <div class="step-body">
                    <p>Вложи энергию в план, чтобы Claude мог <strong>сделать всю реализацию с одного прохода</strong>. Не проталкивай, когда пошло не так — возвращайся в plan mode и переписывай план.</p>

                    <div class="highlight-box">
                        <div class="label">Практики команды</div>
                        Один коллега поручает одному Claude написать план, а затем запускает <strong>второй Claude, чтобы тот ревьюил план как staff-инженер</strong>. Другой рассказывает, что как только что-то идёт не так — сразу возвращается в plan mode и перепланирует.
                    </div>

                    <p>Также явно просят Claude входить в plan mode для <strong>шагов верификации, а не только для сборки</strong>.</p>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">T</span>ry "refactor cli.tsx"

<span class="string">▮▮ plan mode on</span> (shift+Tab для переключения)
                    </div>

                    <a href="https://x.com/bcherny/status/2017742745365057733" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(1)">← worktrees</button>
                    <button class="nav-btn" onclick="switchTab(3)">CLAUDE.md →</button>
                </div>
            '''

T[(1,3)] = '''
                <div class="step-header">
                    <div class="step-number">3</div>
                    <div class="step-title">Инвестируй в свой CLAUDE.md</div>
                </div>
                <div class="step-body">
                    <p>После каждой корректировки заканчивай фразой: <strong>«Обнови свой CLAUDE.md, чтобы больше не повторять эту ошибку»</strong>. Claude жутковато хорош в написании правил для самого себя.</p>

                    <div class="highlight-box">
                        <div class="label">Ключевая практика</div>
                        Безжалостно редактируй свой CLAUDE.md со временем. Итерируй, пока уровень ошибок Claude ощутимо не снизится.
                    </div>

                    <p>Один из инженеров просит Claude вести <strong>папку заметок для каждой задачи/проекта</strong>, которая обновляется после каждого PR. А CLAUDE.md просто указывает на неё.</p>

                    <div class="code-block">
<span class="comment">Memory files  ·  /memory</span>
<span class="string">└ ~/.claude/CLAUDE.md:</span> 76 tokens
<span class="string">└ CLAUDE.md:</span> 4k tokens
                    </div>

                    <a href="https://x.com/bcherny/status/2017742747067945390" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(2)">← plan</button>
                    <button class="nav-btn" onclick="switchTab(4)">skills →</button>
                </div>
            '''

T[(1,4)] = '''
                <div class="step-header">
                    <div class="step-number">4</div>
                    <div class="step-title">Пиши свои skills</div>
                </div>
                <div class="step-body">
                    <p>Пиши свои skills и <strong>коммить их в git</strong>. Переиспользуй в каждом проекте.</p>

                    <div class="highlight-box">
                        <div class="label">Советы от команды</div>
                        <ul style="margin: 8px 0 0 16px; line-height: 1.8;">
                            <li>Если делаешь что-то чаще раза в день — превращай в skill или команду</li>
                            <li>Сделай slash-команду <strong>/techdebt</strong> и запускай в конце каждой сессии, чтобы находить и убивать дубли в коде</li>
                            <li>Настрой slash-команду, которая синхронизирует 7 дней Slack, GDrive, Asana и GitHub в один контекст-дамп</li>
                            <li>Собери agents-аналитиков, которые пишут dbt-модели, ревьюят код и тестируют изменения в dev</li>
                        </ul>
                    </div>

                    <a href="https://x.com/bcherny/status/2017742748984742078" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(3)">← CLAUDE.md</button>
                    <button class="nav-btn" onclick="switchTab(5)">bugs →</button>
                </div>
            '''

T[(1,5)] = '''
                <div class="step-header">
                    <div class="step-number">5</div>
                    <div class="step-title">Claude сам чинит большинство багов</div>
                </div>
                <div class="step-body">
                    <p>Подключи <strong>Slack MCP</strong>, вставляй в Claude ветку с баг-репортом из Slack и просто говори «fix». Переключение контекста не нужно.</p>

                    <p>Или просто скажи <strong>«Пойди и почини упавшие CI-тесты»</strong>. Не микроменеджь, как именно.</p>

                    <div class="highlight-box">
                        <div class="label">Прокаченный совет</div>
                        Скармливай Claude логи docker, чтобы разбирать распределённые системы — он удивительно хорош в этом.
                    </div>

                    <div class="code-block">
<span class="prompt">&gt;</span> почини это https://ant.slack.com/archives/...

<span class="string">● slack - search_public (MCP)</span>(query: "in:C07VBS...")
  Ищет сообщения в публичных Slack-каналах...

<span class="comment">'slack_search_public' в общем случае не</span>
<span class="comment">для user consent на использование 'slack_search_p...</span>
                    </div>

                    <a href="https://x.com/bcherny/status/2017742750473720121" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(4)">← skills</button>
                    <button class="nav-btn" onclick="switchTab(6)">prompting →</button>
                </div>
            '''

T[(1,6)] = '''
                <div class="step-header">
                    <div class="step-number">6</div>
                    <div class="step-title">Прокачай свой промптинг</div>
                </div>
                <div class="step-body">
                    <p><strong>а. Бросай Claude вызов.</strong> Скажи: «Погоняй меня по этим изменениям и не открывай PR, пока я не пройду твой тест». Пусть Claude будет твоим ревьюером. Или скажи: «Докажи мне, что это работает», — и пусть Claude диффит поведение между main и твоей фича-веткой.</p>

                    <p><strong>б. После посредственного фикса</strong> скажи: «Зная всё, что ты теперь знаешь, выброси это и реализуй элегантное решение».</p>

                    <p><strong>в. Пиши детальные спеки</strong> и убирай двусмысленность до передачи работы. Чем конкретнее — тем лучше результат.</p>

                    <div class="highlight-box">
                        <div class="label">Ключевая мысль</div>
                        Не принимай первое же решение. Проси Claude сделать лучше — обычно он может.
                    </div>

                    <a href="https://x.com/bcherny/status/2017742752566632544" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(5)">← bugs</button>
                    <button class="nav-btn" onclick="switchTab(7)">terminal →</button>
                </div>
            '''

T[(1,7)] = '''
                <div class="step-header">
                    <div class="step-number">7</div>
                    <div class="step-title">Настройка терминала и окружения</div>
                </div>
                <div class="step-body">
                    <p>Команда обожает <strong>Ghostty</strong>! Многим нравится его синхронный рендеринг, 24-битный цвет и нормальная поддержка юникода.</p>

                    <p>Чтобы легче жонглировать Claude'ами, через <strong>/statusline</strong> настрой status bar так, чтобы всегда видеть использование контекста и текущую git-ветку. Многие ещё цветом и именем помечают табы терминала, иногда через tmux — один таб на задачу/worktree.</p>

                    <div class="highlight-box">
                        <div class="label">Голосовой ввод</div>
                        Пользуйся голосовым вводом. Говоришь в 3 раза быстрее, чем печатаешь, а в результате промпты становятся заметно детальнее. (На macOS — <strong>fn x2</strong>)
                    </div>

                    <div class="code-block">
<span class="comment">┌──────────────────────────────────────────┐</span>
<span class="comment">│ ● ● ●  │  1 ⌘1  │  2 ● ⌘2  │  3 ⌘3  │  4 │</span>
<span class="comment">├──────────────────────────────────────────┤</span>
<span class="comment">│ × * Claude Code (node)                   │</span>
<span class="comment">│                                          │</span>
<span class="comment">│ Claude Code v2.1.29                      │</span>
<span class="comment">│ Opus 4.5 · Claude Enterprise             │</span>
<span class="comment">│ /code/claude                             │</span>
<span class="comment">└──────────────────────────────────────────┘</span>
                    </div>

                    <a href="https://x.com/bcherny/status/2017742753971769626" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(6)">← prompting</button>
                    <button class="nav-btn" onclick="switchTab(8)">subagents →</button>
                </div>
            '''

T[(1,8)] = '''
                <div class="step-header">
                    <div class="step-number">8</div>
                    <div class="step-title">Используй subagent'ов</div>
                </div>
                <div class="step-body">
                    <p><strong>а.</strong> Добавляй «use subagents» к любому запросу, где хочешь бросить на задачу больше компьюта.</p>

                    <p><strong>б.</strong> Выноси отдельные подзадачи в subagent'ы, чтобы основной контекст главного агента оставался чистым и сфокусированным.</p>

                    <p><strong>в.</strong> Роутить permission-запросы в Opus 4.5 через хук — пусть сам сканирует на атаки и авто-аппрувит безопасные.</p>

                    <div class="code-block">
<span class="prompt">&gt;</span> используй 5 subagent'ов, чтобы исследовать кодовую базу

<span class="string">● Запускаю 5 explore-агентов параллельно чтобы...</span>

<span class="command">● Running 5 Explore agents...</span> (ctrl+o развернуть)
  ├─ <span class="string">Explore entry points and startup</span> · 10 t...
  │  └ Bash: Find CLI or main entry files
  ├─ <span class="string">Explore React components structure</span> · 14...
  │  └ Bash: ls -la /Users/boris/code/clau...
  ├─ <span class="string">Explore tools implementation</span> · 14 tool...
  │  └ Bash: Find tool implementation files
  ├─ <span class="string">Explore state management</span> · 13 tool uses
  │  └ Search: **/screens/REPL.tsx
  └─ <span class="string">Explore testing infrastructure</span> · 13 to...
     └ Search: test/mocks/**/*.ts
                    </div>

                    <a href="https://x.com/bcherny/status/2017742755737555434" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(7)">← terminal</button>
                    <button class="nav-btn" onclick="switchTab(9)">data →</button>
                </div>
            '''

T[(1,9)] = '''
                <div class="step-header">
                    <div class="step-number">9</div>
                    <div class="step-title">Используй Claude для данных и аналитики</div>
                </div>
                <div class="step-body">
                    <p>Проси Claude Code использовать <strong>«bq» CLI</strong>, чтобы вытаскивать и анализировать метрики на лету. В нашем репозитории закоммичен BigQuery skill, и вся команда гоняет через него аналитические запросы прямо в Claude Code.</p>

                    <div class="highlight-box">
                        <div class="label">Слова Boris'а</div>
                        «Лично я не написал ни строчки SQL больше полугода».
                    </div>

                    <p>Это работает с <strong>любой базой, у которой есть CLI, MCP или API</strong>.</p>

                    <a href="https://x.com/bcherny/status/2017742757666902374" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(8)">← subagents</button>
                    <button class="nav-btn" onclick="switchTab(10)">learning →</button>
                </div>
            '''

T[(1,10)] = '''
                <div class="step-header">
                    <div class="step-number">10</div>
                    <div class="step-title">Учиться вместе с Claude</div>
                </div>
                <div class="step-body">
                    <p>Несколько советов от команды, как использовать Claude Code для обучения:</p>

                    <p><strong>а.</strong> Включи output style «Explanatory» или «Learning» через /config, чтобы Claude объяснял <em>почему</em> он вносит те или иные правки.</p>

                    <p><strong>б.</strong> Попроси Claude сгенерировать <strong>визуальную HTML-презентацию</strong> по незнакомому коду. Слайды получаются на удивление хорошими!</p>

                    <p><strong>в.</strong> Проси Claude рисовать <strong>ASCII-диаграммы</strong> новых протоколов и кодовых баз — это помогает быстрее разобраться.</p>

                    <p><strong>г.</strong> Собери <strong>skill для интервального повторения</strong>: ты объясняешь, как понял, Claude задаёт уточняющие вопросы для закрытия пробелов и сохраняет результат.</p>

                    <div class="highlight-box" style="background: rgba(74, 222, 128, 0.1); border-color: var(--green-success);">
                        <div class="label" style="color: var(--green-success);">Главный вывод</div>
                        Claude Code — это не только про код. Это мощный инструмент для обучения, если настроить его объяснять и обучать.
                    </div>

                    <a href="https://x.com/bcherny/status/2017742759218794768" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(9)">← data</button>
                    <button class="nav-btn" onclick="switchTab(0)">back to intro →</button>
                </div>
            '''

T[(2,0)] = '''
                <div class="intro-panel">
                    <h1>Настраивай своего <span>Claude</span></h1>
                    <p class="subtitle">
                        11 февраля 2026 Boris поделился ещё 12 советами. В этот раз тема — кастомизация: хуки, плагины, агенты, permissions и все способы сделать Claude Code своим.
                    </p>
                    <a href="https://x.com/bcherny/status/2021699851499798911" target="_blank" rel="noopener noreferrer" class="author-link">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>
                        Тред @bcherny от 11 февраля 2026
                    </a>
                    <div class="intro-cta">
                        Кликай по вкладкам выше, чтобы изучить каждый совет <span class="arrow">→</span>
                        <div style="margin-top: 8px; font-size: 11px; color: var(--text-muted);">или используй стрелки ← →</div>
                    </div>
                </div>
            '''

T[(2,1)] = '''
                <div class="step-header">
                    <div class="step-number">1</div>
                    <div class="step-title">Настрой свой терминал</div>
                </div>
                <div class="step-body">
                    <p>Несколько быстрых настроек, чтобы Claude Code ощущался в терминале как надо:</p>

                    <div class="highlight-box">
                        <div class="label">Ключевые настройки</div>
                        <ul style="margin: 8px 0 0 16px; line-height: 2;">
                            <li><strong>Тема:</strong> запусти <code>/config</code>, чтобы выставить светлый/тёмный режим</li>
                            <li><strong>Уведомления:</strong> включи уведомления для iTerm2 или используй свой notifs-хук</li>
                            <li><strong>Переносы строк:</strong> если работаешь в терминале IDE, Apple Terminal, Warp или Alacritty — запусти <code>/terminal-setup</code>, чтобы shift+enter делал перенос (без ручного <code>\\</code>)</li>
                            <li><strong>Vim-режим:</strong> запусти <code>/vim</code></li>
                        </ul>
                    </div>

                    <a href="https://x.com/bcherny/status/2021699859359883608" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(0)">← intro</button>
                    <button class="nav-btn" onclick="switchTab(2)">effort →</button>
                </div>
            '''

T[(2,2)] = '''
                <div class="step-header">
                    <div class="step-number">2</div>
                    <div class="step-title">Подстрой уровень усилий</div>
                </div>
                <div class="step-body">
                    <p>Запусти <code>/model</code> и выбери предпочтительный effort level:</p>

                    <div class="highlight-box">
                        <div class="label">Уровни усилий</div>
                        <ul style="margin: 8px 0 0 16px; line-height: 2;">
                            <li><strong>Low</strong> — меньше токенов и быстрее ответы</li>
                            <li><strong>Medium</strong> — сбалансированное поведение</li>
                            <li><strong>High</strong> — больше токенов и интеллекта</li>
                        </ul>
                    </div>

                    <p>Лично я использую <strong>High для всего</strong>.</p>

                    <div class="code-block">
<span class="comment">|||</span> <span class="command">High effort</span> (по умолчанию)  ← → для выбора

Fast mode: <strong>ON</strong>, доступен с Opus 4.6
                    </div>

                    <a href="https://x.com/bcherny/status/2021699860869902424" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(1)">← terminal</button>
                    <button class="nav-btn" onclick="switchTab(3)">plugins →</button>
                </div>
            '''

T[(2,3)] = '''
                <div class="step-header">
                    <div class="step-number">3</div>
                    <div class="step-title">Ставь плагины, MCP и skills</div>
                </div>
                <div class="step-body">
                    <p>Плагины позволяют ставить <strong>LSP</strong> (теперь доступны для всех крупных языков), <strong>MCP, skills, агентов и кастомные хуки</strong>.</p>

                    <p>Ставь плагины из официального маркетплейса Anthropic или заводи собственный маркетплейс для компании. Закоммить <code>settings.json</code> в репозиторий, чтобы маркетплейсы подтягивались у всей команды автоматически.</p>

                    <div class="highlight-box">
                        <div class="label">С чего начать</div>
                        Запусти <code>/plugin</code>, чтобы посмотреть и поставить плагины.
                    </div>

                    <a href="https://x.com/bcherny/status/2021699862522364149" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(2)">← effort</button>
                    <button class="nav-btn" onclick="switchTab(4)">agents →</button>
                </div>
            '''

T[(2,4)] = '''
                <div class="step-header">
                    <div class="step-number">4</div>
                    <div class="step-title">Пиши кастомных агентов</div>
                </div>
                <div class="step-body">
                    <p>Чтобы сделать кастомного агента, положи <code>.md</code>-файл в <code>.claude/agents</code>. У каждого агента может быть своё имя, цвет, набор инструментов, pre-allowed/pre-disallowed инструменты, permission-режим и модель.</p>

                    <div class="highlight-box">
                        <div class="label">Прокаченный совет</div>
                        Есть малоизвестная фишка: можно задать <strong>агента по умолчанию</strong> для основного чата. Просто пропиши поле <code>"agent"</code> в <code>settings.json</code> или используй флаг <code>--agent</code>.
                    </div>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">используй агента sentry-errors</span>

<strong>sentry-errors</strong>(Тянет логи ошибок из Sentry)

  <span class="command">Search</span>(pattern: "sentry", path: "src")
  <span class="comment">+10 more tool uses (ctrl+o развернуть)</span>
                    </div>

                    <p>Чтобы начать, запусти <code>/agents</code>.</p>

                    <a href="https://x.com/bcherny/status/2021700144039903699" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(3)">← plugins</button>
                    <button class="nav-btn" onclick="switchTab(5)">permissions →</button>
                </div>
            '''

T[(2,5)] = '''
                <div class="step-header">
                    <div class="step-number">5</div>
                    <div class="step-title">Заранее аппрувь типовые разрешения</div>
                </div>
                <div class="step-body">
                    <p>Claude Code использует продвинутую систему permissions — комбинацию <strong>детекции prompt-инъекций, статического анализа, песочницы и человеческого надзора</strong>.</p>

                    <p>Из коробки мы пре-аппрувим небольшой набор безопасных команд. Чтобы добавить ещё — запусти <code>/permissions</code> и пополни allow- и block-списки. Закоммить это в командный <code>settings.json</code>.</p>

                    <div class="highlight-box">
                        <div class="label">Синтаксис с wildcard'ами</div>
                        Мы поддерживаем полноценные wildcard'ы. Попробуй <code>"Bash(bun run *)"</code> или <code>"Edit(/docs/**)"</code>.
                    </div>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">/permissions</span>

<span class="command">Permissions:</span> <strong>[Allow]</strong>  Ask  Deny

52. Bash(gh issue view:*)
53. Bash(gh pr checks:*)
54. Bash(gh pr comment:*)
55. Bash(gh pr diff:*)
56. Bash(gh pr list:*)
                    </div>

                    <a href="https://x.com/bcherny/status/2021700332292911228" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(4)">← agents</button>
                    <button class="nav-btn" onclick="switchTab(6)">sandbox →</button>
                </div>
            '''

T[(2,6)] = '''
                <div class="step-header">
                    <div class="step-number">6</div>
                    <div class="step-title">Включи sandbox</div>
                </div>
                <div class="step-body">
                    <p>Подключи <strong>open-source sandbox-рантайм</strong> Claude Code, чтобы повысить безопасность и уменьшить число permission-запросов.</p>

                    <p>Запусти <code>/sandbox</code>, чтобы включить. Песочница работает локально и поддерживает <strong>изоляцию файлов и сети</strong>. Поддержка Windows — скоро.</p>

                    <div class="highlight-box">
                        <div class="label">Режимы песочницы</div>
                        <ul style="margin: 8px 0 0 16px; line-height: 2;">
                            <li><strong>Sandbox BashTool, with auto-allow</strong> — команды идут в песочницу и авто-аппрувятся</li>
                            <li><strong>Sandbox BashTool, with regular permissions</strong> — песочница + обычные permission-запросы</li>
                            <li><strong>No Sandbox</strong> — поведение по умолчанию</li>
                        </ul>
                    </div>

                    <a href="https://x.com/bcherny/status/2021700506465579443" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(5)">← permissions</button>
                    <button class="nav-btn" onclick="switchTab(7)">statusline →</button>
                </div>
            '''

T[(2,7)] = '''
                <div class="step-header">
                    <div class="step-number">7</div>
                    <div class="step-title">Добавь status line</div>
                </div>
                <div class="step-body">
                    <p>Кастомные status line выводятся прямо под композером и показывают <strong>модель, директорию, остаток контекста, стоимость</strong> — и вообще что угодно, что хочется видеть во время работы.</p>

                    <p>У каждого в команде Claude Code — свой statusline. Запусти <code>/statusline</code>, чтобы начать: Claude сам сгенерирует для тебя statusline по твоим <code>.bashrc</code>/<code>.zshrc</code>.</p>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">_</span>

[Opus] 📁 my-app | 🌿 feature/auth
<span style="color: var(--green-success);">█████████</span><span style="color: var(--text-muted);">░░░░░░░░░</span> 42% | $0.08 | 🕐 7m 3s
                    </div>

                    <a href="https://x.com/bcherny/status/2021700784019452195" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(6)">← sandbox</button>
                    <button class="nav-btn" onclick="switchTab(8)">keybindings →</button>
                </div>
            '''

T[(2,8)] = '''
                <div class="step-header">
                    <div class="step-number">8</div>
                    <div class="step-title">Перенастрой горячие клавиши</div>
                </div>
                <div class="step-body">
                    <p>А ты в курсе, что <strong>любое сочетание клавиш в Claude Code настраивается</strong>?</p>

                    <p>Запусти <code>/keybindings</code> и перепривяжи что угодно. Настройки перечитываются на лету — сразу видно, как ощущается.</p>

                    <div class="highlight-box">
                        <div class="label">Как это устроено</div>
                        Горячие клавиши живут в <code>~/.claude/keybindings.json</code>. Claude сам сгенерирует конфиг — просто опиши, чего ты хочешь.
                    </div>

                    <a href="https://x.com/bcherny/status/2021700883873165435" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(7)">← statusline</button>
                    <button class="nav-btn" onclick="switchTab(9)">hooks →</button>
                </div>
            '''

T[(2,9)] = '''
                <div class="step-header">
                    <div class="step-number">9</div>
                    <div class="step-title">Настрой hooks</div>
                </div>
                <div class="step-body">
                    <p>Хуки — это способ <strong>детерминированно вмешиваться в жизненный цикл Claude</strong>. Используй их, чтобы:</p>

                    <div class="highlight-box">
                        <div class="label">Use cases</div>
                        <ul style="margin: 8px 0 0 16px; line-height: 2;">
                            <li>Автоматически роутить permission-запросы в Slack или Opus</li>
                            <li>Подталкивать Claude продолжить, когда он подходит к концу хода (можно даже запустить агента или промпт, чтобы решить, стоит ли продолжать)</li>
                            <li>Пре-/пост-обрабатывать вызовы инструментов, например — добавлять собственное логирование</li>
                        </ul>
                    </div>

                    <p>Чтобы начать — попроси Claude добавить хук.</p>

                    <a href="https://x.com/bcherny/status/2021701059253874861" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(8)">← keybindings</button>
                    <button class="nav-btn" onclick="switchTab(10)">spinners →</button>
                </div>
            '''

T[(2,10)] = '''
                <div class="step-header">
                    <div class="step-number">10</div>
                    <div class="step-title">Кастомизируй глаголы спиннера</div>
                </div>
                <div class="step-body">
                    <p>Мелочи делают CC личным. Попроси Claude кастомизировать глаголы спиннера — <strong>добавить или заменить дефолтный список</strong> на свои.</p>

                    <p>Закоммить <code>settings.json</code> в репозиторий, чтобы делиться глаголами с командой.</p>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">в моих настройках сделай глаголы спиннера в стиле star trek.</span>

● <span class="command">Update</span>(~/.claude/settings.json)

<span style="color: var(--claude-orange);">✱ Beaming up…</span> (esc — прервать)
                    </div>

                    <a href="https://x.com/bcherny/status/2021701145023197516" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(9)">← hooks</button>
                    <button class="nav-btn" onclick="switchTab(11)">output →</button>
                </div>
            '''

T[(2,11)] = '''
                <div class="step-header">
                    <div class="step-number">11</div>
                    <div class="step-title">Используй output styles</div>
                </div>
                <div class="step-body">
                    <p>Запусти <code>/config</code> и выстави output style, чтобы Claude отвечал <strong>в другом тоне или формате</strong>.</p>

                    <div class="highlight-box">
                        <div class="label">Рекомендуемые стили</div>
                        <ul style="margin: 8px 0 0 16px; line-height: 2;">
                            <li><strong>Explanatory</strong> — отлично, когда знакомишься с новой кодовой базой: Claude по ходу объясняет фреймворки и паттерны</li>
                            <li><strong>Learning</strong> — Claude как коуч проведёт через изменения кода</li>
                            <li><strong>Custom</strong> — создай свой стиль, чтобы подстроить голос Claude под себя</li>
                        </ul>
                    </div>

                    <a href="https://x.com/bcherny/status/2021701379409273093" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(10)">← spinners</button>
                    <button class="nav-btn" onclick="switchTab(12)">customize →</button>
                </div>
            '''

T[(2,12)] = '''
                <div class="step-header">
                    <div class="step-number">12</div>
                    <div class="step-title">Кастомизируй всё!</div>
                </div>
                <div class="step-body">
                    <p>Claude Code сделан так, чтобы отлично работать из коробки. Когда всё же кастомизируешь — <strong>коммить <code>settings.json</code> в git</strong>, чтобы этим пользовалась вся команда.</p>

                    <p>Мы поддерживаем конфигурацию для репозитория, подпапки, лично для тебя или через <strong>политики уровня компании</strong>.</p>

                    <div class="highlight-box">
                        <div class="label">В цифрах</div>
                        Выбирай поведение — скорее всего, его можно настроить. Мы поддерживаем <strong>37 настроек</strong> и <strong>84 env-переменных</strong> (используй поле <code>"env"</code> в <code>settings.json</code>, чтобы не обёртывать всё в wrapper-скрипты).
                    </div>

                    <a href="https://x.com/bcherny/status/2021701636075458648" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(11)">← output</button>
                    <button class="nav-btn" onclick="switchTab(0)">back to intro →</button>
                </div>
            '''

T[(3,0)] = '''
                <div class="intro-panel">
                    <h1>Встроенная поддержка <span>Worktree</span></h1>
                    <p class="subtitle">
                        20 февраля 2026 Boris анонсировал встроенную поддержку git worktree в Claude Code. Агенты теперь могут работать параллельно, не мешая друг другу — в CLI, Desktop, IDE-расширениях, в вебе и на мобильных.
                    </p>
                    <a href="https://x.com/bcherny/status/2025007393290272904" target="_blank" rel="noopener noreferrer" class="author-link">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>
                        Тред @bcherny от 20 февраля 2026
                    </a>
                    <div class="intro-cta">
                        Кликай по вкладкам выше, чтобы изучить каждый совет <span class="arrow">→</span>
                        <div style="margin-top: 8px; font-size: 11px; color: var(--text-muted);">или используй стрелки ← →</div>
                    </div>
                </div>
            '''

T[(3,1)] = '''
                <div class="step-header">
                    <div class="step-number">1</div>
                    <div class="step-title">Изолируйся через <code>claude --worktree</code></div>
                </div>
                <div class="step-body">
                    <p>Чтобы запустить Claude Code в собственном git worktree — просто стартуй с опцией <code>--worktree</code>. Можно <strong>задать имя worktree</strong> или позволить Claude сделать это за тебя.</p>

                    <p>Так можно крутить несколько параллельных сеансов Claude Code в одном репозитории, не затирая правки друг друга.</p>

                    <div class="code-block">
<span class="prompt">$</span> <span class="command">claude --worktree my_worktree</span>

<span class="comment"># Также можно передать --tmux, чтобы запустить в отдельной Tmux-сессии</span>
<span class="prompt">$</span> <span class="command">claude --worktree my_worktree --tmux</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что изменилось</div>
                        В Claude Code Desktop встроенная поддержка worktree была уже давно — теперь она есть и в CLI.
                    </div>

                    <a href="https://x.com/bcherny/status/2025007394967957720" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(0)">← intro</button>
                    <button class="nav-btn" onclick="switchTab(2)">desktop →</button>
                </div>
            '''

T[(3,2)] = '''
                <div class="step-header">
                    <div class="step-number">2</div>
                    <div class="step-title">Worktree-режим в Desktop-приложении</div>
                </div>
                <div class="step-body">
                    <p>Если не хочешь сидеть в терминале — зайди во вкладку <strong>Code</strong> в Claude Desktop и поставь галочку <strong>worktree</strong>.</p>

                    <div class="highlight-box">
                        <div class="label">Как включить</div>
                        Открой Claude Desktop → вкладка Code → поставь галочку «worktree». Всё.
                    </div>

                    <a href="https://x.com/bcherny/status/2025007396691792100" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(1)">← cli</button>
                    <button class="nav-btn" onclick="switchTab(3)">subagents →</button>
                </div>
            '''

T[(3,3)] = '''
                <div class="step-header">
                    <div class="step-number">3</div>
                    <div class="step-title">Subagent'ы теперь поддерживают worktree</div>
                </div>
                <div class="step-body">
                    <p>Subagent'ы тоже умеют работать в изоляции через worktree, чтобы делать больше работы параллельно. Особенно полезно для <strong>крупных батчевых изменений и миграций кода</strong>.</p>

                    <p>Чтобы включить, попроси Claude использовать worktree для своих агентов. Доступно в CLI, Desktop, IDE-расширениях, веб и в мобильном приложении Claude Code.</p>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">Мигрируй весь синхронный io на async. Разбей изменения на батчи</span>
  <span class="command">и запусти 10 параллельных агентов с изоляцией через worktree.</span>
  <span class="command">Пусть каждый агент тестирует свои изменения end-to-end,</span>
  <span class="command">а затем открывает PR.</span>
                    </div>

                    <a href="https://x.com/bcherny/status/2025007398537380028" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(2)">← desktop</button>
                    <button class="nav-btn" onclick="switchTab(4)">agents →</button>
                </div>
            '''

T[(3,4)] = '''
                <div class="step-header">
                    <div class="step-number">4</div>
                    <div class="step-title">Кастомные агенты поддерживают git worktree</div>
                </div>
                <div class="step-body">
                    <p>Subagent'ов можно заставить <strong>всегда работать в собственном worktree</strong>. Для этого достаточно добавить <code>isolation: worktree</code> во frontmatter агента.</p>

                    <div class="code-block">
<span class="comment"># .claude/agents/worktree-worker.md</span>
<span class="key">---</span>
<span class="key">name:</span> <span class="string">worktree-worker</span>
<span class="key">model:</span> <span class="string">haiku</span>
<span class="key">isolation:</span> <span class="string">worktree</span>
<span class="key">---</span>
                    </div>

                    <a href="https://x.com/bcherny/status/2025007400235987300" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(3)">← subagents</button>
                    <button class="nav-btn" onclick="switchTab(5)">non-git →</button>
                </div>
            '''

T[(3,5)] = '''
                <div class="step-header">
                    <div class="step-number">5</div>
                    <div class="step-title">Доступно и для не-git систем контроля версий</div>
                </div>
                <div class="step-body">
                    <p>Если ты на <strong>Mercurial, Perforce или SVN</strong> — определи worktree-хуки, чтобы получить изоляцию без необходимости использовать Git.</p>

                    <div class="code-block">
<span class="prompt">$</span> <span class="command">cat .claude/settings.json</span>
{
  ...
  <span class="key">"hooks"</span>: {
    <span class="key">"WorktreeCreate"</span>: [
      { <span class="key">"command"</span>: <span class="string">"jj workspace add \\"$(cat /dev/stdin | jq -r '.name')\\"" </span>}
    ],
    <span class="key">"WorktreeRemove"</span>: [
      { <span class="key">"command"</span>: <span class="string">"jj workspace forget \\"$(cat /dev/stdin | jq -r '.worktree_path')\\"" </span>}
    ]
  },
  ...
}
                    </div>

                    <a href="https://x.com/bcherny/status/2025007401766948935" target="_blank" rel="noopener noreferrer" class="original-post">
                        ''' + SVG_PATH + '''
                        Открыть оригинал
                    </a>
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab(4)">← agents</button>
                    <button class="nav-btn" onclick="switchTab(0)">back to intro →</button>
                </div>
            '''


def main():
    src = json.load(open(SRC))
    out = []
    for part_idx in range(4):
        part = copy.deepcopy(src['data'][part_idx])
        for tab_idx, tab in enumerate(part['tabs']):
            key = (part_idx, tab_idx)
            if key not in T:
                raise RuntimeError(f"Missing translation for {key}")
            tab['html'] = T[key]
        out.append(part)

    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print('Written', OUT)

if __name__ == '__main__':
    main()
