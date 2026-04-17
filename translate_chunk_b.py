#!/usr/bin/env python3
"""Translate full-content.json data[4..7] to Russian into content-chunk-B.json."""
import json
from pathlib import Path

SRC = Path('/Users/vasyansk/Developers/MyProject/IaaC/Realmanual/claude-rules/full-content.json')
DST = Path('/Users/vasyansk/Developers/MyProject/IaaC/Realmanual/claude-rules/content-chunk-B.json')

SVG16 = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>'
SVG14 = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>'
SVG14_LINK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>'

CTA = '''                    <div class="intro-cta">
                        Кликайте по вкладкам выше, чтобы изучить каждый совет <span class="arrow">→</span>
                        <div style="margin-top: 8px; font-size: 11px; color: var(--text-muted);">или используйте стрелки ← →</div>
                    </div>'''

def intro_link(url, text):
    return f'''                    <a href="{url}" target="_blank" rel="noopener noreferrer" class="author-link">
                        {SVG16}
                        {text}
                    </a>'''

def orig_link(url):
    return f'''                    <a href="{url}" target="_blank" rel="noopener noreferrer" class="original-post">
                        {SVG14}
                        Открыть оригинал
                    </a>'''

def doc_link(url, text):
    return f'''                    <a href="{url}" target="_blank" rel="noopener noreferrer" class="original-post">
                        {SVG14_LINK}
                        {text}
                    </a>'''

def nav(prev_idx, prev_label, next_idx, next_label):
    return f'''                <div class="nav-buttons">
                    <button class="nav-btn" onclick="switchTab({prev_idx})">← {prev_label}</button>
                    <button class="nav-btn" onclick="switchTab({next_idx})">{next_label} →</button>
                </div>'''

# ============ PART 5 (idx 4) ============
P5_T0 = f'''
                <div class="intro-panel">
                    <h1>Отправка в <span>Production</span></h1>
                    <p class="subtitle">
                        27 февраля 2026 года Boris анонсировал две новые встроенные скилы для Claude Code: <strong>/simplify</strong> для улучшения качества кода и <strong>/batch</strong> для автоматизации параллельных миграций кода. В паре они автоматизируют большую часть работы, которая раньше уходила на сопровождение PR до production и параллельные миграции кода.
                    </p>
{intro_link("https://x.com/bcherny/status/2027534984534544489", "Тред @bcherny от 27 февраля 2026")}
{CTA}
                </div>
            '''

P5_T1 = f'''
                <div class="step-header">
                    <div class="step-number">1</div>
                    <div class="step-title">/simplify — улучшение качества кода</div>
                </div>
                <div class="step-body">
                    <p>Используйте <strong>параллельных агентов</strong>, чтобы улучшить качество кода, повысить его эффективность и убедиться в соответствии CLAUDE.md. Просто допишите <code>/simplify</code> к любому промпту.</p>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">hey claude make this code change then run /simplify</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Запускает параллельных агентов, которые проверяют изменённый код на возможности переиспользования, проблемы качества и улучшения эффективности — всё за один проход.
                    </div>

{orig_link("https://x.com/bcherny/status/2027534986178662573")}
                </div>
{nav(0, "intro", 2, "/batch")}
            '''

P5_T2 = f'''
                <div class="step-header">
                    <div class="step-number">2</div>
                    <div class="step-title">/batch — параллельные миграции кода</div>
                </div>
                <div class="step-body">
                    <p>Интерактивно спланируйте миграции кода, затем <strong>выполните их параллельно десятками агентов</strong>. Каждый агент работает в полной изоляции в git worktree, тестирует свою работу и выставляет PR.</p>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">/batch migrate src/ from Solid to React</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Как это работает</div>
                        Вы интерактивно планируете миграцию, затем /batch распределяет работу между параллельными агентами — каждый в своём worktree, каждый тестирует и создаёт PR независимо.
                    </div>

{orig_link("https://x.com/bcherny/status/2027534987462119828")}
                </div>
{nav(1, "/simplify", 0, "back to intro")}
            '''

# ============ PART 6 (idx 5) ============
P6_T0 = f'''
                <div class="intro-panel">
                    <h1>Три фичи. <span>Четыре дня.</span></h1>
                    <p class="subtitle">
                        <strong>/loop</strong> позволяет Claude запускать повторяющиеся задачи без присмотра до 3 дней. <strong>Code Review</strong> направляет команду агентов на каждый PR. <strong>/btw</strong> позволяет задавать вопросы прямо в процессе, не сбивая Claude с потока.
                    </p>
{intro_link("https://x.com/bcherny/status/2030193932404150413", "Тред @bcherny от 7 марта 2026")}
{intro_link("https://x.com/bcherny/status/2031089411820228645", "Тред @bcherny от 9 марта 2026")}
{intro_link("https://x.com/trq212/status/2031506296697131352", "Тред @trq212 от 10 марта 2026")}
{CTA}
                </div>
            '''

P6_T1 = f'''
                <div class="step-header">
                    <div class="step-number">1</div>
                    <div class="step-title">/loop — расписание повторяющихся задач</div>
                </div>
                <div class="step-body">
                    <p>Используйте <strong>/loop</strong>, чтобы планировать повторяющиеся задачи на срок до 3 дней подряд. Claude запускает ваш промпт с заданным интервалом, автономно обрабатывая долгие воркфлоу.</p>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">/loop babysit all my PRs. Auto-fix build issues and when comments come in, use a worktree agent to fix them</span>
                    </div>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">/loop every morning use the Slack MCP to give me a summary of top posts I was tagged in</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Планирует запуск промпта с заданным интервалом. Используйте для присмотра за PR, сводок Slack, мониторинга деплоев или любого повторяющегося воркфлоу — работает без присмотра до 3 дней.
                    </div>

{doc_link("https://code.claude.com/docs/en/scheduled-tasks", "Подробнее: запуск промптов по расписанию")}
                </div>
{nav(0, "intro", 2, "code-review")}
            '''

P6_T2 = f'''
                <div class="step-header">
                    <div class="step-number">2</div>
                    <div class="step-title">Code Review — агенты охотятся за багами</div>
                </div>
                <div class="step-body">
                    <p>Когда открывается PR, Claude отправляет <strong>команду агентов</strong> на охоту за багами. Сначала Anthropic построила это для себя — объём кода на инженера в этом году вырос на <strong>200%</strong>, и ревью стали узким местом.</p>

                    <p>Boris лично использовал это неделями до запуска. Оно ловит реальные баги, которые иначе он бы не заметил.</p>

                    <div class="code-block">
<span class="comment"># В вашем репозитории открывается PR</span>
<span class="comment"># Claude Code автоматически:</span>
<span class="comment">#   1. Читает диф</span>
<span class="comment">#   2. Отправляет специализированных ревью-агентов</span>
<span class="comment">#   3. Оставляет инлайновые комментарии к реальным багам</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Автоматически ревьюит каждый PR командой агентов. Каждый агент фокусируется на своей области — ошибки логики, проблемы безопасности, регрессии производительности — и оставляет инлайновые комментарии прямо в PR.
                    </div>

{orig_link("https://x.com/bcherny/status/2031089411820228645")}
                </div>
{nav(1, "/loop", 3, "/btw")}
            '''

P6_T3 = f'''
                <div class="step-header">
                    <div class="step-number">3</div>
                    <div class="step-title">/btw — задавайте вопросы, пока Claude работает</div>
                </div>
                <div class="step-body">
                    <p>Слеш-команда для <strong>побочных диалогов</strong>, пока Claude активно работает. Один ход, без вызова инструментов, но с полным контекстом разговора. Сделано <strong>@ErikSchluntz</strong> как side-project — 1,5 млн просмотров у запускающего твита.</p>

                    <div class="code-block">
<span class="comment"># Claude посреди задачи, рефакторит auth middleware...</span>
<span class="prompt">&gt;</span> <span class="command">/btw what does the retry logic do?</span>
                    </div>

                    <div class="code-block">
<span class="comment"># Claude отвечает встроенно, не прерывая свою работу:</span>
<span class="string">The retry logic in auth.ts uses exponential backoff</span>
<span class="string">with a max of 3 attempts. It catches 401/403 errors</span>
<span class="string">and refreshes the token before retrying.</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Позволяет задать быстрый вопрос посреди задачи, не прерывая поток Claude. Ответ — один ход без вызова инструментов, но Claude видит полный контекст того, над чем работает, так что ответы привязаны к текущему разговору.
                    </div>

{orig_link("https://x.com/trq212/status/2031506296697131352")}
                </div>
{nav(2, "code-review", 0, "back to intro")}
            '''

# ============ PART 7 (idx 6) ============
P7_T0 = f'''
                <div class="intro-panel">
                    <h1>Релизы в конце <span>недели</span></h1>
                    <p class="subtitle">
                        Команда Claude Code выпустила 8 фич в одном треде: <strong>/effort max</strong> для более глубоких рассуждений, <strong>voice mode</strong> для всех, <strong>remote control sessions</strong>, <strong>setup-скрипты</strong>, <strong>именование сессий</strong>, <strong>/color</strong> и новый хук <strong>PostCompact</strong>.
                    </p>
{intro_link("https://x.com/trq212/status/2032632596572811575", "Тред @trq212 от 13 марта 2026")}
{CTA}
                </div>
            '''

P7_T1 = f'''
                <div class="step-header">
                    <div class="step-number">1</div>
                    <div class="step-title">/effort — режим максимальных рассуждений</div>
                </div>
                <div class="step-body">
                    <p>Установите уровень <strong>'max'</strong>, и Claude будет рассуждать дольше, используя столько токенов, сколько потребуется. Сжигает ваши лимиты быстрее, поэтому активируется <strong>на сессию</strong>.</p>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">/effort max</span>
                    </div>

                    <div class="code-block">
<span class="comment"># Доступны четыре уровня:</span>
<span class="comment">#   low    - быстрые ответы, минимум рассуждений</span>
<span class="comment">#   medium - сбалансированный (по умолчанию)</span>
<span class="comment">#   high   - более глубокие рассуждения</span>
<span class="comment">#   max    - рассуждает столько, сколько нужно</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Устанавливает уровень усилий на рассуждения для текущей сессии. На 'max' Claude думает дольше и тратит больше токенов на ответ — полезно для сложной отладки, архитектурных решений или хитрых мест в коде, где вы хотите, чтобы Claude действительно продумал всё.
                    </div>

{orig_link("https://x.com/trq212/status/2032632596572811575")}
                </div>
{nav(0, "intro", 2, "remote")}
            '''

P7_T2 = f'''
                <div class="step-header">
                    <div class="step-number">2</div>
                    <div class="step-title">Remote Control — запуск новых сессий</div>
                </div>
                <div class="step-body">
                    <p>Запустите <code>claude remote-control</code>, а затем запускайте <strong>новые локальные сессии</strong> прямо из мобильного приложения. Доступно на тарифах Max, Team и Enterprise (v2.1.74+).</p>

                    <div class="code-block">
<span class="prompt">$</span> <span class="command">claude remote-control</span>

<span class="comment"># Затем откройте мобильное приложение Claude</span>
<span class="comment"># Нажмите "Code" → начните новую сессию</span>
<span class="comment"># Claude подключится к вашей локальной машине</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Позволяет запускать новые сессии Claude Code с телефона, подключённые к вашему локальному dev-окружению. Отошли от стола, подумали о чём-то — и стартанули задачу с мобильного, а Claude выполняет её на вашей машине.
                    </div>

{orig_link("https://x.com/trq212/status/2032632597843779861")}
                </div>
{nav(1, "/effort", 3, "voice")}
            '''

P7_T3 = f'''
                <div class="step-header">
                    <div class="step-number">3</div>
                    <div class="step-title">Voice Mode — говорите с Claude Code</div>
                </div>
                <div class="step-body">
                    <p>Voice mode теперь раскатан на <strong>100% пользователей</strong>, в том числе в Claude Code Desktop и Cowork. Иногда просто нужен кто-то, с кем можно поговорить.</p>

                    <div class="code-block">
<span class="comment"># В Claude Code Desktop или Cowork:</span>
<span class="comment"># Кликните иконку микрофона</span>
<span class="comment"># Говорите естественно — Claude слышит и отвечает</span>

<span class="prompt">🎙</span> <span class="string">"Hey Claude, fix all the bugs in this repo."</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Позволяет говорить с Claude Code вместо набора текста. Доступно в Desktop и Cowork — удобно для работы без рук, диктовки сложных требований или когда вы думаете быстрее, чем печатаете.
                    </div>

{orig_link("https://x.com/trq212/status/2032632599429136753")}
                </div>
{nav(2, "remote", 4, "setup")}
            '''

P7_T4 = f'''
                <div class="step-header">
                    <div class="step-number">4</div>
                    <div class="step-title">Setup-скрипты — автоматизация облачных окружений</div>
                </div>
                <div class="step-body">
                    <p>Добавьте <strong>setup-скрипт</strong> в Claude Code на вебе и в desktop. Он запускается перед стартом Claude Code в облачном окружении — установить зависимости, настроить параметры, задать env-переменные.</p>

                    <div class="code-block">
<span class="comment"># В настройках "Update cloud environment":</span>

<span class="comment"># Name:</span>
<span class="string">apps</span>

<span class="comment"># Setup-скрипт (запускается при старте новой сессии):</span>
<span class="keyword">#!/bin/bash</span>
<span class="command">yarn install</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Автоматически запускает bash-скрипт при старте новой сессии Claude Code в облачном окружении. Пропускается при возобновлении существующей сессии. Используйте, чтобы поставить зависимости, настроить конфиги или подготовить окружение до начала работы Claude.
                    </div>

{orig_link("https://x.com/trq212/status/2032632601064907037")}
                </div>
{nav(3, "voice", 5, "--name")}
            '''

P7_T5 = f'''
                <div class="step-header">
                    <div class="step-number">5</div>
                    <div class="step-title">claude --name — именование сессий</div>
                </div>
                <div class="step-body">
                    <p>Называйте сессию при запуске флагом <code>--name</code>. Это упрощает опознание сессий, когда их несколько параллельно.</p>

                    <div class="code-block">
<span class="prompt">$</span> <span class="command">claude --name "auth-refactor"</span>

<span class="comment"># Теперь ваша сессия отображается как "auth-refactor"</span>
<span class="comment"># вместо обезличенного session ID</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Даёт сессии Claude Code человекочитаемое имя при старте. Особенно полезно при жонглировании несколькими worktree или сессиями — вы с первого взгляда понимаете, где какая задача.
                    </div>

{orig_link("https://x.com/trq212/status/2032632602629386348")}
                </div>
{nav(4, "setup", 6, "auto-name")}
            '''

P7_T6 = f'''
                <div class="step-header">
                    <div class="step-number">6</div>
                    <div class="step-title">Автоматическое именование сессий после plan mode</div>
                </div>
                <div class="step-body">
                    <p>После plan mode Claude <strong>автоматически назовёт вашу сессию</strong> исходя из того, над чем вы работаете. Ручное именование не требуется.</p>

                    <div class="code-block">
<span class="comment"># Войдите в plan mode, опишите задачу:</span>
<span class="prompt">&gt;</span> <span class="command">shift+tab</span>
<span class="prompt">[plan]&gt;</span> <span class="string">Refactor the auth middleware to use JWT</span>

<span class="comment"># После выхода из plan mode сессии присваивается имя автоматически:</span>
<span class="comment"># Session: "refactor-auth-jwt"</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Claude выводит описательное имя сессии из разговора в plan mode. Хорошо сочетается с <code>claude --name</code> — используйте <code>--name</code>, когда заранее знаете, что делаете, и пусть авто-именование сработает, когда вы начинаете с планирования.
                    </div>

{orig_link("https://x.com/trq212/status/2032632602629386348")}
                </div>
{nav(5, "--name", 7, "/color")}
            '''

P7_T7 = f'''
                <div class="step-header">
                    <div class="step-number">7</div>
                    <div class="step-title">/color — кастомизация цвета промпта</div>
                </div>
                <div class="step-body">
                    <p>Меняйте цвет поля ввода промпта командой <code>/color</code>. Полезно, чтобы визуально различать сессии, когда их много параллельно.</p>

                    <div class="code-block">
<span class="prompt">&gt;</span> <span class="command">/color</span>

<span class="comment"># Выберите цвет промпта для этой сессии</span>
<span class="comment"># Помогает различать сессии с первого взгляда</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Устанавливает цвет поля ввода промпта в текущей сессии. Когда у вас 3-5 сессий в разных терминалах, цветовая разметка делает очевидным, где какая.
                    </div>

{orig_link("https://x.com/trq212/status/2032632602629386348")}
                </div>
{nav(6, "auto-name", 8, "postcompact")}
            '''

P7_T8 = f'''
                <div class="step-header">
                    <div class="step-number">8</div>
                    <div class="step-title">Хук PostCompact — реакция на сжатие контекста</div>
                </div>
                <div class="step-body">
                    <p>Новое событие хука: <strong>PostCompact</strong>. Срабатывает после того, как Claude сжимает контекст диалога, позволяя подмешать инструкции или выполнить команды при каждом сжатии.</p>

                    <div class="code-block">
<span class="comment"># В конфиге хуков:</span>
<span class="keyword">"hooks"</span>: {{
  <span class="string">"PostCompact"</span>: [{{
    <span class="string">"matcher"</span>: <span class="string">""</span>,
    <span class="string">"hooks"</span>: [{{
      <span class="string">"type"</span>: <span class="string">"command"</span>,
      <span class="string">"command"</span>: <span class="string">"echo 'Context was compacted'"</span>
    }}]
  }}]
}}
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Срабатывает после сжатия окна контекста Claude. Используйте, чтобы повторно подмешать критичные инструкции, которые могли потеряться при сжатии, логировать факт сжатия или запускать любую автоматизацию при сбросе контекста.
                    </div>

{orig_link("https://x.com/trq212/status/2032632602629386348")}
                </div>
{nav(7, "/color", 0, "back to intro")}
            '''

# ============ PART 8 (idx 7) ============
P8_T0 = f'''
                <div class="intro-panel">
                    <h1>Новые <span>суперсилы</span></h1>
                    <p class="subtitle">
                        Auto mode убивает запросы на разрешения за счёт встроенных классификаторов безопасности, <strong>/schedule</strong> создаёт облачные повторяющиеся задания, работающие поверх вашего ноутбука, <strong>iMessage</strong> становится каналом, а <strong>auto-dream</strong> держит память в порядке.
                    </p>
{intro_link("https://x.com/noahzweben/status/2036129220959805859", "Пост @noahzweben от 23 марта 2026")}
{intro_link("https://x.com/bcherny/status/2036555259997462541", "Пост @bcherny от 24 марта 2026")}
{intro_link("https://x.com/trq212/status/2036959638646866021", "Пост @trq212 от 25 марта 2026")}
{CTA}
                </div>
            '''

P8_T1 = f'''
                <div class="step-header">
                    <div class="step-number">1</div>
                    <div class="step-title">Auto Mode — безопасный способ пропускать запросы разрешений</div>
                </div>
                <div class="step-body">
                    <p>Вместо того чтобы одобрять каждую запись файла и bash-команду или полностью отключать разрешения через <code>--dangerously-skip-permissions</code>, <strong>auto mode</strong> позволяет Claude принимать решения о разрешениях за вас.</p>

                    <div class="code-block">
<span class="comment"># Включить auto mode</span>
$ claude --enable-auto-mode

<span class="comment"># Или переключайтесь по shift+tab в сессии:</span>
<span class="comment"># plan mode → auto mode → normal mode</span>
                    </div>

                    <div class="highlight-box">
                        <div class="label">Как это работает</div>
                        Anthropic построила и протестировала классификаторы, которые оценивают каждое действие перед запуском. Безопасные операции (чтение файлов, запуск тестов) авто-одобряются. Рискованные (удаление файлов, force-push, запуск неизвестных скриптов) всё равно выносятся на подтверждение. Это золотая середина между 50 кликами "одобрить" за сессию и yolo-режимом без страховки.
                    </div>

                    <p>Комментарий Boris: <em>"no 👏 more 👏 permission prompts 👏"</em></p>

{orig_link("https://x.com/bcherny/status/2036555259997462541")}
                </div>
{nav(0, "intro", 2, "/schedule")}
            '''

P8_T2 = f'''
                <div class="step-header">
                    <div class="step-number">2</div>
                    <div class="step-title">/schedule — облачные задания прямо из терминала</div>
                </div>
                <div class="step-body">
                    <p>Используйте <code>/schedule</code>, чтобы создавать <strong>повторяющиеся облачные задания</strong> для Claude прямо из терминала. В отличие от <code>/loop</code> (работает локально до 3 дней), запланированные задания выполняются в облаке — они работают даже при закрытом ноутбуке.</p>

                    <div class="code-block">
<span class="comment"># Запланируйте ежедневное обновление документации</span>
$ /schedule a daily job that looks at all PRs shipped
  since yesterday and update our docs based on the
  changes. Use the Slack MCP to message #docs-update
  with the changes
                    </div>

                    <div class="highlight-box">
                        <div class="label">Кейсы использования</div>
                        Команда Anthropic использует это внутри, чтобы автоматически разруливать падения CI, пушить обновления доков и крутить автоматизации, которые должны работать поверх закрытого ноутбука. Думайте об этом как о cron-задачах, но работу делает Claude.
                    </div>

{orig_link("https://x.com/noahzweben/status/2036129220959805859")}
                </div>
{nav(1, "auto mode", 3, "iMessage")}
            '''

P8_T3 = f'''
                <div class="step-header">
                    <div class="step-number">3</div>
                    <div class="step-title">Плагин iMessage — пишите Claude с телефона</div>
                </div>
                <div class="step-body">
                    <p>iMessage теперь доступен как <strong>канал Claude Code</strong>. Установите плагин и пишите Claude так же, как писали бы другу — с любого Apple-устройства.</p>

                    <div class="code-block">
<span class="comment"># Установите плагин iMessage</span>
$ /plugin install imessage@claude-plugins-official
                    </div>

                    <div class="highlight-box">
                        <div class="label">Что это даёт</div>
                        Claude Code становится контактом в приложении Messages. Отправляйте ему задачи, получайте ответы в виде iMessage. Работает с iPhone, iPad или Mac — терминал не нужен. Хорошо сочетается с remote control sessions для запуска работы откуда угодно.
                    </div>

{orig_link("https://x.com/trq212/status/2036959638646866021")}
                </div>
{nav(2, "/schedule", 4, "memory")}
            '''

P8_T4 = f'''
                <div class="step-header">
                    <div class="step-number">4</div>
                    <div class="step-title">Auto-Memory и Auto-Dream — постоянная самоочищающаяся память</div>
                </div>
                <div class="step-body">
                    <p>В Claude Code теперь встроенная система памяти. Запустите <code>/memory</code>, чтобы её настроить.</p>

                    <div class="code-block">
<span class="comment"># Посмотреть и настроить параметры памяти</span>
$ /memory

<span class="comment"># Типы памяти:</span>
<span class="comment">#   User memory    → сохраняется в ~/.claude/CLAUDE.md</span>
<span class="comment">#   Project memory → сохраняется в ./CLAUDE.md</span>

<span class="comment"># Запустить dream (консолидацию памяти)</span>
$ /dream
                    </div>

                    <div class="highlight-box">
                        <div class="label">Auto-memory</div>
                        Когда включено, Claude автоматически сохраняет предпочтения, исправления и паттерны между сессиями. Ручного редактирования CLAUDE.md не требуется — Claude сам пишет воспоминания за вас.
                    </div>

                    <div class="highlight-box" style="margin-top: 12px;">
                        <div class="label">Auto-dream</div>
                        По мере накопления память может замусориться — устаревшие допущения, пересекающиеся записи, низкосигнальные заметки. Auto-dream запускает субагента, который периодически просматривает прошлые сессии, оставляет важное, удаляет лишнее и сливает инсайты в более чистую структурированную память. Название отсылает к тому, как REM-сон консолидирует кратковременную память в долговременную.
                    </div>
                </div>
{nav(3, "iMessage", 0, "back to intro")}
            '''

# ============ ASSEMBLE ============
src = json.load(open(SRC))
data = src['data']

parts_tabs = [
    (4, [P5_T0, P5_T1, P5_T2]),
    (5, [P6_T0, P6_T1, P6_T2, P6_T3]),
    (6, [P7_T0, P7_T1, P7_T2, P7_T3, P7_T4, P7_T5, P7_T6, P7_T7, P7_T8]),
    (7, [P8_T0, P8_T1, P8_T2, P8_T3, P8_T4]),
]

result = []
for idx, htmls in parts_tabs:
    orig = data[idx]
    assert len(orig['tabs']) == len(htmls), f'Mismatch at {idx}: {len(orig["tabs"])} vs {len(htmls)}'
    new_tabs = []
    for t, html in zip(orig['tabs'], htmls):
        new_tabs.append({'label': t['label'], 'html': html})
    result.append({
        'idx': idx,
        'label': orig['label'],
        'tabCount': orig['tabCount'],
        'tabs': new_tabs,
    })

with open(DST, 'w') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print('Written:', DST)
print('Parts:', len(result), 'Tabs per part:', [len(p['tabs']) for p in result])
