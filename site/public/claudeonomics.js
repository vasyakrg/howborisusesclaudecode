
(async function () {
    const root = document.getElementById('dash-root');
    const methEl = document.getElementById('methodology');
    if (!root) return;

    // Prefer the Netlify function (live, refreshes daily). Fall back to
    // the committed JSON so the page still works under a plain static
    // dev server (e.g. `python -m http.server`) where /api/* 404s.
    let data;
    try {
        let res = await fetch('/api/claudeonomics', { cache: 'no-cache' });
        if (!res.ok) throw new Error('api ' + res.status);
        data = await res.json();
    } catch (_apiErr) {
        try {
            const res = await fetch('/claudeonomics-data.json', { cache: 'no-cache' });
            if (!res.ok) throw new Error('HTTP ' + res.status);
            data = await res.json();
        } catch (e) {
            // Data source unavailable — leave the pre-rendered static HTML intact.
            console.warn('claudeonomics: using static fallback,', e.message);
            return;
        }
    }

    const AGENT_ORDER = ['claude-code', 'copilot-cli', 'openai-codex-cli', 'gemini-cli', 'copilot-swe', 'openai-codex-cloud'];

    // Inline SVG logos (from simple-icons, MIT-licensed repackaging of brand marks).
    // Each is a single <svg> with viewBox 0 0 24 24, fill=currentColor so the row
    // accent color shows through. 4 unique marks, 6 rows (GitHub Copilot + OpenAI
    // share across CLI/cloud variants).
    const ANTHROPIC_SVG  = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M17.3041 3.541h-3.6718l6.696 16.918H24Zm-10.6082 0L0 20.459h3.7442l1.3693-3.5527h7.0052l1.3693 3.5528h3.7442L10.5363 3.5409Zm-.3712 10.2232 2.2914-5.9456 2.2914 5.9456Z"/></svg>';
    const COPILOT_SVG    = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M23.922 16.997C23.061 18.492 18.063 22.02 12 22.02 5.937 22.02.939 18.492.078 16.997A.641.641 0 0 1 0 16.741v-2.869a.883.883 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.098 10.098 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952C7.255 2.937 9.248 1.98 11.978 1.98c2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.841.841 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256Zm-11.75-5.992h-.344a4.359 4.359 0 0 1-.355.508c-.77.947-1.918 1.492-3.508 1.492-1.725 0-2.989-.359-3.782-1.259a2.137 2.137 0 0 1-.085-.104L4 11.746v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.359 4.359 0 0 1-.355-.508Zm2.328 3.25c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm-5 0c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm3.313-6.185c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"/></svg>';
    const OPENAI_SVG     = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"/></svg>';
    const GEMINI_SVG     = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M11.04 19.32Q12 21.51 12 24q0-2.49.93-4.68.96-2.19 2.58-3.81t3.81-2.55Q21.51 12 24 12q-2.49 0-4.68-.93a12.3 12.3 0 0 1-3.81-2.58 12.3 12.3 0 0 1-2.58-3.81Q12 2.49 12 0q0 2.49-.96 4.68-.93 2.19-2.55 3.81a12.3 12.3 0 0 1-3.81 2.58Q2.49 12 0 12q2.49 0 4.68.96 2.19.93 3.81 2.55t2.55 3.81"/></svg>';

    const LOGOS = {
        'claude-code':        ANTHROPIC_SVG,
        'copilot-cli':        COPILOT_SVG,
        'copilot-swe':        COPILOT_SVG,
        'openai-codex-cli':   OPENAI_SVG,
        'openai-codex-cloud': OPENAI_SVG,
        'gemini-cli':         GEMINI_SVG,
    };
    // CLI agents run in the user's terminal; cloud agents run async on a service.
    // Split into two challenger charts so we're comparing apples to apples.
    const CLI_CHALLENGER_KEYS = ['copilot-cli', 'openai-codex-cli', 'gemini-cli'];
    const CLOUD_CHALLENGER_KEYS = ['copilot-swe', 'openai-codex-cloud'];

    // Per-agent earliest week to chart. Each line starts on the Monday of
    // the week each product first became publicly available to anyone
    // outside the vendor — research preview, public preview, beta, or
    // open-source release, whichever came first. NOT GA dates. We use
    // first-public-availability so the chart preserves each product's
    // complete adoption history (the preview-phase ramp is usually the
    // most interesting part of the curve), at the cost of not being a
    // strict GA-vs-GA comparison. Methodology spells this out.
    //
    // Dates verified against vendor announcements:
    //   Claude Code:        Feb 24 2025 — research preview (alongside Claude 3.7 Sonnet)
    //   Codex CLI:          Apr 16 2025 product launch, but May–Jul 2025
    //                       data was a noise floor (single-digit weeks
    //                       except a 153 outlier on May 5 that was almost
    //                       certainly fork-pollution). First sustained
    //                       adoption week is Jul 28 2025 (157 commits).
    //                       We clip to Jul 28 so the line doesn't open
    //                       with a misleading outlier. Documented inline.
    //   Codex (ChatGPT):    May 16 2025 product preview, but the
    //                       chatgpt-codex-connector trailer doesn't appear in
    //                       any commits until Sep 1 2025 — the trailer string
    //                       was added later when the connector matured. We
    //                       clip to Sep 1 (first detectable trailer week)
    //                       rather than May 12 (product launch) so the chart
    //                       doesn't show 16 weeks of flat zeros.
    //   Copilot Coding Agent: May 19 2025 — public preview at Microsoft Build
    //   Gemini CLI:         Jun 25 2025 — open-source launch
    //   Copilot CLI:        Sep 25 2025 — public preview
    const AGENT_CUTOFF = {
        'claude-code':        '2025-02-24',
        'openai-codex-cli':   '2025-07-28', // first sustained-adoption week (see comment above)
        'copilot-swe':        '2025-05-19',
        'gemini-cli':         '2025-06-23',
        'openai-codex-cloud': '2025-09-01',
        'copilot-cli':        '2025-09-22',
    };

    // Pick the most-recent closed week for KPI headline (first non-partial from the end).
    const claude = data.agents['claude-code'];
    const closedWeeks = claude.weekly.filter(w => !w.partial && w.count != null);
    const latest = closedWeeks[closedWeeks.length - 1];
    const prior = closedWeeks[closedWeeks.length - 2];
    const latestIdx = claude.weekly.indexOf(latest);

    function fmt(n) {
        if (n == null) return '—';
        if (n >= 1e6) return (n / 1e6).toFixed(n >= 1e7 ? 1 : 2) + 'M';
        if (n >= 1e3) return (n / 1e3).toFixed(n >= 1e4 ? 0 : 1) + 'k';
        return n.toString();
    }
    function pct(n) { return (n * 100).toFixed(n < 0.1 ? 2 : 1) + '%'; }
    function delta(a, b) {
        if (a == null || b == null || b === 0) return null;
        return (a - b) / b;
    }
    function deltaEl(d) {
        if (d == null) return '<span class="delta-flat">—</span>';
        const cls = d > 0.003 ? 'delta-up' : d < -0.003 ? 'delta-down' : 'delta-flat';
        const arrow = d > 0.003 ? '▲' : d < -0.003 ? '▼' : '·';
        return '<span class="' + cls + '">' + arrow + ' ' + (d * 100).toFixed(1) + '%</span>';
    }

    // Totals for the latest closed week across all tracked agents.
    let trackedTotal = 0;
    let priorTrackedTotal = 0;
    for (const key of AGENT_ORDER) {
        const a = data.agents[key];
        if (!a) continue;
        const cur = a.weekly[latestIdx];
        const pre = a.weekly[latestIdx - 1];
        if (cur && cur.count != null && !cur.partial) trackedTotal += cur.count;
        if (pre && pre.count != null && !pre.partial) priorTrackedTotal += pre.count;
    }
    const claudeShare = latest.count / trackedTotal;

    // All-time cumulative: sum all weekly counts (closed + partial).
    const allTime = claude.weekly.reduce((sum, w) => sum + (w.count || 0), 0);

    // ---- Render KPI strip ----
    const kpiHtml = `
      <div class="kpi-strip">
        <div class="kpi">
          <div class="kpi-label">Claude Code / week</div>
          <div class="kpi-value">${fmt(latest.count)}</div>
          <div class="kpi-delta">WoW ${deltaEl(delta(latest.count, prior?.count))}</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">All time</div>
          <div class="kpi-value">${fmt(allTime)}</div>
          <div class="kpi-delta">cumulative since May 2025</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Claude share of tracked</div>
          <div class="kpi-value">${pct(claudeShare)}</div>
          <div class="kpi-delta">of ${fmt(trackedTotal)} weekly commits</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">All tracked agents / week</div>
          <div class="kpi-value small">${fmt(trackedTotal)}</div>
          <div class="kpi-delta">WoW ${deltaEl(delta(trackedTotal, priorTrackedTotal))}</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Week ending</div>
          <div class="kpi-value small">${formatShortDate(latest.end)}</div>
          <div class="kpi-delta">${closedWeeks.length} closed weeks of data</div>
        </div>
      </div>`;

    // ---- Build charts (inline SVG) ----
    // Charts only show closed weeks. Partial (in-progress) weeks are
    // excluded because plotting them as a single data point makes the
    // current-week bar look like a massive drop (only ~5 of 7 days counted).
    // Charts only show closed weeks. Each point carries start+end so the
    // axis labels and tooltips can both show the full week range. We also
    // clip each agent's series to its launch-week cutoff so we don't draw
    // pre-existence data for products that hadn't launched yet.
    const passesCutoff = (agentKey, weekStart) => {
        const cutoff = AGENT_CUTOFF[agentKey];
        return !cutoff || weekStart >= cutoff;
    };
    const heroPts = claude.weekly
        .filter(w => w.count != null && !w.partial && passesCutoff('claude-code', w.start))
        .map(w => ({ x: w.start, end: w.end, y: w.count }));
    const buildSeries = (keys) => keys.map(k => ({
        key: k,
        label: data.agents[k].label,
        color: data.agents[k].color,
        points: data.agents[k].weekly
            .filter(w => w.count != null && !w.partial && passesCutoff(k, w.start))
            .map(w => ({ x: w.start, end: w.end, y: w.count })),
    }));
    const cliChallengers = buildSeries(CLI_CHALLENGER_KEYS);
    const cloudChallengers = buildSeries(CLOUD_CHALLENGER_KEYS);

    const heroFirst = heroPts[0];
    const heroLast = heroPts[heroPts.length - 1];
    // Compute the global min start and max end across all series in a group,
    // so the chart header / x-axis range reflects the earliest line, not just
    // whatever happens to be first in the series array. Each agent has its own
    // launch-date cutoff so the leftmost series varies.
    const seriesDateRange = (series) => {
        const allPts = series.flatMap(s => s.points);
        if (!allPts.length) return { first: null, last: null };
        const first = allPts.reduce((a, b) => (a.x < b.x ? a : b));
        const last = allPts.reduce((a, b) => (a.x > b.x ? a : b));
        return { first, last };
    };
    const { first: cliFirst,   last: cliLast }   = seriesDateRange(cliChallengers);
    const { first: cloudFirst, last: cloudLast } = seriesDateRange(cloudChallengers);

    const challengerChartHtml = (id, title, subtitle, first, last, series) => `
      <div class="chart-section">
        <div class="chart-header">
          <div>
            <div class="chart-title">${title}</div>
            <div class="chart-subtitle">${subtitle}</div>
          </div>
          <div class="chart-subtitle">${first?.x ?? ''} → ${last?.end ?? ''}</div>
        </div>
        <div class="chart-box" id="${id}-chart-box">
          <div id="${id}-chart-mount"></div>
          <div class="chart-tooltip" id="${id}-tooltip">
            <div class="chart-tooltip-label" id="${id}-tooltip-label">—</div>
            <div class="chart-tooltip-count alt"><span id="${id}-tooltip-count">0</span> commits</div>
            <div class="chart-tooltip-time" id="${id}-tooltip-time">—</div>
          </div>
          <div class="chart-x-labels">
            <span>${formatShortDate(first?.x)}</span>
            <span>${formatShortDate(last?.end)}</span>
          </div>
        </div>
      </div>`;

    const chartsHtml = `
      <div class="chart-section">
        <div class="chart-header">
          <div>
            <div class="chart-title">Claude Code — weekly commits</div>
            <div class="chart-subtitle">public GitHub, committer-date bucketed · terminal CLI agent</div>
          </div>
          <div class="chart-subtitle">${heroFirst?.x ?? ''} → ${heroLast?.end ?? ''}</div>
        </div>
        <div class="chart-box" id="hero-chart-box">
          <div id="hero-chart-mount"></div>
          <div class="chart-tooltip" id="hero-tooltip">
            <div class="chart-tooltip-count"><span id="hero-tooltip-count">0</span> commits</div>
            <div class="chart-tooltip-time" id="hero-tooltip-time">—</div>
          </div>
          <div class="chart-x-labels">
            <span>${formatShortDate(heroFirst?.x)}</span>
            <span>${formatShortDate(heroLast?.end)}</span>
          </div>
        </div>
      </div>
      ${challengerChartHtml('cli', 'CLI challengers — weekly commits', 'Terminal agents like Claude Code: Copilot CLI, Codex CLI, Gemini CLI (separate scale)', cliFirst, cliLast, cliChallengers)}
      ${challengerChartHtml('cloud', 'Cloud / async challengers — weekly commits', 'Agents that run on a service, not in your terminal: Copilot Coding Agent, Codex (ChatGPT)', cloudFirst, cloudLast, cloudChallengers)}`;

    // ---- Leaderboard ----
    const leaderboardRows = AGENT_ORDER
        .map(key => {
            const a = data.agents[key];
            if (!a) return null;
            const cur = a.weekly[latestIdx];
            const pre = a.weekly[latestIdx - 1];
            if (!cur || cur.count == null) return null;
            return {
                key, label: a.label, color: a.color, category: a.category || 'cli',
                count: cur.count, prior: pre?.count,
                share: cur.count / trackedTotal,
                delta: delta(cur.count, pre?.count),
            };
        })
        .filter(Boolean)
        .sort((x, y) => y.count - x.count);

    const topCount = leaderboardRows[0]?.count || 1;
    const leaderboardHtml = `
      <div class="chart-section">
        <div class="chart-header">
          <div>
            <div class="chart-title">Agent leaderboard — week of ${formatShortDate(latest.start)} → ${formatShortDate(latest.end)}</div>
            <div class="chart-subtitle">ranked by weekly commits</div>
          </div>
        </div>
        <div class="chart-box" style="padding: 0;">
          <table class="leaderboard">
            <thead>
              <tr>
                <th style="width: 32px;">#</th>
                <th>Agent</th>
                <th class="hide-mobile">Type</th>
                <th class="num">Weekly commits</th>
                <th class="num hide-mobile">Share</th>
                <th class="num hide-mobile">WoW</th>
              </tr>
            </thead>
            <tbody>
              ${leaderboardRows.map((r, i) => `
                <tr style="--row-accent:${r.color};">
                  <td style="color: var(--text-muted);">${i + 1}</td>
                  <td>
                    <div class="agent-cell">
                      <span class="agent-logo" style="color:${r.color}">${LOGOS[r.key] || ''}</span>
                      <span>${r.label}</span>
                    </div>
                  </td>
                  <td class="hide-mobile"><span class="type-pill ${r.category}">${r.category === 'cli' ? 'CLI' : 'Cloud'}</span></td>
                  <td class="num">${r.count.toLocaleString()}</td>
                  <td class="num hide-mobile">${pct(r.share)}</td>
                  <td class="num hide-mobile">${deltaEl(r.delta)}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>`;

    root.innerHTML = kpiHtml + chartsHtml + leaderboardHtml;
    methEl.style.display = 'block';

    // Mount charts (SVG + hover) after HTML is in the DOM
    mountHeroChart(heroPts);
    mountChallengersChart('cli', cliChallengers);
    mountChallengersChart('cloud', cloudChallengers);

    function formatShortDate(iso) {
        if (!iso) return '';
        const d = new Date(iso + 'T00:00:00Z');
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', timeZone: 'UTC' });
    }

    // End-of-line logos sit on top of the chart as absolutely-positioned HTML
    // elements, NOT inside the SVG. The chart SVG uses preserveAspectRatio=none
    // which non-uniformly stretches its viewBox to fill the container — any
    // <g> or nested <svg> inside would get squished horizontally on narrow
    // viewports (mobile: 900 viewBox-wide stretched into ~350 screen pixels).
    // HTML elements live outside that coordinate system, so logos stay at a
    // consistent pixel size.
    //
    // mountEndLogos() takes the chart box, the SVG element, its viewBox width
    // and an array of endpoints {key, color, vx, vy} where vx/vy are in
    // viewBox coords. It positions an absolutely-placed <div> for each logo
    // and sets up a ResizeObserver to reposition on resize.
    function mountEndLogos(chartBoxEl, svgEl, W, H, endpoints) {
        // Clear any previous overlay (on re-render / resize)
        chartBoxEl.querySelectorAll('.chart-end-logo').forEach(n => n.remove());
        if (!endpoints || !endpoints.length) return;

        const place = () => {
            const existing = chartBoxEl.querySelectorAll('.chart-end-logo');
            existing.forEach(n => n.remove());

            const svgRect = svgEl.getBoundingClientRect();
            const boxRect = chartBoxEl.getBoundingClientRect();
            const scaleX = svgRect.width / W;
            const scaleY = svgRect.height / H;
            const svgLeft = svgRect.left - boxRect.left;
            const svgTop = svgRect.top - boxRect.top;
            const size = 18; // CSS pixels — consistent across widths

            // Compute each endpoint's screen position and apply collision
            // avoidance in screen-pixel space. Sort by y, then nudge any
            // label that would overlap the one above it.
            const placed = endpoints
                .filter(ep => LOGOS[ep.key])
                .map(ep => ({
                    ep,
                    screenX: svgLeft + ep.vx * scaleX,
                    screenY: svgTop + ep.vy * scaleY,
                }))
                .sort((a, b) => a.screenY - b.screenY);

            const MIN_GAP = size + 2;
            for (let i = 1; i < placed.length; i++) {
                if (placed[i].screenY - placed[i - 1].screenY < MIN_GAP) {
                    placed[i].screenY = placed[i - 1].screenY + MIN_GAP;
                }
            }

            for (const p of placed) {
                const { ep, screenX, screenY } = p;
                const el = document.createElement('div');
                el.className = 'chart-end-logo';
                el.style.position = 'absolute';
                el.style.left = (screenX + 10) + 'px';       // 10px gap from data point
                el.style.top  = (screenY - size / 2) + 'px'; // center vertically on the line
                el.style.width = size + 'px';
                el.style.height = size + 'px';
                el.style.color = ep.color;
                el.style.pointerEvents = 'none';
                el.innerHTML = LOGOS[ep.key];
                const innerSvg = el.querySelector('svg');
                if (innerSvg) {
                    innerSvg.setAttribute('width', size);
                    innerSvg.setAttribute('height', size);
                    innerSvg.style.fill = ep.color;
                }
                chartBoxEl.appendChild(el);
            }
        };

        // Initial placement after the browser has laid out the svg.
        requestAnimationFrame(place);

        // Reposition on container resize.
        if (typeof ResizeObserver !== 'undefined') {
            const ro = new ResizeObserver(() => place());
            ro.observe(chartBoxEl);
        } else {
            window.addEventListener('resize', place);
        }
    }

    function formatTooltipDate(iso, endIso) {
        const start = new Date(iso + 'T00:00:00Z');
        const end = new Date(endIso + 'T00:00:00Z');
        const opts = { month: 'short', day: 'numeric', year: 'numeric', timeZone: 'UTC' };
        const s = start.toLocaleDateString('en-US', opts);
        const e = end.toLocaleDateString('en-US', opts);
        return `week of ${s} — ${e}`;
    }

    function mountHeroChart(pts) {
        const mount = document.getElementById('hero-chart-mount');
        const W = 900, H = 240, padL = 28, padR = 56, padY = 20;
        const innerW = W - padL - padR, innerH = H - padY * 2;

        if (!pts.length) {
            mount.innerHTML = `<svg class="chart-svg" viewBox="0 0 ${W} ${H}"><text x="${W/2}" y="${H/2}" class="chart-axis-label" text-anchor="middle">no data yet</text></svg>`;
            return;
        }

        const ys = pts.map(p => p.y);
        const maxY = (Math.max(...ys) || 1) * 1.1;
        const xStep = pts.length > 1 ? innerW / (pts.length - 1) : 0;
        const coords = pts.map((p, i) => ({
            x: padL + i * xStep,
            y: padY + innerH - (p.y / maxY) * innerH,
        }));

        const linePath = coords.map((c, i) => (i ? 'L' : 'M') + c.x.toFixed(1) + ',' + c.y.toFixed(1)).join(' ');
        const areaPath = linePath + ` L${coords[coords.length-1].x.toFixed(1)},${(padY+innerH).toFixed(1)} L${coords[0].x.toFixed(1)},${(padY+innerH).toFixed(1)} Z`;
        const gridLines = [0.25, 0.5, 0.75].map(f => {
            const y = padY + innerH * f;
            const label = Math.round(maxY * (1 - f));
            return `<line class="chart-grid-line" x1="${padL}" y1="${y}" x2="${W-padR}" y2="${y}"/><text class="chart-axis-label" x="${padL-4}" y="${y+3}" text-anchor="end">${fmt(label)}</text>`;
        }).join('');
        const endPoint = coords[coords.length - 1];

        mount.innerHTML = `
            <svg id="hero-svg" class="chart-svg" viewBox="0 0 ${W} ${H}" preserveAspectRatio="none">
                <defs>
                    <linearGradient id="heroGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%" style="stop-color:#E07A41;stop-opacity:0.28"/>
                        <stop offset="100%" style="stop-color:#E07A41;stop-opacity:0.02"/>
                    </linearGradient>
                </defs>
                ${gridLines}
                <path d="${areaPath}" fill="url(#heroGrad)"/>
                <path d="${linePath}" class="chart-line hero" stroke="#E07A41"/>
                <line id="hero-hover-line" class="chart-hover-line" stroke="#E07A41" x1="0" y1="${padY}" x2="0" y2="${padY+innerH}"/>
                <circle id="hero-hover-dot" class="chart-hover-dot" fill="#E07A41" cx="0" cy="0" r="5"/>
                <circle cx="${endPoint.x}" cy="${endPoint.y}" r="4" fill="#E07A41"/>
                <rect id="hero-overlay" x="0" y="0" width="${W}" height="${H}" fill="transparent" style="cursor: crosshair;"/>
            </svg>`;

        // Mount end-of-line logo as an HTML overlay (not SVG) so it stays round on mobile
        mountEndLogos(
            document.getElementById('hero-chart-box'),
            document.getElementById('hero-svg'),
            W, H,
            [{ key: 'claude-code', color: '#E07A41', vx: endPoint.x, vy: endPoint.y }]
        );

        // Hover interaction
        const svg = document.getElementById('hero-svg');
        const overlay = document.getElementById('hero-overlay');
        const hoverLine = document.getElementById('hero-hover-line');
        const hoverDot = document.getElementById('hero-hover-dot');
        const tooltip = document.getElementById('hero-tooltip');
        const tooltipCount = document.getElementById('hero-tooltip-count');
        const tooltipTime = document.getElementById('hero-tooltip-time');
        const chartBox = document.getElementById('hero-chart-box');

        overlay.addEventListener('mousemove', (e) => {
            const rect = svg.getBoundingClientRect();
            const scaleX = W / rect.width;
            const mouseX = (e.clientX - rect.left) * scaleX;
            // Snap to nearest point
            let nearest = 0, best = Infinity;
            for (let i = 0; i < coords.length; i++) {
                const d = Math.abs(coords[i].x - mouseX);
                if (d < best) { best = d; nearest = i; }
            }
            const c = coords[nearest];
            const p = pts[nearest];

            hoverLine.setAttribute('x1', c.x);
            hoverLine.setAttribute('x2', c.x);
            hoverLine.setAttribute('y1', c.y);
            hoverLine.setAttribute('y2', padY + innerH);
            hoverLine.style.opacity = '1';

            hoverDot.setAttribute('cx', c.x);
            hoverDot.setAttribute('cy', c.y);
            hoverDot.style.opacity = '1';

            tooltipCount.textContent = p.y.toLocaleString();
            tooltipTime.textContent = formatTooltipDate(p.x, p.end);

            const dotScreenX = (c.x / W) * rect.width;
            const dotScreenY = (c.y / H) * rect.height;
            const tw = tooltip.offsetWidth;
            const th = tooltip.offsetHeight;
            const boxRect = chartBox.getBoundingClientRect();
            const svgLeft = rect.left - boxRect.left;
            let tx = svgLeft + dotScreenX - tw / 2;
            tx = Math.max(4, Math.min(tx, chartBox.offsetWidth - tw - 4));
            tooltip.style.left = tx + 'px';
            tooltip.style.top = Math.max(-th - 20, dotScreenY - th - 12) + 'px';
            tooltip.classList.add('visible');
        });
        overlay.addEventListener('mouseleave', () => {
            hoverLine.style.opacity = '0';
            hoverDot.style.opacity = '0';
            tooltip.classList.remove('visible');
        });
    }

    function mountChallengersChart(idPrefix, series) {
        const mount = document.getElementById(`${idPrefix}-chart-mount`);
        const W = 900, H = 180, padL = 28, padR = 56, padY = 20;
        const innerW = W - padL - padR, innerH = H - padY * 2;

        const allYs = series.flatMap(s => s.points.map(p => p.y));
        if (!allYs.length) {
            mount.innerHTML = `<svg class="chart-svg small" viewBox="0 0 ${W} ${H}"><text x="${W/2}" y="${H/2}" class="chart-axis-label" text-anchor="middle">no data yet</text></svg>`;
            return;
        }
        const maxY = (Math.max(...allYs) || 1) * 1.1;

        // Each series can start at a different week (per-agent cutoff), so we
        // can't index points positionally. Map each point's start date onto a
        // shared time axis spanning min..max across ALL series. This way a
        // series that starts later renders its leftmost point further right.
        const allDates = series.flatMap(s => s.points.map(p => p.x));
        const minDate = allDates.reduce((a, b) => (a < b ? a : b));
        const maxDate = allDates.reduce((a, b) => (a > b ? a : b));
        const minMs = new Date(minDate + 'T00:00:00Z').getTime();
        const maxMs = new Date(maxDate + 'T00:00:00Z').getTime();
        const span = maxMs - minMs || 1;
        const xForDate = (iso) => {
            const ms = new Date(iso + 'T00:00:00Z').getTime();
            return padL + ((ms - minMs) / span) * innerW;
        };

        const seriesCoords = series.map(s => ({
            ...s,
            coords: s.points.map((p) => ({
                x: xForDate(p.x),
                y: padY + innerH - (p.y / maxY) * innerH,
                point: p,
            })),
        }));

        const gridLines = [0.25, 0.5, 0.75].map(f => {
            const y = padY + innerH * f;
            const label = Math.round(maxY * (1 - f));
            return `<line class="chart-grid-line" x1="${padL}" y1="${y}" x2="${W-padR}" y2="${y}"/><text class="chart-axis-label" x="${padL-4}" y="${y+3}" text-anchor="end">${fmt(label)}</text>`;
        }).join('');

        const lines = seriesCoords.map(s => {
            const path = s.coords.map((c, i) => (i ? 'L' : 'M') + c.x.toFixed(1) + ',' + c.y.toFixed(1)).join(' ');
            return `<path d="${path}" class="chart-line" stroke="${s.color}"/>`;
        }).join('');

        // End-of-line dot at each series' final data point (in viewBox coords)
        const endpoints = seriesCoords
            .filter(s => s.coords.length > 0)
            .map(s => ({
                key: s.key,
                color: s.color,
                vx: s.coords[s.coords.length - 1].x,
                vy: s.coords[s.coords.length - 1].y,
            }));
        const endDots = endpoints
            .map(e => `<circle cx="${e.vx.toFixed(1)}" cy="${e.vy.toFixed(1)}" r="3" fill="${e.color}"/>`)
            .join('');

        mount.innerHTML = `
            <svg id="${idPrefix}-svg" class="chart-svg small" viewBox="0 0 ${W} ${H}" preserveAspectRatio="none">
                ${gridLines}
                ${lines}
                ${endDots}
                <line id="${idPrefix}-hover-line" class="chart-hover-line" stroke="#888" x1="0" y1="${padY}" x2="0" y2="${padY+innerH}"/>
                <circle id="${idPrefix}-hover-dot" class="chart-hover-dot" fill="#fff" cx="0" cy="0" r="5"/>
                <rect id="${idPrefix}-overlay" x="0" y="0" width="${W}" height="${H}" fill="transparent" style="cursor: crosshair;"/>
            </svg>`;

        const svg = document.getElementById(`${idPrefix}-svg`);
        const overlay = document.getElementById(`${idPrefix}-overlay`);
        const hoverLine = document.getElementById(`${idPrefix}-hover-line`);
        const hoverDot = document.getElementById(`${idPrefix}-hover-dot`);
        const tooltip = document.getElementById(`${idPrefix}-tooltip`);
        const tooltipLabel = document.getElementById(`${idPrefix}-tooltip-label`);
        const tooltipCount = document.getElementById(`${idPrefix}-tooltip-count`);
        const tooltipTime = document.getElementById(`${idPrefix}-tooltip-time`);
        const chartBox = document.getElementById(`${idPrefix}-chart-box`);

        // Mount end-of-line logos as HTML overlay. mountEndLogos handles
        // collision avoidance in screen-pixel space at placement time, so
        // labels don't overlap regardless of viewBox stretch.
        mountEndLogos(chartBox, svg, W, H, endpoints);

        overlay.addEventListener('mousemove', (e) => {
            const rect = svg.getBoundingClientRect();
            const scaleX = W / rect.width;
            const scaleY = H / rect.height;
            const mouseX = (e.clientX - rect.left) * scaleX;
            const mouseY = (e.clientY - rect.top) * scaleY;

            // Find nearest point across ALL series (by 2D distance)
            let best = Infinity, bestSeries = null, bestCoord = null;
            for (const s of seriesCoords) {
                for (const c of s.coords) {
                    const d = Math.hypot(c.x - mouseX, c.y - mouseY);
                    if (d < best) { best = d; bestSeries = s; bestCoord = c; }
                }
            }
            if (!bestCoord) return;

            hoverLine.setAttribute('x1', bestCoord.x);
            hoverLine.setAttribute('x2', bestCoord.x);
            hoverLine.setAttribute('stroke', bestSeries.color);
            hoverLine.style.opacity = '1';

            hoverDot.setAttribute('cx', bestCoord.x);
            hoverDot.setAttribute('cy', bestCoord.y);
            hoverDot.setAttribute('fill', bestSeries.color);
            hoverDot.style.opacity = '1';

            tooltipLabel.textContent = bestSeries.label;
            tooltipLabel.style.color = bestSeries.color;
            tooltipCount.textContent = bestCoord.point.y.toLocaleString();
            tooltipTime.textContent = formatTooltipDate(bestCoord.point.x, bestCoord.point.end);

            const dotScreenX = (bestCoord.x / W) * rect.width;
            const dotScreenY = (bestCoord.y / H) * rect.height;
            const tw = tooltip.offsetWidth;
            const th = tooltip.offsetHeight;
            const boxRect = chartBox.getBoundingClientRect();
            const svgLeft = rect.left - boxRect.left;
            let tx = svgLeft + dotScreenX - tw / 2;
            tx = Math.max(4, Math.min(tx, chartBox.offsetWidth - tw - 4));
            tooltip.style.left = tx + 'px';
            tooltip.style.top = Math.max(-th - 20, dotScreenY - th - 12) + 'px';
            tooltip.classList.add('visible');
        });
        overlay.addEventListener('mouseleave', () => {
            hoverLine.style.opacity = '0';
            hoverDot.style.opacity = '0';
            tooltip.classList.remove('visible');
        });
    }
})();
